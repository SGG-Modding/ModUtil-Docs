START = "<table><tr><td>\n\t"
END = "\n</td></tr></table>"
ROW = "\n</td></tr><tr><td>\n\t"
ROWSEP = "\n</td></tr></table><table><tr><td>\n\t"
COL = "\n</td><td>\n\t"
COLSEP = "\n</td><td colspan=\"2\">\n\t"
SEP = ">>> "
SKIP = "----"
ANCHORCHR = "#"
ANCHOR = """<a id="user-content-{1}" href="#{1}" aria-hidden="true">{0}</a>"""

import re
import os

def get_anchor( s ):
    clean = re.sub(r"[^A-Za-z0-9\-]","",s.replace(" ","-").lower( ))
    return ANCHOR.format(s,clean)

def rep_code( s ):
    return re.sub(r"`(.*?)`",r"<code>\1</code>",s)

def table( txt ):
    txt = rep_code( txt )
    t = list(map(lambda x: x.split("\n"), txt.split("\n\n")))
    for r in t:
        c = r[0]
        if c[0] == ANCHORCHR:
            r[0] = get_anchor(c[1:])
    return START+ROW.join(map(lambda r: COL.join(r).replace(SKIP,"").replace(COL+SEP,COLSEP), t)).replace(ROW+SEP,ROWSEP)+END
    
def printtable( filename ):
    with open(filename) as file:
        print(table(file.read()))

def qp( name ):
    printtable( "txts/"+name+".txt" )

def relay( ):
    for entry in os.scandir("txts"):
        data = ""
        with open("txts/"+entry.name) as infile:
            data = table(infile.read())
        with open("out/"+entry.name,'w') as outfile:
            outfile.write(data)

if __name__ == "__main__":
    relay( )
