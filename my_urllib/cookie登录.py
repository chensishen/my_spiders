# 使用场景：数据采集的时候，需要绕过登录，然后加入到某个页面

import urllib.request
import urllib.parse

url = 'https://weibo.cn/64514991586/info'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'cookie':'SCF=Aj1hEOmubtqnkxwtYk_PqNrG-urRQh9D2VzsxKftIlP59b-Z0IroeW8Zh09T_qTcGld6I55X6EjzT7aOv2izUd8.; SUB=_2A25KN46vDeRhGeFL7VUW8CzFwjqIHXVpTI5nrDV6PUJbktANLVnfkW1NfdjZAAVQpeOS7raU_NRC8nTw1VrtZQS4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Um-9LAPyjKac4DW0jT4QQ5NHD95QNSKqNS05E1K.cWs4Dqcj9i--fi-zRiKnfi--fiK.0i-2fP0z7eo2pentt; SSOLoginState=1731460863; ALF=1734052863; _T_WM=6125ceca4978035cc02d78ad44d5ae6e; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D20000174',
    # 携带登陆后的信息
    'referer':'https://weibo.cn/',
    # 判断当前路径是不是由上个路径进来的  一般情况下为图片防盗链
    }

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('weibo.html', 'w',encoding='utf-8') as f:
    f.write(content)









