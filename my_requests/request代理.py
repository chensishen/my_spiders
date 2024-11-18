import requests

url = 'http://www.baidu.com/s?'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

data = {
    'wd': 'ip'
}

proxy = {
    'http': '140.255.139.249:3256'
}

response = requests.get(url, params=data, proxies=proxy, headers=headers)

content = response.text

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(content)
