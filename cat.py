import requests
from bs4 import BeautifulSoup

url = "https://www.lespagesjaunesafrique.com/pays/cote-d-ivoire/"

response = requests.get(url)

if response.status_code == 200:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    div_cat = html_soup.findAll('div', attrs={'class': "col-sm-12 ct-u-marginTop20 ct-u-marginBottom10"})
    div_detail = html_soup.findAll('div', attrs={'class': "row"})
    compt = 0
    cnt = 0
    for item in div_cat:
        if compt < 24:
            # ba = item.findAll('div', attrs={'class': "col-sm-12 ct-u-marginTop20 ct-u-marginBottom10"})
            categorie = item.find('h2').get_text()
            print(compt, "\n categorie : " +categorie)
            
            compt += 1
            
    for items in div_detail:
        if cnt < 100:
            det = items.find('a')
            # url = det['href']
            # nom = det.findAll('div', attrs={'class': "col-sm-6 col-md-6 col-lg-4 col-xs-12 ct-u-marginBottom10"})
            # h3 = nom.find('div', attrs={'class': "activites"})
            # print(cnt, "\n url : " + url + "\n titre : " +h3)
            print(det)
            cnt += 1
else:
    print("error", response.status_code)    