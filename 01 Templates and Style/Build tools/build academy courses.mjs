/**
 * Builds the Academy course Word documents (Issue 3 onwards) from course data files.
 *
 *   node "build academy courses.mjs" <data folder> <output folder>
 *
 * Each data file is one course in the Hub's CourseDef shape (scripts/courses/types.ts in
 * herts-mentoring-hub) with a few extra fields: code, issue, tier, changeSummary, and per
 * lesson `required` and `devNotes`. The document layout matches the Hub's export-docx.ts so
 * the documents can be read back into the Hub, and every course is checked against the
 * lesson player's rules before anything is written.
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { createRequire } from "node:module";

const require = createRequire("/Users/wespierce/Projects/Claude/herts-mentoring-hub/package.json");
const {
  AlignmentType, BorderStyle, Document, Footer, HeadingLevel, LevelFormat, Packer, PageBreak, PageNumber,
  Paragraph, ShadingType, Table, TableCell, TableRow, TextRun, WidthType,
} = require("docx");

const NAVY = "003668", TEAL = "157A7C", SLATE = "3D4A57", SKY = "BFD6EA";
const PAGE_W = 9026; // A4 with 1" margins, in DXA
const FONT = "Arial";
// A3 gives "Provincial Grand Mentor"; Issue 3 uses the Provincial Mentor titles pending formal confirmation.
const COPYRIGHT_HOLDER = "Provincial Mentor";

const LABELS = {
  lodge_mentor: "Lodge Mentors", personal_mentor: "Personal Mentors", newer_brother: "Newer Brethren", provincial_team: "Provincial team", all: "Everyone",
  essential: "Essential", recommended: "Recommended", optional: "Optional",
  prepare: "Prepare", guide: "Guide", support: "Support", enlighten: "Enlighten",
  content: "Reading", video: "Video", scenario: "Scenario", reflection: "Private reflection", quiz: "Quiz", resource: "Resource",
  single: "One answer", multiple: "More than one answer", true_false: "True or false",
  foundation: "Foundation course", specialist: "Specialist topic course",
};
const label = (k) => LABELS[k] ?? k.replace(/_/g, " ");

// ---------------------------------------------------------------- validation

const AUDIENCES = ["lodge_mentor", "personal_mentor", "newer_brother", "provincial_team", "all"];
const STAGES = ["entered_apprentice", "fellow_craft", "master_mason", "established"];
const KINDS = ["content", "video", "scenario", "reflection", "quiz", "resource"];

function scenarioProblems(s) {
  if (!s) return ["The scenario has no steps yet."];
  const out = [];
  if (!s.nodes[s.start]) out.push(`The starting step "${s.start}" does not exist.`);
  const reach = new Set(), queue = [s.start];
  while (queue.length) {
    const id = queue.shift();
    if (reach.has(id) || !s.nodes[id]) continue;
    reach.add(id);
    s.nodes[id].choices.forEach((c) => queue.push(c.next));
  }
  for (const [id, n] of Object.entries(s.nodes)) {
    if (!n.text.trim()) out.push(`Step "${id}" has no text.`);
    if (n.text.length > 4000) out.push(`Step "${id}" is over 4000 characters.`);
    if (!reach.has(id)) out.push(`Step "${id}" cannot be reached from the start.`);
    for (const c of n.choices) {
      if (!c.label.trim()) out.push(`A choice in step "${id}" has no label.`);
      if (c.label.length > 500) out.push(`A choice in step "${id}" is over 500 characters.`);
      if ((c.feedback ?? "").length > 1000) out.push(`Feedback in step "${id}" is over 1000 characters.`);
      if (!s.nodes[c.next]) out.push(`A choice in step "${id}" leads to "${c.next}", which does not exist.`);
    }
  }
  if (!Object.values(s.nodes).some((n) => n.choices.length === 0)) out.push("No step ends the scenario (a step with no choices).");
  // Every reachable step must be able to reach an ending.
  const ends = new Set(Object.entries(s.nodes).filter(([, n]) => !n.choices.length).map(([id]) => id));
  let grew = true;
  while (grew) {
    grew = false;
    for (const [id, n] of Object.entries(s.nodes)) if (!ends.has(id) && n.choices.some((c) => ends.has(c.next))) { ends.add(id); grew = true; }
  }
  for (const id of reach) if (!ends.has(id)) out.push(`Step "${id}" can never reach an ending.`);
  return out;
}

function blockProblems(b) {
  switch (b?.type) {
    case "text": return typeof b.markdown === "string" && b.markdown.length <= 20000 ? [] : ["text block too long or missing"];
    case "callout": return typeof b.text === "string" && b.text.length <= 2000 && ["info", "tip", "important", undefined].includes(b.tone) ? [] : ["bad callout"];
    case "principles": return !b.intro || b.intro.length <= 500 ? [] : ["principles intro over 500"];
    case "resource": return b.title && (!b.url || b.url.startsWith("https://")) && (b.description ?? "").length <= 500 ? [] : ["bad resource block"];
    case "video": return b.title && b.url?.startsWith("https://") ? [] : ["bad video block"];
    case "image": return b.path ? [] : ["image has no path"];
    default: return [`unknown block type ${b?.type}`];
  }
}

export function validate(c) {
  const out = [];
  const p = (m) => out.push(`${c.code} ${c.title}: ${m}`);
  if (!["essential", "recommended", "optional"].includes(c.level)) p(`level "${c.level}" is not accepted by the Hub`);
  if (!["prepare", "guide", "support", "enlighten"].includes(c.principle)) p(`bad principle ${c.principle}`);
  for (const a of c.audiences) if (!AUDIENCES.includes(a)) p(`unknown audience ${a}`);
  for (const s of c.stages) if (!STAGES.includes(s)) p(`unknown stage ${s}`);
  let mins = 0;
  for (const m of c.modules) for (const l of m.lessons) {
    const where = `${m.title} / ${l.title}`;
    mins += l.minutes;
    if (!KINDS.includes(l.kind)) p(`${where}: unknown lesson kind ${l.kind}`);
    for (const b of l.blocks) for (const e of blockProblems(b)) p(`${where}: ${e}`);
    if (l.kind === "scenario") for (const e of scenarioProblems(l.scenario)) p(`${where}: ${e}`);
    if (l.kind === "reflection" && !l.prompt) p(`${where}: reflection has no prompt`);
    if (l.kind === "quiz" && !l.questions?.length) p(`${where}: quiz has no questions`);
    for (const q of l.questions ?? []) {
      if (!q.correct.length || q.correct.some((i) => i >= q.options.length)) p(`${where}: bad answer key for "${q.prompt}"`);
      if (q.kind === "single" && q.correct.length !== 1) p(`${where}: single-answer question with ${q.correct.length} keys: "${q.prompt}"`);
      if (q.kind === "true_false" && (q.options.length !== 2)) p(`${where}: true/false needs two options`);
      if (!q.feedbackCorrect || !q.feedbackIncorrect) p(`${where}: question lacks feedback: "${q.prompt}"`);
    }
    if (/—/.test(JSON.stringify(l))) p(`${where}: contains an em-dash (A3 style)`);
  }
  if (Math.abs(mins - c.minutes) > 10) p(`course says ${c.minutes} minutes but lessons add up to ${mins}`);
  if (!c.modules.some((m) => m.lessons.some((l) => l.kind === "quiz" && l.isAssessment !== false))) p("no assessed quiz");
  return out;
}

// ---------------------------------------------------------------- document

/** **bold**, *italic* and [text](url) inside a line of markdown. */
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))/g;
  let last = 0;
  for (const m of text.matchAll(re)) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), ...base, bold: true }));
    else if (t.startsWith("[")) {
      const [, txt, url] = t.match(/\[([^\]]+)\]\(([^)]+)\)/);
      out.push(new TextRun({ text: `${txt} (${url})`, ...base, color: TEAL }));
    } else out.push(new TextRun({ text: t.slice(1, -1), ...base, italics: true }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: "B8C4CF" };
const borders = { top: border, bottom: border, left: border, right: border };

function table(rows, widths, opts = {}) {
  return new Table({
    width: { size: PAGE_W, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((cells, r) => new TableRow({
      tableHeader: opts.header && r === 0,
      children: cells.map((c, i) => new TableCell({
        borders,
        width: { size: widths[i], type: WidthType.DXA },
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        shading: opts.header && r === 0 ? { fill: "DDE9F5", type: ShadingType.CLEAR, color: "auto" } : undefined,
        children: String(c).split("\n").map((line) => new Paragraph({ children: runs(line, opts.header && r === 0 ? { bold: true } : {}) })),
      })),
    })),
  });
}

/** A shaded box: callouts, reflection prompts, development notes. */
function box(title, body, fill, accent) {
  const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  return new Table({
    width: { size: PAGE_W, type: WidthType.DXA },
    columnWidths: [PAGE_W],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: PAGE_W, type: WidthType.DXA },
      borders: { top: none, bottom: none, right: none, left: { style: BorderStyle.SINGLE, size: 24, color: accent } },
      shading: { fill, type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 100, bottom: 100, left: 160, right: 160 },
      children: [
        new Paragraph({ children: [new TextRun({ text: title, bold: true, color: accent })] }),
        ...body.map((b) => new Paragraph({ children: runs(b) })),
      ],
    })] })],
  });
}

