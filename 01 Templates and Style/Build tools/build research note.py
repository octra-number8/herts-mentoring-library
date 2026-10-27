"""Research Note 1: what other Provinces publish for mentoring, and what Hertfordshire should release next.
Usage: build_research_note.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL

template, out_dir = sys.argv[1], sys.argv[2]
b = Builder(template, os.path.join(out_dir, "Research Note 1 Mentoring Documents in Other Provinces Issue 1.docx"), doc_title="Research Note 1 · Other Provinces")
b.opening("Governance · Research Note 1", "What other Provinces publish, and what Hertfordshire should release next",
          "A survey of the mentoring documents published by other Provinces and by UGLE, set against the Hertfordshire library, with a prioritised list of what to release next. "
          "Three of the recommendations were built alongside this note: the Officer Guides series, the Proposer and Seconder’s Guide, and For Partners and Families.",
          [("Audience", "Provincial Grand Mentor, Deputy Provincial Grand Mentor, Assistant Provincial Grand Mentors"),
           ("Issue", "Issue 1, October 2026 · Research carried out 10 October 2026 from published Provincial websites, Solomon and the Project knowledge base")])

b.h1("1", "Method")
b.para("Published mentoring material was reviewed from the Provinces that make theirs public (Somerset, East Lancashire, West Lancashire, Lincolnshire, Wiltshire, Metropolitan Grand Lodge), "
       "from UGLE’s Solomon and Members’ Pathway papers, and from one overseas Constitution with a strong officer-mentoring tradition (Freemasons Victoria). Each set was compared with the "
       "Hertfordshire library as it stands at 10 October 2026. The question asked of every document was not “is it good?” but “what does it give a member or a mentor that nothing of ours does?”", after=6)

b.h1("2", "What other Provinces publish")
b.table([
    ["Province", "What they publish", "Worth noting"],
    ["Somerset", "Candidate’s Guide (What’s it all about?); Initiate’s Guide with the PGM’s welcome; EA, FC and MM guides handed over in open Lodge; Personal Development Guide in five stages with a Record of Experience and Achievement; Lodge Mentor feedback questionnaire; Snippets on symbols; a Royal Arch explanation (Talking Heads); an Initiates’ Evening; a Progression to the Master’s Chair workshop.", "The most complete set. The feedback questionnaire and the fifth stage, Preparing for Office, with a personalised ritual-learning programme, are the two things we lack."],
    ["East Lancashire", "Mentor’s Handbook; Personal Guides for the EA, FC and MM with a description of every office and its jewel, and a progression record on the inside cover.", "Officer descriptions written for the new member, not the officer. Clear, public-domain, no ritual."],
    ["West Lancashire", "Mentors’ Guide; the Pathway Explained A5 booklet bringing membership roles together; Mason Ambassadors.", "The A5 ‘who does what’ booklet is a good model for a one-page Lodge Membership Team card."],
    ["Lincolnshire", "Pathway to Mentoring book; guidance booklets for new members and for prospective officers; an annual mentoring report template; a members’ area registration requirement; branding Understand, Involve, Enjoy, Belong.", "The only Province found with a booklet aimed at prospective officers. Ours now go further, one per office."],
    ["Wiltshire", "Pathway guidance for the mentor (Engage, Encourage, Educate), with Initiation-night practical detail.", "Already in our knowledge base and reflected in the Stage Checklists."],
    ["Metropolitan Grand Lodge", "Mentors’ Handbook v2.0 (2025) covering Craft and Royal Arch; a Retention Team with exit interviews; a Visiting Officer exit form.", "Source of the one-in-three retrieval figure; the five-years-in-office recommendation of the Board of General Purposes."],
    ["UGLE (Solomon)", "Preparing for the Chair; The Responsibilities of a Proposer; Expectation Management; Planned Mentoring; papers on every office.", "Solomon’s office papers are the authoritative national layer; our Officer Guides point to them rather than repeat them."],
    ["Freemasons Victoria", "Mentor’s Guide for Mentoring Lodge Officers: office by office from Steward to Master, with a Mentor’s Note on each, a Senior Warden’s checklist, a year planner and a Masters’ Group for mutual support.", "The best model found for mentoring through office. The Masters’ Group idea is worth borrowing for Hertfordshire."],
], [2000, 4700, 2712], header=True)

b.h1("3", "Where Hertfordshire already leads")
b.para("Against that field the Hertfordshire library is already unusually complete at Tiers A, B, D and E: a one-page canon of principles, a full and a short guide for each mentoring role, a "
       "compendium Handbook, working tools for every ceremony night, a retention owner-document, and in-person courses for Lodge Mentors, Personal Mentors, and Wardens and Masters, with "
       "a New Masons Evening and takeaway cards. No other Province found publishes a facilitator-led course for Wardens and Masters, or a pocket card of the rules that bite in the Chair.", after=6)

b.h1("4", "The gaps")
b.table([
    ["Member-facing office guides", "Every Province describes the offices to the new member; none found describes each office to the man about to hold it. The Personal Mentoring Plan records office progression but nothing in the library tells a new Inner Guard what his year will be like."],
    ["The Proposer and Seconder", "Solomon has a paper; no Province found has a guide of its own. The Proposer is the first mentor a candidate has, and the person the Lodge asks when he leaves."],
    ["Partners and families", "Family, Work, Masonry is the Province’s rule, yet nothing in the library is addressed to the family. Several Lodges hand out their own leaflet; none is Provincial."],
    ["A member-held record", "Somerset’s Record of Experience and Achievement and East Lancashire’s inside-cover progression record give the member his own copy. Ours is the open PLAN-7 decision."],
    ["Feedback", "Somerset asks every new member about his guides and his mentoring. We measure coverage and activity but not yet experience; the member survey in the Framework’s measures has no instrument."],
    ["The Lodge Membership Team on one page", "West Lancashire’s A5 ‘who does what’ booklet. Our Handbook has the table; a card for the Lodge noticeboard does not exist."],
], [3000, 6412])

b.h1("5", "Recommended releases, in order")
b.table([
    ["", "Document", "For", "Status"],
    ["1", "**Officer Guides, C6a to C6f:** Your year as a Steward, Inner Guard, Junior Deacon, Senior Deacon, Junior Warden, Senior Warden. Three pages each: what the office is, what you will actually do, what to learn and how, things nobody tells you, the time it takes, who will help, looking ahead, and a note for the mentor.", "The Brother about to be invested, and his Personal Mentor", "**Built, Issue 1 draft, 10 Oct 2026**"],
    ["2", "**Proposer and Seconder’s Guide, C1a.** Before proposing; the application and interview; Initiation night; the two years after; the Seconder; a checklist.", "Any Brother proposing or seconding", "**Built, Issue 1 draft**"],
    ["3", "**For Partners and Families, C1b.** What he has joined; the secrets question; what it asks of the household; what you are welcome at; who to speak to if concerned.", "Partners and families of candidates and new members", "**Built, Issue 1 draft**"],
    ["4", "**Member-held Progression Record, D1a.** The member’s own copy of the milestones and office record, on one card, with the Solomon modules for each stage.", "Every new member", "Pending decision PLAN-7"],
    ["5", "**New Member Feedback, D7.** Six questions at three months and at one year, on paper or online: did you know what to expect; who to ask; are you enjoying it.", "New members, collated by the Lodge Mentor", "Recommend; gives the Framework’s experience measure an instrument"],
    ["6", "**Lodge Membership Team card, D8.** Who does what for a new member: Proposer, Personal Mentor, Lodge Mentor, Almoner, Membership Officer, DC, Secretary, Royal Arch Representative, on one A5 side.", "The Lodge noticeboard and every new member", "Recommend; content exists in B0 chapter 3"],
    ["7", "**Companions C3 to C5:** Fellow Craft, Master Mason and Royal Arch, wrapped around the national guides.", "Members at each stage", "Planned in the Master Framework; the Ceremony Explained set covers the ceremony side"],
    ["8", "**A Masters’ Group** for each APGM area: Masters and Senior Wardens meeting twice a year with the APGMen, as Victoria does.", "Masters and Senior Wardens", "Recommend as an event, not a document; pairs with The Chair and Beyond"],
    ["9", "**Preceptor’s Guide to the Lodge of Instruction, D9.** How a welcoming LoI paces learning to the member, draws juniors in, and avoids the culture that loses members.", "Preceptors and DCs", "Recommend; the DC Guide covers the DC’s side only"],
], [500, 4600, 2300, 2012], header=True)

b.h1("6", "Design decisions in the Officer Guides")
b.bullets([
    "**Addressed to the officer, not about him.** Every other source describes the offices to a new member. These speak to the man who is about to hold the office, in the second person, in the voice of the Personal Mentor’s Short Guide Issue 2.",
    "**The office is described; the ritual is not.** Duties, position, jewel and tools are public and are stated. Words and floorwork are learned at the Lodge of Instruction, and each guide says so on its first page.",
    "**Lodges differ, so the DC decides.** Where custom varies (who proves visitors, whether the Junior Warden works an Initiation, what happens with a late arrival), the guide says ‘ask the DC’ rather than legislating.",
    "**Readiness in both directions.** Each guide ends with a note for the mentor and the line from the Lodge Mentor’s Guide: nobody pushed before ready, nobody capable left waiting.",
    "**The rules that bite are included where they bite.** Rule 105a and dispensations appear in the Wardens’ guides; Rule 172 in the Senior Deacon’s; the adjustments guidance in the Inner Guard’s.",
    "**Time stated honestly, with the family in it.** Every guide has a section on the time the office takes, and the Wardens’ guides ask the Brother to talk to his family about the two years ahead as one commitment.",
])

b.h1("7", "Sources")
b.table([
    ["Somerset", "somersetfreemasons.org, Membership, Mentoring and Development Team page; Personal Development Guide (A5, v3); Provincial Mentor Handbook (2015)"],
    ["East Lancashire", "Mentoring Programme: Mentor’s Handbook v1.01 and Personal Guides for the EA, FC and MM (in the Project knowledge base)"],
    ["West Lancashire", "Mentors’ Guide v6; The Pathway Explained (A5)"],
    ["Lincolnshire", "Pathway to Mentoring, book 4; Annual Mentoring Report 2024 template"],
    ["Wiltshire", "Pathway Guidance for the Mentor (2023) (in the Project knowledge base)"],
    ["Metropolitan Grand Lodge", "MetGL/MetGC Mentors’ Handbook v2.0, 1 September 2025 (in the Project knowledge base)"],
    ["UGLE", "Solomon: Preparing for the Chair (LP 0169); The Responsibilities of a Proposer (LPa 0505); Members’ Pathway Level 3 papers (in the Project knowledge base)"],
    ["Freemasons Victoria", "Mentor’s Guide for Mentoring Lodge Officers (Growing Together)"],
], [2600, 6812])
b.closing("Master Framework and Library Architecture · Decisions Log · Corrections Register")
print("saved", b.save())
