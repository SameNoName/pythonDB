import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>Delete medication</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

if 'med' in form:
    name1 = form['med'].value
    cur.execute('DELETE FROM medications WHERE name ==?',
    [name1])
    conn.commit()
    conn.close()
    print(html % 'Medication has deleted')   
else:
    print(html % 'Error. Not all fields are filled.')