const spacer = () => new Paragraph({ children: [] });

/** Markdown as used in the course files: paragraphs, lists, quotes, tables and headings. */
function markdown(md) {
  const out = [];
  const lines = md.split("\n");
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim()) continue;
    if (line.startsWith("|")) {
      const rows = [];
      while (i < lines.length && lines[i].startsWith("|")) {
        if (!/^\|[\s:|-]+\|$/.test(lines[i])) rows.push(lines[i].trim().slice(1, -1).split("|").map((c) => c.trim()));
        i++;
      }
      i--;
      const n = rows[0].length;
      const w = Array.from({ length: n }, (_, k) => k < n - 1 ? Math.floor(PAGE_W / n) : PAGE_W - Math.floor(PAGE_W / n) * (n - 1));
      out.push(table(rows, w, { header: true }), spacer());
    } else if (/^#{1,6} /.test(line)) {
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_4, children: runs(line.replace(/^#+ /, "")) }));
    } else if (line.startsWith("> ")) {
      out.push(new Paragraph({ indent: { left: 567 }, border: { left: { style: BorderStyle.SINGLE, size: 12, color: SKY, space: 8 } },
        children: runs(line.slice(2), { italics: true }) }));
    } else if (/^\s*- /.test(line)) {
      out.push(new Paragraph({ numbering: { reference: "bullets", level: /^\s{2,}/.test(line) ? 1 : 0 }, children: runs(line.replace(/^\s*- /, "")) }));
    } else if (/^\s*\d+\. /.test(line)) {
      const [, num, rest] = line.trim().match(/^(\d+)\. (.*)$/);
      out.push(new Paragraph({ indent: { left: 567, hanging: 340 }, children: [new TextRun(`${num}.\t`), ...runs(rest)] }));
    } else {
      out.push(new Paragraph({ children: runs(line) }));
    }
  }
  return out;
}

