# main.py
# python-mini-projects @Ravi Chavare

from lxml import html
import sys
import requests
from pprint import pprint


def main(username):
    url = "https://www.instagram.com/{}/?hl=en".format(username)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[starts-with(@name,"description")]/@content')
    pprint(data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("[!] - Usage: python main.py {username}")