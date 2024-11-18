import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com/bff/ordering/menu'

url = 'https://www.starbucks.com.hk/zh_HK/menu/drinks'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# //div[@class="mb3 lg-mb5 gridItem size12of12 md-size6of12 xh-highlight"]//span[@class="hiddenVisually"]/text()

soup = BeautifulSoup(content, 'lxml')

name_list = soup.find_all('a',class_="product-item-link")

for name in name_list:
    print(name.get_text())

# //a[@class = 'product-item-link']/text()


 







