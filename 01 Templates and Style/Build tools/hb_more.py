"""Parts Three to Five of the Hertfordshire Mentoring Handbook (imported by build_handbook.py)."""
from hmdocx import DEEP, DARK, TEAL, PALE, PALETEAL, MINT

WORDS = [
    ["Lodge", "The basic unit: Freemasons who meet together, with a name and a number. Elects a Master and officers each year."],
    ["Province", "The Lodges of a county area under a Provincial Grand Master. Above the Province is Grand Lodge."],
    ["UGLE", "The United Grand Lodge of England, Freemasons’ Hall, London: the governing body for English Freemasonry."],
    ["Summons", "The notice of a meeting: date, time, dress, business, and who is doing what. Read it."],
    ["Festive Board", "The meal after the meeting. Toasts, Masonic fire, speeches; where friendships are made."],
    ["Masonic fire", "The applause that follows a toast. Hertfordshire has its own, endorsed by the Provincial Grand Master. Show him; nobody expects him to know it."],
    ["Lodge of Instruction", "The rehearsal, usually informal, run by the Preceptor. Where you learn what you saw."],
    ["Installation", "The yearly meeting at which the new Master is installed and appoints his officers."],
    ["Initiation, Passing, Raising", "The three ceremonies that make him an Entered Apprentice, a Fellow Craft and a Master Mason."],
    ["Apron", "White for an Entered Apprentice, then light blue, then dark blue for Provincial or Grand rank. Hence “light blue”."],
    ["Regalia, jewels", "Apron, collar for officers, gloves. Jewels are the medals worn on the breast."],
    ["Visiting", "Attending another Lodge’s meeting as a guest. Encouraged from the start; freely once a Fellow Craft."],
    ["Risings", "The three points near the end of a meeting when the Master rises to ask for communications and apologies."],
    ["Royal Arch, Chapter", "The completion of Pure Antient Masonry. A Chapter is to the Royal Arch what a Lodge is to the Craft."],
    ["Proposer, Seconder", "The two members who put his name forward."],
    ["White Table, Ladies Night", "A dinner to which partners are invited; the Master’s formal dinner each year."],
    ["Dispensation", "Formal permission from the Provincial Grand Master to vary the usual rules: an emergency meeting, a change of date or venue."],
    ["Hermes", "UGLE’s membership administration system. The Secretary records attendance and ceremonies on it; it notifies the Almoner after two consecutive misses."],
    ["Solomon, Archway", "UGLE’s learning platform, and its Royal Arch resource."],
    ["Building Together", "UGLE’s current national framework. Mentoring owns its ENGAGE theme."],
]
LETTERS = [
    ["WM, IPM", "Worshipful Master; Immediate Past Master, who has just left the Chair."],
    ["SW, JW", "Senior and Junior Warden: with the Master, the three principal officers."],
    ["SD, JD, IG", "Senior Deacon, Junior Deacon, Inner Guard: the floor officers."],
    ["DC, ADC", "Director of Ceremonies and his Assistant. Follow the DC."],
    ["Tyler", "The officer outside the door; the first person he met on his Initiation night."],
    ["Bro, W Bro, VW Bro, RW Bro", "Brother; Worshipful Brother (has been Master); Very and Right Worshipful for senior Grand rank."],
    ["EA, FC, MM", "Entered Apprentice, Fellow Craft, Master Mason."],
    ["PM", "Past Master; in Hertfordshire mentoring documents also the Personal Mentor."],
    ["LM", "Lodge Mentor: co-ordinates mentoring and makes sure every new member has a Personal Mentor."],
    ["ProvGM, DepProvGM, APGM", "Provincial Grand Master, his Deputy, and the Assistant Provincial Grand Masters. “PGM” is not used in Hertfordshire mentoring documents because it reads two ways."],
    ["ProvGMen, APGMen", "Provincial Grand Mentor and the Assistant Provincial Grand Mentors."],
    ["VO", "Visiting Officer: visits a Lodge on the Provincial Grand Master’s behalf. A friend, not an inspector."],
    ["LoI, CoI", "Lodge of Instruction; Chapter of Instruction."],
    ["PGL, GL", "Provincial Grand Lodge; Grand Lodge. PProvSGW, PAGDC and the like are Past Provincial or Grand ranks."],
    ["FHLBC, DAWG", "Fleet House Light Blues Club; the Daily Advancement WhatsApp Group."],
    ["MCF", "The Masonic Charitable Foundation. A member, and a former member, remains eligible for its support."],
    ["VSL", "The Volume of the Sacred Law: the book of his own faith on which a candidate takes his Obligation."],
    ["BoC", "The Book of Constitutions: UGLE’s rules. Chapter 18 has the ones a mentor meets."],
]


