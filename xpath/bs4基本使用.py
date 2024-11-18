from bs4 import BeautifulSoup

# 通过解析本地文件 来讲bs4的基础语法
soup = BeautifulSoup(open('my_html.html', 'r', encoding='utf-8'), 'lxml')

# print(soup.a)
# 获取标签属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# 1.find
# 返回第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值找到对应的标签对象
# print(soup.find('a',title='a2'))

# 根据class的值来查找    注意要加下划线
# print(soup.find('a',class_='a1'))
# 2.findall 返回一个列表，查找所有a标签
# print(soup.find('a'))
# 想获取个标签数据，要在findall参数里加列表的数据
# print(soup.find_all(['a','span']))
# limit的作用是查找前几个数据
# print(soup.find_all('li',limit=2))

# 3.select(推荐)
# select返回一个列表 并返回多个数据
# print(soup.select('a'))

# 通过.代表class   我们叫做类选择器
# print(soup.select('.a1'))
# 通过#代表id   我们叫做类选择器
# print(soup.select('#l1'))

# 属性选择器---通过属性寻找对于的id
# 查找li标签中有id的标签
# print(soup.select('li[id]'))

# 查找li标签中有id=l2的标签
# print(soup.select('li[id=l2]'))


# 层次选择器
# 后代选择器
# print(soup.select('div li'))

# 子代选择器
# 第一级子标签
# 很多计算机语言中不加空格不会输出内容
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有内容
# print(soup.select('a,li'))

# 节点信息
# obj = soup.select('#d1')[0]
#如果只有内容string和get_text()都可以使用
#如果标签里还有标签 string就获取不到数据 而get_text()是可以获得数据的
# print(obj.string)
# print(obj.get_text())

# 节点的属性
# obj = soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
# print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])

