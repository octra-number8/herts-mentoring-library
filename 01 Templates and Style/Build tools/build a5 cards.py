"""New Masons Evening takeaway cards: two double-sided A5 cards on the Mentoring section.
Usage: build_a5_cards.py <template.docx> <out_dir>"""
import sys, os, re, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, TEAL, PALE, PALETEAL, DARK, PRINCIPLES, PRINCIPLE_DEFS, RGB
from docx.shared import Pt, Twips, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

template, out_dir = sys.argv[1], sys.argv[2]
A5_W, A5_H, MARGIN = 8391, 11906, 680
BODY = A5_W - 2 * MARGIN  # 7031
SCALE = A5_W / 11906


class Card(Builder):
    def __init__(self, out, title):
        super().__init__(template, out, doc_title=title)
        sec = self.doc.sections[0]
        sec.page_width, sec.page_height = Twips(A5_W), Twips(A5_H)
        sec.left_margin = sec.right_margin = Twips(MARGIN)
        sec.top_margin, sec.bottom_margin = Twips(1000), Twips(760)
        sp = sec._sectPr
        tp = sp.find(qn("w:titlePg"))
        if tp is not None: sp.remove(tp)
        # scale the slim header and footer tables to A5
        for part in (sec.header.part, sec.footer.part):
            root = part._element
            for el in root.iter():
                for attr in (qn("w:w"),):
                    v = el.get(attr)
                    if v and el.tag in (qn("w:tblW"), qn("w:gridCol"), qn("w:tcW"), qn("w:tblInd")):
                        el.set(attr, str(int(round(int(v) * SCALE))))
                if el.tag == qn("w:tcMar"):
                    for m in el:
                        if m.get(qn("w:w")): m.set(qn("w:w"), str(MARGIN))
                if el.tag == qn("w:tab") and el.get(qn("w:pos")):
                    el.set(qn("w:pos"), str(BODY))
        # no page numbers on a printed card: drop the "Page X of Y" runs from the footer
        froot = sec.footer.part._element
        for p_ in list(froot.iter(qn("w:p"))):
            txt = "".join(t.text or "" for t in p_.iter(qn("w:t")))
            if "Page" in txt or p_.find(qn("w:fldSimple")) is not None or any(True for _ in p_.iter(qn("w:instrText"))):
                for r in list(p_):
                    if r.tag == qn("w:r") or r.tag == qn("w:fldSimple"):
                        p_.remove(r)
        # body font a touch smaller for a card
        st = self.doc.styles["Normal"]; st.font.size = Pt(8.5)
        self.doc.styles["List Bullet"].font.size = Pt(8.5)

    def side_title(self, kicker, title, new_page=False):
        p = self.para(kicker, style="DocumentType", after=0)
        if new_page: p.paragraph_format.page_break_before = True
        for r in p.runs: r.font.size = Pt(8.5)
        t = self.para(title, style="Title", after=4)
        for r in t.runs: r.font.size = Pt(18)
        return t

    def h(self, text, color=DEEP):
        p = self.para(text, bold=True, color=color, size=10, before=3, after=1, keep=True)
        return p

    def body(self, text, after=2):
        return self.para(text, size=8.5, after=after)

    def bl(self, items, size=8.5):
        for it in items:
            p = self.doc.add_paragraph(style="List Bullet")
            self._runs(p, it, size=size)
            p.paragraph_format.space_after = Pt(0.5)

    def box(self, lines, fill=PALE, bar=TEAL):
        t = self.doc.add_table(rows=1, cols=1)
        self._widths(t, [BODY]); self._borders(t, {"left": ("single", 18, bar)}); self._margins(t, 50, 50, 120, 120)
        c = t.cell(0, 0); self._shade(c, fill)
        first = True
        for line in lines:
            p = c.paragraphs[0] if first else c.add_paragraph(); first = False
            p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
            self._runs(p, line, color=DARK, size=8.5)
        self._cant_split(t); self.spacer(3)

    def two(self, rows, widths=None, header=False, size=8.5):
        widths = widths or [1800, BODY - 1800]
        t = self.doc.add_table(rows=len(rows), cols=2, style="Mentoring Table")
        self._widths(t, widths)
        for i, (a, b) in enumerate(rows):
            ca, cb = t.cell(i, 0), t.cell(i, 1)
            if header and i == 0:
                self.cell_text(ca, a, bold=True, color="FFFFFF", size=size); self.cell_text(cb, b, bold=True, color="FFFFFF", size=size)
                self._shade(ca, DEEP); self._shade(cb, DEEP)
            else:
                if isinstance(a, list): self.cell_bullets(ca, a, after=1)
                else: self.cell_text(ca, a, size=size)
                if isinstance(b, list): self.cell_bullets(cb, b, after=1)
                else: self.cell_text(cb, b, size=size)
            for c in (ca, cb):
                for p in c.paragraphs:
                    p.paragraph_format.space_before = Pt(0.5); p.paragraph_format.space_after = Pt(0.5)
                    for r in p.runs: r.font.size = Pt(size)
        self._look(t, 1 if header else 0, 0 if header else 1); self._cant_split(t); self.spacer(3)

    def strip(self):
        t = self.doc.add_table(rows=2, cols=4)
        self._widths(t, [BODY // 4] * 4); self._borders(t, {"insideV": ("single", 8, "FFFFFF")}); self._margins(t, 50, 50, 90, 90)
        for i, (name, fill) in enumerate(PRINCIPLES):
            c = t.cell(0, i); self._shade(c, fill)
            p = c.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.space_before = Pt(0)
            r = p.add_run(f"{i+1} "); r.font.color.rgb = RGB("8FD3D1"); r.bold = True; r.font.size = Pt(8.5)
            r = p.add_run(name.upper()); r.font.color.rgb = RGB("FFFFFF"); r.bold = True; r.font.size = Pt(8.5)
            c2 = t.cell(1, i); self._shade(c2, PALE)
            p2 = c2.paragraphs[0]; p2.paragraph_format.space_after = Pt(0); p2.paragraph_format.space_before = Pt(0)
            r = p2.add_run(PRINCIPLE_DEFS[name]); r.font.size = Pt(7); r.font.color.rgb = RGB(DARK)
        self._cant_split(t); self.spacer(3)

    def page_break(self):
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def foot(self):
        self.para("Hertfordshire Provincial Mentoring · mentor@hertfordshirefreemasons.org.uk · solomon.ugle.org.uk · fhlbc.co.uk  |  Prepare • Guide • Support • Enlighten",
                  size=7, color=DARK, before=3, after=0)


# ======================= CARD 1 =======================
c = Card(os.path.join(out_dir, "New Masons Evening Card 1 Issue 1 Draft.docx"), "New Masons Evening · Card 1")
c.side_title("New Masons Evening · Card 1 of 3", "Who’s in your corner")
c.two([
    ["Your Personal Mentor", "One Brother, assigned to you. A friend first: the person you ring, message or sit next to without feeling you are a bother. Your first call for any question."],
    ["Your Lodge Mentor", "Co-ordinates mentoring across the Lodge; makes sure every new member has a Personal Mentor. Your link to the Province."],
    ["The Almoner", "Welfare: health, money, family, bereavement. Anything that touches your life outside the Lodge."],
    ["The Provincial team", "Provincial Grand Mentor, Deputy, and five Assistant Provincial Grand Mentors. Here to help, never to inspect."],
])
c.h("The four principles")
c.strip()
c.h("The journey ahead")
c.two([
    ["Initiation", "Entered Apprentice. Your first night, with your mentor beside you."],
    ["Passing", "Fellow Craft, usually six to twelve months on. You answer the questions in open Lodge."],
    ["Raising", "Master Mason. Visiting opens up fully; a beginning, not a summit."],
    ["One Journey", "The Royal Arch completes Pure Antient Masonry, on your timing. Information, not recruitment."],
    ["Office", "Only when you are ready, and only if you want it."],
], widths=[1500, BODY - 1500])
c.box(["**Two rules run through every stage.** No surprises: you will always know what is coming next. And you set the pace, never the calendar. **Family, Work, Masonry: in that order, always.**"])
c.foot()
c.side_title("New Masons Evening · Card 1 of 3", "What to wear", new_page=True)
c.body("Always check the Summons first. If it says nothing different, this is the standard.", after=4)
c.two([
    ["Suit and shirt", ["Dark lounge suit, preferably black; striped morning trousers with a black jacket are acceptable", "Plain white formal shirt, single or double cuff", "Tails only for Active Provincial Officers at Provincial Grand Lodge"]],
    ["Socks and shoes", ["Plain black socks. Not navy, not patterned, not novelty", "Black shoes, polished. Not trainers, boots or Crocs"]],
    ["Black tie nights", ["Some Lodges dine black tie always, others only at Installation. The Summons will say", "Dinner jacket, smart dress shirt, black bow tie"]],
    ["Tie", ["Provincial tie in any Hertfordshire Lodge; Club tie at FHLBC visits, Gladsmuir 1385 and Provincial Grand Lodge", "Outside Hertfordshire, a plain Masonic tie"]],
    ["Pins", ["Yes. Up to three is the convention; Masonic or charitable, never political. FHLBC members wear the Club pin"]],
    ["Jewels", ["Once you are a Master Mason, up to three. Royal Arch jewel nearest your centre line, then the Tercentenary jewel, then others"]],
    ["Rings and gloves", ["A ring is personal preference. Square and compasses on gloves: avoid dark blue ones unless you hold Provincial or Grand rank"]],
], widths=[1500, BODY - 1500], size=9)
c.box(["**Full Dress / Undress on a Summons** applies to Provincial and Grand Officers, not to you yet. **Letters after names** are Provincial or Grand ranks; nobody minds being asked what theirs means."], fill=PALETEAL)
c.foot()
print("saved", c.save())

# ======================= CARD 2 =======================
c = Card(os.path.join(out_dir, "New Masons Evening Card 2 Issue 1 Draft.docx"), "New Masons Evening · Card 2")
c.side_title("New Masons Evening · Card 2 of 3", "The Festive Board")
c.h("Etiquette")
c.bl([
    "Light-hearted and fun, but the Lodge’s rules still apply: no religion, no politics.",
    "Jackets on, unless the Master says otherwise in summer.",
    "Phones away. A quick photo of dinner, fine; a running text conversation, not. Need a call? Leave the room.",
    "Stand when the Director of Ceremonies stands; follow the Brother next to you.",
])
c.h("Replying to a toast, in six lines")
c.two([
    ["1", "Start with “Worshipful Master, Distinguished Brethren, Brethren all”."],
    ["2", "Thank the Lodge for the meeting, the work, and the Brother who invited or looked after you."],
    ["3", "Mention one thing you enjoyed. One good piece of ritual is plenty."],
    ["4", "Invite them to your next meeting."],
    ["5", "One to two minutes. Do not rush, and do not give a best man’s speech."],
    ["6", "You may move to where people can see you, but no laps of the room."],
], widths=[500, BODY - 500])
c.h("Do I have to attend?")
c.body("You should, and you will enjoy it more if you do. If you cannot, send apologies to the Secretary. Nobody will pressure you; if anything is making it hard, tell your mentor or the Almoner.", after=2)
c.box(["**Taylor’s or Emulation?** The two main workings in Hertfordshire. Emulation is the more relaxed; Taylor’s has more floorwork. Learned one and asked to work in the other? Ask first."])
c.foot()
c.side_title("New Masons Evening · Card 2 of 3", "Visiting, and the questions you asked", new_page=True)
c.h("Can I visit other Lodges?")
c.body("Yes, and it is encouraged. Contact the Lodge Secretary, introduce yourself, and expect to reply to the Visitors’ Toast. Go with your mentor the first time. Lodges work differently; observe before judging, and never criticise another Lodge’s working.", after=3)
c.two([
    ["What do I tell people at work?", "The truth: you have joined a Lodge, you meet a few times a year, there is a dinner, and it raises a lot for charity."],
    ["Can I post about it online?", "Yes, with judgement. The Festive Board and charity events, fine; anything from inside the Lodge room, not."],
    ["Can my partner get involved?", "Yes. White Table evenings invite partners to dine; Ladies Night is the Master’s formal dinner each year."],
    ["When will I take office?", "When you are ready and if you want to. Nobody should push you early, and nobody should leave you waiting. Talk to your mentor."],
    ["What is the Royal Arch?", "The completion of Pure Antient Masonry. Your Lodge’s Royal Arch Representative will explain it when you are ready. Information, not recruitment."],
    ["Can I attend Provincial Grand Lodge?", "Once you are a Master Mason."],
], widths=[2200, BODY - 2200], size=9)
c.box(["**If you are struggling, say so, early, to anyone:** your mentor, the Almoner, the Club. Money, time, family, confidence. The question is always “How can we help?”, never “Why haven’t you been attending?”."], fill=PALETEAL)
c.h("Three things to do this week")
c.bl(["Join the Fleet House Light Blues Club: fhlbc.co.uk/join-us.", "Sign up to Solomon: solomon.ugle.org.uk. Start with Welcome Apprentice.", "Message your mentor with one thing from tonight you want to talk about."])
c.foot()
print("saved", c.save())


# ======================= CARD 3: WORDS AND LETTERS =======================
WORDS = [
    ["Lodge", "The basic unit: Freemasons who meet together, with a name and a number. Elects a Master and officers each year."],
    ["Province", "The Lodges of a county area under a Provincial Grand Master. Above the Province is Grand Lodge."],
    ["UGLE", "The United Grand Lodge of England, Freemasons’ Hall, London: the governing body for English Freemasonry."],
    ["Summons", "The notice of a meeting: date, time, dress, business, and who is doing what. Read it."],
    ["Festive Board", "The meal after the meeting. Toasts, Masonic Fire, speeches; where friendships are made."],
    ["Masonic Fire", "The applause that follows a toast. Your mentor will show you; nobody expects you to know it."],
    ["Lodge of Instruction", "The rehearsal, usually informal, run by the Preceptor. Where you learn what you saw."],
    ["Installation", "The yearly meeting at which the new Master is installed and appoints his officers."],
    ["Initiation, Passing, Raising", "The three ceremonies that make you an Entered Apprentice, a Fellow Craft and a Master Mason."],
    ["Apron", "White for an Entered Apprentice, then light blue, then dark blue for Provincial or Grand rank. Hence “light blue”."],
    ["Regalia, jewels", "Apron, collar for officers, gloves. Jewels are the medals worn on the breast."],
    ["Visiting", "Attending another Lodge’s meeting as a guest. Encouraged from the start."],
    ["Risings", "The three points near the end of a meeting when the Master rises to ask for communications and apologies."],
    ["Royal Arch, Chapter", "The completion of Pure Antient Masonry. A Chapter is to the Royal Arch what a Lodge is to the Craft."],
    ["Proposer, Seconder", "The two members who put your name forward."],
    ["White Table, Ladies Night", "A dinner to which partners are invited; the Master’s formal dinner each year."],
]
LETTERS = [
    ["WM, IPM", "Worshipful Master; Immediate Past Master, who has just left the Chair."],
    ["SW, JW", "Senior and Junior Warden: with the Master, the three principal officers."],
    ["SD, JD, IG", "Senior Deacon, Junior Deacon, Inner Guard: the floor officers."],
    ["DC, ADC", "Director of Ceremonies and his Assistant. Follow the DC."],
    ["Tyler", "The officer outside the door; the first person you met on your Initiation night."],
    ["Bro, W Bro, VW Bro, RW Bro", "Brother; Worshipful Brother (has been Master); Very and Right Worshipful for senior Grand rank."],
    ["EA, FC, MM", "Entered Apprentice, Fellow Craft, Master Mason."],
    ["PM", "Past Master; in Hertfordshire mentoring documents also the Personal Mentor."],
    ["LM", "Lodge Mentor: co-ordinates mentoring and makes sure every new member has a Personal Mentor."],
    ["ProvGM, DepProvGM, APGM", "Provincial Grand Master, his Deputy, and the Assistant Provincial Grand Masters."],
    ["ProvGMen, APGMen", "Provincial Grand Mentor and the Assistant Provincial Grand Mentors."],
    ["VO", "Visiting Officer: visits your Lodge on the Provincial Grand Master’s behalf. A friend, not an inspector."],
    ["LoI, CoI", "Lodge of Instruction; Chapter of Instruction."],
    ["PGL, GL", "Provincial Grand Lodge; Grand Lodge. PProvSGW, PAGDC and the like are Past Provincial or Grand ranks."],
    ["FHLBC, DAWG", "Fleet House Light Blues Club; the Daily Advancement WhatsApp Group."],
    ["Solomon, Hermes", "UGLE’s learning platform; UGLE’s membership administration system."],
]
c = Card(os.path.join(out_dir, "New Masons Evening Card 3 Issue 1 Draft.docx"), "New Masons Evening · Card 3")
c.side_title("New Masons Evening · Card 3 of 3", "Words you will hear")
c.two(WORDS, widths=[1900, BODY - 1900], size=8)
c.foot()
c.side_title("New Masons Evening · Card 3 of 3", "Letters you will see", new_page=True)
c.two(LETTERS, widths=[2000, BODY - 2000], size=8)
c.body("Nobody minds being asked what their letters mean. Ask.", after=0)
c.foot()
print("saved", c.save())
