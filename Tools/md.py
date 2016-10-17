from bs4 import BeautifulSoup

import os,sys

if __name__ == "__main__":
	while True:
		html = raw_input()
		t = BeautifulSoup(html, "lxml")
		ans = "| " + t.find_all('td')[1].text
		ans = ans + " | [" + t.find_all('td')[2]['value'] + "](" + "https://leetcode.com" + t.find_all('td')[2].find('div').find('a')['href'] + ") | " + t.find_all('td')[-3].text + " | " + t.find_all('td')[-2].text + " | | |"
		print ans