function block(b) {
  switch (b.type) {
    case "text": return markdown(b.markdown);
    case "callout": {
      const t = b.tone === "important" ? ["Important", "FDF1E7", "B5541C"] : b.tone === "tip" ? ["Tip", "EEF8F8", TEAL] : ["Note", "F2F7FC", NAVY];
      return [box(t[0], b.text.split("\n"), t[1], t[2]), spacer()];
    }
    case "principles": return [box("Graphic: the four Hertfordshire principles (Prepare, Guide, Support, Enlighten)", b.intro ? [b.intro] : [], "F2F7FC", NAVY), spacer()];
    case "image": return [box("Image", [`${b.alt || "(no description)"}${b.caption ? `: ${b.caption}` : ""}`], "F2F7FC", SLATE), spacer()];
    case "video": return [box("Video", [`${b.title}: ${b.url}`], "F2F7FC", SLATE), spacer()];
    case "resource": return [box("Resource", [b.title, ...(b.description ? [b.description] : []), ...(b.url ? [b.url] : [])], "F2F7FC", SLATE), spacer()];
    default: return [];
  }
}

function question(q, n) {
  const out = [
    new Paragraph({ spacing: { before: 200 }, children: [new TextRun({ text: `Question ${n} `, bold: true, color: NAVY }), new TextRun({ text: `(${label(q.kind)})`, color: SLATE })] }),
    new Paragraph({ children: runs(q.prompt) }),
    table([["", "Answer option", "Correct?"], ...q.options.map((o, i) => [String.fromCharCode(97 + i), o, q.correct.includes(i) ? "Yes" : ""])],
      [600, PAGE_W - 1800, 1200], { header: true }),
  ];
  const fb = [];
  if (q.feedbackCorrect) fb.push(`**If right:** ${q.feedbackCorrect}`);
  if (q.feedbackIncorrect) fb.push(`**If wrong:** ${q.feedbackIncorrect}`);
  if (q.explanation) fb.push(`**Explanation:** ${q.explanation}`);
  for (const f of fb) out.push(new Paragraph({ indent: { left: 340 }, children: runs(f) }));
  return out;
}

