import urllib.request
import urllib.parse

from 基本使用 import response

url = 'https://fanyi.baidu.com/ait/text/translate'


headers={
    #'Accept-Encoding':' gzip, deflate, br, zstd'
    #'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #'Acs-Token':' 1731316108036_1731400977859_XsXAmIRaM+Olcec9K+ueY2XyWIp7iLNhLwewazFmQ/IPoZ0rxHtf57MxpOqb56LLJWgs4QKHh4XuurIC+JVcaaCif3EafmVbf0/8EVK+lX0Tjbk3Nt+iO7N/kCHj4v4syxzr+VNVe1M8JrlaP+xjNo4fW0+lVilXqv/ujW2/NVVN5czEpadJ5YlNn6Riya9yqtlSeKzKrVD89lAJPShT94S4QzJtu/JAnpCoIw4UHEmOefqhPiheKqrN+/xjGlGqAaKmgfFlNr99B7fOPevsOU/TJqh5VnJpGu6av8AbgNzTVC/wEhCEs1oPcp2HsirqYa231Dd9+JtAU3Fx0OwuczRTcpdJ1LJZD3q2q/L4uk7hGRaqdMxil2RXXLKNswE+zGcQZrDKnsQn5qcobDb8ti11cnek7t3pDvqAAjenwfC+lOPwcqrAgSk7ZYUBKNEdD1xPkhnfbrVwykWVa9NP8LW9GCIQB+mnkp8V6tyhdKe745F+4G8irmVDm4zpk/Oy',
    #'Connection':' keep-alive',
    #'Content-Length':' 139',
    #'Content-Type':' application/json',
    'Cookie':'BIDUPSID=A5D27014FBAEBF97ED031844C7888669; PSTM=1730372353; BAIDUID=A5D27014FBAEBF9759EE458AF80BD33B:FG=1; BAIDUID_BFESS=A5D27014FBAEBF9759EE458AF80BD33B:FG=1; ZFY=gTFkaIbfr:ADoBq0xqmZGpACEfVYGWsa7fg3NobsvvLQ:C; __bid_n=192e23ad9cd9216e6fe497; BDUSS=1JZ085NlZLWlVSM2RFaUF-NGQ2Ynh2ckpqNmxkYWo0SGJEcVVxflVpdjlWazFuRVFBQUFBJCQAAAAAAQAAAAEAAACYEpYOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP3JJWf9ySVnNE; BDUSS_BFESS=1JZ085NlZLWlVSM2RFaUF-NGQ2Ynh2ckpqNmxkYWo0SGJEcVVxflVpdjlWazFuRVFBQUFBJCQAAAAAAQAAAAEAAACYEpYOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP3JJWf9ySVnNE; H_PS_PSSID=60941_61027_61055_61071_60853_61130_61113_61140_61117; RT="z=1&dm=baidu.com&si=73b64384-9ea4-42c3-b6b4-e0964d233dfa&ss=m3ed6j2e&sl=1&tt=3ey&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab_sr=1.0.1_ZmJlYWE2NzA2NGMwN2U3ZWZkNzY2NzQ5NmI0N2UyNjJmZWQ2Yjc4ZDk3ZTFiY2NhNTIyMThkZjMxMzc2N2ZhNTdlYmMyNmI2M2FkZDFiMTk1NzE5Y2RjOWNjZmM2NGI4MWM3ZWQ1OTNiZmM1Njc2NmYwMmYzMWJkMWQwZGM2MjRhYzdiY2Y3NzYzYzc0NmNiOTIxNDkzZjlhMWViYTRhNg==',
    #'Host':' fanyi.baidu.com',
    #'Origin: https':'//fanyi.baidu.com',
    #'Referer: https':'//fanyi.baidu.com/mtpe-individual/multimodal?query=spider&lang=en2zh',
    #'Sec-Fetch-Dest':' empty',
    #'Sec-Fetch-Mode':' cors',
    #'Sec-Fetch-Site':' same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    #'accept':' text/event-stream',
    #'sec-ch-ua':' "Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    #'sec-ch-ua-mobile':' ?0',
    #'sec-ch-ua-platform':'"Windows"'
}

data = {"query":"love\n","from":"en","to":"zh","reference":"","corpusIds":'[]',"needPhonetic":'false',"domain":"common","milliTimestamp":'1731410634342'}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# import json
#
# obj = json.loads(content)
# print(obj)















