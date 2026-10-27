// New Masons Evening — Hertfordshire Provincial Mentoring Team
// Structured pptxgenjs deck on the Provincial Mentoring brand.
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");
const FA = require("react-icons/fa");

const OUT = process.argv[2] || "New Masons Evening Issue 1 Draft.pptx";
const SHIELD = process.argv[3];

const THEME = {
  name: "Hertfordshire Provincial Mentoring",
  headFontFace: "DM Sans",
  bodyFontFace: "DM Sans",
  colors: {
    dk1: "1E2329", lt1: "FFFFFF", dk2: "003668", lt2: "F2F7FC",
    accent1: "003668", accent2: "0A4F72", accent3: "106576", accent4: "157A7C",
    accent5: "06345D", accent6: "BFD6EA", hlink: "157A7C", folHlink: "0A4F72",
  },
};
const PR = [["Prepare", "003668"], ["Guide", "0A4F72"], ["Support", "106576"], ["Enlighten", "157A7C"]];

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "New Masons Evening";
pres.author = "Hertfordshire Provincial Mentoring Team";
const C = pres.SchemeColor;
const W = 13.33, H = 7.5;

// ---------- icons ----------
async function icon(name, hex, px = 256) {
  const Comp = FA[name];
  if (!Comp) throw new Error("no icon " + name);
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + hex, size: px }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

// ---------- layouts ----------
function strip(objs, y, h) {
  const w = W / 4;
  PR.forEach(([n, hex], i) => objs.push({ rect: { x: i * w, y, w, h, fill: { color: hex } } }));
}
// Title layout: white, shield right, strip under the identity block
(function () {
  const objects = [];
  objects.push({ text: { text: "Provincial Mentoring", options: { x: 0.6, y: 0.45, w: 8, h: 0.6, fontSize: 24, bold: true, color: "003668", margin: 0 } } });
  objects.push({ text: { text: "Provincial Grand Lodge of Hertfordshire", options: { x: 0.6, y: 1.0, w: 8, h: 0.35, fontSize: 13, color: "06345D", margin: 0 } } });
  objects.push({ text: { text: "Prepare • Guide • Support • Enlighten", options: { x: 0.6, y: 1.3, w: 8, h: 0.35, fontSize: 13, bold: true, color: "157A7C", margin: 0 } } });
  if (SHIELD) objects.push({ image: { x: W - 0.6 - 1.45, y: 0.4, w: 1.45, h: 1.67, path: SHIELD } });
  strip(objects, 2.25, 0.26);
  pres.defineSlideMaster({
    title: "TITLE", background: { color: "FFFFFF" }, objects,
  });
})();
// Section divider: deep blue, big number + name, strip at base
pres.defineSlideMaster({
  title: "SECTION", background: { color: "003668" },
  objects: (() => { const o = [{ rect: { x: 0, y: H - 0.30, w: W, h: 0.04, fill: { color: "FFFFFF" } } }]; strip(o, H - 0.26, 0.26); return o; })(),
});
// Content: white, title top, thin strip at base, footer
(function () {
  const objects = [];
  strip(objects, H - 0.12, 0.12);
  objects.push({ text: { text: "Hertfordshire Provincial Mentoring  ·  New Masons Evening", options: { x: 0.6, y: H - 0.52, w: 8, h: 0.3, fontSize: 9, color: "06345D", margin: 0 } } });
  pres.defineSlideMaster({
    title: "CONTENT", background: { color: "FFFFFF" }, objects,
    slideNumber: { x: W - 1.2, y: H - 0.52, w: 0.6, h: 0.3, fontSize: 9, color: "06345D", align: "right" },
  });
})();

