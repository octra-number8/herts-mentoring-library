"""E6a The Chair and Beyond — one-hour session for Wardens and Masters: facilitator guide and action plan.
Usage: build_chair_course.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, TEAL, PALE, PALETEAL, DARK
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

template, out_dir = sys.argv[1], sys.argv[2]


def facilitator():
    out = os.path.join(out_dir, "E6a The Chair and Beyond Facilitator Guide Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="The Chair and Beyond · Facilitator Guide")
    b.opening("Training and development · E6a", "The Chair and Beyond",
              "The facilitator’s guide for a one-hour session for Wardens, Masters Elect and Masters in the Chair, delivered in person by the "
              "Deputy Provincial Grand Mentor. The things about the year that are not in the ritual book, seen through the eyes of the newest man in the room.",
              [("Audience", "Facilitator (W Bro Wes Pierce, Deputy Provincial Grand Mentor); APGMen delivering it locally"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · Draws on the Lodge Mentor’s Guide Issue 2 (4.6, 4.7, 8.2, 10) and the Personal Mentoring Plan stages 6 and 7")])

    b.h1("1", "What the session does")
    b.para("The ritual book tells a Master what to say. Nothing tells him that the culture of his Lodge is, for one year, his; that the newest "
           "member’s whole impression of Freemasonry will be formed in that year; and that the year after the Chair is the second recognised point "
           "at which good men leave. This hour covers those three things, and gives the Wardens two years’ notice of them.", after=6)
    b.h2("By the end, every participant can")
    b.bullets([
        "Name the five things a Master does for mentoring that nobody else can do.",
        "See his own Lodge year as a new member will experience it, and spot the moments that need designing rather than leaving to chance.",
        "Say where the office queue in his Lodge is pushing men too early or leaving them waiting, and what he will do about it.",
        "Say what Family, Work, Masonry means for the Master himself, and who he delegates to.",
        "Leave with his year after the Chair already sketched: a role, a project, a Brother to mentor.",
    ])
    b.h2("Format")
    b.table([
        ["Length", "Sixty minutes; arrive from 7.00, start 7.15, finish 8.15. Tables of four to six, Masters and Wardens mixed."],
        ["Who", "Junior and Senior Wardens, Masters Elect, Masters in the Chair. Six to twenty-four. Lodge Mentors welcome as observers."],
        ["Materials", "The Chair and Beyond action sheet and pocket card, one each per participant. One library set per table: Lodge Mentor’s Short Guide, Stage Checklists, Warning Signs card, the Principles page."],
        ["Follow-up", "Action sheets photographed and kept. The Lodge Mentor of each participant told what he committed to. APGMen follows up within the month."],
    ], [1900, 7512])

    b.h1("2", "Run-sheet: sixty minutes")
    b.para("Each segment opens with two true-or-false statements on the screen: hands up for true, then the answer. Two minutes, inside the segment time. The twelve statements, their answers and their sources are in section 7, with ten more facts for questions from the floor. The pocket card carries all twenty-two.", after=6)
    b.table([
        ["Time", "Segment", "What you do"],
        ["0.00", "Why you (7 min)", "Open on the newest man in the room: whoever was initiated most recently into any Lodge represented. His whole impression of Freemasonry will be formed in somebody’s year in the Chair. Then the two recognised drop-out windows: the first two years, and the year after the Chair. The Master is standing in both at once: his new members are in the first, and he is about to enter the second."],
        ["0.07", "Your year through a new man’s eyes (10 min)", "Walk one year of your Lodge as an Initiate experiences it: the ballot, Initiation night, the second meeting that is mostly business, the nights he cannot attend, his Passing, the summer break. Ask the room which of those moments their Lodge designs and which it leaves to chance. Then the five things only the Master can do (section 3). Action sheet box 1."],
        ["0.17", "Exercise: the office queue (8 min)", "On the action sheet, each Master or Warden maps his progressive officers for the next three years and marks two men: one at risk of being pushed before he is ready, one capable man left waiting. Four minutes writing; four minutes of examples round the room. Land it: a bored Brother leaves as surely as a frightened one."],
        ["0.25", "Running a happy year (10 min)", "Not the ritual: the management. Working with the Secretary, DC, Almoner and Lodge Mentor; the Festive Board tone (the joke at the bar that cost a member); never letting a new or joining member dine alone; hearing the Lodge Mentor’s report with the same weight as the Treasurer’s. Then the Master’s own wellbeing: Family, Work, Masonry applies to him too; delegate; it is a team, not a performance."],
        ["0.35", "For the Wardens: two years’ notice (8 min)", "What to do now: learn the Lodge, not only the ritual; shadow the Master at the Committee and with the Secretary; choose your team early and kindly; plan your year’s programme now; visit; make sure the Royal Arch has been explained to you; keep your own mentor. Action sheet box 2."],
        ["0.43", "After the Chair (10 min)", "The second window. The Immediate Past Master’s year: a seat, a role and a purpose, or a slow fade. Included, Involved, Interested. Past Masters make the best Personal Mentors; say that plainly and ask who in the room will take one. Plan the year after from Installation day; the Lodge Mentor will ask. Action sheet box 3."],
        ["0.53", "Action plan and close (7 min)", "Box 4: one thing I will change in my year, or in my two years as a Warden, by a date. Round the room, one sentence each. Close on the principles and Family, Work, Masonry."],
    ], [1000, 2700, 5712], header=True)

    b.h1("3", "The five things only the Master can do")
    b.table([
        ["1", "Set the tone", "The culture of the Lodge for a year is the Master’s. What he laughs at, who he sits with, how he speaks to the newest member: the Lodge copies it."],
        ["2", "Hear the Lodge Mentor’s report", "On the Committee agenda, with the same weight as the Treasurer’s. Ask who has a Personal Mentor and a Plan, who has been missed, and what the Lodge could change."],
        ["3", "Brief the Lodge on mentoring", "Once in the year, in open Lodge: what mentoring is in Hertfordshire, and that we are all mentors to others. The Lodge Mentor has the presentation."],
        ["4", "Protect juniors from pressure", "No office before ready; no ritual beyond ability; no Chapter sales pitch at the bar. And no capable man left waiting. The Master owns the office queue with the DC."],
        ["5", "Own the Step 3 conversation", "When a member is drifting and the matter touches Lodge culture, office or another member, the Master has the conversation, with the Almoner alongside for welfare. “How can we help?”, never “Why weren’t you there?”"],
    ], [700, 2600, 6112])

    b.h1("4", "Teaching points, in the facilitator’s words")
    b.panel(["**The newest man in the room.** Every Master should be able to name him, say who his Personal Mentor is, and say what his next ceremony is. If he cannot, that is the first action."], fill=PALE, bar=DEEP)
    b.h2("The second meeting")
    b.para("The Initiate’s second meeting is often mostly business, and nobody has told him. He sits at dinner next to two men who talk across him "
           "about people he does not know. It is the moment most often left to chance, and it is the Master’s to design: a word before the meeting, "
           "a seat beside his mentor, a Brother briefed to include him.", after=6)
    b.h2("The joke at the bar")
    b.para("“Well, look who’s remembered where we meet.” Everyone laughed; so did he; and he wrote his letter in January. The Master sets whether "
           "that joke gets told. One quiet word to the Lodge about how returning members are greeted is worth a year of retention work.", after=6)
    b.h2("Family, Work, Masonry, for the Master too")
    b.para("The year in the Chair is the point at which a Lodge is most likely to ask too much of one man. The Master who delegates, who lets the "
           "Wardens and the DC carry their share, and who protects his own family and work, finishes the year wanting more Freemasonry, not less. "
           "The one who does not is the one the Lodge loses in the year after.", after=6)
    b.h2("Included, Involved, Interested")
    b.para("The Immediate Past Master’s year decides whether a Lodge keeps its Past Masters. A seat is not a purpose. A role, a project, a Brother "
           "to mentor: agree it before Installation, not after. Past Masters make the best Personal Mentors because they remember what the "
           "Chair cost and what it gave.", after=6)

    b.h1("5", "Working with the other officers in your year")
    b.table([
        ["Lodge Mentor", "Your report on the agenda; who has a mentor and a Plan; the office queue; the newest man. Three minutes a meeting."],
        ["Director of Ceremonies", "Ceremony preparation, the Lodge of Instruction, and how juniors are drawn into ritual gently. The office queue is a joint decision."],
        ["Secretary", "The candidate timeline your year hangs from; the attendance record after every meeting; same-day notice of any resignation."],
        ["Almoner", "Welfare, and Step 3 alongside you. Welcome new members jointly."],
        ["Treasurer", "Arrears as an early signal. Agree that a first missed subscription earns a quiet word, not a letter that reads like a final demand."],
        ["Royal Arch Representative", "One Journey’s bridge. Agree what is said about the Royal Arch, when and by whom. Information, not recruitment."],
    ], [2600, 6812])

    b.h1("6", "Materials and follow-up")
    b.table([
        ["Materials", ["Action sheet and pocket card, one each per participant", "Library set per table", "Slides on a screen if the room has one; the session runs without them", "Lodge Mentor’s Short Guide for any Master who has not seen it"]],
        ["Follow-up", ["Action sheets photographed; each participant’s Lodge Mentor told what he committed to", "APGMen follows up within the month", "Wardens invited to the next running of this session before their own Installation", "Feedback on one question: what will you do differently in your year?"]],
    ], [1600, 7812])

    b.h1("7", "Facts to have in your pocket")
    b.para("The twelve true-or-false statements, in running order, with the answer and the fact to land. Sources: the Book of Constitutions as set out in the "
           "PGL Hertfordshire Secretaries’ Handbook (2026) and Lodge Director of Ceremonies Guide (2025); the UGLE Members’ Pathway papers; Solomon. "
           "Nothing here is from memory; if challenged, the Handbook page is the answer.", after=6)
    b.table([
        ["Seg", "Statement", "Answer, and the fact to land"],
        ["1", "The Secretary accepts a resignation on the Lodge’s behalf.", "**False.** He has no power to; he acknowledges receipt only. The man then has sixty days to withdraw it; in a Hermes Province the sixty days run from the day his email arrives. Lengthened from 21 days in 2015 so that someone had time to have the conversation. Spoken at the Risings, a resignation is irrevocable unless the Lodge votes on the spot to invite withdrawal: ask for a proposer and seconder immediately. *(Rule 183; Pathway, Resignation: the opportunity to reconsider)*"],
        ["1", "The Immediate Past Master is an officer of the Lodge.", "**False.** The Handbook’s precedence list says so in terms. The year after the Chair comes with a seat and no role, unless the Lodge gives him one. *(Secretaries’ Handbook, Precedence)*"],
        ["2", "A Lodge must leave at least four weeks between a candidate’s degrees.", "**True,** and it is a minimum, not a target. The PGM encourages double ceremonies so no Initiate is kept waiting; a Degree by Request lets another Lodge pass or raise your candidate on a written request from Master and Secretary. *(Rules 172, 173; Handbook, Conferring the Degrees)*"],
        ["2", "The Secretary may hold a Grand Lodge Certificate back until the Brother next attends.", "**False.** Presented as soon as it arrives, or sent recorded delivery and minuted. A passport, kept with his regalia, not framed. The presentation is a moment the Master can design. *(Handbook; MetGL Mentors’ Handbook)*"],
        ["3", "A Warden invested a meeting late can still be elected Master the following year.", "**False** without a dispensation. A Warden must serve a full year, Installation to Installation. *(Rules 105a, 109)*"],
        ["3", "A Master may serve two years running in the same Lodge.", "**True.** Proclaimed, not installed again; the Address to the Master not given; no Past Master’s jewel until he installs his successor; not Master of two Lodges at once without dispensation. *(Rules 107, 115; Handbook, Master continuing in office)*"],
        ["4", "A member two full years in arrears ceases to be a member automatically.", "**True,** announced in open Lodge and minuted. The Treasurer saw the first missed subscription eighteen months earlier: a quiet word then, not a letter. *(Rule 148)*"],
        ["4", "Hertfordshire fire has the Provincial Grand Master’s blessing.", "**True,** as a Provincial tradition, with the written caveat that its speed should not “reach the level of absurdity and thus become undignified”. Show the new man before his first Festive Board. *(DC Guide, Toasts)*"],
        ["5", "Five Brethren are enough to open a Lodge.", "**True:** five, not counting Tyler and candidate; two members; one Installed Master. No Installed Master: abandoned and minuted. Master Elect absent from his Installation: postponed, held within five weeks. *(Rule 119; Handbook, Unavoidable absence)*"],
        ["5", "The Deputy and Assistant Provincial Grand Masters attend as the PGM’s representative.", "**False.** They represent themselves by their Patents; anyone wearing a chain represents themselves: offer the gavel. Salutations completed before the Official Visitor enters; first wine-taking at an Installation is with him. *(Handbook, Official Visits; DC Guide)*"],
        ["6", "A Brother who has resigned from every Lodge can never visit again.", "**False.** Any Lodge once; one Lodge three times in twelve months with a view to joining, if the Master confirms that purpose in writing to the Secretary. *(Rule 127, since September 2020)*"],
        ["6", "Hermes tells the Almoner automatically after two consecutive misses.", "**True.** The call within seven days is still the Lodge’s to make; wait for the notification and a month is already lost. *(Pathway, Tracking attendance and apologies)*"],
    ], [750, 2900, 5762], header=True)
    b.h2("Ten more, for questions from the floor")
    b.table([
        ["Dispensations", "Via Hermes, three weeks to three months ahead, before the summons is printed; £12 at present; not granted automatically. Emergency meeting: dispensation read first, only its business transacted, previous minutes not confirmed, no Risings. *(Handbook, Dispensations)*"],
        ["The Installation speech", "About three minutes: thank the electors and the organisers, do not repeat what others have said. Get the toast list early and practise the names and titles. *(Solomon, Preparing for the Chair)*"],
        ["The Master’s Song", "The Handbook warns that a Master may be “overcome” after it and forget to thank the proposer of his toast; Preceptors are asked to brief him. The Master alone handles the gavel at dinner. *(Handbook, Official Visits; DC Guide)*"],
        ["The social year", "“You can have a very successful social year without having to remortgage your house.” No rule on guest numbers; nobody excluded. Committee meetings about thirty minutes. *(Solomon, Preparing for the Chair)*"],
        ["White Table", "Never at an Installation or Initiation; toasts without fire; anything on a Masonic subject is said in the meeting, not in the reply at dinner; the charity collection taken in the meeting. *(Handbook, White Table procedure)*"],
        ["The register", "The Secretary must record the reason for every cessation of membership: the Lodge already holds its own exit data. Resist “he wasn’t really right for us”. *(Rule 146; Pathway, Lessons learned from losses)*"],
        ["Inclusion", "Kneeling is not obligatory; Jewish Brethren stand covered; the candidate is consulted on the Volume and the manner of his Obligation. *(DC Guide, Preparing the Lodge)*"],
        ["The youngest Brother", "Let him help the DC lay out the Lodge so he learns what will happen. The simplest moment to design for a man with no job yet. *(DC Guide, Inclusion and Involvement)*"],
        ["1813", "At the Union, Pure Antient Masonry was declared to consist of three degrees including the Supreme Order of the Holy Royal Arch. Information, never recruitment. *(UGLE; In That Order, chapter 10)*"],
        ["What we do not claim", "There is no published national figure for the share of resignations that fall in the first years or after the Chair. The two windows rest on Provincial experience and the Pathway papers. Say so if asked; do not put a percentage on it."],
    ], [2200, 7212])
    b.closing("The Chair and Beyond action sheet and pocket card · Lodge Mentor’s Short Guide · Stage Checklists · Warning Signs card · Personal Mentoring Plan stages 6 and 7")
    print("saved", b.save())


def action_sheet():
    out = os.path.join(out_dir, "E6a The Chair and Beyond Action Sheet Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="The Chair and Beyond · Action Sheet")
    b.para("Training and development · E6a", style="DocumentType")
    tp = b.para("The Chair and Beyond: my action sheet", style="Title", after=4)
    for r in tp.runs: r.font.size = Pt(26)
    b.para("Name: ______________________    Lodge: ______________________    Office now: ☐ JW  ☐ SW  ☐ Master Elect  ☐ WM    Date: __________", size=10.5, color=DARK, after=8)

    b.h2("1  The newest man in my Lodge")
    b.table([["His name", ""], ["His Personal Mentor", ""], ["His next ceremony, and when", ""], ["One moment in my year I will design for him rather than leave to chance", ""]], [3600, 5812], row_height=520)

    b.h2("2  The office queue, next three years")
    b.table([["Office", "This year", "Next year", "Year after"], ["Senior Warden", "", "", ""], ["Junior Warden", "", "", ""], ["Senior Deacon", "", "", ""], ["Junior Deacon", "", "", ""], ["Inner Guard", "", "", ""], ["Steward(s)", "", "", ""]], [2200, 2404, 2404, 2404], header=True, row_height=420)
    b.table([["At risk of being pushed before he is ready", ""], ["Capable, and left waiting", ""], ["What I will say to the DC", ""]], [3600, 5812], row_height=520)

    b.h2("3  After the Chair")
    b.para("Agreed before Installation, not after. A seat is not a purpose.", size=10.5, color=DARK, after=4)
    b.table([["My role in the Lodge after the Chair", ""], ["A project I will take on", ""], ["A Brother I will mentor", ""], ["Something beyond the Lodge: Province, Royal Arch, visiting", ""]], [3600, 5812], row_height=520)

    b.h2("4  The one thing I will change")
    b.panel(["**In my year, or in my two years as a Warden:**", "", "**By when:**  ____________________        **Who else needs to know:**  ______________________________"], fill=PALETEAL, bar=TEAL)
    b.para("Keep this sheet. Your Lodge Mentor will be told what you committed to, and your Assistant Provincial Grand Mentor will ask you about it within the month.", size=10.5, italic=True, color=DARK, after=4)
    b.para("Prepare • Guide • Support • Enlighten  ·  Family, Work, Masonry: in that order, always. For the Master too.", bold=True, size=10.5, color=TEAL, after=0)
    print("saved", b.save())


facilitator()
action_sheet()
