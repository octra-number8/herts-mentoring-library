"""Convert a pandoc-gfm markdown export of a library document onto the Hertfordshire Mentoring template.
Usage: md2hm.py <template.docx> <in.md> <out.docx> --ref "B1" --title "Lodge Mentor's Guide" --doctype "Practitioner handbooks · B1"
       --purpose "..." --meta "Audience=...;Issue=..." [--skip-until "# Foreword"] [--drop-contents]
Handles: #/##/### headings, paragraphs with **bold** and *italic*, - bullets, pipe tables (first row header if bold or if --header-tables),
single-cell HTML tables -> panels, multi-column HTML tables -> header tables, blockquotes -> panels."""
import sys, os, re, argparse, html
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL, FULL_WIDTH

ap = argparse.ArgumentParser()
ap.add_argument("template"); ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--ref", required=True); ap.add_argument("--title", required=True); ap.add_argument("--doctype", required=True)
ap.add_argument("--purpose", default=""); ap.add_argument("--meta", default=""); ap.add_argument("--skip-until", default=None)
ap.add_argument("--drop-contents", action="store_true"); ap.add_argument("--foreword-panel", action="store_true")
ap.add_argument("--stop-at", default=None); ap.add_argument("--plain-headings", action="store_true")
a = ap.parse_args()


class HB(Builder):
    def table(self, rows, widths, **kw):
        t = super().table(rows, widths, **kw)
        if len(rows) <= 6:
            for r in t.rows[:-1]:
                for c in r.cells:
                    for pp in c.paragraphs: pp.paragraph_format.keep_with_next = True
        return t


b = HB(a.template, a.out, doc_title=a.title)
meta = [tuple(x.split("=", 1)) for x in a.meta.split(";") if "=" in x]
b.opening(a.doctype, a.title, a.purpose, meta)

lines = open(a.src, encoding="utf8").read().split("\n")
if a.skip_until:
    for i, l in enumerate(lines):
        if l.strip().startswith(a.skip_until):
            lines = lines[i:]; break
if a.stop_at:
    for i, l in enumerate(lines):
        if l.strip().startswith(a.stop_at):
            lines = lines[:i]; break


def clean(s):
    s = html.unescape(s)
    s = s.replace("\\'", "’").replace("\\\"", "\"").replace("\\.", ".").replace("\\-", "-").replace("\\|", "|").replace("\\*", "*").replace("\\_", "_").replace("\\[", "[").replace("\\]", "]").replace("\\#", "#")
    s = re.sub(r"<[^>]+>", "", s)
    return s.strip()


def md_inline(s):
    # convert markdown bold/italics to the Builder's **bold** / *italic* which _runs understands; already same syntax
    return clean(s)


def flush_para(buf):
    if not buf: return
    text = " ".join(x.strip() for x in buf).strip()
    if not text: return
    if text.startswith("> "):
        b.panel([md_inline(text[2:])], fill=PALE, bar=TEAL); return
    b.para(md_inline(text), after=6)


