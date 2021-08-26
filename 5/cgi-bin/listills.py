import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>List ills</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

cur.execute('SELECT namei, grp FROM ills')
text = ''
for (namei, grp) in cur.fetchall():
    text = text + '<P>' + namei + ' ' + grp
print(html % text)