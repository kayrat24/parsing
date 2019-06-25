from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = urlopen('https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/')
soup = BeautifulSoup(html,'lxml')

body = soup.findAll('article', class_='listing-item')

result_price = []
result_title = []
result_photo = []

for x in body:
    try:
        price = x.find('div', class_='listing-item-main').find('p', class_='listing-item-title')
        get_price = price.get_text()
        get_price_r = get_price.replace('\n', '').replace('\xa0', '')
        result_price.append(get_price_r)

        title = x.find('div', class_='listing-item-main').find('a', class_='listing-item-title')
        get_title = title.get_text()
        result_title.append(get_title)
        
        photo = x.find('img', class_='listing-item-photo')
        get_photo = photo.get('src')
        result_photo.append(get_photo)
    except Exception as e:
        print(e)    

for i in range(len(result_title)):
    # result.append(result_title[i] + ' ' + result_price[i] + ' ' + result_photo[i])
    thedict = {"title" : result_title[i], "price" : result_price[i], 'pic' : result_photo[i]}
    result = f'#{i+1}\nТема в лалафо: {thedict["title"]}\nЦена {thedict["price"]}\nСсылка на фото: {thedict["pic"]}; \n\n'
    f = open('lalafo.csv', 'a')
    f.write(str(result))
    f.close()
    print(result)
