// Twenty shareable WhatsApp cards, Hertfordshire Provincial Mentoring brand. 1080x1080 JPEG.
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const OUT = process.argv[2]; fs.mkdirSync(OUT, { recursive: true });
const shield = "data:image/png;base64," + fs.readFileSync(path.join(__dirname, "../art/PGLH-Shield-header.png")).toString("base64");
const font = (w) => "data:font/woff2;base64," + fs.readFileSync(path.join(__dirname, `fonts/dm-sans-latin-${w}-normal.woff2`)).toString("base64");
const C = { prepare: "#003668", guide: "#0A4F72", support: "#106576", enlighten: "#157A7C", dark: "#06345D", pale: "#F2F7FC", sky: "#BFD6EA", mint: "#8FD3D1", paleteal: "#E6F2F2", ink: "#1E2329" };

const cards = [
  { n: 1, kicker: "Hertfordshire mentoring", head: "Prepare • Guide • Support • Enlighten", body: "Four principles, practised together, from first enquiry to beyond the Chair. Not stages: habits.", layout: "principles" },
  { n: 2, kicker: "In that order, always", head: "Family. Work. Masonry.", body: "A member managing a busy life is not disengaged. Freemasonry fits into his life; it does not demand that his life fit around it.", layout: "dark" },
  { n: 3, kicker: "Freemasonry must be fun", head: "A man who is enjoying himself attends.", body: "A man who attends participates. A man who participates belongs. And a man who belongs does not resign.", layout: "light" },
  { n: 4, kicker: "The right question", head: "“How can we help?”", body: "Never “Why weren’t you there?”. The first opens a door; the second puts a man on the defensive.", layout: "teal" },
  { n: 5, kicker: "Did you know?", head: "Two windows.", body: "Most members who leave do so in their first two years, or in the year after the Chair. A Master is standing in both at once.", layout: "dark" },
  { n: 6, kicker: "Design the moment", head: "His second meeting is the one everyone forgets.", body: "Hero of his Initiation; then mostly business, and nobody told him. A word before, a seat beside his mentor, a Brother briefed to include him.", layout: "light" },
  { n: 7, kicker: "Did you know?", head: "The Secretary cannot accept a resignation.", body: "He acknowledges receipt only. The member then has sixty days to withdraw it. Sixty days is a conversation, not a formality.", src: "Rule 183, Book of Constitutions", layout: "teal" },
  { n: 8, kicker: "Did you know?", head: "Your signature keeps the door open.", body: "A Brother who has resigned from every Lodge may visit one Lodge three times in a year with a view to joining, if the Master confirms it in writing.", src: "Rule 127, Book of Constitutions", layout: "dark" },
  { n: 9, kicker: "Early intervention", head: "Two misses. Seven days.", body: "After two consecutive meetings missed, a call within seven days of the second. A welfare call, never a whip: he was missed, and several Brethren asked after him.", layout: "light" },
  { n: 10, kicker: "Readiness, not pressure", head: "A bored Brother leaves as surely as a frightened one.", body: "No office before he is ready. No capable man left waiting. The office queue is a mentoring decision.", layout: "teal" },
  { n: 11, kicker: "One Journey", head: "Information, not recruitment.", body: "The Royal Arch completes Pure Antient Masonry, on his timing. Never a surprise, never a sales pitch. The decision is his alone.", layout: "dark" },
  { n: 12, kicker: "Did you know?", head: "The Grand Lodge Certificate is a passport, not a picture.", body: "Presented as soon as it arrives, kept with his regalia, never held back until he next attends. Make the presentation a moment.", layout: "light" },
  { n: 13, kicker: "Did you know?", head: "Five to open.", body: "Five Brethren, not counting the Tyler and the candidate; two of them members; one an Installed Master. A small Lodge needs its Past Masters.", src: "Rule 119, Book of Constitutions", layout: "teal" },
  { n: 14, kicker: "Did you know?", head: "Four weeks is a minimum, not a target.", body: "A candidate who waits a year for his Second Degree is a candidate at risk. Double ceremonies and a Degree by Request are there to be used.", src: "Rule 172", layout: "dark" },
  { n: 15, kicker: "After the Chair", head: "A seat is not a purpose.", body: "The Immediate Past Master is not an officer of the Lodge. Included, Involved, Interested: a role, a project, a Brother to mentor. Agree it before Installation.", layout: "light" },
  { n: 16, kicker: "Did you know?", head: "Spring Initiates are more likely to leave.", body: "The summer break interrupts their first months. Plan deliberate contact and one social touchpoint for every Brother initiated between January and June.", layout: "teal" },
  { n: 17, kicker: "We are all mentors", head: "Past Masters make the best Personal Mentors.", body: "They remember what the Chair cost and what it gave. Who in your Lodge will take a Brother this year?", layout: "dark" },
  { n: 18, kicker: "Warning signs", head: "The pattern is the signal.", body: "A Brother who has always come twice a year is content. A stalwart who stops coming is not. Watch for the break in his own pattern.", layout: "light" },
  { n: 19, kicker: "Tonight", head: "Never let a new member dine alone.", body: "Who he sits with at his first three Festive Boards decides what he thinks Freemasonry is. Move seats.", layout: "teal" },
  { n: 20, kicker: "Every month", head: "First Tuesday, 7pm, on Teams.", body: "The Provincial mentoring call: open to every Lodge Mentor and Personal Mentor. Bring a question, share what works.", src: "mentor@hertfordshirefreemasons.org.uk", layout: "dark" },
];

