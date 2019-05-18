import requests
import time
from notify_run import Notify
from bs4 import BeautifulSoup
notify=Notify()
URL="https://www.spicinemas.in/chennai/now-showing/"
time_cntr=0
loop=1
cnt=0
time_to_sleep=60 #2 minutes
movies_check=["SHAZAM","AVENGERS"] # movies to look out for 
notify.send("You'll get notifications now")
summary=""
while loop==1:
	if time_cntr!=1:
		time.sleep(time_to_sleep)
		time_cntr+=1
		continue
	else:
		time_cntr=0
	r=requests.get(URL)
	soup=BeautifulSoup(r.content,'html5lib')
	s=str(soup.prettify())
	movie_names=[]
	temp_name=""
	for i in range(0,len(s)-10):
		if s[i:i+9]=="img alt=\"":
			temp_name=""
			for j in range(i+9,i+100):
				if s[j]=='"':
					break
				else:
					temp_name=temp_name+s[j]
			movie_names.append(temp_name)
	for i in movies_check:
		found=0
		for j in movie_names:
			if i in j:
				found=1
		if found==1:
			summary+=i+" found book tickets now! "
		else:
			summary+=i+" not found "
	notify.send(summary)