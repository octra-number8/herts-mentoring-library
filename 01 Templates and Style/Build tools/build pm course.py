"""E2a Personal Mentor Course — facilitator guide and participant workbook on the template.
Usage: build_pm_course.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, TEAL, PALE, PALETEAL, DARK
from docx.shared import Pt

template, out_dir = sys.argv[1], sys.argv[2]

CASE = ("“I joined at thirty-four, proposed by a colleague I liked. My Initiation was extraordinary; I drove home buzzing. "
        "Then came my second meeting: nobody had told me it was mainly business, and I sat at dinner next to two men who talked "
        "across me all night about people I didn’t know. At my first rehearsal evening I was told after ten minutes there was "
        "nothing for me and I should get off home. Work went mad that spring; I missed two meetings. Nobody rang. When I came back, "
        "someone at the bar said, ‘Well, look who’s remembered where we meet.’ Everyone laughed. I laughed too. My subscription renewal "
        "came in January with a letter that read like a final demand. I paid it, and then I sat down one Sunday and wrote a different "
        "letter. The Secretary’s reply was very polite. It said my resignation had been received and would be reported to the Lodge. "
        "Nobody ever asked me why.”")

CLOSED = ["“Did you enjoy the ceremony?”", "“Are you settling in alright?”", "“Have you got any questions?”",
          "“Are you coming to the next meeting?”", "“Is the ritual learning going okay?”", "“Everything alright at home?”"]
OPEN = ["What did you make of tonight?", "What has surprised you most so far?", "What have you been wondering about that nobody has explained?",
        "What would make the next few months work well for you?", "How are you finding the learning, and what would help?",
        "How are things generally, with work and home, and how does Lodge fit around it all at the moment?"]

SCENARIOS = [
    ("A", "The overwhelmed Entered Apprentice",
     "Your mentee, initiated two months ago, says at the Festive Board: “Honestly, I still haven’t a clue what’s going on in there. "
     "Everyone else seems to just know.” He is smiling, but he has said it twice now.",
     "What do you do tonight, this week, this month?",
     "Normalise it: everyone felt this. Name the two shocks (unfamiliar sights, unfamiliar language). Book the one-to-one before the next meeting. "
     "Pace the information; do not try to explain everything in one go. Point him at the Initiate’s Guide and Welcome Apprentice on Solomon, together."),
    ("B", "The quiet drift",
     "A Master Mason of three years, not your mentee but a man you know, has missed two consecutive meetings without apology. "
     "The Treasurer mentions his subscription is unpaid. He was passed over for Inner Guard last year.",
     "Who acts, in what order, and what is said in the first phone call?",
     "His Personal Mentor or the best-placed friend rings within seven days of the second miss. Tone: “you were missed”, never “why weren’t you there”. "
     "The Treasurer’s signal goes to the Almoner and Lodge Mentor, not round the bar. Under-use is a likely cause: name it as a possibility. "
     "This is Step 1 of the four steps, and most concerns end here."),
    ("C", "The ritual dread",
     "Your mentee has been offered his first office. He tells you privately he barely slept before his Second Degree questions and is "
     "thinking of saying no: “I’m just not a performer, and I think they’ll think less of me.”",
     "What does good mentoring look like here, in both directions: to him, and to the Lodge?",
     "Protect him from pressure in both directions. No office before he is ready, but explore what ready would need: the Lodge of Instruction, "
     "a small first piece, a shared office. His contribution is valid with or without ritual. Speak to the Lodge Mentor so the DC and WM know where he is, "
     "and so he is not left waiting either."),
    ("D", "The eager recruiter",
     "At the bar, a well-meaning senior Brother is pressing your recently raised mentee about joining the Chapter: “You’re not a proper Mason "
     "till you’ve done it, you know. I’ll put your name down.” Your mentee looks cornered.",
     "What do you do in the moment, and afterwards?",
     "Rescue him in the moment with grace: a change of subject, a drink to fetch, a Brother he must meet. Never embarrass the senior Brother publicly. "
     "Afterwards, reaffirm: information, not recruitment; the decision and its timing are his alone; the Royal Arch Representative is the person to talk to when he is ready. "
     "A quiet word via the Lodge Mentor if it recurs."),
]


# ======================= FACILITATOR GUIDE =======================
def facilitator():
    out = os.path.join(out_dir, "E2a Personal Mentor Course Facilitator Guide Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="Personal Mentor Course · Facilitator Guide")
    b.opening("Training and development · E2a", "Personal Mentor Course",
              "The facilitator’s guide for the Province’s Personal Mentor course: a two-hour evening delivered in person by the Deputy Provincial Grand Mentor. "
              "Conversation is the method as well as the subject.",
              [("Audience", "Facilitator (W Bro Wes Pierce, Deputy Provincial Grand Mentor); any APGMen or Lodge Mentor delivering it on his behalf"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · Builds on the Personal Mentor Workshop (E2, July 2026)")])

    b.h1("1", "What the course does")
    b.para("Most Personal Mentors have never been trained to mentor, and most do not need much. What they need is confidence in a handful of skills: "
           "asking questions that open people up, listening properly, sitting with silence, spotting trouble early, and knowing where their role ends. "
           "The course teaches exactly that, mostly by doing rather than being told. Every exercise is a conversation, because that is the job.", after=6)
    b.h2("By the end, every participant can")
    b.bullets([
        "Say what a Personal Mentor is and is not, in one sentence each, and name the boundary with the Almoner and the Lodge Mentor.",
        "Turn a closed question into an open one, and ask it.",
        "Listen for tone and hesitation, and hold a three-second silence.",
        "Recognise the warning signs, and say who acts, in what order, under the four steps.",
        "Find the Mentor Meeting Guide, the Stage Checklists and the Warning Signs card, and say when to reach for each.",
        "Name one thing he will do differently with his mentee this month.",
    ])
    b.h2("Who it is for")
    b.para("Personal Mentors, newly appointed or long-serving; Lodge Mentors who want to run it locally; eight to sixteen participants. "
           "Fewer than six and the pair exercises thin out; more than sixteen and the debriefs run long. Mixed experience is an asset: the "
           "experienced hear what being new felt like, and the new hear what good looks like.", after=6)

    b.h1("2", "Format")
    b.table([
        ["Length", "One evening, two hours. Arrive from 7.00, start 7.15, finish 9.15."],
        ["Venue", "A Masonic centre or Lodge room with tables of four and space to move into pairs. A flipchart."],
        ["Group size", "Eight to sixteen. Fewer than six and the pair exercises thin out; more than sixteen and the debriefs run long."],
        ["Materials", "Printed workbook per participant; one set of the library documents per table; slides on a screen if the room has one, though the course runs without them."],
        ["Follow-up", "Names to the Lodge Mentor and APGMen; everyone added to DAWG and told about the monthly call; a message from the facilitator one month on."],
    ], [1900, 7512])

    b.h1("3", "Run-sheet: two hours")
    b.table([
        ["Time", "Segment", "What you do"],
        ["0.00", "Welcome and the story of a man we lost (15 min)", "Two sentences on why they are here, then read the case study aloud, slowly, from the workbook. Ask: where were the moments this could have been turned around? Flipchart them; there are at least six. Land it: none required expertise, all required someone noticing. The role in one sentence: a friend with a purpose."],
        ["0.15", "What the role is, and is not (15 min)", "Walk the IS / IS NOT table (slide and workbook page 2). Emphasise the boundaries that free people: not a ritual coach, not a welfare officer, not a reporter. Coach, not counsellor. Referring early is the skill, not the failure. Read the four principles from the canon page; say they are not stages."],
        ["0.30", "Exercise 1: questions that open doors (30 min)", "Teach open versus closed in two minutes with the two ceremony questions. Pairs rewrite the six closed questions (workbook page 3); five minutes; compare across the room; then show the model answers. Live practice: three minutes each way on “What did you make of your own Initiation, all those years ago?” Debrief: what did it feel like to be asked properly?"],
        ["1.00", "Exercise 2: listening and the three-second rule (25 min)", "Demonstrate bad listening for sixty seconds with a volunteer: interrupt, top his story, fill every pause. Let them laugh. Teach: listen for tone and hesitation, not only words; when silence falls, count to three before speaking; what he says next is usually the real answer. Pairs repeat Exercise 1 with the listener forbidden to speak except to ask one further question. Debrief: what did you hear the second time that you missed the first?"],
        ["1.25", "Exercise 3: scenarios (25 min)", "Tables of four take one scenario each (workbook pages 5 to 6), ten minutes: tonight, this week, this month, and who else needs to know. Report back, two minutes a table. Draw out the four steps and the hand-offs on the Warning Signs card. Use the debrief keys in section 5."],
        ["1.50", "The tools and the close (10 min)", "Two minutes each on the Mentor Meeting Guide and the Stage Checklists: where they live, when to reach for them. Then the commitment: each participant writes one thing he will do differently with his mentee this month (workbook page 8) and says it aloud. Close on the four principles and “Family, Work, Masonry”."],
    ], [1000, 2900, 5512], header=True)

    b.h1("4", "Scripts and teaching points")
    b.h2("The role in one sentence")
    b.panel(["**A Personal Mentor is a friend with a purpose.** Not an expert, not a teacher, not a ritualist: the person a new Brother can ring, message or sit next to without feeling he is bothering anyone."], fill=PALE, bar=DEEP)
    b.h2("Open versus closed")
    b.para("“Did you enjoy the ceremony?” invites “yes”. “What did you make of tonight?” invites the truth. The test of an open question is that you cannot "
           "predict the answer. Most mentors ask closed questions out of kindness, to make it easy to answer. The kindness is in the open question, "
           "because it says: I want to know what you actually think.", after=6)
    b.h2("The three-second rule")
    b.para("When silence falls, count to three before you speak. The mentee will usually fill it, and what he says then is the real answer. Most of us "
           "fill silence within a second because it feels awkward. The awkwardness is yours, not his; he is thinking.", after=6)
    b.h2("Coach, not counsellor")
    b.para("If he tells you something that touches his health, money, family or safety, speak to the Lodge Almoner and the Lodge Mentor promptly. "
           "You are not expected to carry it alone, and he will be better served if you do not. Referring early is the skill, not the failure.", after=6)
    b.h2("The four steps, in one breath")
    b.para("Personal Mentor first, warm and informal. Then the Lodge Mentor, who takes the overview and asks what the Lodge could change. Then the "
           "Worshipful Master, with the Almoner alongside for welfare. Then the Province. Most concerns end at step one and never look like a process.", after=6)

    b.h1("5", "Exercise materials and debrief keys")
    b.h2("Exercise 1: model answers (do not show until after the rewrite)")
    b.table([[c, o] for c, o in zip(CLOSED, OPEN)], [4000, 5412])
    b.h2("Exercise 3: debrief keys")
    b.table([[f"{k}  {t}", key] for k, t, _, _, key in SCENARIOS], [2600, 6812])

    b.h1("6", "Materials checklist")
    b.table([
        ["Bring", ["Workbook, one per participant, printed single-sided for writing", "Library set per table: Personal Mentor’s Short Guide, Mentor Meeting Guide, Stage Checklists, Warning Signs card, the Principles page", "Slides on a screen if the room has one; the course runs without them", "Flipchart and pens; name badges; a volunteer briefed for the bad-listening demonstration"]],
    ], [1600, 7812])

    b.h1("7", "After the course")
    b.bullets([
        "Names of attendees to each Lodge Mentor and APGMen; attendance noted on the Provincial register.",
        "Every attendee added to DAWG and told about the monthly mentoring call: first Tuesday, 7pm, Teams.",
        "One month on, a message from the facilitator to each attendee: “What did you try, and what happened?” It models the habit the course teaches.",
        "Feedback captured on one question: what will you do differently? Collate it for the next issue of this guide.",
    ])
    b.closing("Personal Mentor Course Workbook · Personal Mentor Course slides · Personal Mentor’s Short Guide · Mentor Meeting Guide · Warning Signs card")
    print("saved", b.save())


# ======================= WORKBOOK =======================
def writing_lines(b, n=5):
    rows = [[""] for _ in range(n)]
    t = b.doc.add_table(rows=n, cols=1)
    b._widths(t, [9412])
    b._borders(t, {"insideH": ("single", 4, "9FB3C8"), "bottom": ("single", 4, "9FB3C8")})
    b._margins(t, 120, 120, 60, 60)
    for r in t.rows:
        r.cells[0].paragraphs[0].paragraph_format.space_after = Pt(6)
    b.spacer()


def workbook():
    out = os.path.join(out_dir, "E2a Personal Mentor Course Workbook Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="Personal Mentor Course · Workbook")
    b.opening("Training and development · E2a", "Personal Mentor Course Workbook",
              "Your workbook for the Province’s Personal Mentor course. Bring it to the session, write in it, and keep it: "
              "the exercises are the ones you will use with your mentee.",
              [("Participant", "Name:  ______________________________     Lodge:  ______________________________"),
               ("Delivered by", "W Bro Wes Pierce, Deputy Provincial Grand Mentor · Issue 1, October 2026")])

    b.h1("1", "The story of a man we lost")
    b.panel([CASE], fill=PALE, bar=DEEP)
    b.para("**Where were the moments this could have been turned around?** Mark them in the story and list them here.", after=4, keep=True)
    writing_lines(b, 6)

    b.h1("2", "What the role is, and is not")
    b.table([
        ["Your role is", "Your role is not"],
        [["His first point of contact for any question", "Someone who keeps in touch between meetings", "A listener who notices when something changes", "His bridge to the Lodge and the Province"],
         ["The only person who can help him", "A ritual coach; that is the Lodge of Instruction", "Someone who monitors or reports on him", "A replacement for the Lodge Mentor, who co-ordinates"]],
    ], [4706, 4706], header=True)
    b.para("**The four principles.** Defined once in *The Hertfordshire Mentoring Principles*. They run together, all the time. They are not stages.", after=6, keep=True)
    b.principles_strip()
    b.panel(["**Coach, not counsellor.** If he tells you something that touches his health, money, family or safety, speak to the Lodge Almoner and the Lodge Mentor promptly. Referring early is the skill, not the failure."], fill=PALETEAL, bar=TEAL)

    b.h1("3", "Exercise 1: questions that open doors")
    b.para("A closed question invites a one-word answer. An open question invites the truth. Rewrite each of these so that you could not predict the answer.", after=6)
    b.table([["Closed", "Your open version"]] + [[c, ""] for c in CLOSED], [4000, 5412], header=True, row_height=560)
    b.para("**Live practice, three minutes each way.** Ask your partner: *“What did you make of your own Initiation, all those years ago?”* Then listen. Note one thing he said that you would not have guessed.", after=4, keep=True)
    writing_lines(b, 3)

    b.h1("4", "Exercise 2: listening, and the three-second rule")
    b.panel(["**The rule.** When silence falls, count to three before you speak. He will usually fill it, and what he says then is the real answer.",
             "**Listen for** tone, hesitation, what he returns to, and what he does not say."], fill=PALE, bar=DEEP)
    b.para("Repeat the conversation from Exercise 1. This time the listener may say nothing except to ask one further question. Afterwards:", after=4, keep=True)
    b.para("**What did you hear the second time that you missed the first?**", after=4, keep=True)
    writing_lines(b, 4)

    b.h1("5", "Exercise 3: scenarios")
    b.para("Your table takes one scenario. Ten minutes. What would you do **tonight, this week, this month**, and **who else needs to know**?", after=6)
    for k, t, sit, q, _ in SCENARIOS:
        b.h2(f"Scenario {k}: {t}")
        b.panel([sit, f"**{q}**"], fill=PALE, bar=TEAL)
        b.table([["Tonight", ""], ["This week", ""], ["This month", ""], ["Who else needs to know", ""]], [2400, 7012], row_height=720)

    b.h1("6", "The warning signs and the four steps")
    b.para("Risk shows as a break in his own pattern, not as a low level of attendance. One sign is nothing. A pattern is a conversation.", after=6)
    b.table([
        ["Attendance", "Two or more consecutive meetings missed without a word; attending only Installations or socials; a summer absence that runs into autumn."],
        ["Participation", "Reluctance to accept work or office; withdrawal from conversation; missing the Lodge of Instruction while holding office; visible unhappiness."],
        ["Communication", "Unanswered calls and messages; expressed frustration; repeated talk of time or money pressure; subscription arrears."],
    ], [2400, 7012])
    b.table([
        ["Step 1", "You. Friendly, informal contact after any unexpected absence. After two consecutive misses, within seven days of the second meeting."],
        ["Step 2", "The Lodge Mentor. Takes the overview; asks what the Lodge itself could change; keeps a discreet note; closes the loop with the member."],
        ["Step 3", "The Worshipful Master, with the Almoner alongside for anything touching welfare."],
        ["Step 4", "The Province. An impartial voice, or a different Lodge where he might thrive. Referral is responsible mentoring, not failure."],
    ], [1400, 8012])
    b.panel(["**The right question.** Always “How can I help?”, never “Why haven’t you been attending?”."], fill=PALE, bar=DEEP)

    b.h1("7", "The tools, and where they live")
    b.table([
        ["Personal Mentor’s Short Guide", "The role, the journey at a glance, the conversations that matter, help for you. Read it on the train."],
        ["Mentor Meeting Guide", "A conversation guide for one-to-one meetings, stage by stage. Reach for it before each one-to-one."],
        ["Stage Checklists", "One page each for Initiation night, the second meeting, before Passing and Raising, Installation and first LoI."],
        ["Warning Signs card", "The signs and the four steps on one card for your pocket."],
        ["Solomon", "UGLE’s learning platform: solomon.ugle.org.uk. Send him there, and go yourself."],
        ["Monthly mentoring call", "First Tuesday of the month, 7pm, Teams. Bring questions."],
        ["DAWG", "The Daily Advancement WhatsApp Group, run by the Provincial Mentoring Team. Ask to be added."],
    ], [3000, 6412])

    b.h1("8", "My commitment")
    b.panel(["**One thing I will do differently with my mentee this month:**"], fill=PALETEAL, bar=TEAL)
    writing_lines(b, 4)
    b.para("**By when:**  ____________________        **I will know it worked when:**  ______________________________________________", after=10)
    b.para("**Family, Work, Masonry: in that order, always.** Freemasonry must be fun. A man who is enjoying himself attends; a man who attends participates; "
           "a man who participates belongs; and a man who belongs does not resign. That is the whole job.", color=DARK, after=6)
    b.closing("Personal Mentor Course Facilitator Guide · Personal Mentor’s Short Guide · Mentor Meeting Guide · Stage Checklists · Warning Signs card")
    print("saved", b.save())


facilitator()
workbook()
