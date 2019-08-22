# from bs4 import BeautifulSoup
#
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
# soup = BeautifulSoup(html,'lxml')
#
# # print(soup.prettify())
# print("1:",soup.title)
# print("2:",soup.title.name)
# print("3:",soup.title.string)
# print("4:",soup.title.parent.name)
# print("5:",soup.p)
# print("6:",soup.p["class"])
# print("7:",soup.a)
# print("8:",soup.find_all('a'))
# print("9:",soup.find(id='link3'))
# 通过select()直接传入CSS选择器就可以完成选择 熟悉前端的人对CSS可能更加了解，其实用法也是一样的 .表示class #表示id 标签1，标签2
# 找到所有的标签1和标签2 标签1 标签2 找到标签1内部的所有的标签2 [attr] 可以通过这种方法找到具有某个属性的所有标签 [atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print('1:',soup.select('.panel .panel-heading'))
# print('2:',soup.select('ul li'))
# print('3:',soup.select('#list-2 .element'))
# print('4:',type(soup.select('ul')[0]))
# print("5:",soup.select('li'))
# for content in soup.select('li'):
#     print(content.get_text())
#     print(content['class'])
#     print(content.attrs['class'])
#     # print(content.get)

# import requests
#
# response  = requests.get("https://www.baidu.com")
# print('1:',response)
# print('2:',type(response))
# print('3:',response.status_code)
# print('4:',type(response.text))
# print('5:',response.text)
# print('6:',response.cookies)
# print('7:',response.content)
# print('8:',response.content.decode("utf-8"))


# import time
# from selenium  import webdriver
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(8)
# driver.get("https://www.baidu.com")
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
# driver.find_element_by_xpath("//*[@id='su']").click()
# time.sleep(2)
# # 第二个判断方法
# #  //*[@id="20"]/h3/a #\32 0 > h3 > a
# ele_string = driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
# if (ele_string == "Selenium - Web Browser Automation"):
#     print("测试成功，结果和预期结果匹配！" )
#     driver.quit()

# coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# import os
# r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
# fengjing = r.content
# soup = BeautifulSoup(fengjing, "html.parser")
# # print("soup content:",soup.contents)
# # 找出所有的标签
# images = soup.find_all(class_="lazy")
# # print images # 返回list对象
# # print("images:",images)
# for i in images:
#     jpg_rl = i["data-original"]  # 获取url地址
#     title = i["title"]           # 返回title名称
#     print(title)
#     print(jpg_rl)
#     print("")

# import requests
#
# # 先打开登录首页，获取部分cookie
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#            }  # get方法其它加个ser-Agent就可以了
#
# s = requests.session()
# r = s.get(url, headers=headers,verify=False)
# print(s.cookies)
# coding:utf-8

# import yaml
# import os
#
# cur = os.path.dirname(os.path.realpath(__file__))
#
# def get_token(yamlName="token.yaml"):
#     '''
#     从token.yaml读取token值
#     :param yamlName: 配置文件名称
#     :return: token值
#     '''
#     p = os.path.join(cur, yamlName)
#     print('p:',p)
#     f = open(p,'rb')
#     print("f:",f)
#     a = f.read()
#     t = yaml.load(a)
#     f.close()
#     return t["token"]
#
# if __name__ =="__main__":
#     print(get_token())


import  unittest
import os
#
# class test_group(unittest.TestCase):
#     case_path = os.path.join(os.getcwd(),"test_case")
#     def testMinus(self):
#         self.assertEqual(6 - 5,9 - 8)
#         print("减法 is success")
#     def testDivide(self):
#         d = 9/4
#         e = 2.25
#         self.assertEqual(d,e)
#         print("除法 is success")
#
#     def all_case(self):
#         discase=unittest.defaultTestLoader.discover(self,case_path,pattern='test*.py',top_level_dir=None)
#         return  discase
#
# # if __name__ == "__main__":
# #     unittest.main()
#
# if __name__ =="_main__":
#     unittest.TextTestRunner().run(all_case)
#
#
#
import  random


seed = ["1","2","3","4","5","6","7a"]
print("hahah:",seed[random.randrange(0,len(seed), 1, int)])
idx = 0
while True:
    if idx > 10:
        break
    idx += 1
    seed[random.randrange(0,len(seed), 1, int)]






