import cgi
import sqlite3

html = """Content-type: text/html

<HTML>
<BODY>
    <H1>List medications</H1>
    <P>
    %s
</BODY>
</HTML>
"""

conn = sqlite3.connect('med')
cur = conn.cursor()

form = cgi.FieldStorage()

cur.execute('SELECT medications.name, medications.company, medications.date, medications.enddate, medications.type, medications.count, ills.namei FROM medications, ills WHERE medications.i == ills.id')
text = ''
for (name, company, date, enddate, type, count, namei) in cur.fetchall():
    text = text + '<P>' + name + ' : ' + company + ', date of manufacture: ' + str(date) + ', shelf life ' + str(enddate) + ', type ' + type + ', Number of packages ' + str(count) + ', ill ' + namei
print(html % text)