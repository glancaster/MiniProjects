# main.py
# python-mini-project @Mitesh

import os
import sys

def main(string,dir=os.curdir):
    files = os.listdir(os.chdir(dir))
    for item in files:
        path = os.path.abspath(item)
        if os.path.isdir(path):
            main(string,dir = path)
        if os.path.isfile(path):
            with open(path) as f:
                if string in f.read():
                    print(string, "Found in:", path)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("[!] - Usage: python main.py {search string}")
