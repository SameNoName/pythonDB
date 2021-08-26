import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>Delete ill</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

if 'ill' in form:
    ill = form['ill'].value
    cur.execute('DELETE FROM ills WHERE namei ==?',
    [ill])
    conn.commit()
    conn.close()
    print(html % 'Ill has deleted')   
else:
    print(html % 'Error. Not all fields are filled.')