// Hertfordshire Provincial Mentoring — shared pptxgenjs brand kit.
// const kit = await require("./hmslides.js").create({ shield, title, author, footer }); ... await kit.finish(out)
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");
const FA = require("react-icons/fa");

const THEME = {
  name: "Hertfordshire Provincial Mentoring",
  headFontFace: "DM Sans", bodyFontFace: "DM Sans",
  colors: { dk1: "1E2329", lt1: "FFFFFF", dk2: "003668", lt2: "F2F7FC", accent1: "003668", accent2: "0A4F72", accent3: "106576", accent4: "157A7C", accent5: "06345D", accent6: "BFD6EA", hlink: "157A7C", folHlink: "0A4F72" },
};
const PR = [["Prepare", "003668"], ["Guide", "0A4F72"], ["Support", "106576"], ["Enlighten", "157A7C"]];
const W = 13.33, H = 7.5;

async function icon(name, hex, px = 256) {
  const Comp = FA[name]; if (!Comp) throw new Error("no icon " + name);
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + hex, size: px }));
  return "image/png;base64," + (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
}

async function create({ shield, title, author, footer }) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = title; pres.author = author || "Hertfordshire Provincial Mentoring Team";

  function strip(objs, y, h) { const w = W / 4; PR.forEach(([n, hex], i) => objs.push({ rect: { x: i * w, y, w, h, fill: { color: hex } } })); }
  (function () {
    const objects = [];
    objects.push({ text: { text: "Provincial Mentoring", options: { x: 0.6, y: 0.45, w: 8, h: 0.6, fontSize: 24, bold: true, color: "003668", margin: 0 } } });
    objects.push({ text: { text: "Provincial Grand Lodge of Hertfordshire", options: { x: 0.6, y: 1.0, w: 8, h: 0.35, fontSize: 13, color: "06345D", margin: 0 } } });
    objects.push({ text: { text: "Prepare • Guide • Support • Enlighten", options: { x: 0.6, y: 1.3, w: 8, h: 0.35, fontSize: 13, bold: true, color: "157A7C", margin: 0 } } });
    if (shield) objects.push({ image: { x: W - 0.6 - 1.45, y: 0.4, w: 1.45, h: 1.67, path: shield } });
    strip(objects, 2.25, 0.26);
    pres.defineSlideMaster({ title: "TITLE", background: { color: "FFFFFF" }, objects });
  })();
  pres.defineSlideMaster({ title: "SECTION", background: { color: "003668" }, objects: (() => { const o = [{ rect: { x: 0, y: H - 0.30, w: W, h: 0.04, fill: { color: "FFFFFF" } } }]; strip(o, H - 0.26, 0.26); return o; })() });
  (function () {
    const objects = []; strip(objects, H - 0.12, 0.12);
    objects.push({ text: { text: footer, options: { x: 0.6, y: H - 0.52, w: 8, h: 0.3, fontSize: 9, color: "06345D", margin: 0 } } });
    pres.defineSlideMaster({ title: "CONTENT", background: { color: "FFFFFF" }, objects, slideNumber: { x: W - 1.2, y: H - 0.52, w: 0.6, h: 0.3, fontSize: 9, color: "06345D", align: "right" } });
  })();

  const k = { pres, W, H, PR, C: pres.SchemeColor, icon };
  k.content = (t, section) => {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
    s.addText(t, { x: 0.6, y: 0.45, w: W - 1.2, h: 0.8, fontSize: 32, bold: true, color: "003668", margin: 0, isTextBox: true, objectName: "Title" });
    return s;
  };
  k.titleSlide = (section, main, sub, line3) => {
    const s = pres.addSlide({ masterName: "TITLE", sectionTitle: section });
    s.addText(main, { x: 0.6, y: 2.9, w: 11.5, h: 1.3, fontSize: 54, bold: true, color: "003668", margin: 0, isTextBox: true, objectName: "Title" });
    s.addText(sub, { x: 0.6, y: 4.2, w: 10.5, h: 0.9, fontSize: 20, color: "06345D", margin: 0, isTextBox: true, objectName: "Subtitle" });
    if (line3) s.addText(line3, { x: 0.6, y: 5.4, w: 11, h: 0.5, fontSize: 16, bold: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Line 3" });
    return s;
  };
  k.divider = (num, name, sub, presenter, section) => {
    const s = pres.addSlide({ masterName: "SECTION", sectionTitle: section });
    s.addText(String(num), { x: 0.9, y: 1.6, w: 2.2, h: 2.2, fontSize: 120, bold: true, color: "8FD3D1", margin: 0, isTextBox: true, objectName: "Number" });
    const two = name.length > 26;
    s.addText(name, { x: 3.4, y: two ? 1.4 : 1.9, w: 9, h: two ? 1.9 : 1.2, fontSize: two ? 40 : 44, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Section title" });
    s.addText(sub, { x: 3.4, y: two ? 3.45 : 3.1, w: 9, h: 0.8, fontSize: 18, color: "BFD6EA", margin: 0, isTextBox: true, valign: "top", objectName: "Section subtitle" });
    if (presenter) s.addText(presenter, { x: 3.4, y: two ? 4.5 : 4.3, w: 9, h: 0.7, fontSize: 16, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, objectName: "Presenter" });
    return s;
  };
  k.dark = (section, main, sub) => {
    const s = pres.addSlide({ masterName: "SECTION", sectionTitle: section });
    const two = main.length > 30;
    s.addText(main, { x: 0.9, y: two ? 1.6 : 2.3, w: 11.5, h: two ? 2.2 : 1.3, fontSize: two ? 44 : 54, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "bottom", objectName: "Dark title" });
    if (sub) s.addText(sub, { x: 0.9, y: two ? 4.0 : 3.7, w: 11, h: 1.6, fontSize: 20, color: "BFD6EA", margin: 0, isTextBox: true, valign: "top", objectName: "Dark sub" });
    return s;
  };
  k.bullets = (s, items, o) => {
    const arr = items.map((t, i) => ({ text: t, options: { bullet: { code: "25A0", indent: 18 }, breakLine: i < items.length - 1, paraSpaceAfter: 6 } }));
    s.addText(arr, Object.assign({ fontSize: 16, color: "1E2329", valign: "top", margin: 0, isTextBox: true }, o));
  };
  k.card = (s, x, y, w, h, head, body, opts = {}) => {
    const fill = opts.fill || "F2F7FC";
    s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, line: { color: fill }, rectRadius: 0.08, objectName: "Card " + head });
    const ty = y + 0.18;
    if (opts.icon) s.addImage({ data: opts.icon, x: x + 0.22, y: y + 0.2, w: 0.42, h: 0.42 });
    s.addText(head, { x: x + (opts.icon ? 0.78 : 0.25), y: ty, w: w - (opts.icon ? 1.0 : 0.5), h: 0.45, fontSize: opts.headSize || 16, bold: true, color: opts.headColor || "003668", margin: 0, isTextBox: true, valign: "middle" });
    if (Array.isArray(body)) {
      const arr = body.map((t, i) => ({ text: t, options: { bullet: { code: "25A0", indent: 16 }, breakLine: i < body.length - 1, paraSpaceAfter: 4 } }));
      s.addText(arr, { x: x + 0.25, y: ty + 0.5, w: w - 0.5, h: h - 0.8, fontSize: opts.fontSize || 14, color: "1E2329", valign: "top", margin: 0, isTextBox: true });
    } else if (body) {
      s.addText(body, { x: x + 0.25, y: ty + 0.5, w: w - 0.5, h: h - 0.8, fontSize: opts.fontSize || 14, color: "1E2329", valign: "top", margin: 0, isTextBox: true });
    }
  };
  k.qa = (s, x, y, w, h, q, a, hex = "003668", qs = 15, as_ = 13.5) => {
    s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Panel " + q.slice(0, 20) });
    s.addText(q, { x: x + 0.25, y: y + 0.15, w: w - 0.5, h: 0.5, fontSize: qs, bold: true, color: hex, margin: 0, isTextBox: true, valign: "top" });
    s.addText(a, { x: x + 0.25, y: y + 0.62, w: w - 0.5, h: h - 0.75, fontSize: as_, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  };
  k.numbered = (s, x, y, w, h, num, head, body, hex, opts = {}) => {
    s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Numbered " + num });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.25, y: y + 0.22, w: 0.6, h: 0.6, fill: { color: hex }, line: { color: hex }, objectName: "Circle " + num });
    s.addText(String(num), { x: x + 0.25, y: y + 0.22, w: 0.6, h: 0.6, fontSize: 18, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(head, { x: x + 1.0, y: y + 0.22, w: w - 1.2, h: 0.6, fontSize: opts.headSize || 16, bold: true, color: hex, margin: 0, isTextBox: true, valign: "middle" });
    s.addText(body, { x: x + 0.25, y: y + 0.95, w: w - 0.5, h: h - 1.1, fontSize: opts.fontSize || 13.5, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  };
  k.principles = (s, y = 2.5, defs) => {
    defs = defs || { Prepare: "Ready for each stage before it happens. There should never be any surprises.", Guide: "Accurate, honest, timely information. Never dependency.", Support: "Present, responsive, compassionate. “How can we help?”, never “Why aren’t you attending?”", Enlighten: "Understanding, curiosity and enjoyment of Freemasonry, for life." };
    PR.forEach(([nme, hex], i) => {
      const x = 0.6 + i * 3.1;
      s.addShape(pres.ShapeType.rect, { x, y, w: 2.9, h: 1.1, fill: { color: hex }, line: { color: hex }, objectName: "Principle " + nme });
      s.addText([{ text: String(i + 1) + "  ", options: { color: "8FD3D1", fontSize: 18, bold: true } }, { text: nme.toUpperCase(), options: { color: "FFFFFF", fontSize: 20, bold: true } }], { x: x + 0.25, y, w: 2.6, h: 1.1, valign: "middle", margin: 0, isTextBox: true });
      s.addShape(pres.ShapeType.rect, { x, y: y + 1.1, w: 2.9, h: 2.3, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, objectName: "Principle text " + nme });
      s.addText(defs[nme], { x: x + 0.25, y: y + 1.25, w: 2.4, h: 2.0, fontSize: 13.5, color: "06345D", margin: 0, isTextBox: true, valign: "top" });
    });
  };
  k.timer = (s, text) => { // small "time box" top right on exercise slides
    s.addShape(pres.ShapeType.roundRect, { x: W - 0.6 - 2.3, y: 0.5, w: 2.3, h: 0.6, fill: { color: "157A7C" }, line: { color: "157A7C" }, rectRadius: 0.08, objectName: "Timer" });
    s.addText(text, { x: W - 0.6 - 2.3, y: 0.5, w: 2.3, h: 0.6, fontSize: 15, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
  };
  k.section = (t) => pres.addSection({ title: t });
  k.finish = async (out) => { await pres.writeFile({ fileName: out }); await applyTheme(out, THEME); return out; };
  return k;
}
module.exports = { create, THEME, PR, W, H };
