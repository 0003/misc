__author__ = 'will'

from bs4 import BeautifulSoup
import requests
import collections

main = "http://www.pro-football-reference.com/super-bowl/"
pfr = "http://www.pro-football-reference.com"
r = requests.get(main)
data = r.text
soup = BeautifulSoup(data)

def make_int(s):
    return int(s.text)


def parse_box_score(url):
    print url
    r= requests.get(url).text
    s = BeautifulSoup(r)
    a = s.find_all('td', {"align":"right"})
    #print a
    #print a[0].text
    try:
        t1, t2, t3, t4 = int(a[0].text),int(a[1].text),int(a[2].text),int(a[3].text)
    except:
        print a[0].text,a[1].text,a[2].text,a[3].text

    #print t1, t2, t3,t4
    u1, u2, u3, u4 = int(a[5].text),int(a[6].text),int(a[7].text),int(a[8].text)
    #print u1, u2, u3, u4
    #assert sum([t1, t2, t3, t4]) == int(a[4].text)
   #assert sum([u1, u2, u3, u4]) == int(a[9].text)

    tq1 = t1
    tq2 =  tq1 + t2
    tq3 = tq2 + t3
    tq4 = tq3 +t4

    assert tq4 == int(a[4].text)

    uq1 = u1
    uq2 =  uq1 + u2
    uq3 = uq2 + u3
    uq4 = uq3 +u4

    assert uq4 == int(a[9].text)

    return {"Q1":(tq1,uq1), "Q2": (tq2,uq2), "Q3": (tq3,uq3), "Q4": (tq4,uq4)}

def get_ints(d,quarter):
    t, u = d[quarter]
    t = t % 10
    u =  u % 10
    return t, u




box_scores = []
for link in soup.find_all('a'):
    boxscore_link = link.get("href")
    if 'boxscore' in boxscore_link:
        box_scores.append(pfr + boxscore_link)
        print pfr + boxscore_link



scores = []
print box_scores

for link in box_scores[2:]:
    print link
    scores.append(parse_box_score(link))

print scores
print len(scores)

print get_ints(scores[0],"Q3")

q1 = []
q2 = []
q3 = []
q4 = []
c1= collections.defaultdict(int)
c2= collections.defaultdict(int)
c3= collections.defaultdict(int)
c4 = collections.defaultdict(int)

for score in scores:

    sc = get_ints(score,"Q1")
    print 'before', sc
    q1.append(sc)
    sc = tuple(sorted(sc))
    print 'after', sc
    c1[sc] +=1

    sc = get_ints(score,"Q2")
    print 'before', sc
    q2.append(sc)
    sc = tuple(sorted(sc))
    print 'after', sc
    c2[sc] +=1

    sc = get_ints(score,"Q3")
    print 'before', sc
    q3.append(sc)
    sc = tuple(sorted(sc))
    print 'after', sc
    c3[sc] +=1

    sc = get_ints(score,"Q4")
    print 'before', sc
    q4.append(sc)
    sc = tuple(sorted(sc))
    print 'after', sc
    c4[sc] +=1

counts1 = sorted(c1.items(),key=lambda x: x[1], reverse = True)
counts2 = sorted(c2.items(),key=lambda x: x[1], reverse = True)
counts3 = sorted(c3.items(),key=lambda x: x[1], reverse = True)
counts4 = sorted(c4.items(),key=lambda x: x[1], reverse = True)

make_str = lambda l: str(l)
with open('results.txt','w') as f:

    f.write('Quarter 1 \n')
    f.write(str(counts1))

    f.write('\n Quarter 2 \n')
    f.write(str(counts2))

    f.write('\n Quarter 3 \n')
    f.write(str(counts3))

    f.write('\n Quarter 4 \n')
    f.write(str(counts4))

print


