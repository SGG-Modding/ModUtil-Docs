START = "<table><tr><td>\n\t"
END = "\n</td></tr></table>"
ROW = "\n</td></tr><tr><td>\n\t"
ROWSEP = "\n</td></tr></table><table><tr><td>\n\t"
COL = "\n</td><td>\n\t"
COLSEP = "\n</td><td colspan=\"2\">\n\t"
SEP = ">>> "
SKIP = "----"

import re

def rep_code( s ):
    return re.sub(r"`(.*?)`",r"<code>\1</code>",s)

def table( txt ):
    txt = rep_code( txt )
    t = map(lambda x: x.split("\n"), txt.split("\n\n"))
    return START+ROW.join(map(lambda r: COL.join(r).replace(SKIP,"").replace(COL+SEP,COLSEP), t)).replace(ROW+SEP,ROWSEP)+END
    
def printtable( filename ):
    with open(filename) as file:
        print(table(file.read()))

def qp( name ):
    printtable( "txts/"+name+".txt" )
