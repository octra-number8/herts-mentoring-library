"""B1a Lodge Mentor's Short Guide — built on the Hertfordshire Mentoring template.
Usage: build_lm_guide.py <template.docx> <out.docx>"""
import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from hmdocx import Builder, DEEP, TEAL, PALE, PALETEAL

template, out = sys.argv[1], sys.argv[2]
b = Builder(template, out, doc_title="Lodge Mentor’s Short Guide")

b.opening(
    "Practitioner guide · B1a",
    "Lodge Mentor’s Short Guide",
    "For the Brother who has just been appointed Lodge Mentor: what the role is, what to put in place, and what to "
    "check through the year. The full detail is in the Lodge Mentor’s Guide.",
    [
        ("Audience", "Lodge Mentors, newly appointed or returning. Useful to Worshipful Masters when appointing one."),
        ("Issue", "Issue 1 (Draft for Review), October 2026 · Deputy Provincial Grand Mentor, on behalf of the Provincial Grand Mentor"),
    ],
)

# 1
b.h1("1", "What the role is")
b.para("You are the co-ordinator, not the mentor to every member. Your job is to make sure mentoring happens and happens well: "
       "every new and joining member has a friend assigned to him, nobody drifts unnoticed, and the Lodge treats mentoring as its "
       "culture rather than your office.", after=6)
b.table([
    ["Your role is", "Your role is not"],
    [[
        "Assigning a Personal Mentor to every new and joining member, promptly",
        "Supporting your Personal Mentors and equipping them",
        "Opening and reviewing a Personal Mentoring Plan for each member",
        "Watching for patterns across the Lodge and acting early",
        "The Lodge’s link to the Province; the man who briefs the Lodge once a year",
    ], [
        "Personal Mentor to everyone. Share the work",
        "The ritual coach. That is the Lodge of Instruction and the DC",
        "The Almoner. Welfare is his; you refer to him",
        "An inspector or a report-writer on members",
        "A one-year office. Three to five years is the recommendation",
    ]],
], [4706, 4706], header=True)
b.para("**The four principles.** Mentoring in Hertfordshire rests on four principles, defined once in "
       "*The Hertfordshire Mentoring Principles*. They run together, all the time. They are not stages.", after=6, keep=True)
b.principles_strip()

# 2
b.h1("2", "Your first month")
b.para("Six things to put in place before anything else. Most take an hour.", after=4, keep=True)
b.bullets([
    "**Ask for your induction** from the Provincial Grand Mentor’s office if you have not had it. It comes with the Lodge Mentor’s Charge and the Mentor’s Jewel.",
    "**Get the list.** From the Secretary: every candidate in the pipeline, every member initiated, passed or raised in the last two years, every joining member in his first year. These are the men under mentoring.",
    "**Check each one has a Personal Mentor and a Plan.** Where there is a gap, fill it this month, not next.",
    "**Meet the Secretary, the Almoner and the Worshipful Master** for ten minutes each. Agree the attendance record after every meeting, same-day notice of any resignation, and a place for your report on the Lodge Committee agenda.",
    "**Join the monthly mentoring call:** first Tuesday of the month, 7pm, on Teams. Open to you and to every Personal Mentor.",
    "**Ask your Assistant Provincial Grand Mentor to visit.** Ideally at the next Initiation. He is there to help, never to inspect.",
])
b.h2("Choosing a Personal Mentor")
b.para("Choose for time, temperament and the potential for friendship, not for seniority: a patient listener who knows the Lodge, "
       "will keep in touch between meetings, and can say “I don’t know, but I’ll find out”. The Proposer is often right because trust "
       "already exists, but not always. Past Masters make excellent Personal Mentors and often need the purpose. Give him the "
       "Personal Mentor’s Short Guide the day you ask him.", after=6)

