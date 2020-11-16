import requests
from bs4 import BeautifulSoup
from HEADERS import headers
from threading import Thread

url1 = "https://kushalreddy.aternos.me"



def status():
    re1 = requests.get(url1,headers=headers)
    
    soup1 = BeautifulSoup(re1.text,"html.parser")
    
    stat1 = soup1.find_all("span",class_="status-label")

    for i in stat1:
        if (i.text) != None:
            return(f"{url1} is {i.text}")

        elif i.text == None:
            pass
            
    #s = stat[0]
    #print(s.text)

def server1():
    re  = requests.get(url1,headers=headers)
    soup = BeautifulSoup(re.text,"html.parser")
    stat = soup.find_all("span",class_="status-label")
    for i in stat:
        return f"{url1}server is {i.text}"

#print(server2())