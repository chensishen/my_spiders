import urllib.request

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1731485462876_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v':'2.5.22',
    'cookie':'tb_city=440100; tb_cityName="uePW3Q=="; isg=BPr6EJC7SUF_icUtaoNNsWhcSyAcq36F73IEewTzBQ1Y95ox7Dt-lYSBRwMr_PYd',
    'priority':'u=1, i',
    'referer':'https://www.taopiaopiao.com/?spm=a1z21.3046609.city.4.10ed112aarmjKb&tbpm=3&city=440100',
    'sec-ch-ua':'"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'x-requested-with':'XMLHttpRequest'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content=content.split('(')[1].split(')')[0]

with open('city.json','w',encoding='utf-8') as f:
    f.write(content)

import json
import jsonpath

obj = json.load(open('city.json','r',encoding='utf-8'))

# obj = json.loads('city.json')

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(city_list)










