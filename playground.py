#playground
import os
import time
def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

def writing():
    with open("dir/sample","a") as f:
        text = str(time.time_ns())
        f.write(text)

if __name__ == '__main__':
    writing()