function lesson(l, num, course) {
  const assessed = l.kind === "quiz" && l.isAssessment !== false;
  const meta = [`${label(l.kind)} · about ${l.minutes} minutes`];
  if (assessed) meta.push(`counts towards completion, pass mark ${l.passMark ?? course.passMark}%`);
  else if (l.kind === "quiz") meta.push("does not count towards completion");
  if (l.required === false) meta.push("optional activity");
  const out = [
    new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(`Lesson ${num}: ${l.title}`)] }),
    new Paragraph({ children: [new TextRun({ text: meta.join(" · "), color: SLATE, size: 20 })] }),
    ...l.blocks.flatMap(block),
  ];
  if (l.prompt) out.push(box("Reflection prompt (the learner's answer is private to them)", l.prompt.split("\n"), "EEF8F8", TEAL), spacer());
  if (l.scenario) {
    out.push(new Paragraph({ children: runs(`**Branching scenario.** Starts at step ${l.scenario.start}. A step with no choices ends the scenario.`) }));
    for (const [id, node] of Object.entries(l.scenario.nodes)) {
      out.push(new Paragraph({ heading: HeadingLevel.HEADING_4, children: [new TextRun(`Step ${id}${node.choices.length ? "" : " (ending)"}`)] }),
        ...node.text.split("\n").filter((t) => t.trim()).map((t) => new Paragraph({ children: runs(t) })));
      if (node.choices.length) out.push(table([["Choice", "Goes to", "Feedback shown"], ...node.choices.map((c) => [c.label, c.next, c.feedback ?? ""])],
        [3800, 1100, PAGE_W - 4900], { header: true }));
    }
    out.push(spacer());
  }
  l.questions?.forEach((q, i) => out.push(...question(q, i + 1)));
  if (l.questions) out.push(spacer());
  out.push(box("Development notes", ["Ideas, extra detail, examples or questions for this lesson:", ...(l.devNotes ? l.devNotes.split("\n") : [""])], "FAFAF7", "8A8F95"), spacer());
  return out;
}

