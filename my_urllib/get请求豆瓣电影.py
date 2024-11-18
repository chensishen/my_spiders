import urllib.request
import urllib.parse
import json

from twisted.spread.pb import respond

from 请求对象的地址 import request

url = 'https://api.bilibili.com/pgc/season/index/result?st=2&order=2&area=-1&style_id=-1&release_date=-1&season_status=-1&sort=0&page=1&season_type=2&pagesize=20&type=1'

url = 'https://api.bilibili.com/pgc/season/index/result?st=2&order=2&area=-1&style_id=-1&release_date=-1&season_status=-1&sort=0&page=2&season_type=2&pagesize=20&type=1'

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',

        'Cookie':"i-wanna-go-back=-1; buvid4=58D7ED9D-5126-DD9D-1231-75CC799173D637244-022122018-h4u3028hmIs2xzzkm93ZwRIqXgkftZrKuA0wY6DiovqBRVhFirbxkQ%3D%3D; enable_web_push=DISABLE; buvid3=306416D9-BBB6-5569-4F9F-21F92F3DDA8A41802infoc; b_nut=1703424641; b_ut=5; _uuid=C5D767F6-E5B7-41E1-E158-6B6E917CE26E44285infoc; header_theme_version=CLOSE; rpdid=|(~k|~llmRY0J'u~|YYuYYlR; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; LIVE_BUVID=AUTO9217222417928782; DedeUserID=1578851426; DedeUserID__ckMd5=394c610925e97fe6; PVID=1; CURRENT_QUALITY=80; buvid_fp=0b8d700d23122ac2770515211bbb9e0e; SESSDATA=c0e2fcd1%2C1746758106%2Cd725a%2Ab1CjBBKEuXDSb-LvGx58m1cmlkE3m2-uuFCVa2n_pKtJe-yeqH4xv9fFAeMBBrlhPezNoSVkd5UjN3emp5a3N1SEFjZDBrczJvd2tCVHpNTXA3dkRObTN2YU5PdURpYmxDZUhZQnlYWmRNMnVpbF85dnJoTEFfOGpEVjBQTXNCX2g5M1hrUmUwMXFRIIEC; bili_jct=6b935ece78bbdd325d7c45ba95342ee1; fingerprint=5053b72e74349d494116022a95a40652; sid=6wun139f; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzE1OTY4OTgsImlhdCI6MTczMTMzNzYzOCwicGx0IjotMX0.GKA0NPnS5OGoyUSCUhfrHhCuFuDYOKHtiNlM8Ge7sBE; bili_ticket_expires=1731596838; bp_t_offset_1578851426=998824297139011584; home_feed_column=4; b_lsid=8B284542_19320046A97; browser_resolution=850-851; CURRENT_BLACKGAP=0; CURRENT_FNVAL=16"
         }

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# obj = json.loads(content)
# print(obj)

# 数据下载到本地
# open 的方法默认是gbk编码 如果向保存汉字指定编码格式为utf-8
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
#
# with open('douban.json','w',encoding='utf-8') as fp:
#     fp.write(content)




