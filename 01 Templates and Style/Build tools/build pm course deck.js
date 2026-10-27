// E2a Personal Mentor Course — slides for in-person (2 h) and online (2 x 60 min) delivery.
const OUT = process.argv[2], SHIELD = process.argv[3];
(async () => {
  const k = await require("./hmslides.js").create({ shield: SHIELD, title: "Personal Mentor Course", footer: "Hertfordshire Provincial Mentoring  ·  Personal Mentor Course" });
  const { pres, W, H, PR } = k;
  const I = {
    user: await k.icon("FaUserFriends", "003668"), heart: await k.icon("FaHeart", "157A7C"), ear: await k.icon("FaHeadphones", "003668"),
    comment: await k.icon("FaCommentDots", "0A4F72"), question: await k.icon("FaQuestionCircle", "003668"), eye: await k.icon("FaEye", "106576"),
    tools: await k.icon("FaToolbox", "157A7C"), check: await k.icon("FaCheckCircle", "157A7C"), ban: await k.icon("FaBan", "0A4F72"),
    users: await k.icon("FaUsers", "0A4F72"), clock: await k.icon("FaClock", "003668"), hands: await k.icon("FaHandsHelping", "157A7C"),
    laptop: await k.icon("FaLaptop", "106576"), book: await k.icon("FaBookOpen", "003668"), flag: await k.icon("FaFlag", "157A7C"),
  };
  const CASE = "“I joined at thirty-four, proposed by a colleague I liked. My Initiation was extraordinary; I drove home buzzing. Then came my second meeting: nobody had told me it was mainly business, and I sat at dinner next to two men who talked across me all night about people I didn’t know. At my first rehearsal evening I was told after ten minutes there was nothing for me and I should get off home. Work went mad that spring; I missed two meetings. Nobody rang. When I came back, someone at the bar said, ‘Well, look who’s remembered where we meet.’ Everyone laughed. I laughed too. My subscription renewal came in January with a letter that read like a final demand. I paid it, and then I sat down one Sunday and wrote a different letter. The Secretary’s reply was very polite. It said my resignation had been received and would be reported to the Lodge. Nobody ever asked me why.”";

  // ---------- opening ----------
  k.section("Welcome");
  let s = k.titleSlide("Welcome", "Personal Mentor Course", "Two hours of conversation about conversation: the handful of skills that make a Personal Mentor the friend a new Brother needs", "Delivered by W Bro Wes Pierce, Deputy Provincial Grand Mentor");
  s.addNotes("One evening of two hours. Have the workbook to hand.");

  s = k.content("By the end of tonight you will be able to", "Welcome");
  [["Say what the role is, and is not", "In one sentence each, and name where the Almoner and the Lodge Mentor take over", I.user],
   ["Ask a question that opens a door", "Turn a closed question into an open one, and ask it", I.question],
   ["Listen, and hold a silence", "Hear tone and hesitation, and count to three before you speak", I.ear],
   ["Spot trouble early", "Recognise the warning signs and say who acts, in what order", I.eye],
   ["Reach for the right tool", "The Meeting Guide, the Stage Checklists, the Warning Signs card", I.tools],
   ["Do one thing differently", "With your mentee, this month", I.flag]].forEach(([h, d, ic], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.5 + row * 2.5;
    k.card(s, x, y, 3.85, 2.3, h, d, { icon: ic, fontSize: 14 });
  });
  s.addNotes("Read these quickly; they are the promise. Then say: everything tonight is done by doing. You will talk more than I will.");

  s = k.content("How tonight works", "Welcome");
  k.card(s, 0.6, 1.5, 5.95, 4.9, "In the room", ["Tables of four; you will move into pairs twice", "Workbook in front of you; write in it", "Flipchart for the things we find together", "Nothing tonight touches ritual", "Phones away unless you are using Solomon"], { icon: I.users, fontSize: 16 });
  k.card(s, 6.75, 1.5, 5.95, 4.9, "The deal", ["I will not tell you how to mentor; I will show you three things and let you try them", "Say what you think, not what you think I want", "If you have been a Personal Mentor for twenty years, you are the most useful person here: say what has worked"], { icon: I.hands, fontSize: 16, fill: "E6F2F2" });
  s.addNotes("Set the deal explicitly; it gives the experienced mentors permission to contribute rather than sit back.");

  // ---------- 1 the role ----------
  k.section("1 The role");
  k.divider(1, "The story of a man we lost", "Where were the moments this could have been turned around?", null, "1 The role");

  s = k.content("The story of a man we lost", "1 The role");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.4, w: 12.1, h: 4.6, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Case panel" });
  s.addText(CASE, { x: 0.95, y: 1.6, w: 11.4, h: 4.2, fontSize: 15.5, italic: true, color: "06345D", margin: 0, isTextBox: true, valign: "top", objectName: "Case text" });
  s.addText("A composite drawn from real losses. Every detail has happened to someone.", { x: 0.6, y: 6.2, w: 12, h: 0.4, fontSize: 12, color: "06345D", margin: 0, isTextBox: true, objectName: "Case note" });
  s.addNotes("Read it aloud, slowly. Do not rush the last line. Then: where were the moments? Flipchart. Let them find the six before you show the next slide.");

  s = k.content("Six moments, and none of them needed an expert", "1 The role");
  [["The second meeting", "Nobody said it would be business. Nobody sat with him.", "003668"], ["The rehearsal", "Sent home after ten minutes. “Nothing for you.”", "0A4F72"], ["Two missed meetings", "Nobody rang. The silence was the message.", "106576"],
   ["The bar", "A joke at his expense. Everyone laughed; so did he.", "157A7C"], ["The renewal letter", "Read like a final demand. Paid, and then the other letter.", "06345D"], ["The reply", "Polite. Received. Reported. Nobody asked why.", "003668"]].forEach(([h, d, hex], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.2;
    k.numbered(s, x, y, 3.85, 2.0, i + 1, h, d, hex, { fontSize: 14 });
  });
  s.addText("All of them required someone noticing. That is the role.", { x: 0.6, y: 5.95, w: 12, h: 0.5, fontSize: 18, bold: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Land" });
  s.addNotes("Land it hard: none required expertise, all required noticing. One resignation in three is recovered when someone finally asks why; nobody asked him at all.");

  s = k.content("A friend with a purpose", "1 The role");
  k.card(s, 0.6, 1.5, 5.95, 4.9, "Your role is", ["His first point of contact for any question", "Someone who keeps in touch between meetings", "A listener who notices when something changes", "His bridge to the Lodge and the Province"], { icon: I.check, fontSize: 16 });
  k.card(s, 6.75, 1.5, 5.95, 4.9, "Your role is not", ["The only person who can help him", "A ritual coach. That is the Lodge of Instruction", "Someone who monitors or reports on him", "A replacement for the Lodge Mentor, who co-ordinates", "A welfare officer. That is the Almoner, and referring early is the skill, not the failure"], { icon: I.ban, fontSize: 16, headColor: "0A4F72" });
  s.addNotes("The boundaries free people. Most new Personal Mentors worry they do not know enough. They do not need to know; they need to notice and to ask.");

  s = k.content("The four principles", "1 The role");
  s.addText("Defined once, on the Province’s canon page, and quoted everywhere. They run together, all the time. They are not stages.", { x: 0.6, y: 1.4, w: 12, h: 0.8, fontSize: 16, color: "1E2329", margin: 0, isTextBox: true, objectName: "Lead" });
  k.principles(s, 2.5);
  s.addText("Coach, not counsellor. If it touches his health, money, family or safety: Almoner and Lodge Mentor, promptly.", { x: 0.6, y: 6.15, w: 12, h: 0.5, fontSize: 15, bold: true, italic: true, color: "157A7C", margin: 0, isTextBox: true, objectName: "Tagline" });
  s.addNotes("Read them from the canon page, not from memory. Ask for a show of hands: which of these have you been asked to do that is not part of the role?");

  // ---------- 2 questions ----------
  k.section("2 Questions");
  k.divider(2, "Questions that open doors", "The difference between “did you enjoy it?” and “what did you make of it?”", null, "2 Questions");

  s = k.content("Open or closed?", "2 Questions");
  k.qa(s, 0.6, 1.5, 5.95, 2.2, "“Did you enjoy the ceremony?”", "Invites “yes”. He will say yes whether or not it is true, because you are kind and he does not want to disappoint you.", "0A4F72", 18, 15);
  k.qa(s, 6.75, 1.5, 5.95, 2.2, "“What did you make of tonight?”", "Invites the truth. He has to think, and what he says will tell you where he actually is.", "157A7C", 18, 15);
  k.card(s, 0.6, 3.95, 12.1, 2.45, "The test of an open question", "You cannot predict the answer. Most mentors ask closed questions out of kindness, to make it easy to answer. The kindness is in the open question, because it says: I want to know what you actually think. Start with what, how, or tell me about; never with did, are, is or have.", { fill: "E6F2F2", fontSize: 16 });
  s.addNotes("Two minutes. Then straight into the exercise.");

  s = k.content("Exercise 1: rewrite the six", "2 Questions");
  k.timer(s, "Pairs · 5 minutes");
  ["“Did you enjoy the ceremony?”", "“Are you settling in alright?”", "“Have you got any questions?”", "“Are you coming to the next meeting?”", "“Is the ritual learning going okay?”", "“Everything alright at home?”"].forEach((q, i) => {
    const col = i % 2, row = Math.floor(i / 2), x = 0.6 + col * 6.15, y = 1.45 + row * 1.5;
    s.addShape(pres.ShapeType.roundRect, { x, y, w: 5.95, h: 1.3, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Closed " + (i + 1) });
    s.addText([{ text: (i + 1) + "   ", options: { color: "157A7C", bold: true } }, { text: q, options: { color: "003668", bold: true } }], { x: x + 0.3, y, w: 5.4, h: 1.3, fontSize: 18, valign: "middle", margin: 0, isTextBox: true });
  });
  s.addText("Workbook page 3. Rewrite each so that you could not predict the answer. Compare across the room before the model answers.", { x: 0.6, y: 6.0, w: 12, h: 0.5, fontSize: 14, color: "06345D", margin: 0, isTextBox: true, objectName: "Instruction" });
  s.addNotes("Do not show the model answers until they have tried. Walk the room.");

  s = k.content("Six that work", "2 Questions");
  [["“Did you enjoy the ceremony?”", "What did you make of tonight?"], ["“Are you settling in alright?”", "What has surprised you most so far?"], ["“Have you got any questions?”", "What have you been wondering about that nobody has explained?"],
   ["“Are you coming to the next meeting?”", "What would make the next few months work well for you?"], ["“Is the ritual learning going okay?”", "How are you finding the learning, and what would help?"], ["“Everything alright at home?”", "How are things generally, with work and home, and how does Lodge fit around it all at the moment?"]].forEach(([c, o], i) => {
    const y = 1.4 + i * 0.83;
    s.addText(c, { x: 0.6, y, w: 4.6, h: 0.7, fontSize: 13.5, color: "6B7280", margin: 0, isTextBox: true, valign: "middle", objectName: "Closed q " + i });
    s.addShape(pres.ShapeType.rightArrow, { x: 5.3, y: y + 0.17, w: 0.5, h: 0.36, fill: { color: "BFD6EA" }, line: { color: "BFD6EA" }, objectName: "Arrow " + i });
    s.addShape(pres.ShapeType.roundRect, { x: 5.95, y, w: 6.75, h: 0.7, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.06, objectName: "Open bg " + i });
    s.addText(o, { x: 6.15, y, w: 6.4, h: 0.7, fontSize: 14.5, bold: true, color: "003668", margin: 0, isTextBox: true, valign: "middle", objectName: "Open q " + i });
  });
  s.addNotes("Model answers, not the only answers. The last one is the one that matters: ask it, mean it, wait.");

  s = k.content("Exercise 1, part two: ask it for real", "2 Questions");
  k.timer(s, "Pairs · 3 min each way");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.0, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Question band" });
  s.addText("“What did you make of your own Initiation, all those years ago?”", { x: 1.0, y: 1.5, w: 11.3, h: 2.0, fontSize: 28, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Big question" });
  k.card(s, 0.6, 3.75, 5.95, 2.65, "The asker", ["Ask it once. Then stop.", "One follow-up question at most", "Notice what he returns to"], { icon: I.comment, fontSize: 15 });
  k.card(s, 6.75, 3.75, 5.95, 2.65, "The listener", ["Answer honestly; you were new once", "Notice how it feels to be asked properly", "Afterwards, write one thing your partner said that you would not have guessed"], { icon: I.ear, fontSize: 15 });
  s.addNotes("The question does double duty: it practises the skill and reminds them what being new felt like. Debrief: what did it feel like to be asked properly?");

  // ---------- 3 listening ----------
  k.section("3 Listening");
  k.divider(3, "Listening, and the three-second rule", "What you hear the second time that you missed the first", null, "3 Listening");

  s = k.content("Sixty seconds of bad listening", "3 Listening");
  k.timer(s, "Demonstration · 1 min");
  k.card(s, 0.6, 1.5, 5.95, 4.9, "What you will see", ["Interrupting", "Topping his story with a better one", "Filling every pause", "Looking at the door, the bar, the phone", "Answering a question he did not ask"], { icon: I.ban, fontSize: 16, headColor: "0A4F72" });
  k.card(s, 6.75, 1.5, 5.95, 4.9, "What good looks like", ["Listen for tone and hesitation, not only words", "Notice what he returns to, and what he leaves out", "When silence falls, count to three before you speak", "He will usually fill it. What he says then is the real answer", "The awkwardness is yours, not his. He is thinking"], { icon: I.ear, fontSize: 16, headColor: "157A7C" });
  s.addNotes("Brief a volunteer beforehand. Play it broad; the room will laugh in recognition, and that recognition is the lesson. Then teach the rule.");

  s = k.content("Exercise 2: listening only", "3 Listening");
  k.timer(s, "Pairs · 3 min each way");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 1.6, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Rule band" });
  s.addText("The listener may say nothing, except to ask one further question.", { x: 1.0, y: 1.5, w: 11.3, h: 1.6, fontSize: 26, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Rule" });
  k.card(s, 0.6, 3.35, 5.95, 3.05, "Same question as before", "“What did you make of your own Initiation, all those years ago?” Swap roles from Exercise 1 if you like. Count to three in every silence.", { icon: I.comment, fontSize: 15 });
  k.card(s, 6.75, 3.35, 5.95, 3.05, "Then write, workbook page 4", "What did you hear the second time that you missed the first?", { icon: I.book, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Debrief on one question only: what did you hear the second time? Expect: the real reason, the thing he returned to, the hesitation before an answer.");

  // ---------- 4 scenarios ----------
  k.section("4 Scenarios");
  k.divider(4, "Scenarios", "Tonight, this week, this month. And who else needs to know", null, "4 Scenarios");

  s = k.content("Exercise 3: one scenario per table", "4 Scenarios");
  k.timer(s, "Fours · 10 minutes");
  [["A", "The overwhelmed Entered Apprentice", "Initiated two months ago. “Honestly, I still haven’t a clue what’s going on in there. Everyone else seems to just know.” Smiling, but he has said it twice.", "003668"],
   ["B", "The quiet drift", "A Master Mason of three years, not your mentee. Two consecutive meetings missed without apology. Subscription unpaid. Passed over for Inner Guard last year.", "0A4F72"],
   ["C", "The ritual dread", "Offered his first office. Barely slept before his Second Degree questions; thinking of saying no. “I’m just not a performer, and I think they’ll think less of me.”", "106576"],
   ["D", "The eager recruiter", "At the bar, a senior Brother to your recently raised mentee: “You’re not a proper Mason till you’ve done the Chapter. I’ll put your name down.” Your mentee looks cornered.", "157A7C"]].forEach(([l, h, d, hex], i) => {
    const col = i % 2, row = Math.floor(i / 2), x = 0.6 + col * 6.15, y = 1.45 + row * 2.4;
    s.addShape(pres.ShapeType.roundRect, { x, y, w: 5.95, h: 2.2, fill: { color: "F2F7FC" }, line: { color: "F2F7FC" }, rectRadius: 0.08, objectName: "Scenario " + l });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.25, y: y + 0.2, w: 0.6, h: 0.6, fill: { color: hex }, line: { color: hex }, objectName: "Scenario circle " + l });
    s.addText(l, { x: x + 0.25, y: y + 0.2, w: 0.6, h: 0.6, fontSize: 18, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(h, { x: x + 1.0, y: y + 0.2, w: 4.8, h: 0.6, fontSize: 16, bold: true, color: hex, margin: 0, isTextBox: true, valign: "middle" });
    s.addText(d, { x: x + 0.25, y: y + 0.9, w: 5.45, h: 1.25, fontSize: 12.5, color: "1E2329", margin: 0, isTextBox: true, valign: "top" });
  });
  s.addText("Workbook pages 5 and 6. What do you do tonight, this week, this month, and who else needs to know? Two minutes a table to report back.", { x: 0.6, y: 6.3, w: 12, h: 0.4, fontSize: 13, color: "06345D", margin: 0, isTextBox: true, objectName: "Instruction" });
  s.addNotes("One scenario per table, ten minutes, one reporter per table. Keep the debrief keys for the next slide.");

  s = k.content("Debrief: what good looks like", "4 Scenarios");
  [["A", "Normalise it. Name the two shocks. Book the one-to-one before the next meeting. Pace the information; Initiate’s Guide and Welcome Apprentice, together.", "003668"],
   ["B", "Best-placed friend rings within seven days: “you were missed”. Treasurer’s signal to the Almoner and Lodge Mentor, not round the bar. Under-use named as a cause. Step one of four.", "0A4F72"],
   ["C", "Protect him from pressure both ways. No office before ready; explore what ready would need: LoI, a small first piece, a shared office. His contribution is valid with or without ritual.", "106576"],
   ["D", "Rescue in the moment with grace; never embarrass the senior Brother publicly. Afterwards: information, not recruitment; the timing is his; the Royal Arch Representative when he is ready.", "157A7C"]].forEach(([l, d, hex], i) => {
    const col = i % 2, row = Math.floor(i / 2), x = 0.6 + col * 6.15, y = 1.45 + row * 2.4;
    k.numbered(s, x, y, 5.95, 2.2, l, ["The overwhelmed EA", "The quiet drift", "The ritual dread", "The eager recruiter"][i], d, hex, { fontSize: 13.5 });
  });
  s.addNotes("Show only after every table has reported. Draw the four steps out of B explicitly.");

  s = k.content("The warning signs, and the four steps", "4 Scenarios");
  k.card(s, 0.6, 1.4, 5.95, 2.4, "The pattern is the signal", ["A break in his own pattern, not a low level of attendance", "Two consecutive misses without a word; going quiet; dropping out of LoI; money or time talk; a flat mood at dinner", "One is nothing. A pattern is a conversation"], { icon: I.eye, fontSize: 13.5 });
  k.card(s, 6.75, 1.4, 5.95, 2.4, "The right question", "Always “How can I help?”, never “Why haven’t you been attending?”. The tone decides whether he feels supported or judged. Warm and informal first: a call, a message, a coffee.", { icon: I.heart, fontSize: 14.5, fill: "E6F2F2" });
  [["1", "You", "Friendly, informal contact. After two consecutive misses, within seven days of the second.", "003668"], ["2", "Lodge Mentor", "The overview; what could the Lodge itself change; a discreet note; close the loop.", "0A4F72"], ["3", "Worshipful Master", "Where it touches Lodge culture, office or another member. Almoner alongside for welfare.", "106576"], ["4", "The Province", "An impartial voice, or a Lodge where he might thrive. Responsible mentoring, not failure.", "157A7C"]].forEach(([n, h, d, hex], i) => {
    const x = 0.6 + i * 3.08;
    k.numbered(s, x, 4.0, 2.9, 2.4, n, h, d, hex, { fontSize: 12, headSize: 14 });
  });
  s.addNotes("Most concerns end at step one and never look like a process. The Warning Signs card has all of this on one side.");

  // ---------- 5 tools and close ----------
  k.section("5 Close");
  k.divider(5, "The tools, and one thing", "Where the library lives, and what you will do this month", null, "5 Close");

  s = k.content("Reach for the right tool", "5 Close");
  [["Personal Mentor’s Short Guide", "Five pages. The role, the journey, the conversations, help for you. Read it on the train.", I.book],
   ["Mentor Meeting Guide", "A conversation guide for one-to-ones, stage by stage. Open it before each meeting.", I.comment],
   ["Stage Checklists", "One page each: Initiation night, second meeting, before Passing and Raising, Installation, first LoI.", I.check],
   ["Warning Signs card", "The signs and the four steps on a card for your pocket.", I.eye],
   ["Solomon", "solomon.ugle.org.uk. Send him there, and go yourself. Welcome Apprentice is the place to start.", I.laptop],
   ["People", "The monthly call, first Tuesday 7pm on Teams. DAWG. Your Lodge Mentor. The Provincial office, in confidence.", I.users]].forEach(([h, d, ic], i) => {
    const col = i % 3, row = Math.floor(i / 3), x = 0.6 + col * 4.1, y = 1.45 + row * 2.5;
    k.card(s, x, y, 3.85, 2.3, h, d, { icon: ic, fontSize: 13.5, headSize: 15 });
  });
  s.addNotes("Two minutes each on the Meeting Guide and the Stage Checklists: where they live, when to reach for them.");

  s = k.content("One thing", "5 Close");
  s.addShape(pres.ShapeType.roundRect, { x: 0.6, y: 1.5, w: 12.1, h: 2.4, fill: { color: "003668" }, line: { color: "003668" }, rectRadius: 0.08, objectName: "Commit band" });
  s.addText("One thing I will do differently with my mentee this month.", { x: 1.0, y: 1.5, w: 11.3, h: 2.4, fontSize: 30, bold: true, color: "FFFFFF", margin: 0, isTextBox: true, valign: "middle", objectName: "Commitment" });
  k.card(s, 0.6, 4.15, 5.95, 2.25, "Write it, then say it", "Workbook page 8. By when, and how you will know it worked. Then round the room, one sentence each.", { icon: I.flag, fontSize: 15 });
  k.card(s, 6.75, 4.15, 5.95, 2.25, "You will hear from me", "One month from tonight, a message: what did you try, and what happened? It is the habit the course teaches, so I will practise it on you.", { icon: I.clock, fontSize: 15, fill: "E6F2F2" });
  s.addNotes("Do not let anyone pass. A commitment said aloud is twice as likely to happen.");

  s = k.dark("5 Close", "Family, Work, Masonry: in that order, always.", "Freemasonry must be fun. A man who is enjoying himself attends; a man who attends participates; a man who participates belongs; and a man who belongs does not resign. That is what it is all about. Thank you.");
  s.addText("Prepare  •  Guide  •  Support  •  Enlighten", { x: 0.9, y: 5.6, w: 11, h: 0.5, fontSize: 18, bold: true, color: "8FD3D1", margin: 0, isTextBox: true, objectName: "Principles line" });
  s.addNotes("Close on the principles, read from the canon page. Names to the Lodge Mentors and APGMen; everyone onto DAWG.");

  console.log("written", await k.finish(OUT));
})().catch(e => { console.error(e); process.exit(1); });
