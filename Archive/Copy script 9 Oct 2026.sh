#!/bin/bash
# Copy mentoring documents from the Google Drive folder into the tiered library.
# Copies only; nothing in the source is touched.
S="$HOME/mnt/Mentoring"
D="$HOME/mnt/Herts Mentoring"
log="$D/Archive/copy-log-2026-10-09.txt"
: > "$log"
c() { # c <dest-subfolder> <source-relative-path>...
  dest="$D/$1"; shift
  mkdir -p "$dest"
  for f in "$@"; do
    if [ -e "$S/$f" ]; then cp -p "$S/$f" "$dest/" && echo "OK  $f  ->  $1" >> "$log"
    else echo "MISSING  $f" >> "$log"; fi
  done
}

# ---------- 00 Governance ----------
c "00 Governance" \
  "Framework Development/Master Framework and Library Architecture - Issue 1a - July 2026.docx" \
  "Framework Development/Knowledge Base Analysis - Issue 1a - July 2026.docx" \
  "Framework Development/Corrections Register - Issue 1 - July 2026.docx"
c "00 Governance/Strategy working papers" \
  "Strategy Plan/Pgm Hertfordshire – Vision & Aims (one‑page Summary)-2.docx" \
  "Strategy Plan/Provincial Level.docx" \
  "Strategy Plan/Engaging Mentors.docx" \
  "Mentoring/Progession Planning/5 year planning.docx"
c "00 Governance/Meetings and correspondence" \
  "MM Agenda 05.08.2025 v1.docx" \
  "MM Agenda 05.08.2025 v1.pdf" \
  "Email 29th July 2026.docx" \
  "Mark Butcher/email to secretaries v1.docx" \
  "Mark Butcher/email to VO's v2.docx" \
  "Mentor Awards 2026/Notes - 30th July 2026.docx"
c "00 Governance/Mentoring Lodge proposal" \
  "Mentoring Lodge/Repurposing-Proposal-Mentor Lodge September 2026.docx" \
  "Mentoring Lodge/Special-Interest-Themed-Lodge-Process.docx"
c "Archive/Superseded Issues/Mentoring Lodge proposal" \
  "Mentoring Lodge/Repurposing-Proposal-Document.docx" \
  "Mentoring Lodge/Repurposing-Proposal-Document v2.docx" \
  "Mentoring Lodge/Repurposing-Proposal-Mentor Lodge August 2026.docx"

# ---------- A Canon ----------
c "A Canon" \
  "Framework Development/A1 - The Hertfordshire Mentoring Principles - Issue 1 - July 2026.docx" \
  "Framework Development/A3 - Style Terminology and Data Guide - Issue 1 Draft - July 2026.docx" \
  "Mentoring Framework/Mentoring Framework 2026 v3.1.docx" \
  "Mentoring Framework/Mentoring Framework 2026 v3.1.pdf"
c "A Canon/A1 Guiding Principles artwork" \
  "Mentoring/Guiding Principles/Guiding Principles of Mentoring v2 colour.pdf" \
  "Mentoring/Guiding Principles/Guiding Principles of Mentoring v.2 printable.pdf"
c "Archive/Superseded Issues/A2 Provincial Mentoring Framework" \
  "Mentoring Framework/Mentoring Framework 2026 v2.1.docx" \
  "Mentoring Framework/Mentoring Framework 2026 v2.1.pdf" \
  "Mentoring Framework/Mentoring Framework 2026 v2.2.docx" \
  "Mentoring Framework/Mentoring Framework 2026 v2.2.pdf" \
  "Mentoring Framework/Mentoring Framework 2026 v2.2a.docx" \
  "Mentoring Framework/Mentoring Framework 2026 v2.2a.pdf" \
  "Mentoring Framework/Hertfordshire_Mentoring_Strategy_v3.docx" \
  "Strategy Plan/Mentoring in Hertfordshire - Strategic Plan.docx" \
  "Strategy Plan/Mentoring in Hertfordshire - Strategic Plan.pdf" \
  "Strategy Plan/Mentoring in Hertfordshire - Strategic Plan 2.1.docx" \
  "Strategy Plan/Mentoring in Hertfordshire - Strategic Plan 2.1.pdf"
