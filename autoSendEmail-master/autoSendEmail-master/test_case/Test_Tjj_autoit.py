# /usr/bin/python
# encoding:utf-8

from selenium import webdriver
import time
import random
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#   from pykeyboard import PyKeyboard
# from pymouse import PyMouse
# import autopy
#
# m = PyMouse()
#k = PyKeyboard()
import  random
# seed = "1234567890"
#
# l = []
# for i in range(8):
#     l.append(random.choice(seed))
# ll = ''.join(l)
# 取值标题\描述、短标题
goodstitle = ["北京欢迎你","上海大厦第一高峰","珠穆朗玛峰","布达拉宫","北京天安门","东北北大仓","新疆塔里木盘地"]
#   goodstitle[random.randrange(0,len(seed), 1, int)]

#PHPSESSID=ert44npqpgop0rerk4hev0oe85; _currentUrl_=czoyNzoiL2luZGV4LnBocC9wdWJsaWMvbG9naW50ZXN0Ijs%3D
ss = 'jll69gd90p1t6pi8hlamq14p71'

#driver = webdriver.Chrome()
driver=webdriver.Firefox()
#
# http://shop.tjjshop.cn/index.php/public/logintest
driver.get('http://shop.tjjshop.cn/index.php/index_supplier/index/tag/54/clear/1')

driver.add_cookie({'name': 'PHPSESSID', 'value': ss})

driver.refresh()
 # driver.set_window_size(1080,1000)
driver.maximize_window()
# driver.fullscreen_window()

driver.implicitly_wait(10)
# 商家管理（淘集集）菜单路径：/html/body/div[3]/table/tbody/tr/td[1]/dl/dt[9]/span
target0 = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[1]/dl/dt[9]/span')
print("ceshi------")
# 元素可见设置
driver.execute_script("arguments[0].scrollIntoView();", target0)
time.sleep(2)
# target0.click()
# /html/body/div[3]/table/tbody/tr/td[1]/dl/dt[9]/span
# 判断商品管理 (淘集集)菜单是关闭还是打开状态   class="dt_109 cur"  关闭；class="dt_109" 打开
# www = driver.find_element_by_xpath('/html/body/div[7]/table/tbody/tr/td[1]/dl/dt[9]').get_attribute('textContent')
#  /html/body/div[3]/form/table/tbody/tr/td[1]/dl/dt[9]/span
# www=driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[1]/dl/dt[9]').text
#
# print("test:",www)
# if DT_109 == "dt_109 cur":
#     target0.click()
# else:
#     print("商品管理 (淘集集)菜单是打开状态 ")


# 描述元素的属性  发布商品（淘集集）菜单://*[@id="329"]//*[@id="335"]//*[@id="341"]
target = driver.find_element_by_xpath('//*[@id="341"]')
# 执行js脚本，拖动浏览器滚动条到元素的位置
driver.execute_script("arguments[0].scrollIntoView();", target)
target.click()

time.sleep(2)
#点击创建新商品按钮
driver.find_element_by_xpath('//*[@id="createProduct"]').click()
time.sleep(2)

# a=random.choice('12345678')
# for x in  random.choice(1,3,4):
#     print('33333333')
# # 一级类目
#    服饰： //*[@id="FirstCategoryList"]/option[1]
#   内衣 ：//*[@id="FirstCategoryList"]/option[2]
#   运动：//*[@id="FirstCategoryList"]/option[3]
#   母婴：//*[@id="FirstCategoryList"]/option[4]
#   母婴(不限)：//*[@id="FirstCategoryList"]/option[5]
#   电器：//*[@id="FirstCategoryList"]/option[6]
#   百货：//*[@id="FirstCategoryList"]/option[7]
#  美妆 ：//*[@id="FirstCategoryList"]/option[8]
#   食品：//*[@id="FirstCategoryList"]/option[9]
#

#选择服饰
driver.find_element_by_xpath('//*[@id="FirstCategoryList"]/option[1]').click()
# 服饰-》下装yifu0805.exe
driver.find_element_by_xpath('//*[@id="SecondCategoryList"]/option[1]').click()
#服饰-》下装-》休闲裤(不限)
driver.find_element_by_xpath('//*[@id="ThirdCategoryList"]/option[2]').click()
#点击【确认创建此类商品】按钮
driver.find_element_by_xpath('//*[@id="submitCreateCategoryGoods"]').click()

