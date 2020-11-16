import requests
from bs4 import BeautifulSoup as bs
from requests import status_codes

url="https://www.skysports.com/premier-league-table"
r = requests.get(url)

soup = bs(r.text,"html.parser")
table = soup.find("table",class_="standing-table__table callfn")

for team in table.find_all("tbody"):
    rows = team.find_all("tr")