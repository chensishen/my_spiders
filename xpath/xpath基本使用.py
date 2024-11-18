from lxml import etree

# xpath解析
# 1.本地文件                                      etree。parse
# 2.服务器响应数据response.read().decode('utf-8')  etree。HTML()

# 1.本地文件
# tree = etree.parse('my_html.html')
#
# print(tree)

# tree.xpath('xpath路径')

# 1.路径查询

# 查找ul下面的li
# //查找所有之孙节点，不考虑层级关系
# /直接找子节点
# li_list = tree.xpath('//ul/li')
# print(li_list)
# print(len(li_list))

# 2.谓词查询
# 查找所有有id属性的li标签
# li_list = tree.xpath('//ul/li[@id]/text()')
# print(li_list)
# print(len(li_list))

# 3.属性查询
# id为1的li标签  注意引号问题
# li_list = tree.xpath('//li[@id="l1"]/text()')
# print(li_list)

# 查找id=1的li标签的class的属性值
# li = tree.xpath('//li[@id="l1"]/@class')
# print(li)

# 4.模糊查询
# 查询id中包含l的标签
# li_list = tree.xpath('//li[contains(@id,"l")]/text()')
# print(li_list)
# print(len(li_list))

# 查询id中以l开头的标签
# li_list = tree.xpath('//li[starts-with(@id,"l")]/text()')
# print(li_list)
# print(len(li_list))

# 5.逻辑查询
# 查询id=li,class=c1的标签
# li_list = tree.xpath('//li[@id="l1" and @class="c1"]/text()')
# print(li_list)
# print(len(li_list))

# 查询id=l1或l2的标签
# li_list = tree.xpath('//li[@id="l1" or @id="l2"]/text()')
# li_list = tree.xpath('//li[@id="l1"]/text() | //li[@id="l2"]/text()')
#
# print(li_list)
# print(len(li_list))











