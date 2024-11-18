import urllib.request


proxies_pool = [
    {'http':'202.101.213.14:17152'},
    {'http':'202.101.213.14:17152'},
]

import random

proxies = random.choice(proxies_pool)

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

request = urllib.request.Request(url, headers=headers)

handler = urllib.request.ProxyHandler(proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w',encoding='utf-8') as f:
    f.write(content)




