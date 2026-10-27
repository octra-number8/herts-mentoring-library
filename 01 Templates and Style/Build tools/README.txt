BUILD TOOLS - Hertfordshire Mentoring documents (10 October 2026)

The template Hertfordshire Mentoring Document.docx / .dotx in the folder above is
the settled brand: white first-page header with the shield top right, four-colour
principle strip (Prepare, Guide, Support, Enlighten), slim blue band on following
pages, DM Sans throughout.

Start new documents from the .dotx in Word, or build them in code with python-docx
from the .docx. The scripts here are the ones used to produce the template and the
first guide (B2a):

  build pm guide.py   builds B2a Personal Mentor's Short Guide from the template
                      (python-docx; styles, tables, panels, numbered H1 blocks)
  white band.py       turns the first-page blue band white (already applied in the
                      template; keep for re-processing older files)
  header shield.py    places the shield in the first-page header, right-hand cell
  insert shield.py    older: puts the shield in the band's white tile (superseded)
  PGLH Shield header.png  520 px shield used for embedding (keeps files small)

File names: spaces between words, never hyphens or underscores.

Rules of thumb when building:
  - Section-number blocks in Heading 1 are all deep blue #003668; the four
    principle colours are reserved for the principles themselves.
  - Quote the principles verbatim from A1; order Prepare, Guide, Support, Enlighten.
  - Contact block and copyright line per A3 Style, Terminology and Data Guide.
