"""E1a Lodge Mentor Essentials — one-hour course: facilitator guide and action plan handout.
Usage: build_lm_course.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, TEAL, PALE, PALETEAL, DARK
from docx.shared import Pt

template, out_dir = sys.argv[1], sys.argv[2]

CHARGE = [
    "Brother, the office you have accepted is unlike any other in the Lodge. The Treasurer keeps the accounts and the Secretary keeps the record; you keep something less visible and more easily lost: the experience of every member, from the man who has not yet been Initiated to the Past Master wondering what his Freemasonry is now for.",
    "Your duty is not to mentor every member yourself. It is to make sure that every member is mentored: that each new Brother has a Personal Mentor chosen with care; that those mentors are supported, encouraged and thanked; that no one’s absence goes unnoticed and no one’s question goes unasked; and that the Brethren of your Lodge come to understand that mentoring is not an office but a culture. We are all mentors to others in Freemasonry.",
    "Four words describe the work: Prepare, Guide, Support, Enlighten. Prepare every member for what lies ahead of him, so that there are never any surprises. Guide him with accurate and honest information, so that he navigates an unfamiliar world with confidence. Support him through whatever life and the Lodge may bring, asking always “How can we help?” and never “Why weren’t you there?” And enlighten him, patiently, at his pace, following his curiosity and not your own, so that Freemasonry becomes to him not information learned but a life enjoyed and understood.",
    "Remember the order of things: his family first, his work second, his Masonry third. Hold that line for him even when the Lodge’s programme tempts otherwise, and you will keep men the calendar would have lost.",
    "You do not hold this office alone. Behind you stand the mentors of every Lodge in this Province, the Provincial Mentoring Team, and guidance for every stage of the road. Ask for help early and often; in Hertfordshire, asking is a strength.",
    "And from your first day, look for the Brother who will one day succeed you, for the measure of your work is not what mentoring looks like in your Lodge during your tenure, but what it looks like after it.",
    "May the work be patient and purposeful, and may Freemasonry flourish, root and branch.",
]


def facilitator():
    out = os.path.join(out_dir, "E1a Lodge Mentor Essentials Facilitator Guide Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="Lodge Mentor Essentials · Facilitator Guide")
    b.opening("Training and development · E1a", "Lodge Mentor Essentials",
              "The facilitator’s guide for a one-hour course for Lodge Mentors, delivered in person by the Deputy Provincial Grand Mentor. "
              "The compact companion to the two-hour Lodge Mentor Induction (E1): what the role is, what to put in place, and what to do when it gets difficult.",
              [("Audience", "Facilitator (W Bro Wes Pierce, Deputy Provincial Grand Mentor); APGMen delivering it locally"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · Builds on the Lodge Mentor Induction (E1) and the Lodge Mentor’s Guide Issue 2")])

    b.h1("1", "What the course does")
    b.para("An hour is enough to change what a Lodge Mentor does on Monday, if the hour is spent on the five things that matter and nothing else. "
           "This course is for Lodge Mentors who have been in post a while as much as for the newly appointed; the induction gives the full tour, "
           "this gives the essentials and an action plan. It can be run at a Masonic centre for an APGM area, or at a Lodge Committee.", after=6)
    b.h2("By the end, every participant can")
    b.bullets([
        "Say in one sentence what the Lodge Mentor does: he makes sure mentoring happens; he does not do it all himself.",
        "Name every member of his Lodge who could be a Personal Mentor, and the six things to put in place in his first month.",
        "Quote the four principles and name the two risk windows.",
        "Say who acts, in what order, under the four steps, and where the Almoner, Secretary and Treasurer connect.",
        "Leave with one action for his Lodge, written down, with a date.",
    ])
    b.h2("Format")
    b.table([
        ["Length", "Sixty minutes; arrive from 7.00, start 7.15, finish 8.15. Tables of four to six."],
        ["Materials", "Lodge Mentor’s Short Guide (B1a) and the Action Plan sheet, one per participant. One library set per table."],
        ["Group size", "Six to twenty."],
        ["Follow-up", "Action plans photographed and kept; APGMen contacts each participant within a month."],
    ], [1900, 7512])

    b.h1("2", "Run-sheet: sixty minutes")
    b.table([
        ["Time", "Segment", "What you do"],
        ["0.00", "Why mentoring (7 min)", "One true story of a man lost because nobody noticed: your own, or the composite in the Personal Mentor course. Then the Hertfordshire answer in one line: Freemasonry must be fun; a man who enjoys himself attends, participates, belongs, and does not resign. Retention is the outcome of culture, never a target."],
        ["0.07", "The role: organiser, not everything (10 min)", "The Lodge Mentor makes sure mentoring happens; he does not do it all himself. Walk the IS / IS NOT slide. Tenure three to five years; develop your successor from day one. Choosing Personal Mentors: time, temperament, friendship potential, never seniority; the Proposer considered first, never defaulted to."],
        ["0.17", "Exercise: who could mentor? (5 min)", "Each participant lists every member of his Lodge who could be a Personal Mentor (Action Plan sheet, box 1). Three minutes writing, two minutes of numbers round the room. The list is always longer than they expect."],
        ["0.22", "The principles and the two windows (8 min)", "Read the four principles from the canon page; not stages. The journey in one line, and the two recognised drop-out windows: the first two years, and the year after the Chair. Spring Initiates and the summer break."],
        ["0.30", "Your first month (8 min)", "Six things to put in place: induction and Jewel; the list from the Secretary; a Personal Mentor and Plan for every man on it; ten minutes each with the Secretary, Almoner and Master; the monthly call; your APGMen at the next Initiation. Short Guide section 2."],
        ["0.38", "When it gets difficult (10 min)", "The pattern is the signal, not the attendance level. The four steps and the two-misses, seven-days habit. The hand-offs: Almoner for welfare, Secretary acknowledges only, Treasurer’s arrears as an early signal, Royal Arch Representative for One Journey. Pressure in both directions: the man pushed early and the man left waiting. Escalation is a strength."],
        ["0.48", "The Province behind you (5 min)", "Your APGMen; the monthly call, first Tuesday 7pm Teams; DAWG; induction and the Personal Mentor course for your team; the library and where it lives; one-to-one help in confidence."],
        ["0.53", "Action plan and the Charge (7 min)", "Box 2 of the Action Plan: one thing my Lodge does well, one thing it does not do at all, and the one action I will take by a date. Round the room, one sentence each. Close by reading the Charge aloud, slowly. Thank them."],
    ], [1000, 2700, 5712], header=True)

    b.h1("3", "Teaching points, in the facilitator’s words")
    b.panel(["**The role in one sentence.** The Lodge Mentor is an organiser and co-ordinator. He ensures mentoring happens; he does not need to do it all himself. Sharing the work across suitable, experienced Brethren makes it sustainable and more effective."], fill=PALE, bar=DEEP)
    b.h2("Choosing a Personal Mentor")
    b.para("Time, temperament and the potential for friendship, not seniority. Someone who knows the Lodge, listens patiently, will keep in touch between "
           "meetings, and can say “I don’t know, but I’ll find out”. The Proposer is often right because trust already exists, but not always. Past Masters "
           "make excellent Personal Mentors and often need the purpose. The exercise proves the point: every Lodge has more candidates than it thinks.", after=6)
    b.h2("The two windows")
    b.para("National evidence puts most losses within two years of Initiation, often before Raising, and a second cluster in the year after the Chair. "
           "Spring Initiates are at extra risk because the summer break interrupts their early participation. Plan deliberate summer contact for them.", after=6)
    b.h2("Pressure in both directions")
    b.para("The member pushed too hard: office before he is ready, ritual beyond his ability, the Royal Arch before the time is right. The member left "
           "under-stretched: a capable Brother waiting years for a first office, a Past Master with nothing to do, a joining member whose experience "
           "nobody thought to use. A Brother who is bored will leave as surely as one who is frightened. Raise the office queue with the Master and the DC.", after=6)
    b.h2("Escalation is a strength")
    b.para("Contact your APGMen or the Provincial Grand Mentor’s office when a member is at significant risk, when welfare needs Provincial involvement, "
           "when a Lodge is seeing several resignations, when a member is relocating, or when you simply want a second opinion. The Province exists to "
           "support Lodges, not to judge them. All contact is in confidence.", after=6)

    b.h1("4", "The Charge to the newly appointed Lodge Mentor")
    b.para("Read aloud to close the course. Presented in writing to every new Lodge Mentor on appointment; it complements, and never replaces, the presentation of the Mentor’s Jewel in open Lodge.", italic=True, color=DARK, after=6)
    b.panel(CHARGE + ["*Presented on behalf of the Provincial Grand Mentor, Province of Hertfordshire.*"], fill=PALE, bar=TEAL)

    b.h1("5", "Materials and follow-up")
    b.table([
        ["Materials", ["Lodge Mentor’s Short Guide, one per participant", "Action Plan sheet, one per participant", "Library set per table: Personal Mentor’s Short Guide, Mentor Meeting Guide, Stage Checklists, Warning Signs card, the Principles page", "The Charge, printed, for anyone who has not received it", "Slides on a screen; the course runs without them"]],
        ["Follow-up", ["Action plans photographed and kept; each APGMen follows up his area within a month", "Attendance recorded on the Provincial register; every participant on the monthly call and DAWG", "Participants encouraged to send their Personal Mentors to the Personal Mentor course", "Feedback on one question: what will you do differently?"]],
    ], [1600, 7812])
    b.closing("Lodge Mentor’s Short Guide · Lodge Mentor Induction (E1) · Lodge Mentor’s Guide Issue 2 · Personal Mentor Course · Warning Signs card")
    print("saved", b.save())


def action_plan():
    out = os.path.join(out_dir, "E1a Lodge Mentor Essentials Action Plan Issue 1 Draft.docx")
    b = Builder(template, out, doc_title="Lodge Mentor Essentials · Action Plan")
    b.para("Training and development · E1a", style="DocumentType")
    tp = b.para("Lodge Mentor Essentials: my action plan", style="Title", after=4)
    for r in tp.runs: r.font.size = Pt(26)
    b.para("Name: ____________________________      Lodge: ____________________________      Date: ______________", size=11, color=DARK, after=8)

    b.h2("1  Who in my Lodge could be a Personal Mentor?")
    b.para("Time, temperament and friendship potential, not seniority. Past Masters included. List everyone; the list is always longer than you expect.", size=10.5, color=DARK, after=4)
    t = b.doc.add_table(rows=4, cols=3)
    b._widths(t, [3137, 3137, 3138])
    b._borders(t, {"insideH": ("single", 4, "9FB3C8"), "insideV": ("single", 4, "9FB3C8"), "bottom": ("single", 4, "9FB3C8"), "top": ("single", 4, "9FB3C8")})
    b._margins(t, 110, 110, 100, 100)
    for r in t.rows:
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn
        trPr = r._tr.get_or_add_trPr(); h = OxmlElement("w:trHeight"); h.set(qn("w:val"), "440"); h.set(qn("w:hRule"), "atLeast"); trPr.append(h)
    b.spacer()

    b.h2("2  Against the four principles")
    b.table([["", "One thing my Lodge already does well", "One thing it does not do at all"],
             ["Prepare", "", ""], ["Guide", "", ""], ["Support", "", ""], ["Enlighten", "", ""]], [1500, 3956, 3956], header=True, row_height=620)

    b.h2("3  My first month, or my next month")
    b.table([["Done?", "Action"],
             ["☐", "Induction received, with the Charge and the Mentor’s Jewel"],
             ["☐", "The list from the Secretary: candidates, members in their first two years, joining members in their first year"],
             ["☐", "Every man on the list has a Personal Mentor and a Personal Mentoring Plan"],
             ["☐", "Ten minutes each with the Secretary, the Almoner and the Worshipful Master; attendance record and same-day resignation notice agreed"],
             ["☐", "On the monthly mentoring call: first Tuesday, 7pm, Teams"],
             ["☐", "My Assistant Provincial Grand Mentor invited to the next Initiation"]], [900, 8512], header=True)

    b.h2("4  The one action I will take")
    b.panel(["**What:**", "", "**By when:**  ____________________        **Who else needs to know:**  ______________________________"], fill=PALETEAL, bar=TEAL)
    b.para("Keep this sheet. Your Assistant Provincial Grand Mentor will ask you about it within the month.", size=10.5, italic=True, color=DARK, after=4)
    b.para("Prepare • Guide • Support • Enlighten  ·  Family, Work, Masonry: in that order, always.", bold=True, size=10.5, color=TEAL, after=0)
    print("saved", b.save())


facilitator()
action_plan()
