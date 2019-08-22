# /usr/bin/python
# encoding:utf-8

from selenium import webdriver
import time
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#   from pykeyboard import PyKeyboard
from pymouse.windows import PyMouse
import autopy

m = PyMouse()
#k = PyKeyboard()

seed = "1234567890"
l = []
for i in range(8):
    l.append(random.choice(seed))
ll = ''.join(l)

ss = 'mj3c7b2tobmihu94sl7ikjor12'

#driver = webdriver.Chrome()
driver=webdriver.Firefox()
driver.get('http://shop.shan666.com/index.php/public/logintest')

driver.add_cookie({'name': 'PHPSESSID', 'value': ss})

driver.refresh()

driver.fullscreen_window()

driver.implicitly_wait(10)

target0 = driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[1]/dl/dt[10]/span')

# 元素可见设置
driver.execute_script("arguments[0].scrollIntoView();", target0)
target0.click()

# 描述元素的属性
target = driver.find_element_by_xpath('//*[@id="314"]')
# 执行js脚本，拖动浏览器滚动条到元素的位置
driver.execute_script("arguments[0].scrollIntoView();", target)
target.click()

time.sleep(2)
#点击创建新商品按钮
driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr/td[2]/div[1]/a').click()

time.sleep(2)
#选择服饰
driver.find_element_by_xpath('//*[@id="FirstCategoryList"]/option[1]').click()
# 服饰-》下装
driver.find_element_by_xpath('//*[@id="SecondCategoryList"]/option[1]').click()
#服饰-》下装-》休闲裤(不限)
driver.find_element_by_xpath('//*[@id="ThirdCategoryList"]/option[1]').click()
#点击【确认创建此类商品】按钮
driver.find_element_by_xpath('//*[@id="submitCreateCategoryGoods"]').click()

driver.implicitly_wait(5)
# 上传照片
e = driver.find_element_by_name("UploadGoodsCarouselImgButton")
e.click()

time.sleep(3)

m.click(450, 195)
# autopy.mouse.move(650, 295)
# autopy.mouse.click()

time.sleep(3)

m.click(1175, 443)
time.sleep(3)

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[2]/td[2]/input').send_keys(ll)

driver.find_element_by_xpath('//*[@id="man"]').click()

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[1]/table/tbody/tr[9]/td[2]/input[1]').click()
# 添加规格按钮
driver.find_element_by_xpath('//*[@id="addGoodsSpecButton"]').click()

driver.find_element_by_xpath('//*[@id="addGoodsSpecButton"]').click()

time.sleep(1)

# driver.find_element_by_xpath('//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[1]/select').click()
# time.sleep(1)
sel = driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[1]/td[1]/select')
Select(sel).select_by_value('5')

time.sleep(1)
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/input').send_keys(
    '2222')

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[1]/table/tbody/tr[2]/td/div/a').click()

time.sleep(2)

sel2 = driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[1]/td[1]/select')
Select(sel2).select_by_value('3')
driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[2]/td/div/input').send_keys(
    '3333')  

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div[2]/table/tbody/tr[2]/td/div/a').click()

time.sleep(1)

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[1]').send_keys('500')  # 库存

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[2]').send_keys('0.3')  # 拼团价

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[3]').send_keys('0.5')  # 直购价

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[3]/td[2]/input[4]').click()

time.sleep(7)
# 上传预览图
#//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[4]/td[2]/table/tbody/tr[2]/td[8]/div

driver.find_element_by_css_selector("#AddGoodForm > table > tbody > tr > td:nth-child(9) > div > div:nth-child(4) > table > tbody > tr.addGoodsSkuDetailTr > td:nth-child(2) > table > tbody > tr.GoodsSkuDetailDataTr > td:nth-child(8) > div > div").click()
time.sleep(1)
m.click(440, 195)
time.sleep(2)
m.click(1180, 445)
driver.implicitly_wait(5)

# 描述元素的属性
target2 = driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input')
# 执行js脚本，拖动浏览器滚动条到元素的位置
driver.execute_script("arguments[0].scrollIntoView();", target2)

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[2]/table/tbody/tr[10]/td[2]/input').send_keys(
    'http://www.baidu.com')

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[3]/table/tbody/tr[2]/td[2]/input[2]').send_keys('5')

driver.find_element_by_xpath(
    '//*[@id="AddGoodForm"]/table/tbody/tr/td[3]/div/div[3]/table/tbody/tr[2]/td[2]/input[3]').send_keys('5')

# driver.quit()
