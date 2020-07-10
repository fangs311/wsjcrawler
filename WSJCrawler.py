#!/usr/bin/python
"""
Created on Fri Jun 10 11:22:02 2020
@author: Zefang
"""
import urllib3
from datetime import datetime

def main():
	today = datetime.today()
	date = today.strftime("%Y%m%d")
	if(today.weekday() < 6):
		download_newspaper(date)
	if(today.weekday() == 5):
		download_magazine(date)
		
def download_newspaper(date):
	path = "/volume1/book/Journals/WallStreetJournal/"
	url = "https://customercenter.wsj.com/todaysPaper/"
	filename = "WSJNewspaper_"+ date +".pdf"
	
	http = urllib3.PoolManager()
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	response = http.request('GET', url, preload_content=False)
	with open(path + filename,"wb") as out: 
		out.write(response.data)
	print("Completed "+filename)

def download_magazine(date):
	path = "/volume1/book/Journals/WallStreetJournalMagazine/"
	url1 = "http://ereader.wsj.net/eebrowser/ipad/html5.check.20032416//action/php-script/down_full.php?&archiveName=The%20Wall%20Street%20Journal%20Magazine_"
	url2 = "&pSetup=wallstreetjournal-xp-wallstreetjournalmag&file=0@/wallstreetjournalmag/"
	url = url1 + date + url2 + date +"/page.pdf"
	filename = "WSJMagazine_" + date + ".pdf"
	
	http = urllib3.PoolManager()
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	response = http.request('GET', url, preload_content=False)
	if (len(response.data) > 2**20):
		with open(path + filename,"wb") as out: 
			out.write(response.data)
		print("Completed "+filename)
	
if __name__ == "__main__":
    main()
