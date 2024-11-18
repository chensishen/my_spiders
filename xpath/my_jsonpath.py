import json
import jsonpath
from mypyc.doc.conf import author

# 书店所有的书

obj = json.load(open('store.json','r',encoding='utf-8'))

# 书店里面所有书的作者
# author_list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(author_list)

# 所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')
# print(author_list)

# store下面所有元素
# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# store里面所有东西的price
# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# 第三个书
# book = jsonpath.jsonpath(obj,'$.store..book[2]')
# print(book)

# 最后一本书
# book = jsonpath.jsonpath(obj,'$..book[(@.length-1)]')
# print(book)

# 前俩本书
# book = jsonpath.jsonpath(obj,'$..book[0,1]')
# book = jsonpath.jsonpath(obj,'$..book[:2]')
# print(book)

# 包含isbn的书   条件过滤要在（）前加？
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')
# print(book_list)

# 那本书超过10元
# book_list = jsonpath.jsonpath(obj,'$..book[?(@.price>10)]')
# print(book_list)








