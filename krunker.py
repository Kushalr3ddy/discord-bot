import requests
from bs4 import BeautifulSoup as bs

url = "https://krunkerio.fandom.com/wiki/Krunker.io_Wiki"

menu = requests.get(url)
classes = requests.get("https://krunkerio.fandom.com/wiki/Classes")

main_menu = bs(menu.content,"lxml")
class_menu = bs(classes.content,"lxml")
menu_items = main_menu.find_all("div",class_='diep-text')
menu_list="Community\nWeapons\nClasses\nGame Stuff\nEconomy\nMaps\nKrunk Hub\nMisc\n"
class_items = class_menu.find_all("table",class_="article-table")[0]
class_img = class_menu.find_all("img",class_="thumbimage")
class_description = class_menu.find_all("p")
for i in class_items:
    print(i.text)