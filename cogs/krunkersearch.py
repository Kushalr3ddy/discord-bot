import requests
from bs4 import BeautifulSoup as bs

re = requests.get("https://krunkerio.fandom.com/wiki/")
c_menu = requests.get("https://krunkerio.fandom.com/wiki/Classes")

menu_soup = bs(c_menu.text,"html.parser")
menu_tbl = menu_soup.find_all('tbody')#,class_="article-table")

print(len(menu_tbl))
"""j = 0
for i in menu_tbl:
    print(i.text)
    j+=1
    if j ==4:
        print("\n")
        j=0"""
        