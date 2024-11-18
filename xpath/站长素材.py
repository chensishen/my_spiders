# 需求   下载前十页地址
# https://sc.chinaz.com/tupian/siwameinvtupian.html
# https://sc.chinaz.com/tupian/siwameinvtupian_2.html

import urllib.request
from lxml import etree


def create_request(page):
    if(page==1):
        url = "https://sc.chinaz.com/tupian/siwameinvtupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/siwameinvtupian_"+str(page)+".html"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

#//div[@class="container"]//div[@class="item"]/img/@data-original

def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:'+src;
        urllib.request.urlretrieve(url, './love_img/'+name+'.jpg')




start_page = int(input('请输入起始页码'))
end_page = int(input('请输入结束页码'))

for page in range(start_page, end_page+1):
    request = create_request(page)
    content = get_content(request)
    down_load(content)








