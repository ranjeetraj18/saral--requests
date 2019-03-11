import json
import requests
import os.path
from os import path

# if path.exists("courses.json"):
# 	with open("courses.json","r+") as count:
# 		data=json.load(count)
# 		# print(data)
# else:
url="http://saral.navgurukul.org/api/courses"
w = requests.get(url).text
# print (w)
with open("cours.json","w+") as count:
	count.write(w)
	data = json.loads(w)
	print (data)

a=0
for i in data["availableCourses"]:
	a+=1
	var=(a,i["name"])
	print (var)

user=int(input("enter the nuber\n"))
r=(data["availableCourses"])
id1=str(r[user-1]["id"])
# print (id1)

new_url ='http://saral.navgurukul.org/api/courses/'+str(id1)+'/exercises'
# print (new_url)
page =requests.get(new_url).json()
# print(page)

num=0
for j in page['data']:
	num+=1
	new = (num,j["name"])
	print(new)

user2 = int(input("enter your num\n"))
B = page['data']
slug = B[user2-1]['slug']
# print(slug)


url1='http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(id1,slug)
raw1=requests.get(url1)
slug_data=raw1.json()
print  (slug_data['content'])