# 3
b.h1("3", "What you make sure happens")
b.para("The Personal Mentor accompanies the member; you make sure each step is in place. The Stage Checklists give one-page versions for the night itself.", after=6)
b.table([
    ["Before Initiation", [
        "You hear of every new enquiry early; agree this with the Membership Officer and Secretary.",
        "The candidate meets members socially before his interview, and the interview is honest about cost, time and commitment.",
        "After the ballot: Personal Mentor assigned and Plan opened within the week; the evening explained practically, never the ceremony; contact the day before.",
    ]],
    ["Initiation night", [
        "Personal Mentor seated next to him; introduced to the Tyler and Junior Deacon beforehand.",
        "Festive Board explained in advance, a short reply in his hand, and he never dines alone.",
        "Secretary has sent his details so the Provincial Welcome Letter goes out promptly.",
    ]],
    ["Entered Apprentice", [
        "Check-in within two days and a one-to-one before the next meeting have both happened. Ask the Personal Mentor; do not assume.",
        "The evenings he cannot attend are used for companionship and learning, not lost.",
        "Spring Initiates get deliberate summer contact. The summer break is where early losses begin.",
    ]],
    ["After Passing and Raising", [
        "Ceremony reviewed, the right Guide handed over, visiting encouraged and the first visit accompanied.",
        "After Raising, mentoring intensifies rather than fades: the first of two drop-out windows.",
        "The Royal Arch explained as the completion of his journey, on his timing, through the Royal Arch Representative.",
    ]],
    ["Into office and the Chair", [
        "Readiness runs both ways: never pressured early, never left waiting. Raise the office queue with the Worshipful Master and DC.",
        "Master Elect prepared for the year and, from Installation day, for what follows it: the second drop-out window.",
        "Outgoing Master given a next role. Included, Involved, Interested.",
    ]],
    ["Joining members and re-joiners", [
        "A Personal Mentor for the first year as a guide to this Lodge, not a teacher of Freemasonry. Ask what he wants from his membership.",
        "If he has migrated in, confirm his safe arrival to the Provincial Grand Mentor’s office so the sending Lodge can close its loop.",
    ]],
], [2300, 7112])

# 4
b.h1("4", "Watching for patterns")
b.para("Risk shows as a break in a member’s own pattern, not as a low level of attendance. The stalwart who stops coming is the one to "
       "worry about. The Secretary’s attendance record is your early-warning system; the Personal Mentor is the man who will hear the real "
       "reason behind the stated one. The Warning Signs card has the full list.", after=6)
b.table([
    ["Step 1", "Personal Mentor. Friendly, informal contact after any unexpected absence. After two consecutive misses, contact within seven days of the second meeting."],
    ["Step 2", "You. Take the overview, ask what the Lodge itself could change (timing, cost, culture, an office that does not fit), keep a discreet note, close the loop with the member."],
    ["Step 3", "Worshipful Master’s conversation, where it touches Lodge culture, office or another member. The Almoner alongside for anything touching welfare."],
    ["Step 4", "Provincial referral, where an impartial voice helps or the member might thrive in another Lodge. Referral is responsible mentoring, not failure."],
], [1400, 8012])
b.panel(["**A resignation letter starts a conversation; it does not end one.** The Secretary acknowledges only. You, the Almoner and the "
         "Provincial Office are told the same day, and the best-placed person has an unhurried, private conversation whose purpose is "
         "understanding, not persuasion. Where that happens, roughly one resignation in three is recovered."], fill=PALETEAL, bar=TEAL)
b.panel(["**The right question.** Always “How can we help?”, never “Why haven’t you been attending?”."], fill=PALE, bar=DEEP)

