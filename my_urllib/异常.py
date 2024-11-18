import urllib.request
import urllib.error

# httperror是urlerror的子类

url = 'https://blog.csdn.net/qq_44907926/article/details/118585030'

url = 'https://www.goudan.cn'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)

except urllib.error.HTTPError:
    print('HTTPError')
except urllib.error.URLError:
    print('URLError')
























