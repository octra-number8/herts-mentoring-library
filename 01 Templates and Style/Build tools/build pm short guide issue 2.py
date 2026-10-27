"""B2a Personal Mentor's Short Guide, Issue 2 (Wes Pierce's text of 10 October 2026), on the Hertfordshire Mentoring template.
Usage: build_pm_short_guide2.py <template.docx> <out.docx>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL, MINT

template, out = sys.argv[1], sys.argv[2]
class B(Builder):
    def table(self, rows, widths, **kw):
        t = super().table(rows, widths, **kw)
        if len(rows) <= 6:
            for r in t.rows[:-1]:
                for c in r.cells:
                    for pp in c.paragraphs: pp.paragraph_format.keep_with_next = True
        return t

b = B(template, out, doc_title="Personal Mentor’s Short Guide")

b.opening("Practitioner handbooks · B2a", "Personal Mentor’s Short Guide",
          "A practical guide to helping a Brother through his Masonic journey.",
          [("Audience", "Personal Mentors, and any Brother asked to look after a new member"),
           ("Issue", "Issue 2 (Draft for Review), October 2026 · Hertfordshire Freemasons, Provincial Mentoring Team"),
           ("Companions", "Personal Mentor’s Guide (full) · Mentor Meeting Guide · Stage Checklists · Warning Signs card")])

b.para("Being asked to act as someone’s Personal Mentor is an important role, but it doesn’t need to be complicated.", after=6)
b.para("This short guide explains what the role involves, how you can support a Brother at different stages of his Masonic journey and where to find help when you need it.", after=6)
b.para("It’s not intended to tell you how to have every conversation or deal with every situation. Every Brother is different, and good mentoring is about understanding the individual and providing the right support at the right time.", after=6)
b.para("For more detailed information, please refer to the full Personal Mentor’s Guide.", after=6)

# 1
b.h1("1", "Understanding your role")
b.para("The most important thing to understand is that **you don’t need to know everything about Freemasonry to be a good Personal Mentor.**", after=6)
b.para("Your role is to be someone your Brother knows he can turn to. Someone he feels comfortable asking questions, talking to and seeking advice from.", after=6)
b.para("You are there to help him settle into his Lodge, understand what’s going on around him and enjoy his Freemasonry.", after=6)
b.para("Sometimes that might mean explaining something about a ceremony. Other times, it might simply be a telephone call to see how he’s getting on.", after=6)
b.para("It’s about building a relationship, rather than just carrying out a task.", after=6)
b.h2("What we expect from a Personal Mentor")
b.table([
    ["Your role is to", ["Be a friendly and approachable point of contact.", "Keep in touch, particularly between Lodge meetings.", "Help him understand and enjoy his Freemasonry.", "Introduce him to other members and opportunities within the Lodge and Province.", "Recognise when he might need a little extra support.", "Help him find the answers to questions you cannot answer yourself."]],
    ["Your role isn’t to", ["Know everything about Freemasonry.", "Teach him ritual. That’s where the Lodge of Instruction comes in.", "Monitor his attendance or report on his progress.", "Take responsibility for every aspect of his Masonic development.", "Replace the Lodge Mentor, who oversees mentoring within the Lodge."]],
], [2200, 7212])
b.para("Good mentoring is about being available, approachable and taking an interest.", after=6)
b.h2("The four principles of Hertfordshire Mentoring")
b.para("Our approach to mentoring is built around four principles.", after=4)
b.principles_strip()
b.table([
    ["PREPARE", "Making sure a Brother knows what to expect and feels comfortable about the next stage of his journey."],
    ["GUIDE", "Helping him understand Freemasonry, answering questions and pointing him towards reliable information."],
    ["SUPPORT", "Being there when he needs help, encouragement or simply someone to talk to."],
    ["ENLIGHTEN", "Encouraging him to learn more, develop his understanding and discover the wider opportunities Freemasonry offers."],
], [1800, 7612])
b.panel(["These aren’t four separate stages. They should be part of everything we do as mentors, throughout a Brother’s Masonic journey."], fill=PALE, bar=DEEP)

# 2
b.h1("2", "Getting started")
b.para("When you’re appointed as a Personal Mentor, your first priority should be getting to know the Brother you’re supporting.", after=6)
b.para("The Lodge Mentor should make the introduction, but it’s also worth having a conversation with his Proposer.", after=6)
b.para("Find out a little about him, his interests, family commitments and anything else that might help you understand his circumstances.", after=6)
b.para("Remember that everyone joins Freemasonry for different reasons, and not everyone will want the same things from it.", after=6)
b.h2("Your first conversation")
b.para("This doesn’t need to be a formal meeting. A coffee, a drink or a conversation after a Lodge meeting is absolutely fine. Use the opportunity to get to know each other. You might want to:", after=3)
b.bullets([
    "Explain a little about yourself and your own Masonic journey.",
    "Talk about why he decided to join Freemasonry.",
    "Ask what he’s hoping to get from being a member.",
    "Explain what a Personal Mentor does and how you can help.",
    "Reassure him that he can ask questions, however simple they might seem.",
    "Agree how you’ll keep in touch.",
])
b.para("One of the most useful things you can do is share some of your own experiences, particularly the things you found confusing when you first joined. We’ve all been the new Brother in the room at some point.", after=6)
b.panel(["Make it clear that **Freemasonry should be enjoyable, there is no pressure to rush through anything, and you’re there to help him get the most from his membership.**"], fill=PALETEAL, bar=TEAL)

# 3
b.h1("3", "Supporting a Brother through his Masonic journey")
b.para("There are certain points during a Brother’s Masonic journey when a little extra guidance and support can make a real difference. The following is intended as a reminder of the things worth considering at each stage.", after=6)
b.para("It’s not a checklist that must be completed in a particular order. Use your judgement and adapt your approach to the Brother you’re supporting.", after=6)

b.h2("Before his Initiation")
b.para("For most candidates, their Initiation will be their first proper experience of a Lodge meeting. There will naturally be some uncertainty about what to expect. Your job is to help him feel comfortable and prepared.", after=6)
b.para("Make sure he understands the practical arrangements, including where to go, when to arrive, what to wear and what he needs to bring. If appropriate, arrange to meet socially beforehand and include his partner or family.", after=6)
b.para("A quick telephone call or message the day before his Initiation is a good opportunity to answer any last-minute questions and reassure him.", after=6)
b.para("The aim is simple: **he should arrive looking forward to the evening rather than worrying about it.**", after=6)

b.h2("On his Initiation evening")
b.para("Your Brother will have a lot to take in, and much of it will be completely new to him. Make sure he knows where to go and introduce him to the Tyler and Junior Deacon before the meeting.", after=6)
b.para("After the ceremony, try to sit near him and introduce him to other members. The Festive Board can be just as unfamiliar as the ceremony itself, so explain the toasts, Masonic Fire and anything he might be asked to do. If he’s expected to make a short reply, help him prepare beforehand.", after=6)
b.para("Most importantly, make sure he’s included throughout the evening. Nobody should come away from their Initiation feeling they’ve been left to work things out for themselves.", after=6)

b.h2("His first few weeks as an Entered Apprentice")
b.para("A day or two after his Initiation, give him a call. Ask him how he found the evening, what he enjoyed and whether there was anything he didn’t understand. Try to arrange some time together before his next Lodge meeting to talk through the ceremony and answer his questions.", after=6)
b.para("Over the following meetings, help him become familiar with:", after=3)
b.bullets([
    "The different Lodge offices and who does what.",
    "Lodge etiquette and how meetings operate.",
    "The Festive Board and its traditions.",
    "The charitable side of Freemasonry.",
    "The Initiate’s Guide and other useful resources.",
    "Solomon, the UGLE learning platform.",
    "The Lodge of Instruction and how it can help him.",
])
b.para("It’s also worth introducing him to opportunities beyond his own Lodge, such as visiting other Lodges, the Fleet House Light Blues Club and the Daily Advancement WhatsApp Group (DAWG).", after=6)
b.para("Don’t overwhelm him with information. There’s plenty of time, and he’ll probably take more in through a few relaxed conversations than being given everything at once.", after=6)

b.h2("Between his degrees")
b.para("This is a period where Personal Mentors can make a particularly important difference. Depending on the ceremony being worked, your Brother may not be able to attend every Lodge meeting. It’s easy for a new member to feel he’s missing out or that everyone else is getting on with things without him.", after=6)
b.para("Keep in touch and make sure he continues to feel part of the Lodge. Use the opportunity to talk about his experiences, introduce him to more members and help him develop his understanding. If he’s preparing for his next degree, make sure he’s comfortable and knows what is expected.", after=6)
b.panel(["**Progression should always be based on the Brother’s readiness, not simply because there’s a date available in the Lodge calendar.**"], fill=PALE, bar=DEEP)

b.h2("After his Passing")
b.para("Arrange to catch up with him shortly after the ceremony. Ask how he found it and whether there are any parts he’d like to understand better. Introduce the Fellow Craft’s Guide and encourage him to explore the meaning of the degree.", after=6)
b.para("If possible, arrange for him to see another Passing ceremony at a different Lodge. As he becomes more comfortable, you can start talking about the next stage of his journey. Again, there’s no need to rush.", after=6)

b.h2("After his Raising")
b.para("Becoming a Master Mason is an important milestone, but it certainly isn’t the end of his Masonic journey. In many ways, it’s where the wider opportunities of Freemasonry really begin. It’s also a point where some members can lose direction if they don’t understand what comes next.", after=6)
b.para("Make time to meet with him and discuss the opportunities now available. These might include visiting other Lodges, becoming involved in Lodge activities, developing his Masonic knowledge and taking on a role when he feels ready.", after=6)
b.para("Help him understand visiting etiquette, how to sign in as a visitor and how to respond to the Visitors’ Toast. It’s also a good opportunity to explain how his Lodge, the Province and United Grand Lodge fit together. Introduce the Master Mason’s Guide and, where possible, arrange to go visiting together.", after=6)

b.h2("Life as a Master Mason")
b.para("Not every Brother wants the same experience from Freemasonry. Some enjoy ritual, others prefer the social side, charity work, visiting or learning more about the history and traditions. Your role is to help him find the areas that interest him. Encourage him to get involved, but don’t assume everyone wants to follow the same path.", after=6)
b.para("The Royal Arch is another part of the Masonic journey that he should understand. When appropriate, explain what it is and introduce him to the Lodge Royal Arch Representative if he’d like to know more. The important thing is that he knows what opportunities are available and can decide what interests him.", after=6)

b.h2("Taking office and beyond")
b.para("At some point, your Brother may be invited to take an office within the Lodge. For some members, this is something they’re keen to do. For others, the thought of learning ritual or taking on additional responsibilities can be quite daunting.", after=6)
b.para("Have an honest conversation about what the role involves and whether he feels ready. Make sure he knows what support is available, particularly through the Lodge of Instruction. Nobody should feel pressured to accept an office before they’re comfortable doing so.", after=6)
b.para("And remember, mentoring shouldn’t automatically stop when someone becomes a Master Mason, takes office or even becomes a Past Master. Circumstances change, and every Brother can benefit from a little support from time to time.", after=6)

# 4
b.h1("4", "Having the right conversations")
b.para("You don’t need a formal agenda or a set of prepared questions to be a good mentor. In most cases, a normal conversation is all that’s needed. The important thing is to show an interest, listen and give your Brother the opportunity to raise anything that’s on his mind.", after=6)
b.para("Some simple questions can help:", after=3)
b.bullets([
    "How did you find the last meeting?",
    "Was there anything in the ceremony you didn’t understand?",
    "How are you getting on at the Lodge of Instruction?",
    "Is there anything about Freemasonry you’d like to know more about?",
    "Are you enjoying it?",
    "How are things generally?",
])
b.para("That last question is particularly important. Remember, we’re supporting the person, not just his involvement in Freemasonry.", after=6)
b.para("If he raises something that’s worrying him, take the time to listen and understand the situation. You don’t need to have every answer or solve every problem yourself. Sometimes the most helpful thing you can do is put him in touch with the right person.", after=6)
b.para("If you’re unsure about anything relating to Lodge procedures or Masonic practice, check with the Lodge Mentor rather than guessing.", after=6)
b.h2("Looking after our members")
b.para("Occasionally, a Brother may share something personal relating to his health, family, finances or wellbeing. These situations need to be handled sensitively and with appropriate discretion. You aren’t expected to deal with them on your own.", after=6)
b.panel(["Where a welfare concern arises, involve the Lodge Almoner and speak to the Lodge Mentor so that the Brother can receive the right support. The important thing is that we recognise when someone needs help and make sure that help is available."], fill=PALETEAL, bar=TEAL)

# 5
b.h1("5", "Recognising when someone might need support")
b.para("One of the most valuable things a Personal Mentor can do is notice when something changes. It might be that a Brother:", after=3)
b.bullets([
    "Has missed a couple of meetings without explanation.",
    "Has stopped responding to messages.",
    "No longer attends the Lodge of Instruction.",
    "Mentions that he’s struggling with time or money.",
    "Seems quieter or less involved than usual.",
    "Doesn’t appear to be enjoying his Freemasonry.",
])
b.para("None of these things necessarily means there’s a problem. We all have busy lives and other commitments. However, if you notice a change, it’s worth picking up the telephone and having a conversation.", after=6)
b.para("Don’t make assumptions, and don’t turn it into a discussion about attendance. A simple *“Haven’t seen you for a while, how are things?”* is usually a much better starting point.", after=6)
b.para("If you’re concerned, speak to the Lodge Mentor so you can agree how best to support him.", after=6)
b.panel(["**We’re not trying to persuade members to attend more meetings. We’re trying to make sure they feel valued, included and supported.** If a Brother is enjoying his Freemasonry and feels part of his Lodge, attendance will usually take care of itself."], fill=PALE, bar=DEEP)

# 6
b.h1("6", "Where to find help and support")
b.para("As a Personal Mentor, you’re not expected to do everything yourself. There’s a wider mentoring structure within Hertfordshire to support both you and the Brother you’re mentoring.", after=6)
b.table([
    ["Your Lodge Mentor", "Your first point of contact for advice or assistance. The Lodge Mentor co-ordinates mentoring within the Lodge and can help with questions, concerns or situations where additional support might be needed."],
    ["Your Lodge Almoner", "The person to speak to when a Brother needs welfare support, whether that’s related to health, finances, bereavement or family circumstances."],
    ["The Provincial Mentoring Team", "We’re here to support Lodge Mentors and Personal Mentors, provide guidance and help where something needs wider Provincial involvement. If you’re unsure about something, please get in touch. Email: mentor@hertfordshirefreemasons.org.uk"],
    ["Monthly Mentoring Call", "We hold a regular online mentoring call on the first Tuesday of each month at 7pm. It’s open to Lodge Mentors and Personal Mentors and gives everyone an opportunity to ask questions, share experiences and hear what’s happening across the Province."],
    ["Solomon", "UGLE’s learning platform provides a wide range of information and resources to support Masonic learning and development. solomon.ugle.org.uk"],
], [2600, 6812])
b.h2("Keeping a simple record")
b.para("It’s useful to keep a brief note of when you’ve spoken to your Brother and any areas you’ve discussed. This doesn’t need to be anything formal or complicated. It’s simply a way of helping you remember what you’ve covered and whether there’s anything you agreed to follow up.", after=6)
b.para("Keep any notes private and only share relevant information with the Lodge Mentor where appropriate.", after=6)
b.para("If you’re ever concerned about a Brother or unsure whether something needs raising, have a conversation with your Lodge Mentor. It’s always better to ask than to leave something that could have been addressed earlier.", after=6)

# 7
b.h1("7", "Remember why we’re doing this")
b.para("Freemasonry should be something we enjoy. We join for different reasons, and we all have different expectations, but friendship, support and a sense of belonging are an important part of what makes our organisation special.", after=6)
b.para("As Personal Mentors, we have an opportunity to make a real difference to someone’s experience, particularly during those early years when everything is unfamiliar.", after=6)
b.para("You don’t need to be an expert. You don’t need to have all the answers. You simply need to take an interest, be approachable and make sure your Brother knows he’s got someone he can turn to.", after=6)
b.panel(["And remember: **Family first. Work second. Freemasonry third.** We should never lose sight of that.",
         "If a Brother enjoys his Freemasonry, he’ll want to attend. If he attends, he’ll become involved. If he becomes involved, he’ll develop friendships and feel part of the Lodge. And that’s ultimately what good mentoring is about."], fill=PALE, bar=DEEP)
b.para("**Prepare. Guide. Support. Enlighten.**", size=13, color=TEAL, after=4)
b.para("*Hertfordshire Freemasons | Provincial Mentoring Team · Supporting Brethren throughout their Masonic journey.*", size=10, color=DARK, after=4)
b.closing("Personal Mentor’s Guide (full) · Mentor Meeting Guide · Stage Checklists · Warning Signs card · The Hertfordshire Mentoring Handbook")
print("saved", b.save())