function course(c) {
  const lessons = c.modules.reduce((n, m) => n + m.lessons.length, 0);
  const body = [
    new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(c.title)] }),
    new Paragraph({ children: [new TextRun({ text: `Hertfordshire Provincial Mentoring Academy · ${c.code} · ${c.issue} · Draft for Provincial review`, color: SLATE })] }),
    new Paragraph({ children: [new TextRun({ text: "Prepare • Guide • Support • Enlighten", color: TEAL, italics: true })] }),
    spacer(),
    new Paragraph({ children: runs(c.summary, { italics: true }) }),
    spacer(),
    table([
      ["Course", `${c.code} ${c.title}`],
      ["Type", label(c.tier)],
      ["Who it is for", c.audienceText ?? c.audiences.map(label).join(", ")],
      ["Level", label(c.level)],
      ["Principle", label(c.principle)],
      ["Length", `About ${c.minutes} minutes: ${c.modules.length} module${c.modules.length === 1 ? "" : "s"}, ${lessons} lessons. Progress is saved, so it can be taken in several sittings.`],
      ["Pass mark", `${c.passMark}% in the final assessment. You can try again.`],
      ["Completion", c.completion],
      ["Adapted from", c.source],
      ["Issue", `${c.issue}, ${c.issueDate}`],
    ], [2400, PAGE_W - 2400]),
    spacer(),
  ];
  if (c.changeSummary?.length) body.push(box(`What changed in ${c.issue}`, c.changeSummary.map((s) => `- ${s}`.replace(/^- /, "• ")), "F2F7FC", NAVY), spacer());
  body.push(
    new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun("How to work on this document")] }),
    ...[
      "Edit and add text freely. Use Track Changes and comments if more than one person is working on it.",
      "Keep the Module and Lesson headings so changes can be matched back to the course. To add a lesson, copy an existing lesson heading and give it a new number such as 2.3a.",
      "Quizzes: mark the right answers with Yes in the Correct? column. Each question needs at least one right answer. Where several answers are reasonable, the question is set as More than one answer and the explanation says why.",
      "Scenarios: each step names the step its choices go to. Every choice leads to a step that exists, and every route reaches an ending.",
      "Lessons marked optional activity do not count towards completion.",
      "Use the Development notes box under each lesson for ideas you have not yet written up. Notes for reviewers are in there too.",
      "House style (A3): no ceremony or ritual content, no em-dashes, Brother with a capital B, British English.",
      "The matching file in the Course data folder (for example E1.json) holds exactly this content in the Hub's import format, and the Word document is built from it.",
    ].map((t) => new Paragraph({ numbering: { reference: "bullets", level: 0 }, children: runs(t) })),
  );
  c.modules.forEach((m, mi) => {
    body.push(new Paragraph({ children: [new PageBreak()] }),
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(`Module ${mi + 1}: ${m.title}`)] }),
      new Paragraph({ children: runs(m.summary, { italics: true, color: SLATE }) }));
    m.lessons.forEach((l, li) => body.push(...lesson(l, `${mi + 1}.${li + 1}`, c)));
  });
  body.push(spacer(), new Paragraph({ children: [new TextRun({ text: `© ${COPYRIGHT_HOLDER}, Province of Hertfordshire, 2026. Provincial Office, Fleet House, 10 Parkway, St Albans AL3 6PA · 01727 833061 · mentor@hertfordshirefreemasons.org.uk`, color: SLATE, size: 18 })] }));

  return new Document({
    creator: "Hertfordshire Provincial Mentoring Hub",
    title: `${c.code} ${c.title} ${c.issue}`,
    styles: {
      default: { document: { run: { font: FONT, size: 22 }, paragraph: { spacing: { after: 100, line: 288 } } } },
      paragraphStyles: [
        { id: "Title", name: "Title", basedOn: "Normal", run: { size: 48, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { after: 120 } } },
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 34, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 120, after: 120 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 27, bold: true, color: TEAL, font: FONT }, paragraph: { spacing: { before: 360, after: 60 }, outlineLevel: 1 } },
        { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, color: NAVY, font: FONT }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2 } },
        { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 22, bold: true, color: SLATE, font: FONT }, paragraph: { spacing: { before: 160, after: 60 }, outlineLevel: 3 } },
      ],
    },
    numbering: { config: [{ reference: "bullets", levels: [
      { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 284 } } } },
      { level: 1, format: LevelFormat.BULLET, text: "◦", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1134, hanging: 284 } } } },
    ] }] },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
        new TextRun({ text: `${c.code} ${c.title} · ${c.issue} · Draft for Provincial review · Page `, size: 18, color: SLATE }),
        new TextRun({ children: [PageNumber.CURRENT], size: 18, color: SLATE }),
      ] })] }) },
      children: body,
    }],
  });
}

async function main() {
  const [dataDir, outDir] = process.argv.slice(2);
  if (!dataDir || !outDir) { console.error("usage: node build-academy-courses.mjs <data folder> <output folder>"); process.exit(2); }
  mkdirSync(outDir, { recursive: true });
  const files = readdirSync(dataDir).filter((f) => f.endsWith(".json")).sort();
  const courses = files.map((f) => JSON.parse(readFileSync(join(dataDir, f), "utf8")));
  const problems = courses.flatMap(validate);
  if (problems.length) { console.error(problems.join("\n")); process.exit(1); }
  for (const c of courses) {
    const file = join(outDir, `${c.code} ${c.fileTitle ?? c.title} ${c.issue}.docx`);
    writeFileSync(file, await Packer.toBuffer(course(c)));
    const n = c.modules.reduce((a, m) => a + m.lessons.length, 0);
    const q = c.modules.flatMap((m) => m.lessons).reduce((a, l) => a + (l.questions?.length ?? 0), 0);
    console.log(`${c.code}: ${c.modules.length} modules, ${n} lessons, ${q} questions, ${c.minutes} min -> ${file}`);
  }
}

if (process.argv[1]?.endsWith("build academy courses.mjs")) main().catch((e) => { console.error(e); process.exit(1); });
