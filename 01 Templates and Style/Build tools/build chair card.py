"""E6a The Chair and Beyond pocket card: one double-sided A5 takeaway for Wardens and Masters.
Usage: build_chair_card.py <template.docx> <out_dir>"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmcard import Card, BODY
from hmdocx import PALE, PALETEAL

template, out_dir = sys.argv[1], sys.argv[2]

# Side A: the twelve rules that bite in a Master's year
RULES = [
    ["1", "**The Secretary cannot accept a resignation.** He acknowledges receipt only. The man then has sixty days to withdraw it; in a Hermes Province they run from the day his email arrives. Lengthened from 21 days in 2015 so that someone had time to have the conversation. *(Rule 183)*"],
    ["2", "**A resignation spoken at the Risings is irrevocable the moment it is said**, unless the Lodge votes immediately to invite its withdrawal. Ask for a proposer and seconder on the spot. *(Rule 183)*"],
    ["3", "**Your signature keeps a door open.** A Brother who has resigned from every Lodge may visit any Lodge once; he may visit one Lodge three times in twelve months with a view to joining, if the Master confirms that purpose in writing to the Secretary. *(Rule 127)*"],
    ["4", "**Two full years in arrears and he ceases to be a member automatically**, announced in open Lodge and minuted. The Treasurer saw the first missed subscription eighteen months earlier. A quiet word then, not a letter. *(Rule 148)*"],
    ["5", "**Five to open:** five Brethren, not counting Tyler and candidate; two of them members; one an Installed Master. No Installed Master present: the meeting is abandoned and minuted. Master Elect absent from his Installation: postponed, and held within five weeks. *(Rule 119)*"],
    ["6", "**Four weeks between degrees is a minimum, not a target.** The PGM encourages double ceremonies so no Initiate is kept waiting, and a Degree by Request lets another Lodge pass or raise your candidate on a written request from Master and Secretary. *(Rules 172, 173)*"],
    ["7", "**The Warden invested late.** A Warden must serve a full year, Installation to Installation, to be eligible for the Chair. Invested at a later meeting, he cannot be elected Master without a dispensation. *(Rules 105a, 109)*"],
    ["8", "**The Grand Lodge Certificate is presented as soon as it arrives**, or sent recorded delivery and minuted; the Secretary may not hold it back until the Brother next attends. A passport, kept with his regalia, not framed. Make the presentation a moment. *(Secretaries’ Handbook)*"],
    ["9", "**The Immediate Past Master is not an officer of the Lodge.** A seat and no role, unless the Lodge gives him one. And no Past Master’s jewel until he has installed his successor. *(Secretaries’ Handbook; Rule 107)*"],
    ["10", "**Anyone wearing a chain represents themselves.** The Deputy and Assistants are never “the PGM’s representative”; offer the gavel. Salutations are completed before the Official Visitor enters; the first wine-taking at an Installation is with him. *(Secretaries’ Handbook; DC Guide)*"],
    ["11", "**Hermes tells the Almoner after two consecutive misses.** The call within seven days is still the Lodge’s to make: “How can we help?”, never “Why weren’t you there?”. *(Members’ Pathway)*"],
    ["12", "**Dispensations: three weeks to three months ahead, via Hermes, and before the summons is printed.** Emergency meeting: dispensation read first, only its business transacted, previous minutes not confirmed, no Risings. *(Secretaries’ Handbook)*"],
]

# Side B: ten more for the Festive Board and the year
MORE = [
    ["Hertfordshire fire", "A Provincial tradition endorsed by the Provincial Grand Master, with the written caveat that its speed should not “reach the level of absurdity”. Show the new man before his first Festive Board; nobody expects him to know it."],
    ["Three minutes", "The Installation speech: thank the electors and organisers, do not repeat what others have said, sit down. Get the toast list early and practise the names and titles; it is what most Masters forget until the night."],
    ["The Master’s Song", "The Handbook warns that a Master may be “overcome” after it and forget to thank the proposer of his toast. The Master alone handles the gavel at dinner."],
    ["“Without having to remortgage your house”", "Solomon’s advice on the social year. Spend what you can afford; there is no rule on guest numbers; nobody should feel excluded. Committee meetings: about thirty minutes."],
    ["White Table", "Never at an Installation or Initiation. Toasts without fire. Anything you want to say on a Masonic subject is said in the meeting, not in your reply at dinner."],
    ["The register already knows", "The Secretary must record the reason for every cessation of membership. Your Lodge holds its own exit data. Resist the comfortable story: “he wasn’t really right for us”. *(Rule 146)*"],
    ["Kneeling is not obligatory", "Jewish Brethren stand covered; the candidate is consulted on the Volume and the manner of his Obligation. Inclusion is the Master’s responsibility, not the DC’s alone."],
    ["The youngest Brother sets up the Temple", "The DC Guide’s suggestion: let him help lay out the Lodge so he learns what will happen. The simplest moment to design for a man with “no job yet”."],
    ["1813", "At the Union, Pure Antient Masonry was declared to consist of three degrees, including the Supreme Order of the Holy Royal Arch. One sentence for when the Royal Arch Representative speaks: information, never recruitment."],
    ["Two windows", "The first two years, and the year after the Chair. The Master is standing in both at once. Plan the year after from Installation day; the Lodge Mentor will ask."],
]

c = Card(template, os.path.join(out_dir, "E6a The Chair and Beyond Pocket Card Issue 1 Draft.docx"), "The Chair and Beyond")
c.side_title("The Chair and Beyond · Pocket card", "Twelve things nobody tells a Master")
c.two(RULES, widths=[520, BODY - 520], size=7.3)
c.foot()
c.side_title("The Chair and Beyond · Pocket card", "Ten more for the year", new_page=True)
c.two(MORE, widths=[1750, BODY - 1750], size=7.3)
c.box(["**Sources:** Book of Constitutions via the PGL Hertfordshire Secretaries’ Handbook (2026) and Lodge Director of Ceremonies Guide (2025); UGLE Members’ Pathway; Solomon, *Preparing for the Chair*. **Family, Work, Masonry: in that order, always. For the Master too.**"], fill=PALETEAL)
c.foot()
print("saved", c.save())
