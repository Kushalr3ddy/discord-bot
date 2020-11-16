"""from pydogapi import DogAPI
dog = DogAPI()
print(dog.list())"""

import requests as re
import json
url ="https://api.woofbot.io/v1/"

r = re.get(f"{url}breeds")
data = json.loads(r)
#print(data["response"])