# 5
b.h1("5", "Working with the Lodge")
b.para("Several officers hold a piece of mentoring. Your job is to make the pieces connect. A short word with each, regularly, is usually all it takes.", after=6)
b.table([
    ["Worshipful Master", "Sets the tone and owns Step 3. Ask him to hear your report with the same weight as the Treasurer’s, to brief the Lodge on mentoring once a year, and to protect junior Brethren from pressure."],
    ["Almoner", "Welfare: health, money, bereavement, family. Welcome new members jointly. Refer anything touching welfare and note only “referred to Almoner”."],
    ["Secretary", "The candidate timeline and the attendance record. Ask for the record after each meeting, early notice of ballots, and same-day notice of any resignation."],
    ["Director of Ceremonies and Preceptor", "Ceremony preparation and the culture of the Lodge of Instruction. Agree how juniors are drawn into ritual gently and how the office queue is managed fairly."],
    ["Membership Officer", "The pipeline. Agree how early you hear of a new enquiry, and review joiners and leavers together at least once a year."],
    ["Treasurer", "Often first to see disengagement: a subscription in arrears. Agree that a first missed subscription earns a quiet word to you or the Almoner."],
    ["Royal Arch Representative", "One Journey’s bridge. Agree what is said about the Royal Arch, when and by whom, so that information is consistent and interest meets a warm introduction."],
], [2600, 6812])

# 6
b.h1("6", "The Lodge Mentor’s year")
b.table([
    ["Every meeting", "Every candidate and new member has a Personal Mentor and a Plan. Attendance record collected. Pattern-breaks passed to the Personal Mentor within seven days. No new or joining member dines alone."],
    ["Every month", "Monthly mentoring call. A short word with each Personal Mentor: how is he getting on, does he need anything."],
    ["Every quarter", "Update your Assistant Provincial Grand Mentor. Review Plans with Personal Mentors. Check the office queue and the under-stretched with the Worshipful Master and Director of Ceremonies."],
    ["Each ceremony", "Before: Stage Checklist worked through with the Personal Mentor; candidate contacted the day before. After: check-in and first one-to-one confirmed; Welcome Letter sent."],
    ["Installation", "Master Elect prepared for the year and for after it. Outgoing Master’s next role agreed. A Past Master or two confirmed as Personal Mentors."],
    ["Summer", "Deliberate contact and a social touchpoint for every spring Initiate and Entered Apprentice."],
    ["Once a year", "Brief the whole Lodge on mentoring. Review joiners and leavers with the Membership Officer. Review records, destroy what is no longer needed, and brief your likely successor. Take your Personal Mentors to the workshop."],
], [2000, 7412])

# 7
b.h1("7", "Help for you")
b.table([
    ["Your Assistant Provincial Grand Mentor", "Your nearest source of advice, a visitor at Initiations, and the route for your quarterly picture of the Lodge."],
    ["Provincial Grand Mentor’s office", "For a specific situation, a difficult conversation or simply to think aloud, in confidence. Also for your induction and the Personal Mentor workshop dates. mentor@hertfordshirefreemasons.org.uk"],
    ["Monthly mentoring call", "First Tuesday of the month, 7pm, Teams. Questions, shared experience and news from the Provincial team."],
    ["Solomon", "UGLE’s learning platform and the authoritative answer to most questions: solomon.ugle.org.uk"],
], [2600, 6812])
b.para("**Records.** Keep only what mentoring needs: contact details, key dates, milestones, brief notes of support given. The member knows a Plan is kept "
       "and may see it. Welfare belongs in the Almoner’s records, not yours. Keep Plans secure, do not circulate them, pass them to your successor, "
       "and close and destroy a Plan within twelve months of a member resigning, migrating or dying.", after=8)
b.panel(["**Escalation is responsible mentoring, not failure.** The Province exists to support Lodges, not to judge them, and every contact is in confidence.",
         "Family, Work, Masonry: in that order, always. Freemasonry must be fun. A man who is enjoying himself attends; a man who attends participates; "
         "a man who participates belongs; and a man who belongs does not resign. Your job is to make that true for every member of your Lodge."], fill=PALE, bar=TEAL)
b.closing("Lodge Mentor’s Guide (Issue 2, September 2026) · Personal Mentor’s Short Guide · Stage Checklists · Warning Signs card · Retention, Retrieval and Migration Guide")
print("saved", b.save())
