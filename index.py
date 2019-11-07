import requests
from bs4 import BeautifulSoup

url = "https://www.lespagesjaunesafrique.com/"

response = requests.get(url)

if response.status_code == 200:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    div_pays = html_soup.findAll('div', attrs={'class': "col-sm-4 col-xs-6 col-md-4 col-lg-3"}) 
    compt = 0
    for item in div_pays:
        if compt < 53:
            ba = item.find('a')
            url = ba['href']
            texte = ba.find('div', attrs={'class': "drapeaux"}).get_text()
            print(compt, "\n url : " + url + "\n texte : " +texte)
            
            compt += 1
    
    # for items in ct:
    #     pays = ct.find('div', attrs={'class': "col-sm-4 col-xs-6 col-md-4 col-lg-3"})
    #     print(pays)
    # print(div_pays)
else:
    print("error", response.status_code)    