import requests
import json
from bs4 import BeautifulSoup
import time

g = 0
l = 0
llist = []

resp = requests.get(f'https://hobbygames.ru/warhammer-40000')
soup = BeautifulSoup(resp.text, "html.parser")
data = list(soup.findAll('a', class_='name'))


for i in range(len(data)):
    data[i] = str(data[i])
    g = data[i].find('href="')
    l = data[i].find('title')
    llist.append(data[i][g+6:l-2])
    
print(llist)

for i in range(len(llist)):
    time.sleep(3)
    resp = requests.get(llist[i])
    soup = BeautifulSoup(resp.text, "html.parser")
    data = list(soup.findAll('div', class_='desc-text'))
    data = str(data)
    g = data.find('Вес: ')
    l = data.find('</li></ul>')
    print(data[g:l])


