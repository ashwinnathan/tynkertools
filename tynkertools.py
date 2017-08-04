from bs4 import BeautifulSoup
from bs4 import re
import getpass
import requests
from requests.auth import HTTPBasicAuth

username = raw_input("Username: ")
pswd = getpass.getpass("Password:")


def searchCodeAThon():
	searches = []
	page_start = raw_input("Enter start page: ")
	page_end = raw_input("Enter end page: ")
	num_users = raw_input("Enter number of searches: ")
	for num in range(0, int(num_users)):
		search_term = raw_input("Please enter search term: ")
		searches.append(search_term)
	for search in searches: 
		for page_num in range(int(page_start),int(page_end)):
			page = requests.get('http://www.tynker.com/tools/community?t=codeathon&v=published&s=' + str(page_num), auth=(username, pswd))	
			soup = BeautifulSoup(page.text, 'html.parser')
			projects = soup.find_all('li', class_="card")
			for proj in projects:
				if str(search) in proj.text:
					print '\n'
					print "Page: " + str(page_num + 1)
					link = proj.find('a', href=re.compile('community-details'))
					print 'http://www.tynker.com/tools/' + str(link['href'])
					proj_name = proj.find('div', class_="card-title")
					print proj_name.get_text()
					print '\n'


def findUser():
	queue = raw_input("Select queue: ")
	if queue == "web":
		url = 'http://www.tynker.com/tools/community?t=projects&v=approval&s=0'
	elif queue == "mobile":
		url = 'https://dev.tynker.com/tools/publishing?src=production&v=approval&s=0'
	else:
		url = 'http://www.tynker.com/tools/community?t=codeathon&v=approval&s=0'
	page = requests.get(url, auth=(username, pswd))	
	soup = BeautifulSoup(page.text, 'html.parser')
	user = raw_input("Username to search for: ")
	page_num = 0
	while True:
		if str(user) in page.text:
			print "Page: " + str(page_num + 1)
		page_num += 1
		if "dev" not in url:
			url = url[:-1] + str(page_num)
		else:
			url = 'https://dev.tynker.com/tools/publishing?src=production&v=approval&s=' + str(page_num * 50)
		page = requests.get(url, auth=(username, pswd))	
		soup = BeautifulSoup(page.text, 'html.parser')
		if "dev" not in url:
			if not soup.find('li', class_="card"):
				break
		else:
			if not soup.find('div', class_="cb"):
				break


				
while True:
	function = raw_input("Which function would you like to use: ")
	if function.lower() == "search":
		searchCodeAThon()
	elif function.lower() == "finduser":
		findUser()
	else:
		print "Options are \"search\" and \"finduser\" "


				


