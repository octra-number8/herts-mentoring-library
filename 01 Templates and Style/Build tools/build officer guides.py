"""C6 Officer Guides: six short member-facing guides, one per progressive office, in the Hertfordshire voice.
Usage: build_officer_guides.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL

template, out_dir = sys.argv[1], sys.argv[2]

COMMON_LEARN = [
    "Little and often. Ten minutes a day, out loud, beats an hour on the night before.",
    "Understand it before you memorise it. Words that mean something stay; words that are only sound go under pressure.",
    "Record it and listen in the car. Then record yourself and listen to that.",
    "Go to the Lodge of Instruction. It is where the words and the floorwork come together, and where nobody minds a mistake.",
    "Never practise where anyone who is not a Mason can see or hear you.",
    "Nerves are normal and nobody minds a prompt. What the Lodge remembers is sincerity, not perfection.",
]

OFFICES = [
    dict(ref="C6a", name="Steward", title="Your year as a Steward",
         purpose="Usually the first office a Brother holds, and the one that teaches the Lodge who you are. A short guide to what it involves, what to learn, and who will help.",
         what=("The Stewards look after the comfort of the Lodge and its guests, mostly at the Festive Board: seeing that visitors are welcomed and seated, that glasses are charged before the toasts, "
               "that the raffle and the charity collection happen, and that nobody is left without company. In the Lodge room you will have little or no ritual to deliver; your job is to watch, learn and be useful. "
               "Most Lodges have several Stewards, and most Masters started here."),
         jewel="A cornucopia, the horn of plenty, on a collar. You will be invested with it at the Installation.",
         do=["Arrive early. The Director of Ceremonies and the Junior Warden will tell you what the evening needs; ask if they do not.",
             "Welcome visitors in the bar and at the table. Find out who is dining alone and sit someone with them, or sit there yourself.",
             "Help with the raffle, the alms collection and the wine, as your Lodge’s custom dictates.",
             "Learn the shape of a meeting: the order of business, the Risings, who moves where and why. Sit where you can see the floorwork.",
             "Learn the Festive Board: the order of toasts, Hertfordshire fire, and when to stand.",
             "If you are a Steward at an Installation or an Official Visit, expect a busier night; the DC will brief you."],
         learn=["There is usually nothing to learn by heart as a Steward, and that is the point: the year is for learning the Lodge.",
                "Start on next year’s office now. Ask the Inner Guard to show you what he does, and borrow the words.",
                "Visit another Lodge and watch their Stewards. Lodges do these things differently, and you will pick up good ideas."],
         nobody=["The Stewards’ most useful job is the one on no list: noticing the Brother at the end of the table whom nobody is talking to.",
                 "Reliable attendance as a Steward is the strongest signal a Lodge reads when it plans its office queue.",
                 "You are allowed to enjoy it. The Stewards’ table is often the liveliest in the room."],
         time="One meeting a month in the season, the Lodge of Instruction if you can, and a little time with the DC before an Installation. It should fit comfortably around home and work; if it does not, say so.",
         next_="Inner Guard, usually. Your Lodge Mentor and the DC will talk to you about it before the Master decides, and if you would rather have another year as a Steward, that is a good answer too."),
    dict(ref="C6b", name="Inner Guard", title="Your year as Inner Guard",
         purpose="The first office with a part of the ceremony that is yours. A short guide to what the Inner Guard does, what to learn, and who will help.",
         what=("The Inner Guard sits just inside the door of the Lodge room. His job is to see that only those entitled to be present come in: he answers the Tyler’s knocks, reports to the Lodge, "
               "admits visiting Brethren on the Director of Ceremonies’ word, and receives the candidate at the door in the form the ceremony requires. He works under the direction of the Junior Warden "
               "and alongside the Tyler, and he is the first officer a candidate meets on the night that matters most to him."),
         jewel="Two swords in saltire. Your tools for the ceremonies are kept at the door; the Tyler and the DC will show you which is which.",
         do=["Arrive early and check the door with the Tyler: the knocks you will hear, the tools you will need for the degree being worked, and how your Lodge handles late arrivals.",
             "Learn the reports: short, formal, and the same every meeting. Practise them until they come without thinking.",
             "Learn what happens at the door for each of the three degrees, and the difference between admitting a visitor and receiving a candidate.",
             "Watch the Junior Warden; your cue often comes from him.",
             "On a candidate’s night, remember what the door felt like from his side. A calm Inner Guard steadies a nervous man."],
         learn=["Your pieces are short, which is why this office exists first. Get them word-perfect and then work on delivering them with confidence rather than speed.",
                "Ask the DC or the Preceptor to run the door with you at the Lodge of Instruction before your first meeting in office.",
                "Begin the Junior Deacon’s work during the second half of your year. It is the first office with real learning, and a head start matters."] + COMMON_LEARN[:3],
         nobody=["The Inner Guard is the officer most likely to be caught by a late arrival mid-ceremony. Ask the DC now what your Lodge does, so that you are not improvising.",
                 "Your Personal Mentor should sit as near you as custom allows for your first meeting or two. Ask him.",
                 "Kneeling is not obligatory for candidates and Jewish Brethren stand covered: if you are told of an adjustment, it is not your decision, it is the DC’s and the candidate’s."],
         time="One meeting a month in the season and the Lodge of Instruction most weeks it runs. Perhaps a quarter of an hour a day of learning in the weeks before a ceremony. Family, Work, Masonry: in that order, always.",
         next_="Junior Deacon. It is the first office that takes real learning, so your Lodge Mentor and the DC will want to know by the spring whether you feel ready for it next year. Both answers are allowed."),
    dict(ref="C6c", name="Junior Deacon", title="Your year as Junior Deacon",
         purpose="The first office that asks for real learning, and the one in which you will guide a new Brother through the most important night of his Masonic life. A short guide.",
         what=("The Junior Deacon sits at the right of the Senior Warden. He carries messages and communications from the Senior Warden to the Junior Warden, sees that the Brethren obey the Master’s "
               "commands in the West, and, above all, conducts the candidate through the ceremony of Initiation. On that night the candidate will remember two people: the Master, and the "
               "Brother whose arm he held. That is you."),
         jewel="A dove bearing an olive branch, the emblem of a messenger. You will carry a wand on the floor, and learning to manage it is half the office.",
         do=["Learn the floorwork before the words. Where you go, when, and with whom. The Lodge of Instruction is for this, and you will need several evenings of it.",
             "Learn the Initiation from the candidate’s side: a firm grip of the arm, clear quiet instructions, a steady pace. Nothing in the ceremony should surprise him because you have told him what to do a moment before.",
             "Before the ceremony, meet the candidate with his Personal Mentor and the Tyler. Introduce yourself; say you will be with him throughout.",
             "At every meeting, the small duties: carrying communications, attending to the Senior Warden, the ballot, the alms.",
             "Rehearse the alms collection and the ballot; they are the parts most often fumbled by a new Deacon."],
         learn=["Your spoken part is modest; your movement is not. Walk the floor at the Lodge of Instruction until you could do it in the dark, because on the night the candidate cannot see.",
                "Work with the Senior Deacon as a pair. The two of you set the pace of every ceremony, and a Lodge with two steady Deacons rarely goes wrong.",
                "Watch a Passing and a Raising as a visitor during your year, with the Senior Deacon’s work in mind."] + COMMON_LEARN[:3],
         nobody=["The candidate will squeeze your arm hard. Let him.",
                 "If something goes wrong on the floor, stop, look at the DC, and wait. He will sort it. Nobody but the Past Masters will notice, and they have all done it.",
                 "The Junior Deacon who talks to the candidate at the Festive Board, and again a week later, has done more for retention than most Lodge programmes."],
         time="One meeting a month in the season, the Lodge of Instruction most weeks, and perhaps twenty minutes a day of learning in the weeks before an Initiation. This is the year the time commitment steps up; talk about it at home before you accept.",
         next_="Senior Deacon, which builds directly on this year: the same floorwork, with the Second and Third Degrees added. The Lodge Mentor and DC will ask you in the spring."),
    dict(ref="C6d", name="Senior Deacon", title="Your year as Senior Deacon",
         purpose="The Master’s messenger, and the Brother who conducts candidates through their Passing and Raising. A short guide to the year.",
         what=("The Senior Deacon sits at the right of the Worshipful Master. He carries messages and communications from the Master to the Senior Warden, and conducts the candidate in the "
               "Second and Third Degrees. He is also, in practice, the senior of the two Deacons: the one the Junior Deacon looks to on the floor, and the one the DC relies on when the "
               "ceremony is long."),
         jewel="A dove bearing an olive branch, as for the Junior Deacon. Your wand, like his, is a working tool of the office: carried, grounded and handed with care.",
         do=["Learn the floorwork of the Second and Third Degrees thoroughly. The Third in particular has moments where the candidate depends entirely on you, and where confidence matters more than anywhere else in the Craft.",
             "Prepare the candidate practically with his Personal Mentor: what the evening will ask of him physically, that it is safe, symbolic and dignified, and that you will be beside him throughout.",
             "Attend to the Master: communications, the ballot, whatever he needs on the floor.",
             "Lead the Junior Deacon kindly. You were in his chair a year ago.",
             "If your Lodge works the Traditional History or the Charges by delegation, this is a year in which you may be asked to learn a longer piece. Say yes to what you can and no to what you cannot."],
         learn=["The Third Degree floorwork is the hardest in the Craft to do well and the most rewarding. Take as many Lodge of Instruction evenings as the Preceptor will give you.",
                "Visit two or three Lodges and watch their Senior Deacons at a Raising. You will see things done differently, and some of them better.",
                "Start on the Junior Warden’s work in the second half of the year: it is spoken, not walked, and it is a different kind of learning."] + COMMON_LEARN[:3],
         nobody=["Visiting Brethren notice the Deacons before anyone else. A quiet, unhurried pair on the floor is what makes a Lodge’s ceremonies admired.",
                 "The Senior Deacon is the Brother best placed to notice a candidate who is frightened. Say so to his mentor, and to the DC, before the night.",
                 "Rule 172: there must be at least four weeks between a candidate’s degrees. If your Lodge is planning two ceremonies close together, the DC and Secretary will know; you do not need to."],
         time="As Junior Deacon, with a longer learning curve for the Third Degree: one meeting a month, the Lodge of Instruction most weeks, and steady learning in the weeks before a Raising.",
         next_="Junior Warden, usually: your first year in the principal officers’ chairs and the first with the Festive Board in your care. The Master will discuss it with you before the Installation."),
    dict(ref="C6e", name="Junior Warden", title="Your year as Junior Warden",
         purpose="Your first year as a principal officer: a chair, a column, the Festive Board, and the first year that counts towards the Chair. A short guide.",
         what=("The Junior Warden sits in the South. In the Lodge room he has set responses in the opening and closing, calls the Brethren from labour to refreshment and back again, and in many Lodges "
               "proves visiting Brethren before a meeting. Outside the Lodge room he is responsible for the Festive Board: the catering, the seating, the Stewards and the comfort of guests. "
               "With the Master and the Senior Warden he is one of the three principal officers, and a full year as a Warden, Installation to Installation, is what makes a Brother eligible for the Chair."),
         jewel="The plumb rule, the emblem of uprightness. You will also have a gavel, and a column that stands or lies according to whether the Lodge is at labour or refreshment.",
         do=["Learn your responses in the openings and closings of all three degrees, and the calling off and on. Short pieces, but there are many of them, and they come every meeting.",
             "Take charge of the Festive Board with the Stewards: numbers, dietary needs, seating that mixes new members in, visitors looked after, and the toast list agreed with the DC.",
             "Learn to prove a visitor, if your Lodge gives that duty to the Junior Warden. The DC will teach you.",
             "Prepare and practise your Festive Board toast; it is part of the office in most Lodges.",
             "Be ready, if asked, to work a First Degree ceremony in the Chair during your year. Many Lodges give the Junior Warden an Initiation; the DC will say if yours does.",
             "Visit with a purpose: other Lodges’ Installations build the contacts that fill your own."],
         learn=["Your words come at every meeting, so they settle quickly. The craft of this year is managing people: Stewards, caterers, visitors.",
                "If you are to work a First Degree, start now. The Preceptor and the DC will build you a plan.",
                "Read the By-laws and the summons with new eyes: next year you plan a year, and the year after it is yours."] + COMMON_LEARN[:1],
         nobody=["The Festive Board tone is yours to set from the South. “Look who’s remembered where we meet” gets said, or not, depending on the officers at the top table.",
                 "A first missed subscription, a Brother who always leaves before the toasts, a Steward who has stopped coming: you will see these before the Almoner does. Tell the Lodge Mentor.",
                 "Rule 105a: a Warden must serve a full year, Installation to Installation, to be eligible for the Chair. If you were invested at a later meeting, speak to the Secretary now about a dispensation."],
         time="One meeting a month, the Lodge of Instruction most weeks, the Festive Board arrangements between meetings, and a growing number of visits. This is where the diary fills. Family, Work, Masonry, in that order; say so to the Master if it is becoming too much.",
         next_="Senior Warden: the understudy year, and the one in which you choose your team and plan your year in the Chair. The Province’s session The Chair and Beyond is for you from here."),
    dict(ref="C6f", name="Senior Warden", title="Your year as Senior Warden",
         purpose="The understudy year. A chair in the West, a Lodge to learn from the inside, and twelve months to plan the year that follows. A short guide.",
         what=("The Senior Warden sits in the West, opposite the Master. He has set responses in the openings and closings, closes the Lodge at the Master’s command, and is the Master’s "
               "second in command: if the Master is absent, the Senior Warden conducts the business from his own pedestal, though an Installed Master must occupy the Chair to open and close the Lodge "
               "and confer degrees. In practice the year is about watching how the Lodge is run, choosing the officers you will appoint, and planning your own year in the Chair."),
         jewel="The level, the emblem of equality. Your gavel and column, as for the Junior Warden, answer the Master’s.",
         do=["Learn your responses in all three degrees, and the closings, until they are automatic.",
             "Shadow the Master: at the Lodge Committee, with the Secretary over the summons, with the DC over the ceremonies, with the Treasurer over the money. Ask what he would do differently.",
             "Choose your team early and kindly. Who continues, who moves up, who is ready, who is being pushed, who is left waiting. Talk to the DC and the Lodge Mentor, not only to your friends.",
             "Plan your year now: candidates in the pipeline, ceremonies, a talk or demonstration for a meeting without a candidate, the social calendar, a White Table, the charity.",
             "Assign the Charges, the Tools and the Tracing Boards early for your year, so the Brethren who will deliver them have time.",
             "Visit widely, and attend other Lodges’ Installations: the Brethren who see you there will fill your own.",
             "Make sure the Royal Arch has been explained to you, on your timing, by the Lodge’s Royal Arch Representative.",
             "Go to The Chair and Beyond, the Province’s one-hour session for Wardens and Masters, before your Installation."],
         learn=["The ritual of the Chair is learned in this year, and the Installation itself asks a great deal of the Master Elect. Agree a learning plan with the Preceptor by the autumn and keep to it.",
                "Learn the governance as well as the words: the Book of Constitutions, your By-laws, what a dispensation is for, who may open the Lodge if the Master is late. The Secretaries’ Handbook and the Province are there to ask.",
                "Get the toast list early and practise the names and titles. It is what most Masters forget until the night."] + COMMON_LEARN[:2],
         nobody=["Rule 105a: a full year as a Warden, Installation to Installation, is the qualification for the Chair. Invested late, you will need a dispensation; ask the Secretary now.",
                 "The Installation speech is about three minutes: thank the electors and the organisers, do not repeat what others have said, and sit down.",
                 "You can have a very successful year without having to remortgage your house. Spend what you can afford; nobody should feel excluded.",
                 "The year after the Chair is the second recognised point at which good men leave. Plan it now, from the West: a role, a project, a Brother to mentor."],
         time="The heaviest year before the Chair: learning for the Installation, visits, planning, and the Committee. Talk to your family about the two years ahead as one commitment, not two surprises. Delegate from the start; it is a team, not a performance.",
         next_="The Chair. Then the year after it, which matters as much. Your Lodge Mentor will be alongside you for both."),
]


def build(o):
    out = os.path.join(out_dir, f"{o['ref']} {o['title'].replace('’', '')} Issue 1 Draft.docx")
    b = Builder(template, out, doc_title=o["title"])
    b.opening(f"Member guides · {o['ref']}", o["title"], o["purpose"],
              [("For", f"The Brother about to be invested as {o['name']}, and his Personal Mentor"),
               ("Issue", "Issue 1 (Draft for Review), October 2026 · One of six Officer Guides, Steward to Senior Warden. The office is described here; the words and floorwork are learned at the Lodge of Instruction, never from a document.")])
    b.h1("1", "What the office is")
    b.para(o["what"], after=6)
    b.table([["Your jewel", o["jewel"]]], [1800, 7612])
    b.h1("2", "What you will actually do")
    b.bullets(o["do"])
    b.h1("3", "What to learn, and how")
    b.bullets(o["learn"])
    b.h1("4", "Things nobody tells you")
    b.bullets(o["nobody"])
    b.h1("5", "The time it takes")
    b.para(o["time"], after=6)
    b.h1("6", "Who will help")
    b.table([
        ["Your Personal Mentor", "Still yours. Office does not end mentoring; it changes the conversation. Tell him if the learning is not going well, or the diary."],
        ["The Director of Ceremonies", "Owns the ceremonies and the floor. He will tell you what your Lodge does, which is what matters; Lodges differ."],
        ["The Preceptor and the LoI", "Where the office is learned. Go even in the weeks when there is nothing for you to do."],
        ["The Lodge Mentor", "Watches the office queue for the whole Lodge: nobody pushed before he is ready, nobody left waiting. Say so to him if either is happening to you."],
        ["The Province", "mentor@hertfordshirefreemasons.org.uk, the monthly mentoring call on the first Tuesday at 7pm, and Solomon (solomon.ugle.org.uk), which has a paper on every office."],
    ], [2800, 6612])
    b.h1("7", "Looking ahead")
    b.para(o["next_"], after=6)
    b.panel(["**For your mentor.** Three questions for the conversation before the Installation: Does he want this office this year, and has he said so to his family? What is the one piece he is worried about, and who will help him with it? What will we do together in the second half of the year to make the next office feel easy?",
             "**Readiness, not pressure, in either direction.** Nobody should take an office before he feels able, and nobody capable should be left waiting. Family, Work, Masonry: in that order, always."], fill=PALE, bar=DEEP)
    b.closing("Officer Guides series · Personal Mentor’s Short Guide · The Chair and Beyond")
    print("saved", b.save())


for o in OFFICES:
    build(o)
