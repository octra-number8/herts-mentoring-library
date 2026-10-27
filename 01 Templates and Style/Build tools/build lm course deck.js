// E1a Lodge Mentor Essentials — one-hour course slides, in person or Teams.
const OUT = process.argv[2], SHIELD = process.argv[3];
(async () => {
  const k = await require("./hmslides.js").create({ shield: SHIELD, title: "Lodge Mentor Essentials", footer: "Hertfordshire Provincial Mentoring  ·  Lodge Mentor Essentials" });
  const { pres, W, H, PR } = k;
  const I = {
    users: await k.icon("FaUsers", "003668"), user: await k.icon("FaUserFriends", "0A4F72"), check: await k.icon("FaCheckCircle", "157A7C"),
    ban: await k.icon("FaBan", "0A4F72"), eye: await k.icon("FaEye", "106576"), list: await k.icon("FaClipboardList", "003668"),
    phone: await k.icon("FaPhoneAlt", "0A4F72"), calendar: await k.icon("FaCalendarAlt", "106576"), map: await k.icon("FaMapSigns", "157A7C"),
    flag: await k.icon("FaFlag", "157A7C"), heart: await k.icon("FaHeart", "157A7C"), balance: await k.icon("FaBalanceScale", "003668"),
    book: await k.icon("FaBookOpen", "003668"), whatsapp: await k.icon("FaWhatsapp", "157A7C"), hands: await k.icon("FaHandsHelping", "0A4F72"),
    clock: await k.icon("FaClock", "003668"), sun: await k.icon("FaSun", "0A4F72"),
  };

  k.section("Welcome");
  let s = k.titleSlide("Welcome", "Lodge Mentor Essentials", "One hour on the five things that change what a Lodge Mentor does on Monday", "Delivered by W Bro Wes Pierce, Deputy Provincial Grand Mentor");
  s.addNotes("Sixty minutes. Participants have the Lodge Mentor's Short Guide and the Action Plan sheet.");

  s = k.content("The hour", "Welcome");
  [["1", "Why mentoring", "7 min", "003668"], ["2", "The role: organiser, not everything", "15 min", "0A4F72"], ["3", "Principles and the two windows", "8 min", "106576"],
   ["4", "Your first month", "8 min", "157A7C"], ["5", "When it gets difficult", "10 min", "06345D"], ["6", "The Province, your plan, the Charge", "12 min", "003668"]].forEach(([n, t, d, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.5 + row * 2.5;
    k.numbered(s, x, y, 3.85, 2.3, n, t, d, hex, { fontSize: 16, headSize: 16 });
  });
  s.addNotes("Set expectations: one exercise, one action plan, and the Charge to close.");

  k.section("1 Why");
  s = k.content("Why mentoring", "1 Why");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.6, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Story panel" });
  s.addText("A good man, lost because nobody noticed.", { x: 1.0, y: 1.5, w: 11.3, h: 2.6, fontSize: 28, bold: true, italic: true, color: "003668", margin: 0, isTextBox: true, valign: "middle", objectName: "Story prompt" });
  k.card(s, 0.6, 4.35, 5.95, 2.05, "The Hertfordshire answer", "Freemasonry must be fun. A man who is enjoying himself attends; a man who attends participates; a man who participates belongs; and a man who belongs does not resign.", { icon: I.heart, fontSize: 15, fill: "E6F2F2" });
  k.card(s, 6.75, 4.35, 5.95, 2.05, "Retention is an outcome", "Of culture, never a target. Where someone finally asks why, one resignation in three is recovered. Where nobody asks, none are.", { icon: I.balance, fontSize: 15 });
  s.addNotes("Tell your own story, or the composite from the Personal Mentor course. Seven minutes including the two cards.");

  k.section("2 The role");
  s = k.content("Organiser, not everything", "2 The role");
  k.card(s, 0.6, 1.5, 5.95, 4.9, "The Lodge Mentor", ["Makes sure mentoring happens; does not do it all himself", "Assigns a Personal Mentor to every new and joining member, promptly", "Supports his Personal Mentors and equips them", "Opens and reviews a Personal Mentoring Plan for each member", "Watches for patterns and acts early", "The Lodge’s link to the Province; briefs the Lodge once a year", "Three to five years; develops his successor from day one"], { icon: I.check, fontSize: 14.5 });
  k.card(s, 6.75, 1.5, 5.95, 4.9, "Not the Lodge Mentor", ["Personal Mentor to everyone. Share the work", "The ritual coach. That is the Lodge of Instruction and the DC", "The Almoner. Welfare is his; you refer to him", "An inspector or a report-writer on members", "A one-year office"], { icon: I.ban, fontSize: 14.5, headColor: "0A4F72" });
  s.addNotes("Sharing the work is what makes it sustainable. The man who tries to mentor everyone himself burns out in a year and leaves nothing behind.");

  s = k.content("Choosing a Personal Mentor", "2 The role");
  k.card(s, 0.6, 1.5, 3.9, 4.9, "Choose for", ["Time", "Temperament: a patient listener", "The potential for friendship", "Knows the Lodge well", "Can say “I don’t know, but I’ll find out”"], { icon: I.user, fontSize: 15 });
  k.card(s, 4.7, 1.5, 3.9, 4.9, "Not for", ["Seniority", "Rank", "Being the Proposer, by default. Consider him first; trust exists. But not always", "Being free on the night"], { icon: I.ban, fontSize: 15, headColor: "0A4F72" });
  k.card(s, 8.8, 1.5, 3.9, 4.9, "Often overlooked", ["Past Masters: excellent mentors who often need the purpose", "Joining members with experience from elsewhere", "The quiet Master Mason of ten years who has never been asked", "Give each one the Personal Mentor’s Short Guide the day you ask"], { icon: I.eye, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Leads straight into the exercise.");

  s = k.content("Exercise: who could mentor?", "2 The role");
  k.timer(s, "On your own · 3 min");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.2, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Exercise band" });
  s.addText("List every member of your Lodge who could be a Personal Mentor. Everyone. Past Masters included.", { x: 1.0, y: 1.5, w: 11.3, h: 2.2, fontSize: 26, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Exercise text" });
  k.card(s, 0.6, 3.95, 5.95, 2.45, "Action Plan sheet, box 1", "Three minutes writing. Then a number from each person round the room.", { icon: I.list, fontSize: 15 });
  k.card(s, 6.75, 3.95, 5.95, 2.45, "What you will find", "The list is always longer than you expected. The question is not whether your Lodge has the people; it is whether anyone has asked them.", { icon: I.users, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Five minutes total. Collect the numbers aloud; they land the point better than any slide.");

  k.section("3 Principles");
  s = k.content("The four principles", "3 Principles");
  s.addText("Defined once on the canon page and quoted everywhere. They run together, all the time. They are not stages.", { x: 0.6, y: 1.4, w: 12, h: 0.8, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, objectName: "Lead" });
  k.principles(s, 2.5);
  s.addText("Family, Work, Masonry: in that order, always.", { x: 0.6, y: 6.15, w: 12, h: 0.5, fontSize: 15, bold: true, italic: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Tagline" });
  s.addNotes("Read from the canon page. Every document in the library quotes this text; so should every Lodge Mentor.");

  s = k.content("The journey, and the two windows", "3 Principles");
  const steps = [["Enquiry to Initiation", "003668"], ["Entered Apprentice", "0A4F72"], ["Fellow Craft", "106576"], ["Master Mason", "157A7C"], ["Office and the Chair", "06345D"], ["Beyond the Chair", "003668"]];
  steps.forEach(([t, hex], i) => {
    const x = 0.6 + i * 2.05;
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.55, y: 1.6, w: 0.75, h: 0.75, fill: { color: hex }, line: { color: hex }, objectName: "Stage " + (i + 1) });
    s.addText(String(i + 1), { x: x + 0.55, y: 1.6, w: 0.75, h: 0.75, fontSize: 20, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    if (i < steps.length - 1) s.addShape(pres.ShapeType.line, { x: x + 1.35, y: 1.975, w: 0.65, h: 0, line: { color: "BFD6EA", width: 2 }, objectName: "Link " + i });
    s.addText(t, { x, y: 2.5, w: 1.9, h: 0.8, fontSize: 13, bold: true, color: hex, align: "center", margin: 0, isTextBox: true, valign: "top" });
  });
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 3.5, w: 6.3, h: 1.0, fill: { color: "0A4F72" }, line: { color: "0A4F72" }, rectRadius: 0.08, objectName: "Window 1" });
  s.addText("Risk window 1: the first two years, often before Raising", { x: 0.85, y: 3.5, w: 5.9, h: 1.0, fontSize: 15, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle" });
  s.addShape(pres.ShapeType.roundRect, { x: 8.8, y: 3.5, w: 3.9, h: 1.0, fill: { color: "06345D" }, line: { color: "06345D" }, rectRadius: 0.08, objectName: "Window 2" });
  s.addText("Risk window 2: the year after the Chair", { x: 9.05, y: 3.5, w: 3.5, h: 1.0, fontSize: 15, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle" });
  k.card(s, 0.6, 4.75, 5.95, 1.65, "Spring Initiates", "The summer break interrupts their early participation. Plan deliberate summer contact and a social touchpoint for every one of them.", { icon: I.sun, fontSize: 13.5 });
  k.card(s, 6.75, 4.75, 5.95, 1.65, "Past Masters", "Included, Involved, Interested: a role, a project, a Brother to mentor. Prepare the Master Elect for after the Chair from Installation day.", { icon: I.hands, fontSize: 13.5 });
  s.addNotes("Two windows, two habits: summer contact for spring Initiates; a next role agreed for every outgoing Master.");

  k.section("4 First month");
  s = k.content("Your first month: six things", "4 First month");
  [["Ask for your induction", "If you have not had it. It comes with the Charge and the Mentor’s Jewel.", I.book, "003668"],
   ["Get the list", "From the Secretary: candidates, members in their first two years, joining members in their first year. These are the men under mentoring.", I.list, "0A4F72"],
   ["Mentor and Plan for every man on it", "Where there is a gap, fill it this month, not next.", I.user, "106576"],
   ["Ten minutes each", "Secretary, Almoner, Worshipful Master. Agree the attendance record after every meeting, same-day notice of any resignation, and your report on the Committee agenda.", I.phone, "157A7C"],
   ["Join the monthly call", "First Tuesday, 7pm, Teams. Open to you and every Personal Mentor.", I.calendar, "06345D"],
   ["Invite your APGMen", "To the next Initiation. He is there to help, never to inspect.", I.map, "003668"]].forEach(([h, d, ic, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.numbered(s, x, y, 3.85, 2.3, i + 1, h, d, hex, { fontSize: 12.5, headSize: 14.5 });
  });
  s.addNotes("Short Guide section 2 has the same six. Most take an hour. Action Plan box 3 is the checklist.");

  k.section("5 Difficult");
  s = k.content("When it gets difficult", "5 Difficult");
  k.card(s, 0.6, 1.4, 5.95, 2.3, "The pattern is the signal", ["A break in his own pattern, not a low level of attendance. The stalwart who stops coming is the one to worry about", "The Secretary’s attendance record is your early-warning system", "Two misses, seven days: the habit"], { icon: I.eye, fontSize: 13.5 });
  k.card(s, 6.75, 1.4, 5.95, 2.3, "The hand-offs", ["Almoner: anything touching welfare. Note only “referred to Almoner”", "Secretary: acknowledges a resignation only; cannot accept it; you and the Almoner told the same day", "Treasurer: a first missed subscription earns a quiet word", "Royal Arch Representative: One Journey’s bridge"], { icon: I.hands, fontSize: 12.5 });
  [["1", "Personal Mentor", "Warm, informal. After two misses, within seven days of the second.", "003668"], ["2", "You", "The overview; what could the Lodge change; a discreet note; close the loop.", "0A4F72"], ["3", "Worshipful Master", "Lodge culture, office or another member. Almoner alongside for welfare.", "106576"], ["4", "The Province", "An impartial voice, or a Lodge where he might thrive. A strength, not a failure.", "157A7C"]].forEach(([n, h, d, hex], i) => {
    k.numbered(s, 0.6 + i * 3.08, 3.9, 2.9, 2.5, n, h, d, hex, { fontSize: 12, headSize: 14 });
  });
  s.addNotes("The Retention, Retrieval and Migration Guide is the owner-document; the Warning Signs card has this on one side.");

  s = k.content("Pressure, in both directions", "5 Difficult");
  k.card(s, 0.6, 1.5, 5.95, 4.9, "The member pushed too hard", ["Office before he feels ready or confident", "Ritual beyond his current ability", "Progression faster than he wishes", "The Royal Arch or other orders before the time is right", "Anything that makes him feel inadequate, unwelcome or judged", "“Sink or swim” runs counter to UGLE guidance. Address it directly; escalate if needed"], { icon: I.ban, fontSize: 15.5, headColor: "0A4F72" });
  k.card(s, 6.75, 1.5, 5.95, 4.9, "The member left under-stretched", ["A capable Brother waiting years for a first office", "A Brother who was never asked: to visit, to take a small piece, to help", "A Past Master with nothing to do; a joining member whose experience nobody used", "A Master Mason of years who stopped learning because nobody offered", "Ask what he would like; find a role; raise the office queue with the Master and DC", "A bored Brother leaves as surely as a frightened one"], { icon: I.balance, fontSize: 15.5 });
  s.addNotes("Readiness runs both ways. The under-stretched member is the quieter loss and the more common one in Lodges with long office queues.");

  k.section("6 Close");
  s = k.content("The Province behind you", "6 Close");
  [["Your APGMen", "One per area. Advice, a visitor at Initiations, your quarterly update.", I.map],
   ["Monthly mentoring call", "First Tuesday, 7pm, Teams. Lodge Mentors and Personal Mentors.", I.calendar],
   ["DAWG", "The Daily Advancement WhatsApp Group, run by the Provincial Mentoring Team.", I.whatsapp],
   ["Training", "Induction for you; the Personal Mentor course for your team. Send them.", I.users],
   ["The library", "Short Guides, Meeting Guide, Stage Checklists, Warning Signs card, Retention Guide. Provincial website and your APGMen.", I.book],
   ["One-to-one, in confidence", "mentor@hertfordshirefreemasons.org.uk. A difficult conversation, a second opinion, or simply to think aloud.", I.phone]].forEach(([h, d, ic], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.card(s, x, y, 3.85, 2.3, h, d, { icon: ic, fontSize: 15, headSize: 15 });
  });
  s.addNotes("Five minutes. The library set is on each table.");

  s = k.content("Your action plan", "6 Close");
  k.timer(s, "On your own · 3 min");
  k.card(s, 0.6, 1.5, 5.95, 2.3, "Against the four principles", "One thing my Lodge already does well. One thing it does not do at all. Action Plan sheet, box 2.", { icon: I.check, fontSize: 15 });
  k.card(s, 6.75, 1.5, 5.95, 2.3, "The one action", "What, by when, and who else needs to know. Box 4. Then one sentence each, round the room.", { icon: I.flag, fontSize: 15, fill: "E6F2F2" });
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 4.05, w: 12.1, h: 2.35, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Plan band" });
  s.addText("Your Assistant Provincial Grand Mentor will ask you about it within the month. That is the point.", { x: 1.0, y: 4.05, w: 11.3, h: 2.35, fontSize: 24, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Plan text" });
  s.addNotes("Do not let anyone pass. Photograph the sheets before they leave.");

  s = k.dark("6 Close", "The Charge", "Brother, the office you have accepted is unlike any other in the Lodge… Your duty is not to mentor every member yourself. It is to make sure that every member is mentored.");
  s.addText("Read in full from the facilitator guide. Presented in writing to every new Lodge Mentor on appointment.", { x: 0.9, y: 5.6, w: 11, h: 0.6, fontSize: 14, italic: true, color: "8FD3D1", margin: 0, isTextBox: true, objectName: "Charge note" });
  s.addNotes("Read the whole Charge aloud, slowly, from section 4 of the facilitator guide. Then thank them, and stop.");

  s = k.dark("6 Close", "Prepare • Guide • Support • Enlighten", "Family, Work, Masonry: in that order, always. May the work be patient and purposeful, and may Freemasonry flourish, root and branch. Thank you.");
  s.addNotes("Close. Names to the register; everyone on the call and DAWG.");

  console.log("written", await k.finish(OUT));
})().catch(e => { console.error(e); process.exit(1); });
