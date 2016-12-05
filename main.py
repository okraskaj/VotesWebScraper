import urllib
from bs4 import BeautifulSoup
from operator import itemgetter

r = urllib.urlopen('http://website/projects')       #change here
soup = BeautifulSoup(r,"lxml")

btns = soup.find_all("a", class_="btn-default")     #change here
links = []

for element in btns:
    links.append(element["href"])

prefix = "http://website"                           #change here
links = [prefix + link for link in links]
soups = {}
for link in links:
    r = urllib.urlopen(link)
    su = BeautifulSoup(r,"lxml")
    soups[link] = su

top = {}
for k in soups:
    span = soups[k].find_all("span", class_="badge") #change here
    top[k] = int(span[0].text)

good_top = {}
for item in top:
    good_top[item.split("/")[-1]]=top[item]

for item in sorted(good_top.items(), key=itemgetter(1),reverse = True):
    print("%s - %d"%(item[0],int(item[1])))