c "Archive/Superseded Issues/A1 Guiding Principles artwork" \
  "Mentoring/Guiding Principles of Mentoring.pdf" \
  "Mentoring/Guiding Principles of Mentoring v2.pdf" \
  "Mentoring/Guiding Principles/Guiding Principles of Mentoring.pdf" \
  "Mentoring/Guiding Principles/Guiding Principles of Mentoring 2.pdf" \
  "Mentoring/Guiding Principles/Guiding Principles of Mentoring 2a.pdf"

# ---------- B Practitioner Handbooks ----------
c "B Practitioner Handbooks" \
  "Mentoring Framework/Lodge-Mentors-Guide-Issue2-Sept2026.docx" \
  "Framework Development/Personal Mentors Guide - Issue 1a (aligned) - July 2026.docx" \
  "Framework Development/B6 - Retention Retrieval and Migration Guide - Issue 1 Draft - July 2026.docx" \
  "Mentoring/Role of the Lodge Mentor.pdf"
c "B Practitioner Handbooks/Leaflets" \
  "Mentoring/Individual Mentors/Individual Mentors v3.pdf" \
  "Mentoring/Individual Mentors/Individual Mentors v3 print.pdf"
c "Archive/Superseded Issues/B1 Lodge Mentors Guide" \
  "Mentoring Guide/Lodge-Mentors-Guide-Hertfordshire.docx"
c "Archive/Superseded Issues/B2 Personal Mentors Guide" \
  "Mentoring Guide/Personal-Mentors-Guide-Hertfordshire.docx"
c "Archive/Superseded Issues/Leaflets" \
  "Mentoring/Individual Mentors/Individual Mentors.pdf" \
  "Mentoring/Individual Mentors/Individual Mentors v2.pdf" \
  "Mentoring/Individual Mentors/Individual Mentors v2a.pdf" \
  "Mentoring/Individual Mentors/Individual Mentors v2a colour.pdf" \
  "Mentoring/Individual Mentors/Individual Mentors v2a printable.pdf" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v1.pdf" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v2.pdf" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v2a.pdf" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v2 colour.pdf" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v2 printable.pdf" \
  "Mentoring/1st Degree - Initiate/1st Degree Initiates.pdf" \
  "Mentoring/2nd Degree/2nd Degree visual.pdf"

# ---------- C Member Guides ----------
c "C Member Guides" \
  "Framework Development/C1 - Considering Freemasonry - Issue 1 Draft - July 2026.docx" \
  "Framework Development/C2 - New Brothers Guide - Issue 1 Draft - July 2026.docx"
c "C Member Guides/Leaflets" \
  "Mentoring/Mentoring Candidates/Mentoring candidates v3.pdf" \
  "Mentoring/1st Degree - Initiate/1st Degree Initiates v2.pdf" \
  "Mentoring/2nd Degree/2nd Degree.pdf"
c "C Member Guides/Welcome letter" \
  "Mentoring/Welcome Letter/Mentoring Letter.pdf" \
  "Mentoring/Welcome Letter/Page 1.pdf" \
  "Mentoring/Welcome Letter/Page 2.pdf"

# ---------- D Tools and Checklists ----------
c "D Tools and Checklists" \
  "Framework Development/D2 - Mentor Meeting Guide - Issue 1 Draft - July 2026.docx" \
  "Framework Development/D3 - Stage Checklists - Issue 1 Draft - July 2026.docx" \
  "Framework Development/D4 - Warning Signs Card - Issue 1 Draft - July 2026.docx" \
  "Mentoring Guide/Personal-Mentoring-Plan-Hertfordshire.docx" \
  "Mentors Jewel/Mentors Jewel.docx"

# ---------- E Training and Development ----------
c "E Training and Development" \
  "Framework Development/E1 - Lodge Mentor Induction and Charge - Issue 1 Draft - July 2026.docx" \
  "Framework Development/E2 - Personal Mentor Workshop - Issue 1 Draft - July 2026.docx"
