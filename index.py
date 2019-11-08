import requests
from bs4 import BeautifulSoup

url = "https://github.com/DoumbiaMamoutou/projet_groupe1"

response = requests.get(url)

if response.status_code == 200:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    div_nav = html_soup.find('div', attrs={'class': "overall-summary overall-summary-bottomless"})
    div_ul = div_nav.find('ul', attrs={'class': "numbers-summary"})
    div_li = div_ul.findAll('li')
    cnt = 0
    for items in div_li:
    	if cnt < 5:
	    	a = items.find('a')
	    	url = a['href']
	    	des = a.find('span', attrs={'class': "num text-emphasized"}).get_text()
	    	print(url, des)
	    	cnt += 1
    	
else:
    print("error", response.status_code)    