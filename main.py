"""
calisthenics(
LOGDATE DATE NOT NULL,
PUSHUPS INT NOT NULL,
PULLUPS INT NOT NULL,
SQUATS  INT NOT NULL,
COMMENTS VARCHAR(50) NULL,
RATING DECIMAL(1,1) NOT NULL,
PRIMARY KEY (LOGDATE));
"""

import sqlite3

conn = sqlite3.connect('log.db')

cur = conn.cursor()
cur.execute("SELECT * FROM calisthenics")

sqlite_insert_with_param = """INSERT INTO 'calisthenics' 
('LOGDATE', 'PUSHUPS', 'PULLUPS') values (?, ?, ?, ?, ? ,?)"""

cur.execute("""INSERT INTO calisthenics values (?, ?, ?, ?, ? ,?)""", )

rows = cur.fetchall()

for row in rows:
	print(row)

