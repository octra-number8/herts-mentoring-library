// E6a The Chair and Beyond — one-hour session for Wardens and Masters.
const OUT = process.argv[2], SHIELD = process.argv[3];
(async () => {
  const k = await require("./hmslides.js").create({ shield: SHIELD, title: "The Chair and Beyond", footer: "Hertfordshire Provincial Mentoring  ·  The Chair and Beyond" });
  const { pres, W, H, PR } = k;
  const I = {
    user: await k.icon("FaUserFriends", "003668"), users: await k.icon("FaUsers", "0A4F72"), eye: await k.icon("FaEye", "106576"),
    gavel: await k.icon("FaGavel", "003668"), balance: await k.icon("FaBalanceScale", "0A4F72"), heart: await k.icon("FaHeart", "157A7C"),
    comment: await k.icon("FaCommentDots", "0A4F72"), flag: await k.icon("FaFlag", "157A7C"), home: await k.icon("FaHome", "003668"),
    calendar: await k.icon("FaCalendarAlt", "106576"), hands: await k.icon("FaHandsHelping", "157A7C"), list: await k.icon("FaClipboardList", "003668"),
    utensils: await k.icon("FaUtensils", "0A4F72"), sun: await k.icon("FaSun", "0A4F72"), compass: await k.icon("FaCompass", "106576"),
    ban: await k.icon("FaBan", "0A4F72"), check: await k.icon("FaCheckCircle", "157A7C"), clock: await k.icon("FaClock", "003668"),
  };

  // True-or-false opener: one question slide, one answer slide, per segment.
  const quiz = (section, pairs) => {
    let q = k.content("True or false?", section);
    pairs.forEach(([stmt, ans, fact, src], i) => {
      const y = 1.5 + i * 2.45;
      q.addShape(pres.ShapeType.roundRect, { x: 0.6, y, w: 12.1, h: 2.2, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Statement " + (i + 1) });
      const hex = i === 0 ? "003668" : "0A4F72";
      q.addShape(pres.ShapeType.ellipse, { x: 0.95, y: y + 0.75, w: 0.7, h: 0.7, fill: { color: hex }, line: { color: hex }, objectName: "Q circle " + (i + 1) });
      q.addText(String(i + 1), { x: 0.95, y: y + 0.75, w: 0.7, h: 0.7, fontSize: 20, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
      q.addText(stmt, { x: 1.95, y, w: 10.5, h: 2.2, fontSize: 24, bold: true, color: "06345D", margin: 0, isTextBox: true, valign: "middle" });
    });
    q.addText("Hands up for true. Then the answer.", { x: 0.6, y: 6.45, w: 12.1, h: 0.4, fontSize: 15, bold: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Prompt" });
    q.addNotes("Two statements, hands up for true, reveal on the next slide. Two minutes, inside the segment time. " + pairs.map((p, i) => (i + 1) + ": " + (p[1] ? "TRUE" : "FALSE") + ". " + p[2]).join(" "));
    let a = k.content("The answers", section);
    pairs.forEach(([stmt, ans, fact, src], i) => {
      const y = 1.5 + i * 2.45, hex = ans ? "157A7C" : "0A4F72";
      a.addShape(pres.ShapeType.roundRect, { x: 0.6, y, w: 12.1, h: 2.2, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Answer " + (i + 1) });
      a.addShape(pres.ShapeType.roundRect, { x: 0.95, y: y + 0.25, w: 1.35, h: 0.5, fill: { color: hex }, line: { color: hex }, rectRadius: 0.1, objectName: "Badge " + (i + 1) });
      a.addText(ans ? "TRUE" : "FALSE", { x: 0.95, y: y + 0.25, w: 1.35, h: 0.5, fontSize: 15, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
      a.addText(stmt, { x: 2.5, y: y + 0.22, w: 9.9, h: 0.56, fontSize: 16, bold: true, color: "06345D", margin: 0, isTextBox: true, valign: "middle" });
      a.addText(fact, { x: 0.95, y: y + 0.9, w: 11.4, h: 0.95, fontSize: 14, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
      a.addText(src, { x: 0.95, y: y + 1.82, w: 11.4, h: 0.3, fontSize: 11, italic: true, color: "0A4F72", margin: 0, isTextBox: true, valign: "top" });
    });
    a.addNotes("Land each one in a sentence and move on. All twenty-two facts, with sources, are in section 7 of the facilitator guide and on the pocket card.");
  };

  k.section("Welcome");
  let s = k.titleSlide("Welcome", "The Chair and Beyond", "An hour for Wardens and Masters: the things about your year that are not in the ritual book, seen through the eyes of the newest man in the room", "Delivered by W Bro Wes Pierce, Deputy Provincial Grand Mentor");
  s.addNotes("Sixty minutes. Participants have the action sheet and the pocket card. Tables mixed: Masters and Wardens together. Each segment opens with two true-or-false statements, inside the segment time.");

  s = k.content("The hour", "Welcome");
  [["1", "Why you", "7 min", "003668"], ["2", "Your year through a new man’s eyes", "10 min", "0A4F72"], ["3", "Exercise: the office queue", "8 min", "106576"],
   ["4", "Running a happy year", "10 min", "157A7C"], ["5", "For the Wardens: two years’ notice", "8 min", "06345D"], ["6", "After the Chair, your plan, the close", "17 min", "003668"]].forEach(([n, t, d, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.5 + row * 2.5;
    k.numbered(s, x, y, 3.85, 2.3, n, t, d, hex, { fontSize: 16, headSize: 16 });
  });

  k.section("1 Why you");
  quiz("1 Why you", [
    ["The Secretary accepts a resignation on the Lodge’s behalf.", false, "He has no power to. He acknowledges receipt only, and the man then has sixty days to withdraw it; in a Hermes Province the sixty days run from the day his email arrives. Lengthened from 21 days in 2015 so that someone had time to have the conversation. Said aloud at the Risings, a resignation is irrevocable unless the Lodge votes to invite withdrawal on the spot.", "Rule 183; UGLE Members’ Pathway, Resignation: the opportunity to reconsider; PGL Herts Secretaries’ Handbook"],
    ["The Immediate Past Master is an officer of the Lodge.", false, "He is not; the Handbook’s precedence list says so in terms. Constitutionally the year after the Chair comes with a seat and no role at all, unless the Lodge gives him one. That is the whole of “Included, Involved, Interested” in one fact.", "PGL Herts Secretaries’ Handbook, Precedence"],
  ]);
  
  s = k.content("The newest man in the room", "1 Why you");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.3, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Question band" });
  s.addText("Who was initiated most recently into a Lodge represented here? Who is his Personal Mentor? What is his next ceremony?", { x: 1.0, y: 1.5, w: 11.3, h: 2.3, fontSize: 24, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Question" });
  k.card(s, 0.6, 4.05, 5.95, 2.35, "His whole impression of Freemasonry", "will be formed in somebody’s year in the Chair. What he sees, who sits with him, whether anyone rings when he misses a meeting. That year is yours.", { icon: I.eye, fontSize: 15 });
  k.card(s, 6.75, 4.05, 5.95, 2.35, "If you cannot answer", "that is the first action on your sheet. Every Master should know the newest man by name, his mentor, and his next step.", { icon: I.flag, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Ask it for real. Let the silence sit. Then the two windows.");

  s = k.content("Two windows, and you are standing in both", "1 Why you");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 5.95, h: 2.2, fill: { color: "0A4F72" }, line: { color: "0A4F72" }, rectRadius: 0.08, objectName: "Window 1" });
  s.addText([{ text: "Risk window 1\n", options: { fontSize: 14, color: "8FD3D1", bold: true } }, { text: "The first two years, often before Raising", options: { fontSize: 22, color: "FFFFFF", bold: true } }], { x: 0.95, y: 1.5, w: 5.3, h: 2.2, margin: 0, isTextBox: true, valign: "middle" });
  s.addShape(pres.ShapeType.roundRect, { x: 6.75, y: 1.5, w: 5.95, h: 2.2, fill: { color: "06345D" }, line: { color: "06345D" }, rectRadius: 0.08, objectName: "Window 2" });
  s.addText([{ text: "Risk window 2\n", options: { fontSize: 14, color: "8FD3D1", bold: true } }, { text: "The year after the Chair", options: { fontSize: 22, color: "FFFFFF", bold: true } }], { x: 7.1, y: 1.5, w: 5.3, h: 2.2, margin: 0, isTextBox: true, valign: "middle" });
  k.card(s, 0.6, 3.95, 5.95, 2.45, "Your new members are in the first", "Every Initiate, Fellow Craft and newly raised Brother in your year. Their mentors do the work; you set whether the Lodge lets them.", { icon: I.users, fontSize: 15 });
  k.card(s, 6.75, 3.95, 5.95, 2.45, "You are about to enter the second", "The Immediate Past Master’s year decides whether a Lodge keeps its Past Masters. Plan it from Installation day, not after.", { icon: I.user, fontSize: 15 });
  s.addNotes("Retention is the outcome of culture, never a target. The culture of the Lodge for one year is the Master's.");

  k.section("2 A new man's eyes");
  quiz("2 A new man's eyes", [
    ["A Lodge must leave at least four weeks between a candidate’s degrees.", true, "A minimum, not a target. The Provincial Grand Master encourages double ceremonies so that no Initiate is kept waiting, and a Degree by Request lets another Lodge pass or raise your candidate on a written request from the Master and Secretary. A man who waits a year for his Second is a man at risk.", "Rules 172 and 173; PGL Herts Secretaries’ Handbook, Conferring the Degrees"],
    ["The Secretary may hold a Grand Lodge Certificate back until the Brother next attends.", false, "It is presented as soon as it arrives, or sent recorded delivery and minuted. It is a passport, kept with his regalia, not framed. The presentation is a moment the Master can design.", "PGL Herts Secretaries’ Handbook; MetGL Mentors’ Handbook"],
  ]);
  
  s = k.content("Your year through a new man’s eyes", "2 A new man's eyes");
  const moments = [["The ballot", "Does he know anyone before his interview?", "003668"], ["Initiation night", "Mentor beside him; Tyler and Junior Deacon introduced; never dines alone", "0A4F72"], ["The second meeting", "Mostly business, and nobody told him. The moment most often left to chance", "106576"], ["Nights he cannot attend", "Higher degrees. Companionship and learning, or dead time?", "157A7C"], ["His Passing", "At his pace, never the calendar’s", "06345D"], ["The summer break", "Spring Initiates: deliberate contact, or silence until autumn", "003668"]];
  moments.forEach(([h, d, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.25;
    k.numbered(s, x, y, 3.85, 2.05, i + 1, h, d, hex, { fontSize: 13.5, headSize: 15 });
  });
  s.addText("Which of these does your Lodge design, and which does it leave to chance?", { x: 0.6, y: 6.0, w: 12, h: 0.45, fontSize: 16, bold: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Ask" });
  s.addNotes("Ask the room. The second meeting is the one to dwell on: a word before the meeting, a seat beside his mentor, a Brother briefed to include him.");

  s = k.content("Five things only the Master can do", "2 A new man's eyes");
  [["Set the tone", "The culture of the Lodge for a year is yours. What you laugh at, who you sit with, how you speak to the newest member: the Lodge copies it.", I.gavel, "003668"],
   ["Hear the Lodge Mentor’s report", "On the Committee agenda, with the same weight as the Treasurer’s. Who has a mentor and a Plan; who has been missed; what the Lodge could change.", I.list, "0A4F72"],
   ["Brief the Lodge on mentoring", "Once in your year, in open Lodge. The Lodge Mentor has the presentation. We are all mentors to others.", I.comment, "106576"],
   ["Protect juniors from pressure", "No office before ready; no ritual beyond ability; no Chapter sales pitch at the bar. And no capable man left waiting.", I.balance, "157A7C"],
   ["Own the Step 3 conversation", "When a member is drifting and it touches Lodge culture, office or another member, the Master has the conversation. Almoner alongside for welfare.", I.heart, "06345D"]].forEach(([h, d, ic, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.numbered(s, x, y, 3.85, 2.3, i + 1, h, d, hex, { fontSize: 12.5, headSize: 14.5 });
  });
  k.card(s, 8.8, 3.95, 3.85, 2.3, "The right question", "Always “How can we help?”, never “Why weren’t you there?”", { icon: I.heart, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Action sheet box 1 while this is on screen: the newest man, his mentor, his next ceremony, one moment you will design.");

  k.section("3 The office queue");
  quiz("3 The office queue", [
    ["A Warden invested a meeting late can still be elected Master the following year.", false, "Not without a dispensation. A Warden must serve a full year, Installation to Installation, to be eligible for the Chair. The office queue has to allow for it.", "Rules 105a and 109"],
    ["A Master may serve two years running in the same Lodge.", true, "He is proclaimed, not installed again; the Address to the Master is not given; and he receives no Past Master’s jewel until he has installed his successor. He may not be Master of two Lodges at once without a dispensation.", "Rules 107 and 115; PGL Herts Secretaries’ Handbook, Master continuing in office"],
  ]);
  
  s = k.content("Exercise: the office queue", "3 The office queue");
  k.timer(s, "On your own · 4 min");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 1.9, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Exercise band" });
  s.addText("Map your progressive officers for the next three years. Mark two men: one at risk of being pushed before he is ready, and one capable man left waiting.", { x: 1.0, y: 1.5, w: 11.3, h: 1.9, fontSize: 22, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Exercise text" });
  k.card(s, 0.6, 3.65, 5.95, 2.75, "Pushed too hard", ["Office before he feels ready or confident", "Ritual beyond his current ability", "Progression faster than he wishes", "Anything that makes him feel inadequate or judged"], { icon: I.ban, fontSize: 14, headColor: "0A4F72" });
  k.card(s, 6.75, 3.65, 5.95, 2.75, "Left waiting", ["A capable Brother years from a first office behind a long queue", "A Brother never asked: to visit, to take a small piece, to help", "A Past Master with nothing to do", "A bored Brother leaves as surely as a frightened one"], { icon: I.balance, fontSize: 14 });
  s.addNotes("Action sheet box 2. Four minutes writing, four minutes of examples. The office queue is a joint decision with the DC; the Master owns it.");

  k.section("4 A happy year");
  quiz("4 A happy year", [
    ["A member two full years in arrears ceases to be a member automatically.", true, "Announced in open Lodge and minuted. The Treasurer saw the first missed subscription eighteen months earlier: a quiet word then, not a letter that reads like a final demand.", "Rule 148; PGL Herts Secretaries’ Handbook, Membership"],
    ["Hertfordshire fire has the Provincial Grand Master’s blessing.", true, "Endorsed as a Provincial tradition, with the written caveat that its speed should not “reach the level of absurdity and thus become undignified”. A new man’s first embarrassment is usually fire nobody showed him. Explain it before his first Festive Board.", "PGL Herts Lodge Director of Ceremonies Guide, Toasts"],
  ]);
  
  s = k.content("Running a happy year: the management, not the ritual", "4 A happy year");
  [["Lodge Mentor", "Your report on the agenda. Three minutes a meeting: who has a mentor and a Plan, the office queue, the newest man.", I.user],
   ["Director of Ceremonies", "Ceremony preparation, the Lodge of Instruction, and how juniors are drawn into ritual gently.", I.gavel],
   ["Secretary", "The candidate timeline your year hangs from; the attendance record after every meeting; same-day notice of a resignation.", I.list],
   ["Almoner", "Welfare, and Step 3 alongside you. Welcome new members jointly.", I.hands],
   ["Treasurer", "Arrears as an early signal. A first missed subscription earns a quiet word, not a letter that reads like a final demand.", I.balance],
   ["The Festive Board", "You set whether “look who’s remembered where we meet” gets said. Never let a new or joining member dine alone.", I.utensils]].forEach(([h, d, ic], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.card(s, x, y, 3.85, 2.3, h, d, { icon: ic, fontSize: 13.5, headSize: 15 });
  });
  s.addNotes("The joke at the bar cost a member in the case study every mentor in the Province has heard. One quiet word to the Lodge about how returning members are greeted is worth a year of retention work.");

  s = k.content("Family, Work, Masonry: for the Master too", "4 A happy year");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.0, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "FWM band" });
  s.addText("The year in the Chair is the point at which a Lodge is most likely to ask too much of one man.", { x: 1.0, y: 1.5, w: 11.3, h: 2.0, fontSize: 24, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "FWM text" });
  k.card(s, 0.6, 3.75, 3.9, 2.65, "Delegate", "The Wardens, the DC and the Secretary carry their share. It is a team, not a performance.", { icon: I.users, fontSize: 14.5 });
  k.card(s, 4.7, 3.75, 3.9, 2.65, "Protect home and work", "Say no to the fourth visit in a month. The Lodge will understand; your family will notice.", { icon: I.home, fontSize: 14.5 });
  k.card(s, 8.8, 3.75, 3.9, 2.65, "Keep your own mentor", "The Master who finishes the year wanting more Freemasonry is the one who had someone to talk to during it.", { icon: I.heart, fontSize: 14.5, fill: "E6F2F2" });
  s.addNotes("The Master who does not delegate is the one the Lodge loses in the year after.");

  k.section("5 Wardens");
  quiz("5 Wardens", [
    ["Five Brethren are enough to open a Lodge.", true, "Five, not counting the Tyler and the candidate; two of them members; one an Installed Master. No Installed Master present and the meeting is abandoned and minuted. A Master Elect who cannot attend his Installation: postponed, and held within five weeks.", "Rule 119; PGL Herts Secretaries’ Handbook, Unavoidable absence"],
    ["The Deputy and Assistant Provincial Grand Masters attend as the PGM’s representative.", false, "They represent themselves by their Patents and should never be called his representative. Anyone wearing a chain represents themselves: offer the gavel. Salutations are completed before the Official Visitor enters, and the first wine-taking at an Installation is with him.", "PGL Herts Secretaries’ Handbook, Official Visits; DC Guide"],
  ]);
  
  s = k.content("For the Wardens: two years’ notice", "5 Wardens");
  [["Learn the Lodge, not only the ritual", "Who is new, who is drifting, who is waiting. Sit with the Lodge Mentor once a quarter.", I.eye],
   ["Shadow the Master", "At the Committee, with the Secretary, at the Festive Board. Watch what works and what you will do differently.", I.user],
   ["Choose your team early, and kindly", "Readiness runs both ways. Talk to the DC and the Lodge Mentor now about who is ready and who is waiting.", I.users],
   ["Plan your year now", "Programme, speakers, the social calendar, a White Table, the charity. A year planned as a Warden is a year enjoyed as Master.", I.calendar],
   ["Visit, and complete your own journey", "Visit across the Province; make sure the Royal Arch has been explained to you, on your timing.", I.compass],
   ["Keep your own mentor", "Senior Wardens drift too. The man who got you to the Chair is still useful on the way through it.", I.heart]].forEach(([h, d, ic], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.card(s, x, y, 3.85, 2.3, h, d, { icon: ic, fontSize: 13.5, headSize: 14.5 });
  });
  s.addNotes("Action sheet box 2 again for the Wardens: the office queue is theirs to inherit.");

  k.section("6 After the Chair");
  quiz("6 After the Chair", [
    ["A Brother who has resigned from every Lodge can never visit again.", false, "He may visit any Lodge once, and one Lodge three times in twelve months with a view to joining, provided the Master confirms that purpose in writing to the Secretary. The Master’s signature keeps the door open.", "Rule 127 (since September 2020); UGLE Members’ Pathway"],
    ["Hermes tells the Almoner automatically after two consecutive misses.", true, "It does. The call within seven days is still the Lodge’s to make, and a Lodge that waits for the notification has already lost a month. “How can we help?”, never “Why weren’t you there?”.", "UGLE Members’ Pathway, Tracking attendance and apologies"],
  ]);
  
  s = k.content("After the Chair", "6 After the Chair");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 1.7, fill: { color: "06345D" }, line: { color: "06345D" }, rectRadius: 0.08, objectName: "IPM band" });
  s.addText("A seat is not a purpose. The Immediate Past Master’s year decides whether a Lodge keeps its Past Masters.", { x: 1.0, y: 1.5, w: 11.3, h: 1.7, fontSize: 22, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "IPM text" });
  [["Included", "A seat, yes, and a voice: on the Committee, at the Lodge of Instruction, at the planning of the next year.", "003668"], ["Involved", "A role or a project: the archive, the social calendar, a ceremony to work, a Brother to mentor.", "106576"], ["Interested", "New questions: symbolism, history, the Royal Arch, the Province. Welcome them.", "157A7C"]].forEach(([h, d, hex], i) => {
    k.numbered(s, 0.6 + i * 4.1, 3.45, 3.85, 2.95, ["I", "I", "I"][i], h, d, hex, { fontSize: 14, headSize: 17 });
  });
  s.addNotes("Agree it before Installation, not after. Past Masters make the best Personal Mentors because they remember what the Chair cost and what it gave. Ask who in the room will take a mentee. Action sheet box 3.");

  s = k.content("Your action sheet", "6 After the Chair");
  k.timer(s, "On your own · 3 min");
  k.card(s, 0.6, 1.5, 3.9, 2.4, "Box 1", "The newest man: name, mentor, next ceremony, one moment you will design.", { icon: I.eye, fontSize: 14 });
  k.card(s, 4.7, 1.5, 3.9, 2.4, "Boxes 2 and 3", "The office queue, and your year after the Chair: a role, a project, a Brother to mentor.", { icon: I.list, fontSize: 14 });
  k.card(s, 8.8, 1.5, 3.9, 2.4, "Box 4", "One thing you will change in your year, or in your two years as a Warden. By when.", { icon: I.flag, fontSize: 14, fill: "E6F2F2" });
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 4.15, w: 12.1, h: 2.25, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Plan band" });
  s.addText("One sentence each, round the room. Your Lodge Mentor will be told what you committed to, and your APGMen will ask you about it within the month.", { x: 1.0, y: 4.15, w: 11.3, h: 2.25, fontSize: 22, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Plan text" });
  s.addNotes("Do not let anyone pass. Photograph the sheets.");

  s = k.dark("6 After the Chair", "Prepare • Guide • Support • Enlighten", "Family, Work, Masonry: in that order, always. For the Master too. Freemasonry must be fun; a man who is enjoying himself attends, participates, belongs, and does not resign. Thank you.");
  s.addNotes("Close on the principles. Sheets photographed; Lodge Mentors told.");

  console.log("written", await k.finish(OUT));
})().catch(e => { console.error(e); process.exit(1); });
