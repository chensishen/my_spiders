# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# 第一页
# cname: 广州
# pid:
# pageIndex: 1
# pageSize: 10

# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# 第二页
# cname: 广州
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

from spyder.plugins.completion.decorators import request

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'


def create_request(page):
    data = {
        'cname': '广州',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(base_url, data, headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    with open('kfc'+str(page)+'.json', 'w', encoding='utf-8') as fp:
        fp.write(content)




if __name__ == '__main__':
    star_page = int(input('输入起始页码'))
    end_page = int(input('输入结束页码'))
    for page in range(star_page, end_page + 1):
        down_load(get_content(create_request(page)),page)
