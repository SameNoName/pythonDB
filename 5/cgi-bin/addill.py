import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>Add ill</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

if 'illname' in form and 'group' in form:
    name = form['illname'].value
    group = form['group'].value
    cur.execute('INSERT INTO ills(namei, grp) VALUES (?, ?)',
    (name, group))
    conn.commit()
    conn.close()
    text = '<b>' + name + '</b> added.'
    print(html % text)
else:
    print(html % 'Error. Not all fields are filled.')