driver.implicitly_wait(5)
# 商品标题                     /html/body/div[3]/form/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[2]/td[2]/input
driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[2]/td[2]/input').send_keys(goodstitle[random.randrange(0,len(goodstitle), 1, int)])
# 上传照片  //*[@id="UploadNewGoodsCarouselImgButton"]
e = driver.find_element_by_name("UploadGoodsCarouselImgButton")
e.click()

time.sleep(5)
os.system(r'C:\Users\lenovo\Desktop\update\yifu0805.exe')
# os.system(r'C:\Users\lenovo\Desktop\update\up_picture1.exe')
time.sleep(5)
#商品描述/ //*[@id="GoodsDescription"]
driver.find_element_by_id("GoodsDescription").send_keys(goodstitle[random.randrange(0,len(goodstitle), 1, int)])
#商品详情图
driver.find_elements_by_xpath('//*[@id="UploadNewGoodsParticularsImgButton"]')
# 上传照片
e = driver.find_element_by_name("UploadGoodsParticularsImgButton")
e.click()
os.system(r'C:\Users\lenovo\Desktop\update\yifu0805.exe')
time.sleep(5)

#首页推荐位图片
#商品短标题

# 商品所属性别：男//*[@id="man"]
driver.find_element_by_xpath('//*[@id="man"]').click()
#*商品所属年龄段:儿童（0-6岁）//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[9]/td[2]/input[1]
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[9]/td[2]/input[1]').click()
# 添加规格按钮//*[@id="addGoodsSpecButton"]
driver.find_element_by_xpath('//*[@id="addGoodsSpecButton"]').click()
driver.find_element_by_xpath('//*[@id="addGoodsSpecButton"]').click()
time.sleep(1)

# driver.find_element_by_xpath('//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[1]/select').click()
# time.sleep(1)
# 选择类型:颜色：3
sel = driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[1]/select')
Select(sel).select_by_value('3')
#添加按钮前面的输入框值：即类型内容
time.sleep(1)
#//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/input
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/input').send_keys(
    'Red')
#添加按钮
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/a').click()

time.sleep(2)
#尺寸：
sel2 = driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[1]/td[1]/select')
Select(sel2).select_by_value('4')
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[2]/td/div/input').send_keys(
    'XL')

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[2]/td/div/a').click()

time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[1]').send_keys('900')  # 库存

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[2]').send_keys('0.3')  # 拼团价

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[3]').send_keys('0.5')  # 直购价
# 确定按钮
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[4]').click()

time.sleep(3)
# 上传预览图
#//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[8]/div
                                      #AddGoodForm > table > tbody > tr > td:nth-child(9) > div > div:nth-child(4) > table > tbody > tr.addGoodsSkuDetailTr > td:nth-child(2) > table > tbody > tr.GoodsSkuDetailDataTr > td:nth-child(8) > div
driver.find_element_by_css_selector("#AddGoodForm > table > tbody > tr > td:nth-child(9) > div > div:nth-child(4) > table > tbody > tr.addGoodsSkuDetailTr > td:nth-child(2) > table > tbody > tr.GoodsSkuDetailDataTr > td:nth-child(8) > div").click()

os.system(r'C:\Users\lenovo\Desktop\update\specDetailImgSingle.exe')

driver.implicitly_wait(5)

# 描述元素的属性
#  PDD商品链接 //*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input
target2 = driver.find_element_by_xpath('//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input')
# 执行js脚本，拖动浏览器滚动条到元素的位置
driver.execute_script("arguments[0].scrollIntoView();", target2)
#  //*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input').send_keys(
    'http://www.baidu.com')
#单次限量
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[3]/table/tbody/tr[2]/td[2]/input[2]').send_keys('555')

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[3]/table/tbody/tr[2]/td[2]/input[3]').send_keys('556')

time.sleep(2)
#提交并上架
driver.find_element_by_xpath('//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[3]/table/tbody/tr[4]/td[2]/input[4]').click()
#  driver.find_elements_by_class_name("submitFormPutaway submit_default").click()
print("create goods success!")
# driver.quit()