import sqlite3

conn = sqlite3.connect('log.db')

cur = conn.cursor()
cur.execute("SELECT * FROM calisthenics")

rows = cur.fetchall()

for row in rows:
	print(row)
