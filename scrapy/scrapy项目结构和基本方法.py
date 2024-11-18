#1.项目结构
# 项目名字
#         项目名字
#                spiders文件
#                   init
#                   自定义爬虫文件     核心功能文件*******
#         init
#         items   定义数据结构的地方，爬取的数据包含那些
#         middleware 中间件   代理
#         pipelines  管道     处理下载的数据
#         settings    配置外键  ua定义对
#
#2.response的属性和方法
#   response.text   获取的是响应的字符串
#   response.content    获取二进制文件
#   response.xpath      可以直接使用xpath方法解析response内容
#   response.extract()  提取seletor对象的data值
#   response.extract_first()    提取的seletor列表的第一个数据
#
#