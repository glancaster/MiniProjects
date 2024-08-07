# main.py
# python-mini-projects @Mitesh and @Michael Mba

import requests
from bs4 import BeautifulSoup 
import sys
from pprint import pprint

def main(url):
    if ("https" or "http") in url:
        data = requests.get(url)
    else:
        data = requests.get("https://" + url)

    soup = BeautifulSoup(data.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))

    pprint(links)
    # You can append or write this data to a file with open(file, "w") as f:  f.write(links)




if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print("[!] - Usage: python main.py {url}")