"""Turn the first-page blue identity band white: text in deep blue/dark blue/teal, principle strip kept."""
import sys, zipfile, re
src, out = sys.argv[1], sys.argv[2]

def patch_header1(t):
    # the band rows: every 003668 fill except the strip's first cell -> white.
    # Strip row is the last <w:tr>; protect it.
    head, strip = t.rsplit("<w:tr>", 1)
    head = head.replace('w:fill="003668"', 'w:fill="FFFFFF"')
    # text colours on the now-white band
    head = head.replace('<w:color w:val="FFFFFF"/>', '<w:color w:val="003668"/>')
    head = head.replace('<w:color w:val="BFD6EA"/>', '<w:color w:val="06345D"/>')
    head = head.replace('<w:color w:val="8FD3D1"/>', '<w:color w:val="157A7C"/>')
    # top spacer row: shrink it so the title block sits near the top edge but keeps a margin
    head = re.sub(r'(<w:trHeight w:val=")454(" w:hRule="exact"/>)', r'\g<1>340\2', head, count=1)
    return head + "<w:tr>" + strip

zi = zipfile.ZipFile(src); zo = zipfile.ZipFile(out + ".tmp", "w", zipfile.ZIP_DEFLATED)
for it in zi.infolist():
    d = zi.read(it.filename)
    if it.filename == "word/header1.xml":
        d = patch_header1(d.decode("utf-8")).encode("utf-8")
    zo.writestr(it, d)
zo.close(); zi.close()
import os; os.replace(out + ".tmp", out)
print("white band ->", out)
