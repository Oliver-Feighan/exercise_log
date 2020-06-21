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
import datetime

connection = sqlite3.connect('log.db')

cursor = connection.cursor()

sqlite_insert_with_param = """INSERT INTO 'calisthenics' 
("LOGDATE", "PUSHUPS", "PULLUPS", "SQUATS", "COMMENTS", "RATING") values (?, ?, ?, ?, ? ,?)"""

data = (datetime.datetime.now(), 0, 0, 0, "went for swim", "NULL")

cursor.execute("""INSERT INTO calisthenics values (?, ?, ?, ?, ? ,?)""", data)

connection.commit()

connection.close()