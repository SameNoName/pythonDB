import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>Add medication</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

if 'medicationname' in form and 'company' in form and 'date' in form and 'enddate' in form and 'type' in form and 'count' in form and 'ill' in form:
    name1 = form['medicationname'].value
    company1 = form['company'].value
    date = form['date'].value
    enddate = form['enddate'].value
    type1 = form['type'].value
    count1 = form['count'].value
    ill = form['ill'].value
    cur.execute('SELECT id, namei FROM ills WHERE namei ==?',
    [ill])
    row = cur.fetchone()
    if row:
        (id, namei) = row
        cur.execute('INSERT INTO medications(name, company, date, enddate, type, count, i) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (name1, company1, date, enddate, type1, count1, id))
        conn.commit()
        conn.close()
        text = '<b>' + name1 + '</b> added.'
        print(html % text)
    else:
        print(html % 'Error. Could not find ill.')
else:
    print(html % 'Error. Not all fields are filled.')