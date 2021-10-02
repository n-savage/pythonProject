# Basic scraper
# import libraries
import urllib3
from bs4 import BeautifulSoup


def main(name):
    print(f'Checking page; {name}')
    http = urllib3.PoolManager()
    r = http.request('GET', name)
    soup = BeautifulSoup(r.data, "html.parser")
    print(soup.text)


if __name__ == '__main__':
    main("https://www.google.co.uk")


