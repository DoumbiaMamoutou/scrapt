import requests
from bs4 import BeautifulSoup

url = "http://www.abidjanguide.com/"

response = requests.get(url)

if response.status_code == 200:
    ##----------------- Récuperation html --------------------------##
    html_soup = BeautifulSoup(response.text, 'html.parser')
    ##----------------- RECUPAREATION CONTENU  --------------------##
    div_title = html_soup.find('div', attrs={'class': "navbar-header"})
    h1_title = div_title.find('h1')
    ##---------------- RECUPERATION PRESENTATION ----------------##
    div_presentation = html_soup.findAll('div', attrs={'class': "col-md-2"})
    compt = 0
    for item in div_presentation:
        if compt < 3:
            # print(compt)
            # print(item.text)
            ba = item.find('a')
            url = ba['href']
            img = ba.find('img')
            h3 = ba.find('h3')
            
            image = img['src']
            titre = h3.text
            print(compt, "\n" +"url : " +url +"\n"+ "image : " +image +"\n"+ "titre : " +titre +"\n")
            compt += 1
    div_carrousel = html_soup.find('div', attrs={'class': "container"})
    div_car = div_carrousel.findAll('div', attrs={'class': "slide"})
    div_inner = div_carrousel.findAll('div', attrs={'class': "carousel-inner"})
    
    print(div_inner)
    
else:
    print("error", response.status_code)
