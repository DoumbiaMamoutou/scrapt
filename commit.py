import requests
from bs4 import BeautifulSoup

url = "https://github.com/DoumbiaMamoutou/projet_groupe1/commits/master"

response = requests.get(url)

if response.status_code == 200:
    html_soup = BeautifulSoup(response.text, 'html.parser')
    div_ol = html_soup.find('ol', attrs={'class': "commit-group table-list table-list-bordered"})
    div_li = div_ol.findAll('li', attrs={'class': "commit commits-list-item js-commits-list-item table-list-item js-navigation-item js-details-container Details js-socket-channel js-updatable-content"})
    cnt = 0
    for items in div_li:
        if cnt < 100:
            table = items.find('div', attrs={'class': "table-list-cell"})
            p = table.find('p', attrs={'class': "commit-title h5 mb-1 text-gray-dark"})
            a = p.find('a', attrs={'class': "message js-navigation-open"})
            url = a['href']
            a2 = p.find('a')
            url2 = a2['href']
            div = table.find('div', attrs={'class': "commit-meta commit-author-section no-wrap d-flex flex-items-center mt-1"})
            ava = div.find('div', attrs={'class': "AvatarStack flex-self-start "})
            avat = ava.find('div', attrs={'class': "AvatarStack-body"})
            avta_a = avat.find('a', attrs={'class': "avatar"})
            ima = avta_a.find('img')
            image = ima['src']
            div2 = div.find('div')
            a_div = div2.find('a').get_text()
            url_a = a_div['href']
            realative = div2.find('relative-time', attrs={'class': "no-wrap"}).get_text()
            commit = items.find('div', attrs={'class': "commit-links-cell table-list-cell"})
            d_commit = commit.find('div', attrs={'class': "commit-links-group BtnGroup"})
            a_commit = d_commit.find('a', attrs={'class': "sha btn btn-outline BtnGroup-item"}).get_text()
            a_commit_url = a_commit['href']
            a_commit2 = commit.find('a', attrs={'class': "btn btn-outline tooltipped tooltipped-sw"})
            a_commit2_url = a_commit2['href']
            print(a,url, a2, url2, image,a_div, url_a,realative, a_commit, a_commit_url, a_commit2_url)
            cnt += 1
    # print(div_li)
    	
else:
    print("error", response.status_code)    