def more(b):
    # ================================================================ PART THREE
    b.part("THREE", "When it goes wrong", "The moments when the culture is tested: when engagement fades, when a resignation letter arrives, when a Brother leaves, and when a member relocates. The owner-document is the Retention, Retrieval and Migration Guide.")
    b.quote("We do not retain members by design; we build a culture that prepares and supports them. Retention follows naturally.", "Provincial Mentoring Framework")
    b.para("Four principles govern everything in this Part. Retention is an outcome, not a target: nothing here is about numbers. Help, never interrogate. "
           "The pattern is the signal: risk shows as a break in an individual’s own pattern, not as a low absolute level of attendance; a Brother who has "
           "always attended twice a year is content, a stalwart who stops coming is not. And retrieval is a team activity: Secretary, Treasurer, Personal "
           "Mentor, Lodge Mentor, Almoner, Worshipful Master and Province each hold a piece, and every concern has a named owner at every moment.", after=6)

    b.h1("13", "Warning signs and the four steps")
    b.para("Most resignations are preceded by warning signs. Noticed early and acted on warmly, they can be addressed before disengagement becomes "
           "irreversible. None of these signs alone is cause for alarm; a combination, or a persistent pattern, warrants action.", after=4)
    b.table([
        ["Attendance", "Two or more consecutive meetings missed without explanation • habitual late arrival or early departure • attending only Installations or social events • ceasing to visit other Lodges • a summer absence that extends into autumn."],
        ["Participation", "Reluctance to accept work or office • withdrawal from conversation and social interaction • missing LoI while holding office • lack of preparation where it was once a point of pride • distraction or visible unhappiness in meetings."],
        ["Communication", "Unanswered calls and messages • expressed frustration, disappointment or disillusionment • repeated mention of time or money pressures • unfavourable comparison with other commitments • subscription arrears (the Treasurer sees this first)."],
    ], [2000, 7412])
    b.para("**Timing intelligence.** The first two years, the months after Raising, and the year after the Chair are the recognised risk windows; contact "
           "intensifies at each. **The stated reason is often not the real reason.** “Work pressure” may mean unsuitable meeting times, a personality "
           "clash, or simple lack of enjoyment. Only a relationship of trust surfaces the real reason, which is why the Personal Mentor, not a form, is "
           "the Province’s early-warning system.", after=6)
    b.h2("The four steps: graduated, warm, and mostly invisible")
    b.table([
        ["Step 1", "Personal Mentor: informal contact", "After any unexpected absence without apology, a friendly call or message: welfare, help if needed, and to say he was missed; several Brethren asked after him. After two consecutive misses, with or without apology, contact within seven days of the second meeting. Hermes will notify the Almoner automatically; the call is still the Lodge’s to make. The member’s needs motivate the call, never any inconvenience to the Lodge."],
        ["Step 2", "Lodge Mentor involved", "Where concern persists or the cause needs more than friendship. Takes the overview, considers what the Lodge itself could change (timing, cost, culture, an office that does not fit), keeps a discreet note, and closes the loop: acts on the cause, then confirms with the member that things actually feel better."],
        ["Step 3", "Worshipful Master’s conversation", "Where the matter touches Lodge culture, office-holding, or relations with another member: a considered private conversation, with the Almoner alongside for anything touching welfare."],
        ["Step 4", "Provincial referral", "Where an impartial third party gives the best chance, or where the member might thrive in a different Lodge. Contact the Provincial Grand Mentor’s office. Referral is a sign of responsible mentoring, not failure."],
    ], [900, 2300, 6212])
    b.key("The question is always “How can we help?”, never “Why aren’t you attending?”. The first opens a door; the second puts a man on the defensive.")

    b.h1("14", "When a resignation arrives")
    b.para("A resignation letter is the beginning of a conversation, not the end of one. The rules give the Lodge real time; use it.", after=4)
    b.h2("The rules (Rule 183, Book of Constitutions, as it applies in a Hermes Province)")
    b.bullets([
        "**The Secretary acknowledges receipt only.** He has no power to accept a resignation on the Lodge’s behalf, and his reply must not read as acceptance; it says only that the resignation will be reported to the Lodge at the next meeting",
        "**Same-day notifications:** Almoner, Lodge Mentor and the Provincial Office are told without delay",
        "**Sixty days to reconsider.** Hertfordshire uses Hermes, and under the Hermes version of the Rule the sixty-day period runs automatically from the day the Secretary receives the resignation (an email suffices) or from notification in open Lodge. No Lodge vote is needed. The period was lengthened from 21 days in 2015 precisely so that retention conversations had time to work",
        "**A resignation spoken at the Risings** is effective from that moment. The sixty days still run; the conversation still happens",
        "**Note the date.** The Secretary records exactly when he received the resignation; the window is counted from it",
    ])
    b.h2("The retrieval conversation")
    b.para("Within the window, the best-placed person, Almoner, Personal Mentor, Lodge Mentor or sponsor, has an unhurried, private conversation. Its "
           "purpose is understanding, not persuasion.", after=3)
    b.bullets([
        "What has led to this? Listen for the real reason behind the stated one",
        "Is there anything the Lodge could have done differently, or could still do?",
        "Would a change help: reduced involvement for a season, a leave of absence, stepping back from office, a transfer to a Lodge that better fits his circumstances or age profile?",
        "If the cause is money or health, the Almoner leads, and the Masonic Charitable Foundation may be able to help. Resignation should never be the price of a hard year",
        "If he is moving away, this is migration, not loss (Chapter 15). Encourage him to remain a member until he has joined elsewhere",
    ])
    b.para("If he still chooses to go, part with warmth and gratitude. How a Lodge handles a departure is watched by every member who stays, and it "
           "decides whether the door feels open for a return.", after=6)
    b.h2("After a loss: keeping the door open")
    b.para("A Brother who resigns from all Lodges remains a Freemason, and this need not be a permanent loss. Circumstances change back. Under Rule 127 "
           "he may attend any Lodge once as an unattached visitor, signing “unattached” with his last Lodge’s name and number; and with a view to "
           "joining he may attend one Lodge up to three times in twelve months, provided the Master confirms that purpose in writing to the Secretary. "
           "These rights do not extend to Brethren excluded or expelled, or who resigned from the Craft itself.", after=4)
    b.bullets([
        "The Almoner keeps in touch: a birthday card, the Provincial newsletter, invitations to social functions and White Table evenings",
        "He remains eligible for Masonic Charitable Foundation support; say so when he leaves, it matters",
        "Some of the Craft’s best returners were invited back by a Lodge that simply never stopped being friendly",
    ])
    b.h2("Lessons learned")
    b.para("Resist the comfortable story: “he wasn’t really right for us”. The Secretary’s register already records the reason for every cessation of "
           "membership (Rule 146), so the Lodge holds its own exit data. Collate the real reasons across several departures and look for patterns: timing, "
           "cost, culture, a particular period, a particular office. The Lodge Mentor and Membership Officer review losses together at least annually; "
           "several resignations in a short period warrant a fuller Lodge review. Themes, anonymised and never blaming, are shared with the Provincial "
           "Mentoring Team through the normal reporting rhythm, so the Province can act on what individual Lodges cannot see.", after=4)

    b.h1("15", "Migration, escalation and reporting")
    b.quote("Migration is a continuation of mentoring, not an administrative exercise.", "Provincial Mentoring Framework")
    b.para("Relocation is one of the most common causes of loss, and one of the clearest opportunities to keep a member in Freemasonry.", after=3)
    b.bullets([
        "**Identify early.** Mentors ask about house and job moves as a matter of course, and act on hints in conversation or changes in availability",
        "**Trigger the process.** Contact the Provincial Grand Mentor’s office, which initiates the Member Migration Process with the destination Province: introductions, visits to candidate Lodges, support until he is settled. Hermes increasingly automates the cross-Provincial notification; verify the current process with the Provincial Office",
        "**Keep him a member until he lands.** Encourage him to retain membership, or accept a courtesy arrangement, until he has joined his new Lodge, so his service is unbroken",
        "**Stay in touch until settled.** The sending Lodge’s duty ends not at the county boundary but when he is happily at home in his new Lodge, and every case is followed to a conclusion",
        "**Hertfordshire receives migrants too.** Treat an inbound migrant as a joining member (Chapter 11) and confirm his safe arrival to the Provincial Grand Mentor’s office so the loop is closed for the sending Lodge",
    ])
    b.h2("When to escalate to the Province")
    b.para("When a resignation risk needs impartial help; when a welfare matter exceeds the Almoner’s local means; when a dispute is entangled with the "
           "concern; when several members are affected at once; when a Lodge sees a pattern of early disengagement; when a relocation triggers migration; "
           "or when you would simply like a second opinion. Escalation is responsible mentoring. The Province exists to support Lodges, not to judge them, "
           "and all contact is treated in confidence.", after=4)
    b.h2("Reporting")
    b.para("Retention and retrieval experience flows through the normal rhythm: the monthly mentoring call, quarterly returns to your Assistant Provincial "
           "Grand Mentor, and the annual report, as anonymised themes, never named cases, and never attributing blame. The Province measures the process, "
           "not the person: coverage (every new member with a named Personal Mentor), activity (contact within the canonical timings, pattern-breaks "
           "actioned within seven days), experience (the member survey) and retrieval (resignations that received a conversation within the window).", after=4)

    # ================================================================ PART FOUR
    b.part("FOUR", "Learning and the Province", "How mentoring supports learning, where accurate answers live, and the Provincial support that stands behind every mentor.")

    b.h1("16", "Supporting learning")
    b.para("Accurate, consistent learning builds confidence and enjoyment. Inaccurate or inconsistent learning breeds confusion, frustration and "
           "disengagement. Mentoring supports two kinds.", after=4)
    b.table([
        ["Guided learning", "What a member needs to know to take part fully and confidently: the signs, tokens and words of each degree as taught in the Lodge; test questions before progression; ritual relevant to an office; etiquette and procedure; the structure of English Freemasonry. Planned, accurate, and overseen by those with the experience to do it well. The Lodge of Instruction is its natural home, and the Lodge Mentor works with the Preceptor and DC so that LoI is welcoming to junior Brethren and not only a rehearsal for officers."],
        ["Personal learning", "What the individual wishes to explore for his own curiosity and fulfilment: history and symbolism; the meaning of ceremony, regalia and ritual; the story of the Lodge itself; the Royal Arch and the rest of Pure Antient Masonry. Led by his interests, lifelong, and welcomed. Interpretation is offered with humility: different Brethren read a symbol differently, and none of them wrongly."],
    ], [2000, 7412])
    b.h2("Learning ritual, for the member who wants to")
    b.bullets([
        "Little and often beats one long session; ten minutes a day, out loud",
        "Understand it before memorising it. Ritual that means something is remembered; ritual that is only sound is lost under pressure",
        "Record it and listen: in the car, on a walk. Then record yourself and listen to that",
        "Work with a partner who prompts, and go to the Lodge of Instruction, where the floorwork and the words come together",
        "Never practise where a non-Mason can see or hear signs, tokens or words, including at home",
        "Nerves are normal and nobody minds a prompt. What the Lodge remembers is sincerity, not perfection",
    ])
    b.h2("Solomon and Archway")
    b.para("Solomon (solomon.ugle.org.uk) is UGLE’s online learning platform and the primary authoritative resource for members in England. It contains "
           "accurate, UGLE-approved material for every stage: short nuggets, papers, and the Diploma for those who want a structured course. Use it "
           "alongside, never instead of, face-to-face conversation; where digital access is difficult, print from it. Archway, UGLE’s developing Royal "
           "Arch resource, sits alongside it for One Journey material. Steer members away from unverified online content, speculation and material from "
           "other Masonic traditions. When in doubt, refer to Solomon or ask the Provincial Grand Mentor’s office.", after=4)
    b.panel(["**The ritual standard.** Hertfordshire mentoring documents never reveal ritual. Prepare a member for what a ceremony will ask of him practically, and let the ceremony do what it is designed to do. The Ceremony Explained series exists for the conversation afterwards. Never expose a non-Mason to signs, tokens or words."], fill=PALE, bar=DEEP)

    b.h1("17", "The Province behind you")
    b.table([
        ["Induction for new Lodge Mentors", "Every newly appointed Lodge Mentor is invited to Lodge Mentor Essentials, a one-hour induction covering the role, the library and how to reach the Province, and receives the Lodge Mentor’s Charge."],
        ["Your Assistant Provincial Grand Mentor", "One for each APGM area. Your nearest source of advice, a visitor at Initiations, and the route for your quarterly picture of mentoring in the Lodge."],
        ["Monthly mentoring call", "Hosted by the Deputy Provincial Grand Mentor on the first Tuesday of the month at 7pm by Teams, open to all Lodge and Personal Mentors. Questions, shared experience and news from the Provincial team."],
        ["Personal Mentor Course", "A two-hour in-person workshop for Personal Mentors: asking good questions, listening, the conversations that matter, and the scenarios that test them. Bring your Personal Mentors."],
        ["The Chair and Beyond", "A one-hour session for Wardens, Masters Elect and Masters: the year through a new man’s eyes, the office queue, the year after the Chair."],
        ["New Masons Evening", "An evening for Brethren in their first two years: mentoring, Learning and Development, and the Fleet House Light Blues Club in one room, with takeaway cards."],
        ["Combined Mentoring and L&D meetings", "Twice-yearly Provincial events for new Brethren. Encourage every new member to attend one."],
        ["The Visitors’ Festival", "Each year the Provincial team selects an exemplary First, Second and Third Degree ceremony for newly initiated, passed and raised Brethren to attend as visitors, seated with the Provincial Mentoring Team."],
        ["The Welcome Letter", "Every new Initiate receives a personal letter from the Provincial team shortly after his Initiation, with the charge after Initiation, the odes, a Solomon nugget, an introduction to the Light Blues Club and an invitation to DAWG. Make sure the Secretary has sent the details promptly."],
        ["Mentoring and Membership Past Masters’ Lodge", "Meets twice a year as the formal meeting point for mentoring, membership and Learning and Development across the Province."],
        ["Mentor’s Jewel", "Presented, with its explanation, to every Brother appointed Lodge Mentor."],
        ["Annual Mentors Award Dinner", "Lodges nominate the Brethren who quietly live the principles; the Province thanks them."],
        ["DAWG", "The Daily Advancement WhatsApp Group, run by the Provincial Mentoring Team: a daily piece of Masonic interest and a community of mentors."],
        ["The mentoring library", "Every document in this Handbook’s list, updated at each issue and available from the Provincial Grand Mentor’s office and the Provincial website."],
        ["One-to-one support", "For a specific situation, a difficult conversation or simply to think aloud, contact the Provincial Grand Mentor’s office directly. In confidence."],
    ], [2800, 6612])
    b.h2("The Lodge Mentor’s year")
    b.table([
        ["Every meeting", "Every candidate and new member has a Personal Mentor and a Plan. Collect the attendance record from the Secretary; pass any pattern-break to the Personal Mentor within seven days. No new or joining member dines alone."],
        ["Every month", "Join the Provincial mentoring call. A short word with each Personal Mentor: how is he getting on, does he need anything. Check the DAWG."],
        ["Every quarter", "Update your Assistant Provincial Grand Mentor. Review Plans with Personal Mentors. Check the office queue and the under-stretched with the WM and DC."],
        ["Before each ceremony", "Work through the Stage Checklist with the Personal Mentor. Confirm the candidate has been contacted the day before."],
        ["After each ceremony", "Confirm the check-in and the first one-to-one have happened. Confirm the Welcome Letter has gone (Initiations)."],
        ["Installation", "Prepare the Master Elect for the year and for what follows it. Speak to the outgoing Master about his next role. Confirm a Past Master or two as Personal Mentors."],
        ["Summer", "Deliberate contact and a social touchpoint for every spring Initiate and Entered Apprentice."],
        ["Once a year", "Brief the whole Lodge on mentoring. Review joiners and leavers with the Membership Officer. Review records, destroy what is no longer needed, and brief your likely successor. Attend the Personal Mentor Course with your team."],
    ], [2000, 7412])

    # ================================================================ PART FIVE
    b.part("FIVE", "Reference", "The rules a mentor meets, the practical answers a new Brother asks for, the words and letters he will hear, and where to find everyone.")

    b.h1("18", "Rules every mentor should know")
    b.para("Drawn from the Book of Constitutions as set out in the PGL Hertfordshire Secretaries’ Handbook and Lodge Director of Ceremonies Guide, and "
           "from UGLE’s Members’ Pathway papers. Nothing here is from memory; if challenged, the Handbook page is the answer. Verify at each issue.", after=4)
    b.table([
        ["Rule", "What it says", "Why a mentor cares"],
        ["183 Resignation", "The Secretary acknowledges receipt only; he cannot accept. In a Hermes Province the member has sixty days from receipt (or from notification in open Lodge) to withdraw his resignation.", "Sixty days is the retrieval window. Same-day notice to Almoner, Lodge Mentor and Province."],
        ["127 Unattached Brethren", "A Brother who has resigned from every Lodge may visit any Lodge once, and one Lodge three times in twelve months with a view to joining, if the Master confirms that purpose in writing to the Secretary.", "The door stays open. The Master’s signature keeps it so."],
        ["148 Arrears", "Two full years in arrears and he ceases to be a member automatically; announced in open Lodge and minuted.", "The Treasurer saw the first missed subscription eighteen months earlier. A quiet word then."],
        ["146 Register", "The Secretary records every member’s dates and the reason for every cessation of membership.", "The Lodge holds its own exit data. Use it for lessons learned."],
        ["172, 173 Degrees", "At least four weeks between degrees. A Degree by Request lets another Lodge pass or raise a candidate on written request from the Master and Secretary; the PGM encourages double ceremonies.", "Four weeks is a minimum, not a target. A candidate kept waiting a year is a candidate at risk."],
        ["119 Quorum", "Five Brethren, not counting Tyler and candidate; two members; one Installed Master. No Installed Master: the meeting is abandoned. Master absent: IPM, then senior Past Master. Master Elect absent from his Installation: postponed, held within five weeks.", "What happens when the Lodge is thin on the ground, and why a small Lodge needs its Past Masters."],
        ["105a, 109 Wardens", "A Warden must serve a full year, Installation to Installation, to be eligible for the Chair; invested late, he needs a dispensation.", "Plan the office queue with it in mind."],
        ["107, 115 The Master", "A Master may continue for a second year, proclaimed not re-installed, and receives no Past Master’s jewel until he installs his successor. Not Master of two Lodges at once without dispensation.", "The Chair ends when he hands it on."],
        ["Grand Lodge Certificate", "Presented as soon as it arrives, or sent recorded delivery and minuted. The Secretary may not hold it back until the Brother next attends.", "A passport, kept with his regalia, not framed. Make the presentation a moment."],
        ["Dispensations", "Via Hermes, three weeks to three months ahead, before the summons is printed. At an emergency meeting the dispensation is read first, only its business transacted, previous minutes not confirmed, no Risings.", "A special ceremony needs planning weeks ahead."],
        ["Official visits", "The Deputy and Assistant Provincial Grand Masters represent themselves; anyone wearing a chain is offered the gavel. Salutations are completed before the Official Visitor enters; the first wine-taking at an Installation is with him.", "What the new man sees at an Installation, explained in advance."],
        ["The IPM", "The Immediate Past Master is not an officer of the Lodge.", "A seat and no role unless the Lodge gives him one. Chapter 12."],
        ["Inclusion", "Kneeling is not obligatory; Jewish Brethren stand covered; the candidate is consulted on the Volume of the Sacred Law and the manner of his Obligation.", "Confirm adjustments discreetly, through the DC and Secretary, before the night."],
        ["White Table", "Never at an Installation or Initiation; toasts without fire; Masonic business said in the meeting, not at dinner.", "What to tell a partner to expect."],
        ["Two misses", "Hermes notifies the Almoner automatically after two consecutive misses.", "The call within seven days is still the Lodge’s to make."],
    ], [1700, 4300, 3412], header=True)

    b.h1("19", "Dress, etiquette and the Festive Board")
    b.para("The answers a new Brother asks for most. Always check the summons first; if it says nothing different, this is the standard.", after=4)
    b.table([
        ["Suit and shirt", "Dark lounge suit, preferably black; striped morning trousers with a black jacket are acceptable. Plain white formal shirt. Tails only for Active Provincial Officers at Provincial Grand Lodge."],
        ["Socks and shoes", "Plain black socks: not navy, not patterned, not novelty. Black shoes, polished."],
        ["Black tie nights", "Some Lodges dine black tie always, others only at Installation. The summons will say. Dinner jacket, smart dress shirt, black bow tie."],
        ["Tie", "Provincial tie in any Hertfordshire Lodge; Club tie at FHLBC visits, Gladsmuir 1385 and Provincial Grand Lodge. Outside Hertfordshire, a plain Masonic tie."],
        ["Pins and jewels", "Up to three pins is the convention; Masonic or charitable, never political. Once a Master Mason, up to three jewels: Royal Arch jewel nearest the centre line, then the Tercentenary jewel, then others."],
        ["Gloves and rings", "White gloves per Lodge custom; avoid dark blue square-and-compasses gloves unless you hold Provincial or Grand rank. A ring is personal preference."],
        ["Full Dress / Undress", "Applies to Provincial and Grand Officers, not to a new member. Letters after names are Provincial or Grand ranks; nobody minds being asked what theirs means."],
    ], [2000, 7412])
    b.h2("At the Festive Board")
    b.bullets([
        "Light-hearted and fun, but the Lodge’s rules still apply: no religion, no politics",
        "Jackets on, unless the Master says otherwise in summer. Phones away; a quick photo of dinner is fine, a running conversation is not",
        "Stand when the Director of Ceremonies stands; follow the Brother next to you. The Master alone handles the gavel",
        "Masonic fire follows the toasts. Hertfordshire fire is a Provincial tradition, endorsed by the Provincial Grand Master, with the caveat that its speed should not become undignified. Show him before his first dinner",
    ])
    b.h2("Replying to a toast, in six lines")
    b.table([
        ["1", "Start with “Worshipful Master, Distinguished Brethren, Brethren all”."],
        ["2", "Thank the Lodge for the meeting, the work, and the Brother who invited or looked after you."],
        ["3", "Mention one thing you enjoyed. One good piece of ritual is plenty."],
        ["4", "Invite them to your next meeting."],
        ["5", "One to two minutes. Do not rush, and do not give a best man’s speech."],
        ["6", "You may move to where people can see you, but no laps of the room."],
    ], [600, 8812])

    b.h1("20", "Questions new members ask")
    b.para("From the Province’s poll of Brethren in their first two years, and the New Masons Evening. Answer them before they are asked.", after=4)
    b.table([
        ["Do I have to attend every meeting and every dinner?", "You should, and you will enjoy it more if you do. If you cannot, send apologies to the Secretary. Nobody will pressure you; if anything is making it hard, tell your mentor or the Almoner. Family, Work, Masonry: in that order, always."],
        ["Can I visit other Lodges?", "Yes, and it is encouraged; freely once you are a Fellow Craft. Contact the Lodge Secretary, introduce yourself, and expect to reply to the Visitors’ Toast. Go with your mentor the first time. Observe before judging; never criticise another Lodge’s working."],
        ["What do I tell people at work?", "The truth: you have joined a Lodge, you meet a few times a year, there is a dinner, and it raises a great deal for charity."],
        ["Can I post about it online?", "Yes, with judgement. The Festive Board and charity events, fine; anything from inside the Lodge room, not."],
        ["Can my partner get involved?", "Yes. White Table evenings invite partners to dine; Ladies Night is the Master’s formal dinner each year; and partners are welcome at most social events."],
        ["When will I take office?", "When you are ready and if you want to. Nobody should push you early, and nobody should leave you waiting. Talk to your mentor."],
        ["How do I learn the ritual?", "At the Lodge of Instruction, with your mentor and the Preceptor, little and often. Chapter 16 has the tips. Nerves are normal; nobody minds a prompt."],
        ["What is the Royal Arch?", "The completion of Pure Antient Masonry. Your Lodge’s Royal Arch Representative will explain it when you are ready. Information, not recruitment; timing, not inevitability."],
        ["Taylor’s or Emulation?", "The two main workings in Hertfordshire. Emulation is the more relaxed; Taylor’s has more floorwork. Learned one and asked to work in the other? Ask first."],
        ["Can I attend Provincial Grand Lodge?", "Once you are a Master Mason."],
        ["What if I am struggling?", "Say so, early, to anyone: your mentor, the Almoner, the Club. Money, time, family, confidence. The question is always “How can we help?”."],
    ], [3000, 6412])
    b.h2("Three things a new member can do this week")
    b.bullets(["Join the Fleet House Light Blues Club: fhlbc.co.uk.", "Sign up to Solomon: solomon.ugle.org.uk, starting with Welcome Apprentice.", "Message his mentor with one thing from the last meeting he wants to talk about."])

    b.h1("21", "Words and letters")
    b.h2("Words he will hear")
    b.table(WORDS, [2300, 7112])
    b.h2("Letters he will see")
    b.table(LETTERS, [2300, 7112])
    b.para("Nobody minds being asked what their letters mean. Ask.", italic=True, color=DARK, after=4)

    b.h1("22", "Contacts and the library")
    b.table([
        ["Provincial Grand Mentor", "W Bro Mark Butcher, via the Provincial Office"],
        ["Deputy Provincial Grand Mentor", "W Bro Wes Pierce, via the Provincial Office"],
        ["Mentoring email", "mentor@hertfordshirefreemasons.org.uk (Provincial Grand Mentor’s office) · asstmentor@hertfordshirefreemasons.org.uk (Assistant Provincial Grand Mentors)"],
        ["Provincial Office", "Fleet House, 10 Parkway, St Albans, AL3 6PA · 01727 833061 · www.pgherts.org"],
        ["Monthly mentoring call", "First Tuesday of the month, 7pm, on Teams"],
        ["Solomon", "solomon.ugle.org.uk"],
        ["Fleet House Light Blues Club", "fhlbc.co.uk"],
    ], [3000, 6412])
    b.para("This Handbook is reviewed and updated at each issue. Corrections are collected in the Corrections Register and applied at the next issue; "
           "suggestions and corrections to the Provincial Grand Mentor’s office.", after=6)
    b.h2("Revision history")
    b.table([
        ["Issue", "Date", "Author", "Summary"],
        ["Issue 1", "October 2026", "Wes Pierce", "First issue. Compiled from the Lodge Mentor’s Guide Issue 2, the Personal Mentor’s Guide and Quick Guide, the Retention, Retrieval and Migration Guide, the Mentor Meeting Guide, the Stage Checklists, the Warning Signs card, the Ceremony Explained framework, the New Masons Evening cards and the Chair and Beyond session. Rule 183 stated in its Hermes form."],
    ], [1200, 1800, 1600, 4812], header=True)
    b.closing("The Hertfordshire Mentoring Principles · Lodge Mentor’s Guide · Personal Mentor’s Guide · Retention, Retrieval and Migration Guide · Mentor Meeting Guide · Stage Checklists · Warning Signs card · Personal Mentoring Plan")
