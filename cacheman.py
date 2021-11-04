import sqlite3
import os
import time 
import shutil
import logging

cache_path = '/home/yonde/Documents/pt_sshfs_py/tmp'

def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def main():
	log = logging.getLogger(__name__)

	conn = sqlite3.connect("cache.db")

	cur = conn.cursor()

	while(True):
		size = get_dir_size("tmp")
		while(size > 1e+8):
			#old mtime file delete
			cur.execute("SELECT * FROM cache WHERE mtime = (SELECT MIN(mtime) FROM cache WHERE fd = 0)")
			row = cur.fetchone()
			if row:
				path = os.path.join(cache_path,row[0])
				try:
					log.warning("delete %s",path)
					os.remove(path)
				except:
					time.sleep(10)
					continue
				cur.execute("DELETE FROM cache WHERE path = ?",(row[0],))
				conn.commit()
			size = get_dir_size("tmp")
		time.sleep(10)

	conn.close()


if __name__ == '__main__':
	main()
