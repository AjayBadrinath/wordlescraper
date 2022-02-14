import requests
from bs4 import BeautifulSoup
get=requests.get("https://www.nytimes.com/games/wordle/main.bd4cb59c.js")
parsed_page=BeautifulSoup(get.content,'html5lib')
string=parsed_page.prettify()
#x=string.find("cigar")#Get the first index of list
#l=string.find("zymic")#get last index of list+5
f=open("w.txt","w")
f.write(string[string.find('cigar'):string.find('zymic')+6])
f.close()
