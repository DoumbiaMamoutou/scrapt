import requests
from bs4 import BeautifulSoup
# import json

url = "https://pratik.ci/thematiques/loisirs/confiserie"

response = requests.get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

allentreprise = []

# print(html_soup)

entreprise = html_soup.findAll('div', attrs={'class': "views-row"})

for items in entreprise:
    titre = items.find('div', attrs={'class': "field-item even"}).get_text()
    service = items.find('div', attrs={'class': "field-item odd"}).get_text()
    tel = items.find('div', attrs={'class': "field field-name-field-telepone-1 field-type-text field-label-hidden color_black_blold"}).get_text()
    cel = items.find('div', attrs={'class': "field field-name-field-cellulaire1 field-type-text field-label-hidden color_black_blold"}).get_text()
    lieu = items.find('div', attrs={'class': "field field-name-field-localisation-lieu field-type-taxonomy-term-reference field-label-hidden"}).get_text()

    data = {
        'titre': titre,
        'tel': tel,
        'cel': cel,
        'service': service,
        'lieu': lieu,
    }
    allentreprise.append(data)

print(allentreprise)