#!/usr/bin/python

"""
Created on Fri Jun 10 11:22:02 2020
@author: Zefang
"""

import urllib3
from os import getcwd
from datetime import datetime

#run cronjob to daily update
def main():
	today = datetime.today()
	date = today.strftime("%Y%m%d")
	if(today.weekday() < 6):#no newspaper on Sunday
		download_newspaper(date)
	if(today.weekday() == 5):#magazine only on Saturday
		download_magazine(date)

#download WSJ newspaper in pdf		
def download_newspaper(date):
	path = getcwd()
	url = "https://customercenter.wsj.com/todaysPaper/"
	filename = "WSJNewspaper_"+ date +".pdf"
	
	http = urllib3.PoolManager()
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	response = http.request('GET', url, preload_content=False)
	with open(path + filename,"wb") as out: 
		out.write(response.data)
	print("Completed "+filename)

#download WSJ Magazine in pdf	
def download_magazine(date):
	path = getcwd()
	url1 = "http://ereader.wsj.net/eebrowser/ipad/html5.check.20032416//action/php-script/down_full.php?&archiveName=The%20Wall%20Street%20Journal%20Magazine_"
	url2 = "&pSetup=wallstreetjournal-xp-wallstreetjournalmag&file=0@/wallstreetjournalmag/"
	url = url1 + date + url2 + date +"/page.pdf"
	filename = "WSJMagazine_" + date + ".pdf"
	
	http = urllib3.PoolManager()
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	response = http.request('GET', url, preload_content=False)
	if (len(response.data) > 2**20): #fail if return empty page
		with open(path + filename,"wb") as out: 
			out.write(response.data)
		print("Completed "+filename)
	
if __name__ == "__main__":
    main()