c "E Training and Development/E5 Ceremony Explained - source material" \
  "Progression in the Craft/Progression in The Craft.docx" \
  "Progression in the Craft/First Degree Explanation 24 Jan 2025 Lodge Presentation (1).pdf" \
  "Mentoring/1st Degree Tracing Board/Paper and Presentation - First Degree Tracing Board in Modern English.pdf" \
  "Mentoring/1st Degree Tracing Board/28th August - 1st degree tracing board v2.pdf" \
  "Mentoring/1st Degree Tracing Board/1st Degree.odt" \
  "Fish and Chips/First Degree Tracing Board.pdf"

# ---------- F Culture and Communications ----------
c "F Culture and Communications/F1 In That Order (book)" \
  "In That Order - Book/In That Order - Draft 2 - 28.03.2026.docx" \
  "In That Order - Book/In That Order - Draft 2 - 28.03.2026.pdf"
c "Archive/Superseded Issues/F1 In That Order" \
  "In That Order - Book/in_that_order_v2-2.docx"
c "F Culture and Communications/F2 Articles and Newsletters" \
  "Posting Schedule/Prov News Posting Schedule.docx"
c "F Culture and Communications/F3 Lodge Presentations" \
  "Framework Development/F3 - Mentoring Lodge Presentation - Issue 1 Draft - July 2026.pptx" \
  "Mentoring Framework/Hertfordshire_Mentoring_Framework_2026.pptx" \
  "Mentoring Framework/Hertfordshire_Mentoring_Framework_2026.pdf"
c "F Culture and Communications/F4 Events and Awards/Mentor Awards 2026" \
  "Mentor Awards 2026/Mentoring Awards - Video Plan 2026 v2.1.docx" \
  "Mentor Awards 2026/Mentoring Awards - Video Plan 2026 v2.1.pdf" \
  "Mentor Awards 2026/Dear Brother.docx" \
  "Mentor Awards 2026/Enlighten.docx" \
  "Mentor Awards 2026/Awards Nominations.xlsx" \
  "Menu/A5 Booklet Mentoring.pdf" \
  "Menu/Masonic Mentoring Awards crib sheet.docx" \
  "Menu/speaking crib sheet.docx" \
  "Menu/Briefing Note for Neil C.docx" \
  "Menu/Mentoring Handout Page1.pdf" \
  "Menu/Mentoring Handout Page2.pdf" \
  "Menu/Mentoring Handout Page3 v3.pdf" \
  "Menu/Mentoring Handout Page4.pdf"
c "F Culture and Communications/F4 Events and Awards/New Masons Evenings" \
  "Fish and Chips/1st Degree Tracing Board in Modern English.pdf"
c "F Culture and Communications/F4 Events and Awards" \
  "Masonic Walk.docx"

# ---------- Source Material ----------
c "Source Material/UGLE/Building Together modules" \
  "Reference Documents/UGLE/Complete Set Combined.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_1_Fun_and_enjoyment.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_1a_Freemasonry_standards_and_values.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_2_Guided_Learning.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_2a_Learning_Ritual.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_3_Personal_Learning.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_3a_Local_mentoring_structures.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_4_Introduction_to_the_Royal Arch.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_5_Managing_Migration.pdf" \
  "Reference Documents/UGLE/ENGAGE_Continued_Learning_and_Development_5a_Migration_Flow_Chart_(pre-Hermes).pdf" \
  "Reference Documents/UGLE/ENGAGE_Support_the_New_Member_1_Understanding.pdf" \
  "Reference Documents/UGLE/ENGAGE_Support_the_New_Member_2_Participation.pdf" \
  "Reference Documents/UGLE/ENGAGE_Support_the_New_Member_3_Stewardship.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Re-engaging_Inactive_Members_1_Tracking_attendance_and_apologies.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Re-engaging_Inactive_Members_2_Engage_with_non-attending_members.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Re-engaging_Inactive_Members_2a_Resignation_the_opportunity_to_reconsider.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Understand_reasons_for_losses_1_Unattached_Freemasons.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Understand_reasons_for_losses_1a_Rules_governing_attendance_by_Unattached_Freemasons.pdf" \
  "Reference Documents/UGLE/RETRIEVE_Understand_reasons_for_losses_3_Lessons_learned_from_losses.pdf" \
  "Reference Documents/Met/Letter to Lodge Mentor (UGLE).pdf"
