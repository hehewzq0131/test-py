# from lxml import etree
# import  requests
#
# url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E7%A7%91%E6%8A%80&fr=search&red_tag=s1890224318'
# html = requests.get(url).text
# print(html)
# pare = etree.HTML(html).xpath('//div[@class="search_main_wrap"]/h3/a/@href')
# # print(pare)



#-*- coding: UTF-8 -*-

from lxml import etree

source = u'''
<div><p class="p1" data-a="1">测试数据1</p>
<p class="p1" data-a="2">测试数据2</p>
<p class="p1" data-a="3" style="height:100px;">
<strong class="s">测试数据3</strong></p>
<p class="p1" data-a="4" width="200"><img src="1.jpg" class="img"/><br/>
图片</p>
'''
# 从字符串解析
page = etree.HTML(source)
# 元素列表
ps = page.xpath("//p")
p_all=page.xpath("p")

print('p_all',p_all)
for p in ps:
    print(u"属性：%s" % p.attrib)
    print(u"文本：%s" % p.text)
print('==========')
# 文本列表
ts = page.xpath("//p/text()")
for t in ts:
    print(t)

print('---------------')
# xpath定位
ls = page.xpath('//p[@class="p1"][last()]/img')
for l in ls:
    print(l.attrib)
