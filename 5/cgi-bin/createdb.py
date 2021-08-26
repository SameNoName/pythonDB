import sqlite3

conn = sqlite3.connect('med')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS medications')
cur.execute('DROP TABLE IF EXISTS ills')
cur.execute('PRAGMA FOREIGN_KEYS=ON')
sql = '''CREATE TABLE ills (id INTEGER PRIMARY KEY NOT NULL,
namei TEXT,
grp TEXT)'''
cur.execute(sql)
sql = '''CREATE TABLE medications (medication_id INTEGER PRIMARY KEY NOT NULL, 
name TEXT, 
company TEXT, 
date TEXT,
enddate TEXT,
type TEXT,
count INTEGER,
i INTEGER,
FOREIGN KEY(i) REFERENCES ills(id))'''
cur.execute(sql)
conn.commit()
conn.close()

text = 'Tables created'

html = '''Content-type: text/html

<HTML>
<BODY>
%s
</BODY>
</HTML>
'''
print(html %text)