c "Source Material/UGLE/Building Together Conference Sept 2025" \
  "September Conference/Presentations/1. Presentation Morning Session/Building Together September  2025 Morning Session for distribution.pdf" \
  "September Conference/Presentations/2. Afternoon 1st Break Out/Shape Attract afternoon sessoin 1 Building Together September  2025.pdf" \
  "September Conference/Presentations/3. Afternoon 2nd Breakout/Sessions 1 and 2 Building Together September Conference L&D_Mentors_Conferences_2025.pdf" \
  "September Conference/Presentations/3. Afternoon 2nd Breakout/Continue afternoon sessoin 2 Building Together September  2025.pptx" \
  "September Conference/Presentations/4. Final Afternoon Session/Final Session sindlesham Building Together September  2025.pdf" \
  "September Conference/Final Version V2 Logos/Building Together Logo Grid.pdf" \
  "September Conference/Yes if Not No Because icon artwork/Yes if...not no because illustration v3.pdf"
c "Source Material/Hertfordshire Provincial Office/Officer guides" \
  "Other position guidance/Almoners-Guide.pdf" \
  "Other position guidance/Charity-Stewards-Guide-V6.pdf" \
  "Other position guidance/Lodge-Director-of-Ceremonies-Oct-2025-2.pdf" \
  "Other position guidance/PGLH-Lodge-Treasurers-Guide-February-2026-Issue-1.pdf" \
  "Other position guidance/PGLH-Secretaries-Handbook-Jan-2026.pdf"
c "Source Material/Hertfordshire Provincial Office/Visiting Officers" \
  "Mark Butcher/Inspectorate Strategy v2.pdf" \
  "Mark Butcher/Inspectorate Strategy.docx" \
  "Mark Butcher/VO Review Jan 26[38]  -  Read-Only.pptx"
c "Source Material/Other Provinces/Devonshire" "Reference Documents/Devonshire/Lodge-Mentor-booklet-v1.2.pdf"
c "Source Material/Other Provinces/East Lancashire" \
  "Reference Documents/East Lancashire/15-PGLEL-Mentoring-Personal-Guide-ENTERED-APPRENTICE-v1-01F-1.pdf" \
  "Reference Documents/East Lancashire/19-PGLEL-Mentoring-Handbook-V1-01F.pdf"
c "Source Material/Other Provinces/Metropolitan" \
  "Reference Documents/Met/Advice for the Delivery of Mentoring to Experienced Masons.pdf" \
  "Reference Documents/Met/Mentor’s Guide to ENGAGE Support.pdf" \
  "Reference Documents/Met/MetGL MetGC - Mentor's Handbook v2.0 - 01 September 2025.pdf" \
  "Reference Documents/Met/Personal Mentoring Guide.pdf" \
  "Reference Documents/Met/Personal Mentoring Plan V6-0-1 Editable.pdf" \
  "Mentoring/Festive Board/Harlesden Lodge 2098 Etiquette.pdf"
c "Source Material/Other Provinces/Sussex" "Reference Documents/Sussex/Personal-Mentors-Handbook.pdf"
c "Source Material/Other Provinces/West Lancashire" "Reference Documents/West Lancashire/mentors-guide-v7.pdf"
c "Source Material/Other Provinces/Wiltshire" "Reference Documents/Wiltshire/1691590752pathway-guidance-for-the-mentor-230628.pdf"

# ---------- Working Drafts / Archive Reports ----------
c "Working Drafts/2026 Mentors Report" \
  "Annual Report/2026 Mentors Report v1.docx" \
  "Annual Report/2026 Mentors Report v1.2.docx" \
  "Framework Development/2026 Mentors Report - Draft - July 2026.docx"
c "Archive/Reports" "Annual Report/12. 2024 Mentors Report - Revised.docx"

echo "---- summary ----"
grep -c '^OK' "$log"; grep '^MISSING' "$log" || echo "no missing"
