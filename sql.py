import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

# cur.execute("""
# 					CREATE TABLE cache
# 					(
# 						path text,
# 						dirty integer,
# 						mtime integer
# 					)
# 	""")

# cur.execute("""
# 					INSERT INTO cache VALUES ('tmp/file1',0,130133030)
# 	""")

cur.execute("""
					SELECT * FROM cache
	""")

print(cur.fetchone())

conn.commit()

conn.close()