// ---------- helpers ----------
let n = 0;
function content(title, section) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  s.addText(title, { x: 0.6, y: 0.45, w: W - 1.2, h: 0.8, fontSize: 32, bold: true, color: "003668", margin: 0, isTextBox: true, objectName: "Title" });
  return s;
}
function bullets(s, items, o) {
  const arr = items.map((t, i) => ({ text: t, options: { bullet: { code: "25A0", indent: 18 }, breakLine: i < items.length - 1, paraSpaceAfter: 6 } }));
  s.addText(arr, Object.assign({ fontSize: 15, color: "1E2329", valign: "top", margin: 0, isTextBox: true }, o));
}
function card(s, x, y, w, h, head, body, opts = {}) {
  const fill = opts.fill || "F2F7FC";
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.08, objectName: "Card " + head });
  let ty = y + 0.18;
  if (opts.icon) { s.addImage({ data: opts.icon, x: x + 0.22, y: y + 0.2, w: 0.42, h: 0.42 }); }
  s.addText(head, { x: x + (opts.icon ? 0.78 : 0.25), y: ty, w: w - (opts.icon ? 1.0 : 0.5), h: 0.45, fontSize: 16, bold: true, color: opts.headColor || "003668", margin: 0, isTextBox: true, valign: "middle" });
  if (Array.isArray(body)) {
    const arr = body.map((t, i) => ({ text: t, options: { bullet: { code: "25A0", indent: 16 }, breakLine: i < body.length - 1, paraSpaceAfter: 4 } }));
    s.addText(arr, { x: x + 0.25, y: ty + 0.5, w: w - 0.5, h: h - 0.8, fontSize: opts.fontSize || 13, color: "1E2329", valign: "top", margin: 0, isTextBox: true });
  } else {
    s.addText(body, { x: x + 0.25, y: ty + 0.5, w: w - 0.5, h: h - 0.8, fontSize: opts.fontSize || 13, color: "1E2329", valign: "top", margin: 0, isTextBox: true });
  }
}
function qa(s, x, y, w, h, q, a, hex = "003668") {
  // question in colour, answer in ink — the FAQ motif
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "FAQ " + q.slice(0, 20) });
  s.addText(q, { x: x + 0.25, y: y + 0.15, w: w - 0.5, h: 0.5, fontSize: 15, bold: true, color: hex, margin: 0, isTextBox: true, valign: "top" });
  s.addText(a, { x: x + 0.25, y: y + 0.62, w: w - 0.5, h: h - 0.75, fontSize: 13.5, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
}
function divider(num, name, presenter, hex, section, sub) {
  const s = pres.addSlide({ masterName: "SECTION", sectionTitle: section });
  s.addText(String(num), { x: 0.9, y: 1.6, w: 2.2, h: 2.2, fontSize: 120, bold: true, color: "8FD3D1", margin: 0, isTextBox: true, objectName: "Number" });
  s.addText(name, { x: 3.4, y: 1.9, w: 9, h: 1.2, fontSize: 44, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Section title" });
  s.addText(sub, { x: 3.4, y: 3.1, w: 9, h: 0.8, fontSize: 18, color: "BFD6EA", margin: 0, isTextBox: true, valign: "top", objectName: "Section subtitle" });
  s.addText(presenter, { x: 3.4, y: 4.3, w: 9, h: 0.5, fontSize: 16, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, objectName: "Presenter" });
  return s;
}
function notes(s, t) { s.addNotes(t); }

(async () => {
  const I = {
    user: await icon("FaUserFriends", "003668"), users: await icon("FaUsers", "0A4F72"), map: await icon("FaMapSigns", "106576"),
    tie: await icon("FaUserTie", "003668"), socks: await icon("FaSocks", "0A4F72"), shoe: await icon("FaShoePrints", "106576"),
    gem: await icon("FaGem", "157A7C"), ring: await icon("FaRing", "0A4F72"), hands: await icon("FaHandsHelping", "157A7C"),
    utensils: await icon("FaUtensils", "003668"), comment: await icon("FaCommentDots", "0A4F72"), door: await icon("FaDoorOpen", "106576"),
    heart: await icon("FaHeart", "157A7C"), book: await icon("FaBookOpen", "003668"), cert: await icon("FaCertificate", "157A7C"),
    graduation: await icon("FaGraduationCap", "0A4F72"), school: await icon("FaChalkboardTeacher", "106576"), ear: await icon("FaHeadphones", "003668"),
    whatsapp: await icon("FaWhatsapp", "157A7C"), calendar: await icon("FaCalendarAlt", "0A4F72"), pound: await icon("FaPoundSign", "003668"),
    compass: await icon("FaCompass", "106576"), check: await icon("FaCheckCircle", "157A7C"), question: await icon("FaQuestionCircle", "003668"),
    phone: await icon("FaPhoneAlt", "0A4F72"), envelope: await icon("FaEnvelope", "106576"), globe: await icon("FaGlobe", "157A7C"),
    family: await icon("FaHome", "003668"), briefcase: await icon("FaBriefcase", "0A4F72"), square: await icon("FaSquare", "157A7C"),
    lightbulb: await icon("FaLightbulb", "157A7C"), handshake: await icon("FaHandshake", "003668"), star: await icon("FaStar", "0A4F72"),
    ticket: await icon("FaTicketAlt", "106576"), pin: await icon("FaMapPin", "157A7C"), film: await icon("FaFilm", "003668"),
  };

  // ================= OPENING =================
  pres.addSection({ title: "Welcome" });
  let s = pres.addSlide({ masterName: "TITLE", sectionTitle: "Welcome" });
  s.addText("New Masons Evening", { x: 0.6, y: 2.9, w: 11, h: 1.3, fontSize: 54, bold: true, color: "003668", margin: 0, isTextBox: true, objectName: "Title" });
  s.addText("An evening for Brethren in their first two years: the questions you wanted answered, and the people here to help", { x: 0.6, y: 4.2, w: 10.5, h: 0.9, fontSize: 20, color: "06345D", margin: 0, isTextBox: true, objectName: "Subtitle" });
  s.addText("[Date]  ·  [Venue]  ·  Hertfordshire Provincial Mentoring Team", { x: 0.6, y: 5.4, w: 11, h: 0.5, fontSize: 16, bold: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Date and venue" });
  notes(s, "Welcome. Replace [Date] and [Venue]. Open warmly: this evening exists because new Masons told us what they wished someone had explained. No question is too small.");

  s = content("What tonight is for", "Welcome");
  s.addText("You asked. We listened. Earlier this year we polled Brethren across the Province about what they wished someone had told them in their first two years. Tonight is the answer: three short sessions, plenty of time for questions, and the chance to meet the people whose job is to help you enjoy Freemasonry.",
    { x: 0.6, y: 1.5, w: 7.2, h: 2.4, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, valign: "top", objectName: "Intro" });
  card(s, 0.6, 4.1, 3.6, 2.3, "Ask anything", "Cards and pens are on the tables. Write a question at any point and hand it in; we answer them all at the end.", { icon: I.question, fontSize: 14 });
  card(s, 4.4, 4.1, 3.4, 2.3, "Nothing is secret here", "Everything tonight is about how Freemasonry works day to day. Nothing touches ritual.", { icon: I.check, fontSize: 14 });
  card(s, 8.3, 1.5, 4.4, 4.9, "Tonight", [
    "1  Mentoring: the basics, the people and the questions you asked",
    "2  Learning and Development: Solomon, the Academy diploma, learning ritual",
    "3  Fleet House Light Blues Club: your club, your tie, your events",
    "Questions, then the bar",
  ], { fill: "E6F2F2", fontSize: 15 });
  notes(s, "Explain the card system for questions. Point out the three presenters.");

  s = content("Who you'll hear from", "Welcome");
  [["1", "Mentoring", "W Bro Mark Butcher and W Bro Wes Pierce", "Provincial Grand Mentor and Deputy Provincial Grand Mentor", "003668"],
   ["2", "Learning and Development", "W Bro Tom Golds", "Provincial Learning and Development Officer", "106576"],
   ["3", "Fleet House Light Blues Club", "Bro Aaron Ball", "FHLBC Communications Officer", "157A7C"]].forEach(([num, t, p, r, hex], i) => {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.6, w: 3.8, h: 4.6, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Presenter card " + num });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.3, y: 1.9, w: 0.9, h: 0.9, fill: { color: hex }, line: { color: hex }, objectName: "Number circle " + num });
    s.addText(num, { x: x + 0.3, y: 1.9, w: 0.9, h: 0.9, fontSize: 28, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(t, { x: x + 0.3, y: 3.0, w: 3.2, h: 0.9, fontSize: 20, bold: true, color: hex, margin: 0, isTextBox: true, valign: "top" });
    s.addText(p, { x: x + 0.3, y: 4.0, w: 3.2, h: 0.9, fontSize: 16, bold: true, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
    s.addText(r, { x: x + 0.3, y: 4.95, w: 3.2, h: 1.1, fontSize: 13, color: "06345D", margin: 0, isTextBox: true, valign: "top" });
  });
  notes(s, "Introduce each presenter briefly. Mark and Wes share the mentoring section.");

  // ================= 1 MENTORING =================
  pres.addSection({ title: "1 Mentoring" });
  divider(1, "Mentoring", "W Bro Mark Butcher, Provincial Grand Mentor  ·  W Bro Wes Pierce, Deputy Provincial Grand Mentor", "003668", "1 Mentoring", "The people here to help you, the basics nobody explains, and the questions you asked");

  s = content("Who's who in your corner", "1 Mentoring");
  card(s, 0.6, 1.5, 4.0, 4.9, "Your Personal Mentor", ["One Brother, assigned to you", "A friend first: the person you ring, message or sit next to without feeling you are bothering anyone", "Not a ritual coach and not a report-writer", "Your first call for any question"], { icon: I.user, fontSize: 15 });
  card(s, 4.8, 1.5, 4.0, 4.9, "Your Lodge Mentor", ["Co-ordinates mentoring across the Lodge", "Makes sure every new member has a Personal Mentor and nobody drifts", "Your link to the Province", "Ask him if your Personal Mentor cannot help"], { icon: I.users, fontSize: 15 });
  card(s, 9.0, 1.5, 3.7, 4.9, "The Provincial team", ["Provincial Grand Mentor, Deputy, and five Assistant Provincial Grand Mentors, one per area", "Here to help, never to inspect", "mentor@hertfordshirefreemasons.org.uk"], { icon: I.map, fontSize: 15 });
  notes(s, "Make the distinction clear: Personal Mentor accompanies, Lodge Mentor co-ordinates, Province supports. Everyone in this room has one of each.");

  s = content("What we mean by mentoring", "1 Mentoring");
  s.addText("Mentoring in Hertfordshire is a culture, not a programme. It rests on four principles that run together, all the time. They are not stages.", { x: 0.6, y: 1.4, w: 12, h: 0.8, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, objectName: "Lead" });
  const defs = { Prepare: "Ready for each stage before it happens. There should never be any surprises.", Guide: "Accurate, honest, timely information. Never dependency.", Support: "Present, responsive, compassionate. “How can we help?”, never “Why aren’t you attending?”", Enlighten: "Understanding, curiosity and enjoyment of Freemasonry, for life." };
  PR.forEach(([nme, hex], i) => {
    const x = 0.6 + i * 3.1;
    s.addShape(pres.ShapeType.rect, { x, y: 2.5, w: 2.9, h: 1.1, fill: { color: hex }, line: { color: hex }, objectName: "Principle " + nme });
    s.addText([{ text: String(i + 1) + "  ", options: { color: "8FD3D1", fontSize: 18, bold: true } }, { text: nme.toUpperCase(), options: { color: "FFFFFF", fontSize: 20, bold: true } }], { x: x + 0.25, y: 2.5, w: 2.6, h: 1.1, valign: "middle", margin: 0, isTextBox: true });
    s.addShape(pres.ShapeType.rect, { x, y: 3.6, w: 2.9, h: 2.3, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, objectName: "Principle text " + nme });
    s.addText(defs[nme], { x: x + 0.25, y: 3.75, w: 2.4, h: 2.0, fontSize: 13.5, color: "06345D", margin: 0, isTextBox: true, valign: "top" });
  });
  s.addText("Family, Work, Masonry: in that order, always. Freemasonry must be fun.", { x: 0.6, y: 6.15, w: 12, h: 0.5, fontSize: 15, bold: true, italic: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Tagline" });
  notes(s, "Quote the principles as on the canon page. Stress: not stages. The tagline is the Province's house line.");

  s = content("The journey ahead", "1 Mentoring");
  const steps = [["Initiation", "Entered Apprentice. Your first night, the Festive Board, your mentor beside you", "003668"], ["Passing", "Fellow Craft. Usually six to twelve months on; you answer questions in open Lodge", "0A4F72"], ["Raising", "Master Mason. Visiting opens up fully; the Master Mason’s Guide", "106576"], ["One Journey", "The Royal Arch completes Pure Antient Masonry, on your timing: information, not recruitment", "157A7C"], ["Office", "Only when you are ready, and only if you want it. Both answers are valid", "06345D"]];
  steps.forEach(([t, d, hex], i) => {
    const x = 0.6 + i * 2.47, y = 1.7;
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.75, y, w: 0.8, h: 0.8, fill: { color: hex }, line: { color: hex }, objectName: "Step " + t });
    s.addText(String(i + 1), { x: x + 0.75, y, w: 0.8, h: 0.8, fontSize: 22, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    if (i < steps.length - 1) s.addShape(pres.ShapeType.line, { x: x + 1.6, y: y + 0.4, w: 0.85, h: 0, line: { color: "BFD6EA", width: 2 }, objectName: "Connector " + i });
    s.addText(t, { x, y: 2.7, w: 2.3, h: 0.5, fontSize: 18, bold: true, color: hex, align: "center", margin: 0, isTextBox: true });
    s.addText(d, { x, y: 3.2, w: 2.3, h: 1.8, fontSize: 12.5, color: "1E2329", align: "center", margin: 0, isTextBox: true, valign: "top" });
  });
  card(s, 0.6, 5.2, 12.1, 1.2, "Two rules that run through every stage", "There should never be any surprises: you will always know what is coming next. And you set the pace, never the calendar.", { fill: "E6F2F2", fontSize: 14 });
  notes(s, "Keep this high level. One Journey is Hertfordshire's name for the Craft to Royal Arch continuum; the Royal Arch Representative in each Lodge is the person to ask.");

  s = content("The basics: what to wear", "1 Mentoring");
  s.addText("Always check the Summons first. If it says nothing different, this is the standard.", { x: 0.6, y: 1.35, w: 12, h: 0.45, fontSize: 15, color: "06345D", margin: 0, isTextBox: true, objectName: "Lead" });
  card(s, 0.6, 1.95, 3.9, 4.45, "Suit and shirt", ["Dark lounge suit, preferably black", "Black and grey striped morning trousers with a black jacket are acceptable", "Plain white formal shirt, single or double cuff", "Tails only for Active Provincial Officers at Provincial Grand Lodge"], { icon: I.tie, fontSize: 15 });
  card(s, 4.7, 1.95, 3.9, 4.45, "Socks and shoes", ["Plain black socks. Not navy, not patterned, not novelty", "Black shoes, polished", "Not trainers, not boots, and definitely not Crocs", "White gloves where your Lodge wears them; ask your mentor"], { icon: I.socks, fontSize: 15 });
  card(s, 8.8, 1.95, 3.9, 4.45, "Black tie nights", ["Some Lodges dine black tie always, others only at Installation", "Dinner jacket, smart dress shirt, black bow tie", "The Summons will say. If in doubt, ask the Secretary or your mentor", "Jackets stay on at the Festive Board unless the Master says otherwise"], { icon: I.shoe, fontSize: 15 });
  notes(s, "Drawn from the poll FAQ. The socks question came up more than once; say it plainly.");

  s = content("Ties, pins, jewels and rings", "1 Mentoring");
  qa(s, 0.6, 1.4, 6.0, 2.4, "What tie should I wear?", "In any Hertfordshire Lodge, the Provincial tie is permitted. At FHLBC visits, Gladsmuir 1385 and Provincial Grand Lodge, the Club tie is fine. Visiting outside Hertfordshire, wear a plain Masonic tie (the square and compasses tie from shopatfmh.com is the safe choice). Some Lodges wear their own; no harm in asking at the bar.");
  qa(s, 6.75, 1.4, 6.0, 2.4, "Can I wear lapel pins?", "Yes. FHLBC members wear the Club pin. Typically three at most, and always Masonic or charitable, never political. They make a good talking point at the Festive Board.", "0A4F72");
  qa(s, 0.6, 3.95, 6.0, 2.5, "Can I wear jewels?", "Once you are a Master Mason, up to three in Lodge. The Royal Arch jewel sits nearest your centre line, then the Tercentenary jewel, then others. Only jewels you are entitled to, and no other orders’ jewels in a Craft Lodge except the Royal Arch. If in doubt, ask.", "106576");
  qa(s, 6.75, 3.95, 6.0, 2.5, "Rings and gloves?", "A Masonic ring divides opinion: some say Past Masters only, some say anyone, some say points inward until you have been through the Chair. Personal preference. Square and compasses on gloves: no firm rule, but avoid dark blue ones unless you hold Provincial or Grand rank.", "157A7C");
  notes(s, "All four answers are from the poll FAQ. Have a Club tie and pin to hold up.");

  s = content("Reading the Summons", "1 Mentoring");
  qa(s, 0.6, 1.4, 6.0, 1.6, "Full Dress / Undress. What is that?", "It applies to Provincial and Grand Officers, not to you yet. Undress is a plain dark blue collar and apron; Full Dress adds gold edging and frills. It tells those officers what regalia to bring.");
  qa(s, 6.75, 1.4, 6.0, 1.6, "What are the letters after names?", "Provincial or Grand Lodge ranks, Active or Past. Nobody minds being asked what theirs means. Ask.", "0A4F72");
  qa(s, 0.6, 3.15, 6.0, 1.55, "Do I have to attend?", "You should, and you will enjoy it more if you do. If you cannot, send apologies to the Secretary. Nobody will pressure you; if anything is making it hard, tell your mentor, the Almoner or anyone from the Club.", "106576");
  qa(s, 6.75, 3.15, 6.0, 1.55, "Can I attend Provincial Grand Lodge?", "Once you are a Master Mason. Until then, it is one to look forward to.", "157A7C");
  qa(s, 0.6, 4.85, 12.15, 1.55, "Taylor’s or Emulation?", "The two main workings in Hertfordshire. Emulation is the more relaxed; Taylor’s has more floorwork, including squaring the Lodge. Learned Taylor’s and asked to work in an Emulation Lodge? Fine. Emulation floorwork in a Taylor’s Lodge is likely to be frowned on. If in doubt, ask.", "06345D");
  notes(s, "Reassure: the Summons is a letter from your Lodge, not an exam paper.");

  // ---- glossary: eight terms a slide, two columns of four cards ----
  function glossaryCards(s, pairs) {
    pairs.forEach(([term, meaning], i) => {
      const col = i < 4 ? 0 : 1, row = i % 4;
      const x = 0.6 + col * 6.15, y = 1.4 + row * 1.27, w = 5.95, h = 1.15;
      s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Glossary " + term });
      s.addText(term, { x: x + 0.25, y: y + 0.1, w: 2.05, h: h - 0.2, fontSize: 13.5, bold: true, color: "003668", margin: 0, isTextBox: true, valign: "middle" });
      s.addText(meaning, { x: x + 2.45, y: y + 0.1, w: w - 2.7, h: h - 0.2, fontSize: 12.5, color: "1E2329", margin: 0, isTextBox: true, valign: "middle" });
    });
  }
  const WORDS = [
    ["Lodge", "The basic unit: a group of Freemasons who meet together, with a name and a number. Your Lodge elects a Master and officers each year."],
    ["Province", "The Lodges of a county area under a Provincial Grand Master. Hertfordshire is one; above the Province is Grand Lodge."],
    ["UGLE", "The United Grand Lodge of England, at Freemasons’ Hall, Great Queen Street: the governing body for English Freemasonry."],
    ["Summons", "The notice of a meeting: date, time, dress, the business, and who is doing what. Read it; most questions are answered in it."],
    ["Festive Board", "The meal after the meeting. Toasts, Masonic Fire, speeches, and the part of the evening where friendships are made."],
    ["Masonic Fire", "The pattern of applause that follows a toast. Your mentor will show you before your first Festive Board; nobody expects you to know it."],
    ["Lodge of Instruction", "The rehearsal, usually informal, run by the Preceptor. Where you learn what you saw, and where offices are learned."],
    ["Installation", "The meeting each year at which the new Master is installed and appoints his officers. Often black tie; often the biggest night."],
  ];
  const WORDS2 = [
    ["Initiation, Passing, Raising", "The three ceremonies that make you an Entered Apprentice, a Fellow Craft and a Master Mason."],
    ["Apron", "Worn by every Freemason in Lodge. White for an Entered Apprentice, then light blue, then dark blue for Provincial or Grand rank. Hence “light blue”."],
    ["Regalia and jewels", "Apron, collar for officers, and gloves. Jewels are the medals worn on the breast: charity festivals, the Royal Arch and the like."],
    ["Visiting", "Attending another Lodge’s meeting as a guest. Encouraged from the start; your mentor will take you the first time."],
    ["Risings", "The three points near the end of a meeting when the Master rises to ask for communications, apologies and other business."],
    ["Royal Arch, Chapter", "The completion of Pure Antient Masonry. A Chapter is to the Royal Arch what a Lodge is to the Craft; its members are Companions."],
    ["Proposer, Seconder", "The two members who put your name forward. Your Proposer is often, but not always, your Personal Mentor."],
    ["White Table", "A dinner to which partners are invited, sometimes with the untyled part of a meeting. Ladies Night is the Master’s formal dinner."],
  ];
  const LETTERS = [
    ["WM, IPM", "Worshipful Master; Immediate Past Master, who has just left the Chair and sits beside him."],
    ["SW, JW", "Senior and Junior Warden. With the Master, the three principal officers; the Wardens usually become Master in turn."],
    ["SD, JD, IG", "Senior Deacon, Junior Deacon, Inner Guard: the floor officers who conduct candidates and guard the door from inside."],
    ["DC, ADC", "Director of Ceremonies and his Assistant: in charge of how the meeting and the Festive Board run. Follow the DC."],
    ["Tyler", "The officer outside the door. The first person you met on your Initiation night."],
    ["Bro, W Bro, VW Bro, RW Bro", "Brother; Worshipful Brother, who has been Master; Very Worshipful and Right Worshipful for senior Grand rank."],
    ["EA, FC, MM", "Entered Apprentice, Fellow Craft, Master Mason: the three degrees."],
    ["PM", "Past Master in most Masonic writing. In Hertfordshire mentoring documents PM is also the Personal Mentor; context tells you which."],
  ];
  const LETTERS2 = [
    ["LM", "Lodge Mentor: the officer who co-ordinates mentoring in the Lodge and makes sure every new member has a Personal Mentor."],
    ["ProvGM, DepProvGM, APGM", "Provincial Grand Master, his Deputy, and the Assistant Provincial Grand Masters, each with an area of the Province."],
    ["ProvGMen, APGMen", "Provincial Grand Mentor and the Assistant Provincial Grand Mentors. Written this way so they are never confused with the Masters."],
    ["VO", "Visiting Officer: the Provincial officer who visits your Lodge on the Provincial Grand Master’s behalf. A friend, not an inspector."],
    ["LoI, CoI", "Lodge of Instruction; Chapter of Instruction, its Royal Arch equivalent."],
    ["PGL, GL", "Provincial Grand Lodge; Grand Lodge. PProvSGW, PAGDC and the like on a Summons are Past Provincial or Grand ranks."],
    ["FHLBC, DAWG", "Fleet House Light Blues Club; the Daily Advancement WhatsApp Group, run by the Provincial Mentoring Team."],
    ["Solomon, Hermes", "UGLE’s learning platform; UGLE’s membership administration system, which your Secretary uses."],
  ];
  s = content("Words you will hear", "1 Mentoring"); glossaryCards(s, WORDS);
  notes(s, "Nothing here is ritual. Invite them to shout any word they have heard and not understood; the second page has more.");
  s = content("Words you will hear, continued", "1 Mentoring"); glossaryCards(s, WORDS2);
  notes(s, "The glossary is also on the Provincial website; say so.");
  s = content("Letters you will see", "1 Mentoring"); glossaryCards(s, LETTERS);
  notes(s, "The ranks look like alphabet soup for about a year and then stop. Nobody minds being asked what theirs means.");
  s = content("Letters you will see, continued", "1 Mentoring"); glossaryCards(s, LETTERS2);
  notes(s, "ProvGMen and APGMen: explain the spelling once and move on.");

  s = content("The Festive Board", "1 Mentoring");
  card(s, 0.6, 1.4, 6.0, 2.45, "Etiquette", ["Light-hearted and fun, but the Lodge’s rules still apply: no religion, no politics", "Jackets on, unless the Master says otherwise in summer", "Phones away. A quick photo of dinner, fine; a running text conversation, not", "Need to take a call? Excuse yourself and leave the room"], { icon: I.utensils, fontSize: 13 });
  card(s, 6.75, 1.4, 6.0, 2.45, "Masonic Fire and the toasts", ["Your mentor will walk you through the order of toasts and the Fire before your first night", "Stand when the Director of Ceremonies stands; follow the Brother next to you", "You may be asked to reply to a toast. Here is how"], { icon: I.comment, fontSize: 13 });
  card(s, 0.6, 4.0, 12.15, 2.4, "Replying to a toast, in six lines", ["Start with “Worshipful Master, Distinguished Brethren, Brethren all”", "Thank the Lodge for the meeting, the work, and the Brother who invited or looked after you", "Mention one thing you enjoyed; one good piece of ritual is plenty", "Invite them to your next meeting", "One to two minutes. Do not rush, and do not give a best man’s speech", "You may move to where people can see you, but no laps of the room"], { fill: "E6F2F2", fontSize: 13 });
  notes(s, "Offer to send everyone a draft reply they can adapt; the Personal Mentor's Short Guide tells mentors to do this before Initiation night.");

  s = content("Visiting other Lodges", "1 Mentoring");
  qa(s, 0.6, 1.4, 6.0, 2.6, "Can I visit?", "Yes, and it is encouraged. You can visit any Lodge under UGLE. Contact the Lodge Secretary, introduce yourself and say who you are; you may be asked for proof of membership, though most visits start with an invitation. Visiting abroad? Ask the Provincial Secretary first, as Grand Lodge permission may be needed.");
  qa(s, 6.75, 1.4, 6.0, 2.6, "What will it be like?", "Different. Lodges work differently and that is half the point. Observe before judging, and never criticise another Lodge’s working. Sign in on arrival, say thank you to your hosts on the night and again afterwards, and expect to be asked to reply to the Visitors’ Toast.", "0A4F72");
  card(s, 0.6, 4.15, 12.15, 2.25, "Three easy first visits", ["Go with your mentor or a Brother from your Lodge the first time; nobody should visit alone until he wants to", "FHLBC visits are built for this: a group of light blues, a ceremony, a Festive Board and a host Lodge that is expecting you", "The Visitors’ Festival: each year the Province picks an exemplary First, Second and Third Degree for newly initiated, passed and raised Brethren to see, seated with the Mentoring Team"], { icon: I.door, fontSize: 13.5 });
  notes(s, "Brethren who visit are more confident, better informed and far more likely to stay. Isolation is one of the earliest predictors of leaving.");

  s = content("The questions you asked, and a few you will", "1 Mentoring");
  qa(s, 0.6, 1.4, 4.0, 2.45, "What do I tell people at work?", "The truth: you have joined a Lodge, you meet a few times a year, there is a dinner, and it raises a lot for charity. You will be surprised how many say “so is my dad”.");
  qa(s, 4.68, 1.4, 4.0, 2.45, "Can I post about it online?", "Yes, with judgement. Photos from the Festive Board and charity events are fine; anything from inside the Lodge room is not. Treat it as you would your employer’s name.", "0A4F72");
  qa(s, 8.76, 1.4, 4.0, 2.45, "Can my partner get involved?", "Yes. White Table evenings invite partners to dine, and sometimes into the untyled meeting. Ladies Night is the Master’s formal dinner each year, often with a dance, raising money for his charity. Most Lodges run socials too.", "106576");
  qa(s, 0.6, 4.0, 4.0, 2.4, "When will I take office?", "When you are ready and if you want to. Readiness runs both ways: nobody should push you early, and nobody should leave you waiting. Talk to your mentor.", "157A7C");
  qa(s, 4.68, 4.0, 4.0, 2.4, "What is the Royal Arch?", "The completion of Pure Antient Masonry, which UGLE encourages Master Masons to consider before other orders. Your Lodge’s Royal Arch Representative will explain it when you are ready. Information, not recruitment.", "06345D");
  qa(s, 8.76, 4.0, 4.0, 2.4, "What if I am struggling?", "Say so, early, to anyone: your mentor, the Almoner, the Club. Money, time, family, confidence. The question is always “How can we help?”. One resignation in three is recovered by a single honest conversation.", "003668");
  notes(s, "The last card matters most. Make eye contact and slow down.");

  // ================= 2 L&D =================
  pres.addSection({ title: "2 Learning and Development" });
  divider(2, "Learning and Development", "W Bro Tom Golds, Provincial Learning and Development Officer", "106576", "2 Learning and Development", "Solomon, the Academy diploma, the Lodge of Instruction and how to learn ritual without losing sleep");

  s = content("Solomon: UGLE's learning platform", "2 Learning and Development");
  card(s, 0.6, 1.4, 6.0, 2.5, "What it is", ["UGLE’s online learning hub: accurate, approved material for every stage of your journey", "Papers, Nuggets, presentations, quizzes and the Welcome modules", "Free, and open to every member of a UGLE Lodge", "The place to send yourself for an answer you can trust, rather than the internet"], { icon: I.book, fontSize: 13.5 });
  card(s, 6.75, 1.4, 6.0, 2.5, "Getting started tonight", ["Go to solomon.ugle.org.uk on your phone", "Create a login with your name, Lodge name and number", "Search “Getting Started with Solomon”, then “Welcome Apprentice”", "Follow @SolomonUGLE for a daily piece"], { icon: I.globe, fontSize: 13.5 });
  card(s, 0.6, 4.05, 12.15, 2.35, "Use it for the evenings you cannot attend", "When your Lodge works in a higher degree you cannot be in the room. That evening is not dead time: meet your mentor, open Solomon, and use it to explore the history, the symbolism of your own degree, or whatever you are curious about. Solomon sits alongside face-to-face conversation; it never replaces it.", { fill: "E6F2F2", fontSize: 14 });
  notes(s, "Live demo if the Wi-Fi allows. Keep it to two minutes: login, search, Welcome Apprentice.");

  s = content("Solomon Academy and the Diploma", "2 Learning and Development");
  const mods = [["Welcome Apprentice", "003668"], ["Welcome Fellow Craft", "0A4F72"], ["Welcome Master Mason", "106576"], ["Welcome Companion", "157A7C"]];
  mods.forEach(([m, hex], i) => {
    const x = 0.6 + i * 3.1;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.4, w: 2.9, h: 1.3, fill: { color: hex }, line: { color: hex }, rectRadius: 0.08, objectName: "Module " + m });
    s.addText([{ text: "Module " + (i + 1) + "\n", options: { fontSize: 11, color: "8FD3D1", bold: true } }, { text: m, options: { fontSize: 16, color: "FFFFFF", bold: true } }], { x: x + 0.2, y: 1.4, w: 2.6, h: 1.3, valign: "middle", margin: 0, isTextBox: true });
  });
  card(s, 0.6, 2.95, 6.0, 3.45, "How it works", ["Work through a module at your own pace; badges along the way", "A quiz at the end, based only on the module. Score 100% for a certificate; retake as often as you like", "A4 certificate signed by the Chair of UGLE’s Learning and Development Board", "All four certificates earn the Solomon Academy Diploma, signed by the Assistant Grand Master and the Third Grand Principal"], { icon: I.cert, fontSize: 13.5 });
  card(s, 6.75, 2.95, 6.0, 3.45, "What Hertfordshire does with it", ["Solomon does not tell the Province when you pass. You do", "Send your certificate, with your Lodge name and number, to mentor@hertfordshirefreemasons.org.uk", "The Mentoring Team arranges for it to be presented to you in your Lodge, with the Academy tie pin", "Do Welcome Companion when the time is right for you, not before; the Diploma waits"], { icon: I.graduation, fontSize: 13.5 });
  notes(s, "Confirm the presentation process is as stated; it mirrors the Metropolitan approach. Hold up a tie pin.");

  s = content("The Lodge of Instruction", "2 Learning and Development");
  qa(s, 0.6, 1.4, 6.0, 2.3, "What is it?", "A rehearsal for the next meeting, run by the Preceptor. The lines and the movements are walked through so everyone knows what to do on the night. Informal; shirt and tie usually not required. Royal Arch Chapters have the same thing, a Chapter of Instruction.");
  qa(s, 6.75, 1.4, 6.0, 2.3, "Should I go if I have no office?", "Yes. It is the fastest way to understand what you saw on your own night, to learn the questions for your next degree, and to belong. Ask your mentor when and where it meets and go with him the first time.", "0A4F72");
  card(s, 0.6, 3.85, 12.15, 2.55, "Two kinds of learning, and both are yours", ["Guided learning: what you need to take part. The questions and answers between degrees, the etiquette, the structure of the Craft. Planned, paced to you, and delivered by people who do it well", "Personal learning: what you want to explore. History, symbolism, the story of your own Lodge, the Royal Arch. Led by your curiosity and welcomed for life", "Nobody has to learn more ritual than the questions and answers. Many find they want to, and enjoy it. Either way you are a full member of your Lodge"], { icon: I.school, fontSize: 13.5 });
  notes(s, "Per UGLE guidance: not everyone wishes to learn ritual, and that is fine. The minimum is the questions and answers between degrees.");

  s = content("Learning ritual without losing sleep", "2 Learning and Development");
  const tips = [["Start early", "Three to six months before you deliver it. Nobody learns ritual the week before."], ["Little and often", "Ten minutes a day beats an hour on Sunday. Use committed time: the commute, the dog walk."], ["Read, then read aloud", "Silently first, over and over. Look up any word you do not understand. Then out loud, over and over."], ["Record it", "Once your phrasing is right, record yourself, or ask your mentor to, and play it daily."], ["One sentence at a time", "Say one from memory. Add the next. Build the passage up; never try to swallow it whole."], ["Hold the book", "Ask someone to follow the book and tell you where you went wrong afterwards, not during. Never a non-Mason for anything that touches the secrets."], ["Say it in the room", "Rehearse in the Lodge room with one other person, then at the Lodge of Instruction with the group."], ["Understand it", "Words you understand stay learned. Ask what a passage means. Solomon and your mentor will tell you."]];
  tips.forEach(([t, d], i) => {
    const col = i % 4, row = Math.floor(i / 4);
    const x = 0.6 + col * 3.08, y = 1.4 + row * 2.55;
    s.addShape(pres.ShapeType.roundRect, { x, y, w: 2.9, h: 2.4, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Tip " + (i + 1) });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.2, y: y + 0.18, w: 0.5, h: 0.5, fill: { color: PR[col][1] }, line: { color: PR[col][1] }, objectName: "Tip number " + (i + 1) });
    s.addText(String(i + 1), { x: x + 0.2, y: y + 0.18, w: 0.5, h: 0.5, fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(t, { x: x + 0.8, y: y + 0.18, w: 2.0, h: 0.5, fontSize: 14, bold: true, color: "003668", margin: 0, isTextBox: true, valign: "middle" });
    s.addText(d, { x: x + 0.2, y: y + 0.8, w: 2.5, h: 1.5, fontSize: 11.5, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  });
  notes(s, "Based on UGLE's Learning Ritual guidance (Members' Pathway, ENGAGE). The non-Mason point matters: a partner can hold the book for a charge, never for anything covered by the obligation.");

  s = content("More ways to learn, all free", "2 Learning and Development");
  card(s, 0.6, 1.4, 3.9, 2.4, "DAWG", "The Daily Advancement WhatsApp Group, run by the Provincial Mentoring Team: a daily piece of Masonic interest and a community of mentors and new Masons. Ask tonight to be added.", { icon: I.whatsapp, fontSize: 14 });
  card(s, 4.7, 1.4, 3.9, 2.4, "Mentoring and L&D evenings", "Twice a year the Province brings new Brethren together with the mentoring and learning teams. Tonight is one of them. Come to the next.", { icon: I.calendar, fontSize: 14 });
  card(s, 8.8, 1.4, 3.9, 2.4, "The Visitors’ Festival", "An exemplary First, Second and Third Degree each year, chosen for newly initiated, passed and raised Brethren to see as visitors.", { icon: I.ticket, fontSize: 14 });
  card(s, 0.6, 3.95, 3.9, 2.45, "Your guides", "The Initiate’s, Fellow Craft’s and Master Mason’s Guides from UGLE, handed to you after each ceremony. Read them; then ask your mentor about anything in them.", { icon: I.book, fontSize: 14 });
  card(s, 4.7, 3.95, 3.9, 2.45, "Talks and papers", "Many Lodges host a speaker when there is no ceremony. Solomon has hundreds of papers you can read or present yourself; a ten-minute Nugget is a good first piece of work in Lodge.", { icon: I.lightbulb, fontSize: 14 });
  card(s, 8.8, 3.95, 3.9, 2.45, "Ask", "The Brother next to you at the Festive Board has forgotten more than you have learned. He will be delighted to be asked. That is what the Festive Board is for.", { icon: I.handshake, fontSize: 14 });
  notes(s, "Add any Provincial L&D programme details the L&D Officer wants to include, e.g. forthcoming talks.");

  // ================= 3 FHLBC =================
  pres.addSection({ title: "3 Fleet House Light Blues Club" });
  divider(3, "Fleet House Light Blues Club", "Bro Aaron Ball, FHLBC Communications Officer", "157A7C", "3 Fleet House Light Blues Club", "Your club: for every Brother in a white or light blue apron, from tonight");

  s = content("The club for the first part of your journey", "3 Fleet House Light Blues Club");
  s.addText("The Fleet House Light Blues Club exists to engage and support Brethren early in their Masonic life, through events you choose to attend. It is run by its members, for its members, and it is where most new Masons in Hertfordshire make their first friends outside their own Lodge.", { x: 0.6, y: 1.4, w: 12.1, h: 1.1, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, valign: "top", objectName: "Lead" });
  card(s, 0.6, 2.75, 3.9, 3.65, "Explore", ["Invitations to Lodge meetings across Hertfordshire", "Special ceremonies and Festive Boards, as a group of light blues with a host Lodge expecting you", "The easy way to start visiting"], { icon: I.compass, fontSize: 15, headColor: "003668" });
  card(s, 4.7, 2.75, 3.9, 3.65, "Discover", ["Trips to Masonic landmarks and tours", "Talks by guest speakers", "Demonstrations, such as the Emulation Lodge of Improvement at Freemasons’ Hall"], { icon: I.lightbulb, fontSize: 15, headColor: "106576" });
  card(s, 8.8, 2.75, 3.9, 3.65, "Engage", ["Relaxed social events", "A members-only WhatsApp group", "A newsletter with reports and Masonic news", "A committee of Brethren who were new not long ago"], { icon: I.users, fontSize: 15, headColor: "157A7C" });
  notes(s, "Source: fhlbc.co.uk. Explore, Discover, Engage are the club's own three headings.");

  s = content("Who can join, and what it costs", "3 Fleet House Light Blues Club");
  card(s, 0.6, 1.4, 6.0, 2.6, "Who", ["Any Freemason who lives, works or meets in Hertfordshire", "Who has not received Provincial, Grand or Metropolitan rank, past or present, anywhere", "Entered Apprentice, Fellow Craft, Master Mason, Master or Past Master: if you wear a white or light blue apron, you are in", "Yes, an Entered Apprentice can join. Tonight."], { icon: I.check, fontSize: 13.5 });
  card(s, 6.75, 1.4, 6.0, 2.6, "What it costs", ["Membership: £25 to join, then £10 a year", "Entered Apprentices: £10 a year", "Renewal: £10 a year", "You receive a welcome pack and the members’ pin, and an invitation to the WhatsApp group"], { icon: I.pound, fontSize: 13.5 });
  card(s, 0.6, 4.15, 12.15, 2.25, "How to join: two minutes on your phone", ["fhlbc.co.uk/join-us, choose the membership that applies to you, follow the payment instructions", "The welcome pack follows, with the WhatsApp invitation", "Questions: Secretary@fhlbc.co.uk, or any committee member in this room"], { fill: "E6F2F2", icon: I.globe, fontSize: 14 });
  notes(s, "Prices as published at fhlbc.co.uk/join-us at the time of writing; check before the evening.");

  s = content("What's coming up", "3 Fleet House Light Blues Club");
  const ev = [["Fri 16 October", "Emulation Lodge of Improvement", "Freemasons’ Hall, London. A Second Degree demonstration by the Emulation Lodge of Improvement, with a buffet. 6.00 to 9.00 pm.", "003668"], ["Fri 30 October", "Gladsmuir Passing Ceremony", "Gladsmuir Lodge No. 1385, Radlett. A Passing, a three-course Festive Board, and Solomon Academy tie pin presentations. 6.00 to 9.30 pm.", "106576"], ["Sun 15 November", "FHLBC Annual General Meeting", "Halsey Hall, Cheshunt. Free for members, sausage and mash afterwards. Come and have a say in what the club does next year. 6.00 to 9.00 pm.", "157A7C"]];
  ev.forEach(([d, t, desc, hex], i) => {
    const y = 1.4 + i * 1.7;
    s.addShape(pres.ShapeType.roundRect, { x: 0.6, y, w: 12.1, h: 1.5, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Event " + (i + 1) });
    s.addShape(pres.ShapeType.roundRect, { x: 0.8, y: y + 0.2, w: 2.3, h: 1.1, fill: { color: hex }, line: { color: hex }, rectRadius: 0.08, objectName: "Event date " + (i + 1) });
    s.addText(d, { x: 0.8, y: y + 0.2, w: 2.3, h: 1.1, fontSize: 16, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(t, { x: 3.4, y: y + 0.18, w: 9.0, h: 0.5, fontSize: 18, bold: true, color: hex, margin: 0, isTextBox: true, valign: "middle" });
    s.addText(desc, { x: 3.4, y: y + 0.7, w: 9.0, h: 0.75, fontSize: 13, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  });
  s.addText("Full details and booking at fhlbc.co.uk/events. Events listed as at the date of this deck; confirm before the evening.", { x: 0.6, y: 6.5, w: 12.1, h: 0.4, fontSize: 11, italic: true, color: "06345D", margin: 0, isTextBox: true, objectName: "Events note" });
  notes(s, "Update the three events before each delivery. The Gladsmuir evening is the one to push for anyone about to be passed.");

  s = content("The Club tie and pin", "3 Fleet House Light Blues Club");
  card(s, 0.6, 1.4, 6.0, 5.0, "Where the Club tie is right", ["At any FHLBC visit within Hertfordshire", "At Gladsmuir Lodge No. 1385", "At Provincial Grand Lodge", "In your own Lodge, if your Lodge is happy with it; the Provincial tie is always permitted in a Hertfordshire Lodge", "Outside Hertfordshire, wear a plain Masonic tie instead"], { icon: I.tie, fontSize: 16 });
  card(s, 6.75, 1.4, 6.0, 5.0, "The pin", ["Members wear the Club pin on the lapel", "Up to three pins is the convention; Masonic or charitable only", "It is a conversation starter at any Festive Board: “You’re a light blue? Which Lodge?”", "Ties, pins and more at fhlbc.co.uk/fhlbc-merchandise"], { icon: I.pin, fontSize: 16 });
  notes(s, "Tie rules from the poll FAQ. Have stock on the table if possible.");

  // ================= CLOSE =================
  pres.addSection({ title: "Close" });
  s = content("Three things to do this week", "Close");
  [["1", "Join the Club", "fhlbc.co.uk/join-us. Two minutes. Then say hello on the WhatsApp group.", "003668", I.users],
   ["2", "Sign up to Solomon", "solomon.ugle.org.uk. Start Welcome Apprentice, or whichever module is yours. One certificate is one step to the Diploma.", "106576", I.book],
   ["3", "Message your mentor", "Tell him one thing from tonight you want to talk about. If you are not sure who your Personal Mentor is, that is the message.", "157A7C", I.comment]].forEach(([num, t, d, hex, ic], i) => {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.5, w: 3.85, h: 4.6, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Action " + num });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.3, y: 1.85, w: 1.0, h: 1.0, fill: { color: hex }, line: { color: hex }, objectName: "Action circle " + num });
    s.addText(num, { x: x + 0.3, y: 1.85, w: 1.0, h: 1.0, fontSize: 30, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(t, { x: x + 0.3, y: 3.1, w: 3.3, h: 0.6, fontSize: 20, bold: true, color: hex, margin: 0, isTextBox: true, valign: "middle" });
    s.addText(d, { x: x + 0.3, y: 3.8, w: 3.3, h: 2.1, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  });
  notes(s, "Ask for a show of hands at the end of the evening on each.");

  s = pres.addSlide({ masterName: "SECTION", sectionTitle: "Close" });
  s.addText("Your questions", { x: 0.9, y: 2.3, w: 11.5, h: 1.3, fontSize: 54, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, objectName: "Questions title" });
  s.addText("From the cards, and from the floor. If we do not know, we will say so and come back to you through your Lodge Mentor.", { x: 0.9, y: 3.7, w: 11, h: 1.0, fontSize: 20, color: "BFD6EA", margin: 0, isTextBox: true, objectName: "Questions sub" });
  notes(s, "Read each card aloud without naming the writer. Unknown answers go back via the Lodge Mentor in writing.");

  s = content("Thank you. Stay in touch", "Close");
  card(s, 0.6, 1.4, 3.9, 3.0, "Provincial Mentoring Team", ["mentor@hertfordshirefreemasons.org.uk", "Provincial Office, Fleet House, 10 Parkway, St Albans AL3 6PA", "01727 833061"], { icon: I.envelope, fontSize: 14 });
  card(s, 4.7, 1.4, 3.9, 3.0, "Learning and Development", ["solomon.ugle.org.uk", "Your Lodge Mentor for the Lodge of Instruction and the Visitors’ Festival", "DAWG: ask to be added tonight"], { icon: I.graduation, fontSize: 14 });
  card(s, 8.8, 1.4, 3.9, 3.0, "Fleet House Light Blues Club", ["fhlbc.co.uk", "Secretary@fhlbc.co.uk", "Join at fhlbc.co.uk/join-us"], { icon: I.users, fontSize: 14 });
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 4.6, w: 12.1, h: 1.8, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Closing band" });
  s.addText([{ text: "Freemasonry must be fun. ", options: { bold: true, color: "8FD3D1" } }, { text: "A man who is enjoying himself attends; a man who attends participates; a man who participates belongs; and a man who belongs does not resign. Thank you for coming. Now, the bar.", options: { color: "FFFFFF" } }], { x: 0.9, y: 4.75, w: 11.5, h: 1.5, fontSize: 17, margin: 0, isTextBox: true, valign: "middle", objectName: "Closing text" });
  notes(s, "Close on the house line. Thank the host Lodge and the caterers by name.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("written", OUT);
})().catch(e => { console.error(e); process.exit(1); });
