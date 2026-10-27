"""A1 The Hertfordshire Mentoring Principles: the one-page canon on the template. Text verbatim from Issue 1 (July 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from hmdocx import Builder, DEEP, DARK, TEAL, PALE, PALETEAL, PRINCIPLE_DEFS
template, out = sys.argv[1], sys.argv[2]
b = Builder(template, out, doc_title="The Hertfordshire Mentoring Principles")
b.doc.styles["Normal"].font.size = __import__("docx.shared", fromlist=["Pt"]).Pt(9.5)
b.para("Canon · A1", style="DocumentType")
tp = b.para("The Hertfordshire Mentoring Principles", style="Title", after=4)
for r in tp.runs: r.font.size = __import__("docx.shared", fromlist=["Pt"]).Pt(24)
b.panel(["*“Every member, in every Lodge, experiences Freemasonry as welcoming, supportive, engaging, and personally rewarding.”*"], fill=PALE, bar=DEEP)
b.para("Mentoring in Hertfordshire is a culture, not a programme. It supports a Brother from his first enquiry into Freemasonry through every stage of his Masonic journey - properly prepared, thoughtfully guided, actively supported, and continuously enlightened - so that no Brother walks alone.", after=4)
b.table([
    ["PREPARE", "Ensuring members are ready for each stage of their Masonic journey. This begins before interview and continues through practical preparation for ceremonies, office, and progression - ensuring members understand what to expect before it happens. There should never be any surprises."],
    ["GUIDE", "Providing accurate, clear, and timely information and support. Good guidance is honest and grounded in authoritative sources. It dispels myths, answers questions openly, and helps members navigate an unfamiliar world with confidence - without creating dependency."],
    ["SUPPORT", "Being present, responsive, and compassionate throughout. Support is not only practical; it is relational. Members who feel cared for and valued are far more likely to remain engaged and committed. The question is always “How can we help?” - never “Why aren't you attending?”"],
    ["ENLIGHTEN", "Deepening understanding, curiosity, and enjoyment of Freemasonry. Mentoring does not end with the Third Degree; it is a lifelong opportunity to help Brethren appreciate Freemasonry - its purpose, traditions and meaning - rather than simply learn information."],
], [1800, 7612])
b.para("**These four principles are not sequential stages.** They apply continuously and simultaneously throughout a member's journey - from applicant to Entered Apprentice, through each degree, into the Royal Arch, into office, through the Chair and beyond it.", after=3)
b.para("The Lodge Mentor co-ordinates; the Personal Mentor accompanies; but the responsibility belongs to every member of every Lodge. *“We are all mentors to others in Freemasonry.”*", after=3)
b.panel(["*Freemasonry must be fun. A man who is enjoying himself attends; a man who attends participates; a man who participates belongs; and a man who belongs does not resign.*"], fill=PALETEAL, bar=TEAL)
b.para("**Status of this document.** This page is the canonical statement of the Hertfordshire Mentoring Principles. Every mentoring document produced by the Province quotes the principles, their order and their definitions from this page verbatim, and does not restate them. Changes are made here first, by decision of the Provincial Grand Mentor, and flow outward at each document's next issue. *Issue 1, July 2026; Issue 1a, October 2026, on the Provincial template, text unchanged.*", size=9, after=0)
print("saved", b.save())
