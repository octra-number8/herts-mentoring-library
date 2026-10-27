"""C1a Proposer and Seconder's Guide; C1b For Partners and Families. Member-facing, Hertfordshire voice.
Usage: build_c1_guides.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL

template, out_dir = sys.argv[1], sys.argv[2]


class B(Builder):
    def table(self, rows, widths, **kw):
        t = super().table(rows, widths, **kw)
        if len(rows) <= 6:
            for r in t.rows[:-1]:
                for c in r.cells:
                    for pp in c.paragraphs: pp.paragraph_format.keep_with_next = True
        return t


def proposer():
    b = B(template, os.path.join(out_dir, "C1a Proposer and Seconders Guide Issue 1 Draft.docx"), doc_title="Proposer and Seconder’s Guide")
    b.opening("Member guides · C1a", "Proposer and Seconder’s Guide",
              "You are the first mentor a candidate ever has. He will judge Freemasonry by you for his first two years. A short guide to what that asks of you, from the first conversation to long after his Initiation.",
              [("For", "Any Brother who proposes or seconds a candidate, and the Lodge Mentor who supports him"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · Companion to Considering Freemasonry (C1) and the Personal Mentor’s Short Guide")])

    b.para("Nobody joins Freemasonry because of a leaflet. They join because of a man they know and like, who answered their questions honestly and did not oversell it. "
           "That man is you, and the job does not end at the ballot. The Province’s experience, and UGLE’s, is that the candidates who stay are the ones whose Proposer stayed close.", after=6)
    b.panel(["**Two rules run through everything in this guide.** There should never be any surprises: he should know what Freemasonry will ask of him before he applies, not after. And Family, Work, Masonry, in that order, always: a candidate whose family is not on side is a candidate at risk from the start."], fill=PALE, bar=DEEP)

    b.h1("1", "Before you propose anyone")
    b.bullets([
        "**Know him.** The Lodge is taking your word for his character. Ask yourself whether you would be comfortable sitting next to him for twenty years, and whether the Lodge would.",
        "**Make sure he asked.** The best candidates come to Freemasonry out of their own curiosity. A man who was talked into it, or who thinks it will help his business, will not stay, and should not be proposed.",
        "**Tell him what it is, and what it is not.** A society of friends who meet, dine, support each other and give to charity. No secrets worth the name, nothing he could not tell his family or his employer, no advantage to be had, and no obligation that comes before his home or his work.",
        "**Tell him what it costs, in money and time.** The joining fee, the annual subscription, dining, regalia; the number of meetings a year and the Lodge of Instruction; and that office, if he wants it one day, takes more. Say the numbers. A candidate surprised by a bill is a candidate half-way out of the door.",
        "**Involve his partner or family.** Invite them to a social evening before he applies. A partner who has met the Lodge and understands the commitment is his strongest ally; one who learns about it from the bank statement is not.",
        "**Give him the Province’s guide, Considering Freemasonry,** and point him at the UGLE website. Let him read and come back with questions.",
        "**Is this the right Lodge for him?** Age, meeting day, distance, the character of the Lodge. A man unhappy in one Lodge is often happy in another. If a neighbouring Lodge would suit him better, say so; the Province would rather keep him in the Craft than in your Lodge.",
    ])

    b.h1("2", "The application and the interview")
    b.bullets([
        "Speak to the Secretary first. He will tell you how your Lodge handles applications, what the candidate needs to provide, and what will appear on the summons. Your name and the Seconder’s go on it: you are vouching for him in front of the whole Lodge.",
        "Tell the Lodge Mentor at the same time. Mentoring begins before the ballot, and he will want to think about who the candidate’s Personal Mentor should be.",
        "Prepare the candidate for the interview: who will be there, what they will ask, and that he should ask questions too. It is a two-way conversation; he is deciding about the Lodge as much as the Lodge about him.",
        "If your Lodge’s custom allows the Proposer at the interview, go, and then let him answer. If it does not, make sure he knows someone in the room.",
        "After the ballot, tell him the date and keep in touch. The weeks between election and Initiation are long for a candidate who hears nothing.",
    ])

    b.h1("3", "His Initiation")
    b.para("The Lodge Mentor will have assigned a Personal Mentor by now. It may be you; it may not. The Proposer is often the right choice because trust already exists, but not always, and the "
           "Lodge Mentor chooses for time, temperament and friendship, not for who proposed him. Whoever is appointed, you are still his friend in the room, and on the night that means:", after=3)
    b.bullets([
        "Meet him at the door. He should never stand alone in the anteroom.",
        "Introduce him to the Tyler and the Junior Deacon, and to the Master and the DC if you can.",
        "Make sure he knows the practical things: comfortable trousers, reading glasses in his pocket if he needs them, cash for the alms collection and the raffle.",
        "At the Festive Board, sit with him or make sure a briefed Brother does. Explain the toasts and the fire before the meal; steady him before his reply, which he should have seen in draft days earlier.",
        "Walk out with him. Say what the next date is and when you will next speak.",
    ])
    b.panel(["**Good practice.** Ring him the next day. “What did you make of it?” Then listen. Most of what he says will be about the people, not the ceremony. That is the point."], fill=PALETEAL, bar=TEAL)

    b.h1("4", "The two years after")
    b.para("The first two years are the recognised risk window. His Personal Mentor carries the one-to-one work and the Lodge Mentor keeps the overview, but a Proposer who steps back once the "
           "ballot is won has misunderstood the job. What you can do that nobody else can:", after=3)
    b.bullets([
        "**His second meeting.** Mostly business, and nobody has told him. Sit with him, decode the summons, explain what is happening as it happens.",
        "**The nights he cannot attend.** When the Lodge works a higher degree, he goes home. Take him for a drink that evening instead, or arrange for someone who will.",
        "**The summer.** If he was initiated in the spring, the break will swallow his first months unless somebody rings. Be that somebody.",
        "**His Passing and Raising.** Be there, whatever else is in the diary. He will look for you.",
        "**His first visit.** Take him to another Lodge. Visiting is where Freemasonry opens up, and the first time is daunting alone.",
        "**His partner.** Keep the invitation open: White Table, Ladies Night, the social calendar. The family who feels included keeps the member.",
        "**When something changes.** Two missed meetings, a quieter man at dinner, talk of money or time. Tell the Personal Mentor and the Lodge Mentor that week; do not wait to be sure.",
    ])
    b.panel(["**If he ever resigns, you will be the first person the Lodge asks why.** The Secretary cannot accept a resignation, only acknowledge it; the member then has sixty days to withdraw it; and the best-placed person for the conversation in that window is very often the man who brought him in. Keep the friendship warm enough that the conversation is possible."], fill=PALE, bar=DEEP)

    b.h1("5", "The Seconder")
    b.para("Everything above applies to the Seconder, with less of the paperwork and no less of the friendship. In practice the Seconder is the candidate’s second friend in the Lodge: the one who "
           "sits on his other side at the Festive Board, who takes him visiting when the Proposer cannot, and who notices the things the Proposer is too close to see. If you are asked to second a "
           "man you do not know well, meet him properly before you agree. Your name on the summons means the same as the Proposer’s.", after=6)

    b.h1("6", "Checklist")
    b.table([
        ["Before proposing", ["Known him long enough to vouch for him", "He asked; nobody sold it to him", "Costs, time and commitment stated plainly, in numbers", "Partner or family met the Lodge socially", "Considering Freemasonry handed over", "Right Lodge for him, honestly considered"]],
        ["Application", ["Secretary and Lodge Mentor told", "Interview explained; he has questions of his own", "Contact kept up between ballot and Initiation"]],
        ["Initiation night", ["Met at the door; Tyler and Junior Deacon introduced", "Practicalities covered; draft reply seen in advance", "Never dines alone; walked out with", "Rung the next day"]],
        ["Two years after", ["Second meeting designed, not left to chance", "Nights he cannot attend covered", "Summer contact if a spring Initiate", "Present at his Passing and Raising", "First visit taken together", "Family kept in the invitation", "Changes reported to his mentors that week"]],
    ], [2400, 7012])
    b.closing("Considering Freemasonry (C1) · Personal Mentor’s Short Guide · Stage Checklists · Warning Signs card · Solomon: The Responsibilities of a Proposer")
    print("saved", b.save())


def partners():
    b = B(template, os.path.join(out_dir, "C1b For Partners and Families Issue 1 Draft.docx"), doc_title="For Partners and Families")
    b.opening("Member guides · C1b", "For Partners and Families",
              "Someone close to you has joined, or is thinking of joining, a Lodge in Hertfordshire. This is what it will mean for you: what he will do, what it costs, what you are welcome at, and who to speak to if you are ever concerned.",
              [("For", "Partners, families and close friends of candidates and new members"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · Given with Considering Freemasonry (C1), before the application where possible")])

    b.para("Freemasonry in Hertfordshire has a rule that we say out loud: Family, Work, Masonry, in that order, always. A Lodge that asks a member to put it ahead of his home has got it wrong, "
           "and we would want to know. This guide is written so that you know what is being asked of him, and of you, before it starts rather than after.", after=6)

    b.h1("1", "What he has joined")
    b.para("A Lodge is a group of men who meet a few times a year, usually in the evening, for a formal meeting followed by a dinner. The meetings have ceremonies that are centuries old and "
           "make up a kind of moral play: the three degrees he will go through in his first year or two are about honesty, learning and how to live a good life. They are entirely symbolic, safe and "
           "dignified. Between meetings there are rehearsals, social evenings, visits to other Lodges, and a great deal of fundraising for charity. Freemasons are not a religion, not a political "
           "organisation, and not a route to business advantage; a man who joins expecting any of those will be disappointed.", after=6)
    b.h2("The secrets question")
    b.para("He can tell you almost everything. What Freemasons keep to themselves are the traditional ways they recognise one another and some of the words of the ceremonies, in the same way a "
           "surprise is kept for someone who has not yet had it. He cannot tell you those. He can tell you who was there, what was said at dinner, what he is learning, what it means to him, and "
           "anything that worries him. If he ever uses secrecy as a reason not to tell you where he was, that is him, not Freemasonry.", after=6)

    b.h1("2", "What it will ask of your household")
    b.table([
        ["Time", "Most Lodges meet four to eight times a year, on a fixed weekday evening. He will be out from late afternoon to late evening. Add a rehearsal evening most weeks in the season, called the Lodge of Instruction, and the occasional visit to another Lodge. If he later takes an office, the rehearsals matter more and the learning takes time at home."],
        ["Money", "A joining fee, an annual subscription, a dinner each meeting, and some regalia to buy. The Lodge will tell him the figures before he applies; if it has not, ask him to ask. There is a yearly charity collection too, always voluntary and private. Nobody should ever feel they cannot afford to stay, and the Lodge’s Almoner is there precisely for the hard year."],
        ["Learning", "In his first year he will learn a few short answers by heart for each ceremony, and may want to practise them aloud at home. He must not practise where you can hear the words; that is the one bit of Freemasonry you will have to let him keep. Everything else about it he can share."],
        ["The late nights", "The dinner, with its toasts and speeches, can run late. Lodges vary. He will know the pattern after two meetings; ask him to tell you."],
    ], [1700, 7712])

    b.h1("3", "What you are welcome at")
    b.bullets([
        "**White Table evenings:** a dinner after a meeting to which partners and guests are invited. Many Lodges hold one or two a year.",
        "**Ladies Night (or the Master’s dinner):** the Master’s formal dinner each year, often the social highlight of the Lodge.",
        "**Social events:** quiz nights, walks, outings, the Christmas social; whatever your Lodge does. Partners are usually the point of them.",
        "**Provincial events:** carol services, family days, the Provincial church service, charity events across the county.",
        "**The Fleet House Light Blues Club:** the Province’s club for newer members, with social events partners are often invited to (fhlbc.co.uk).",
    ])
    b.para("If you have never been invited to any of these, something has gone wrong, and the Lodge would want to know. Ask him to ask his mentor.", after=6)

    b.h1("4", "What he gets from it, and what you might")
    b.para("Friends he would not otherwise have met, of every age and background; something to learn that is not work; a reason to stand up and speak in front of people; and a place where he is "
           "expected to be kind. Partners often say the same three things: that he comes home in a better mood than he left, that the friends became theirs too, and that it took a year to "
           "understand why he liked it. Give it the year.", after=6)

    b.h1("5", "If you are ever concerned")
    b.para("Every Lodge has two people whose job includes you.", after=3)
    b.table([
        ["The Almoner", "Looks after the welfare of members and their families: illness, bereavement, money, a hard time of any kind. He is discreet, he is used to being asked, and you may contact him directly. Ask your partner for his name, or the Lodge Secretary."],
        ["His mentor", "Every new member in Hertfordshire has a Personal Mentor, a friend in the Lodge whose job is to help him settle in and enjoy it. If you feel the Lodge is asking too much, or he seems to be enjoying it less, the mentor is the person to tell, and he will want to hear it."],
        ["The Province", "The Provincial Mentoring Team is there for members and their families: mentor@hertfordshirefreemasons.org.uk. Anything you raise is in confidence."],
    ], [1700, 7712])
    b.panel(["**Family, Work, Masonry: in that order, always.** If his Lodge ever seems to have forgotten it, say so, to him first and then to his mentor. We mean it."], fill=PALE, bar=DEEP)
    b.closing("Considering Freemasonry (C1) · The New Brother’s Guide (C2) · fhlbc.co.uk · ugle.org.uk")
    print("saved", b.save())


proposer()
partners()
