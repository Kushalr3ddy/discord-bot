import requests
from bs4 import BeautifulSoup as bs

re = requests.get("https://www.reddit.com/r/memes/")

soup = bs(re.text,"lxml")

meme = soup.find_all("img",class_="_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax")

j=0
for i in meme:
    m = i['src']
    j+=1
    if j >=3:
        break