i = 0; para = []; bullets = []
n = len(lines)
h1_counter = 0
while i < n:
    l = lines[i]
    s = l.strip()
    # ---- HTML table block
    if s.startswith("<table>"):
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        j = i
        while j < n and not lines[j].strip().startswith("</table>"): j += 1
        block = "\n".join(lines[i:j + 1]); i = j + 1
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", block, flags=re.S)
        parsed = []
        for r in rows:
            cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, flags=re.S)
            parsed.append(cells)
        if len(parsed) == 1 and len(parsed[0]) == 1:
            cell = parsed[0][0]
            paras = re.findall(r"<p>(.*?)</p>", cell, flags=re.S) or [cell]
            paras = [clean(p.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")) for p in paras]
            if len(paras) >= 2 and paras[0].startswith("**") and len(paras[0]) < 60:
                lab = paras[0].strip("*"); body = " ".join(paras[1:])
                fill, bar = (PALETEAL, TEAL) if lab.lower().startswith("good") else (PALE, DEEP)
                b.panel([f"**{lab}.** {body}"], fill=fill, bar=bar)
            else:
                b.panel(paras, fill=PALE, bar=DEEP)
        else:
            cols = max(len(r) for r in parsed)
            ws = [FULL_WIDTH // cols] * cols
            if cols == 4: ws = [1100, 1600, 1500, FULL_WIDTH - 4200]
            if cols == 2: ws = [2400, FULL_WIDTH - 2400]
            if cols == 3: ws = [1500, 2600, FULL_WIDTH - 4100]
            rr = []
            for r in parsed:
                r = r + [""] * (cols - len(r))
                rr.append([clean(c.replace("<strong>", "").replace("</strong>", "").replace("<p>", "").replace("</p>", " ")) for c in r])
            hdr = "<th" in block
            b.table(rr, ws, header=hdr)
        continue
    # ---- pipe table
    if s.startswith("|"):
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        rows = []
        while i < n and lines[i].strip().startswith("|"):
            row = lines[i].strip()
            if re.match(r"^\|[\s:|-]+\|$", row): i += 1; continue
            cells = [c.strip() for c in row.strip("|").split("|")]
            rows.append(cells); i += 1
        cols = max(len(r) for r in rows)
        rows = [r + [""] * (cols - len(r)) for r in rows]
        first_blank = all(c == "" for c in rows[0])
        if first_blank: rows = rows[1:]
        header = (not first_blank) and all(c.startswith("**") and c.endswith("**") for c in rows[0] if c) and len(rows) > 1 and not all(c.startswith("**") for c in rows[1] if c)
        if header: rows[0] = [c.strip("*") for c in rows[0]]
        rr = [[clean(c) for c in r] for r in rows]
        # strip bold from first column labels (template shades/bolds them)
        for r in rr[(1 if header else 0):]:
            if r[0].startswith("**") and r[0].endswith("**"): r[0] = r[0].strip("*")
        if cols == 2: ws = [2400, FULL_WIDTH - 2400]
        elif cols == 3: ws = [1200, 2600, FULL_WIDTH - 3800]
        else: ws = [FULL_WIDTH // cols] * cols
        b.table(rr, ws, header=header)
        continue
    # ---- July-style headings: "1\. Title" or a bold-only short line
    mnum = re.match(r"^(\d+)\\?\.\s+([A-Z].*)$", s)
    if mnum and len(s) < 90 and not s.endswith("."):
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        b.h1(mnum.group(1), clean(mnum.group(2))); i += 1; continue
    mb = re.match(r"^\*\*([^*]{3,80})\*\*$", s)
    if mb and i + 1 < n and lines[i + 1].strip() == "" and not re.match(r"^\*\*(HERTFORDSHIRE|Issue|Contents)", s):
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        b.h2(clean(mb.group(1))); i += 1; continue
    if a.plain_headings and re.match(r"^[A-Z][A-Za-z'’,:\- ]{3,70}$", s) and not s.endswith(".") and i + 1 < n and lines[i + 1].strip() == "" and (i == 0 or lines[i - 1].strip() == ""):
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        b.h1("", clean(s)); i += 1; continue
    # ---- headings
    m = re.match(r"^(#{1,3})\s+(.*)$", s)
    if m:
        flush_para(para); para = []
        if bullets: b.bullets([md_inline(x) for x in bullets]); bullets = []
        level, text = len(m.group(1)), clean(m.group(2))
        if a.drop_contents and text.lower() == "contents":
            i += 1
            while i < n and not re.match(r"^#{1,3}\s", lines[i]): i += 1
            continue
        if level == 1:
            mm = re.match(r"^(\d+)\.\s+(.*)$", text)
            if mm: b.h1(mm.group(1), mm.group(2))
            else: b.h1("", text)
        elif level == 2:
            b.h2(text)
        else:
            b.para(text, bold=True, color=DEEP, before=4, after=2, keep=True)
        i += 1; continue
    # ---- bullets
    if re.match(r"^[-*]\s+", s):
        flush_para(para); para = []
        bullets.append(re.sub(r"^[-*]\s+", "", s)); i += 1
        # continuation lines
        while i < n and lines[i].startswith("  ") and lines[i].strip() and not re.match(r"^[-*]\s+", lines[i].strip()):
            bullets[-1] += " " + lines[i].strip(); i += 1
        continue
    if s == "":
        flush_para(para); para = []
        if bullets and (i + 1 >= n or not re.match(r"^[-*]\s+", lines[i + 1].strip())):
            b.bullets([md_inline(x) for x in bullets]); bullets = []
        i += 1; continue
    para.append(s); i += 1

flush_para(para)
if bullets: b.bullets([md_inline(x) for x in bullets])
print("saved", b.save())
