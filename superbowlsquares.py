__author__ = 'will'

from bs4 import BeautifulSoup
import requests

main = "http://www.pro-football-reference.com/super-bowl/"
pfr = "http://www.pro-football-reference.com"
r = requests.get(main)
data = r.text
soup = BeautifulSoup(data)

def parse_box_score(url):
    r= requests.get(url).text
    s = BeautifulSoup(r)
    for e in s.contents:
        print e.name

    next_ = s.find_next_siblings()
    print next_







box_scores = []
for link in soup.find_all('a'):
    boxscore_link = link.get("href")
    if 'boxscore' in boxscore_link:
        box_scores.append(pfr + boxscore_link)
        print pfr + boxscore_link

print 'printing'
print parse_box_score(box_scores[-1])