const css = `
@font-face{font-family:"DM Sans";font-weight:400;src:url(${font(400)}) format("woff2")}
@font-face{font-family:"DM Sans";font-weight:500;src:url(${font(500)}) format("woff2")}
@font-face{font-family:"DM Sans";font-weight:700;src:url(${font(700)}) format("woff2")}
@font-face{font-family:"DM Sans";font-weight:800;src:url(${font(800)}) format("woff2")}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1080px;font-family:"DM Sans",sans-serif;-webkit-font-smoothing:antialiased}
.card{position:relative;width:1080px;height:1080px;overflow:hidden;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:flex-start;padding:56px 64px 0 64px}
.brand{font-size:30px;font-weight:700;letter-spacing:-0.01em}
.brand small{display:block;font-size:20px;font-weight:500;opacity:.85;margin-top:4px;letter-spacing:.01em}
.shield{width:118px;height:auto;display:block}
.sb{padding:0}
.dark .sb,.teal .sb{background:#fff;border-radius:16px;padding:12px 14px}
.main{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 64px 24px 64px}
.kicker{font-size:26px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:26px}
.head{font-size:76px;line-height:1.06;font-weight:800;letter-spacing:-0.025em;margin-bottom:34px}
.head.long{font-size:64px}
.body{font-size:34px;line-height:1.38;font-weight:400;max-width:900px}
.src{font-size:24px;font-weight:500;margin-top:30px;opacity:.85}
.foot{display:flex;justify-content:space-between;align-items:center;padding:0 64px 36px 64px;font-size:22px;font-weight:500}
.strip{display:flex;height:22px}.strip div{flex:1}
.panel{border-left:14px solid; padding-left:36px}
/* layouts */
.dark{background:${C.prepare};color:#fff}.dark .kicker{color:${C.mint}}.dark .src,.dark .foot{color:${C.sky}}
.light{background:#fff;color:${C.ink}}.light .kicker{color:${C.enlighten}}.light .head{color:${C.prepare}}.light .src,.light .foot{color:${C.guide}}
.teal{background:${C.enlighten};color:#fff}.teal .kicker{color:${C.mint}}.teal .src,.teal .foot{color:${C.paleteal}}
.principles{background:${C.pale};color:${C.ink}}.principles .kicker{color:${C.guide}}.principles .head{display:none}
.pr{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:10px 0 30px 0}
.pr div{color:#fff;padding:30px 30px;border-radius:10px;min-height:190px}
.pr b{display:block;font-size:40px;font-weight:800;letter-spacing:.02em;margin-bottom:10px}
.pr span{font-size:24px;line-height:1.3;font-weight:400}
`;

function html(c) {
  const long = c.head.length > 34 ? " long" : "";
  const principles = c.layout === "principles" ? `<div class="pr">
    <div style="background:${C.prepare}"><b>1 PREPARE</b><span>Ready for each stage before it happens. There should never be any surprises.</span></div>
    <div style="background:${C.guide}"><b>2 GUIDE</b><span>Accurate, honest, timely information. Never dependency.</span></div>
    <div style="background:${C.support}"><b>3 SUPPORT</b><span>Present, responsive, compassionate. “How can we help?”</span></div>
    <div style="background:${C.enlighten}"><b>4 ENLIGHTEN</b><span>Understanding, curiosity and enjoyment of Freemasonry, for life.</span></div></div>` : "";
  return `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body>
  <div class="card ${c.layout}">
    <div class="top"><div class="brand">Provincial Mentoring<small>Provincial Grand Lodge of Hertfordshire</small></div><div class="sb"><img class="shield" src="${shield}"></div></div>
    <div class="main"><div class="kicker">${c.kicker}</div>${principles}<div class="head${long}">${c.head}</div><div class="body">${c.body}</div>${c.src ? `<div class="src">${c.src}</div>` : ""}</div>
    <div class="foot"><span>Prepare • Guide • Support • Enlighten</span><span>${String(c.n).padStart(2, "0")} / 20</span></div>
    <div class="strip"><div style="background:${C.prepare}"></div><div style="background:${C.guide}"></div><div style="background:${C.support}"></div><div style="background:${C.enlighten}"></div></div>
  </div></body></html>`;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  for (const c of cards) {
    await page.setContent(html(c), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const slug = c.head.replace(/[“”.,:!?•]/g, "").replace(/\s+/g, " ").trim().split(" ").slice(0, 5).join(" ");
    const file = path.join(OUT, `WA ${String(c.n).padStart(2, "0")} ${slug}.jpg`);
    await page.screenshot({ path: file, type: "jpeg", quality: 92 });
    console.log("wrote", path.basename(file));
  }
  await browser.close();
})();
