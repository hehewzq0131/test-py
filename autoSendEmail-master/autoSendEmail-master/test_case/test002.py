# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# #import keys模块
# from selenium.webdriver.common.keys import Keys
# import time
#
# brower = webdriver.Firefox()
# brower.get("http://www.baidu.com")
# #在搜索框中输入selenium的英文，但是多出了一个m
# brower.find_element_by_id("kw").send_keys("seleniumm")
# #删除多出来的m
# time.sleep(3)
# brower.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# time.sleep(3)
# #在输入空格+"python教程"
# brower.find_element_by_id("kw").send_keys(Keys.SPACE)
# #在输入中文的时候，避免出现字符错误，所以在中文字符前加u
# brower.find_element_by_id("kw").send_keys(u"Python教程")
# #输入完成之后点击回车键进行搜索。
# brower.find_element_by_id("kw").send_keys(Keys.ENTER)
# # brower.quit()
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
import pymysql
#     db = pymysql.connect("10.99.22.126","root", "Sjyymysql@2018!","CTE_market_test", charset='utf-8')


# conn=pymysql.connect(host='10.99.22.126',port=3306,user='root',passwd='Sjyymysql@2018!',db='CTE_market_test',charset='utf8')
# cur=conn.cursor()
# sql="SELECT*FROM user_login_log"
# ww=cur.execute(sql)
# res=cur.fetchall()
# print('wwwwwwwwww',res)


# cur.execute("""
# create table if not EXISTS user
# (
#   userid int(11) PRIMARY KEY ,
#   username VARCHAR(20)
# )
# """)
# for i in range(1,10):
#     cur.execute("insert into user(userid,username) values('%d','%s')" %(int(i),'name'+str(i)))
# conn.commit()
#
# cur.close()
# conn.close()
#
# a = 10
# assert a > 0
# print('[a = 10] assert a > 0', 'ok')
from selenium import  webdriver
import time
import json
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver  import  ActionChains

# driver=webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://www.baidu.com/")
# driver.get("http://news.baidu.com/")
# try:

    # driver.find_element_by_link_text("新闻").click() #跳转链接
    # driver.find_elements_by_xpath('//*[@id="u1"]/a[1]')
    # driver.find_element_by_xpath("//*/div[@id='u1']/a[text()='新闻']").click()  # 链接通过路径

    # driver.find_element_by_partial_link_text("主页").click()  #模糊（部分）匹配
    # driver.find_element_by_class_name("s_ipt").send_keys("淘集集")
    # driver.refresh()
    # driver.find_element_by_class_name("bg s_btn").click()
    # driver.find_element_by_partial_link_text("新闻").click()  # 链接进入新闻页面
    # print(driver.current_url)  #  获取当前页面URL
    # print(driver.title)  # 获取当前页面标题
    # time.sleep(2)
    # driver.back()  # 从新闻页范围首页
    # time.sleep(2)
    # driver.forward() # 从首页返回新闻页
    # info=driver.capabilities
    # print("info",driver.capabilities['browserVersion'])  #  打印浏览器version的值
    # driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    # driver.find_elements_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr/td[2]/p/label[1]").
    # driver.find_elements_by_xpath("//*[@id="news"]")
    # driver.find_elements_by_xpath("//*/input[@type='radio']")
    # for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
    #     print('i is %s, and content: %s' % (i.id,i.tag_name))
    #     i.click()
    # //*[@id="TANGRAM__PSP_10__memberPass"]
    # //*[@id="TANGRAM__PSP_10__memberPassLabel"]
    #assert 断言
    # assert "百度一下，你就知道1111" in driver.title
    # print("百度一下，你就知道")


    # print(driver.title)
    # if driver.title == "nihao":
    #     print("nihao 百度一下，你就知道")
    # else:
    #     print("else 百度一下，你就知道")
    # driver.quit()
#     //*[@id="TANGRAM__PSP_10__submit"]
# except Exception as E:
#     print("Assertion test fail.:")
#     driver.quit()
# =======================================//html/body/div[1]/div[1]/div/div[3]/a[7]
# driver.get("http://www.baidu.com/")
# time.sleep(1)
# # 登录按钮 右上角
# driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
# time.sleep(1)
# # 用户名登录
# driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
# #登录
# driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
#
# # 断言方法一    方法isDisplayed()来判断这个元素是否显示
# try :
#     error_message = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error' and text()='请您输入手机/邮箱/用户名']").is_displayed()
#     print ("Test pass. the error message is display.")
# except Exception as e:
#     print ("Test fail.", format(e))
#     print("Exception",Exception)

# 断言方法二，本文重点介绍方法
# error_mes = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text
# print("error_mes:",error_mes)
# try:
#     assert error_mes == '请您填写手机/邮箱/用户名'
#     print ('Test pass.')
# except Exception as e:
#     print ("Test fail.", format(e))


# driver.get("https://www.baidu.com")
# # 定位“百度一下”按钮
# newsize=driver.find_element_by_id("su").get_attribute('class')
# print("newsize",newsize)
# # 查看“百度一下”按钮的尺寸
# print("查看“百度一下”按钮的尺寸",newsize.size)
# try:
#     # element = driver.find_element_by_tag_name('body')
#     # # 组合键 Ctrl+a
#     # element.send_keys(Keys.CONTROL + 'a')
#     # print("success")
#     # elem=driver.find_element_by_id("kw")
#     # elem.send_keys("hello, my world!")
#     # time.sleep(3)
#     # elem.send_keys(Keys.CONTROL + 'a') # 全选
#     # elem.send_keys(Keys.BACK_SPACE) # 退格键删除
#     # element = driver.find_element_by_xpath("//*[@id='lg']/img")
#     #
#     element = driver.find_element_by_xpath("//*[@id='lg']/img")
#     actionChains = ActionChains(driver)
    #ActionChains模块支持，右键，鼠标悬停，拖拽，双击等动作 context_click()  右击
    #double_click()   双击
    #drag_and_drop()  拖动
    # actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    # driver.execute_script("window.alert('这是一个alert弹框。');")
#     driver.get("https://tieba.baidu.com/index.html")
#     time.sleep(1)
#
#     target_elem = driver.find_element_by_link_text("地区")
#     driver.execute_script("return arguments[0].scrollIntoView();",target_elem) # 用目标元素参考去拖动
#     #driver.execute_script("scroll(0,2400)") # 这个是第二种方法，比较粗劣，大概的拖动
#
#     print("success")
# except:
#     print("fail")




# 多窗口切换
# driver.get('http://news.baidu.com')
# time.sleep(1)
#
# driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
# print('输出当前窗口句柄',driver.current_window_handle)  # 输出当前窗口句柄
# handles = driver.window_handles # 获取当前全部窗口句柄集合
# print('输出句柄集合',handles) # 输出句柄集合
#
# for handle in handles:# 切换窗口
#     if handle != driver.current_window_handle:
#         print('switch to second window',handle)
#         driver.close() # 关闭第一个窗口
#         driver.switch_to.window(handle) #切换到第二个窗口
#处理Alert弹窗
# driver.get("https://www.baidu.com")
# time.sleep(1)
# driver.execute_script("window.alert('这是一个测试Alert弹窗');")
# time.sleep(2)
# driver.switch_to_alert().accept()  # 点击弹出里面的确定按钮
# #driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮

# #获取当前页面全部图片信息  图片信息可能包括，图片名称，图片大小
# driver.get("http://news.baidu.com")
# time.sleep(1)
#
# for image in driver.find_elements_by_tag_name("img"):
#     print ('text:',image.text)
#     print ('size:',image.size)
#     print ('tag_name:',image.tag_name)
# #  会在桌面保存一张百度新闻首页的截图，图片后缀是png。注意路径是要两个\\
# driver.get_screenshot_as_file("C:\\Users\\lenovo\\Desktop\\baidu.png")
# driver.quit()


# driver.get("https://www.baidu.com")
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys("selenium")
# time.sleep(1)
# print(driver.title)
# try:
#     assert 'selenium' in driver.title
#     print ('Test pass.')
# except Exception as e:
#     print ('Test fail.')
#     print(driver.title)
#
# import  os
# file_path = os.path.dirname(os.path.abspath('.'))  # 上一级目录
# print('file_path:',file_path)
# path1=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
# print('path1:',path1)
# path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径
# print('path2:',path2)
#
# print("OS:" , os.name)
# # print("split:", os.path.split(test002))
# print("splitext:", os.path.splitext(test002))
# print("dirname:", os.path.basename(test002))
# print("basename:" + os.path.basename(test002))

# import time
# from selenium import webdriver
#
# driver = webdriver.Firefox() # 打开chrome，如果没有安装chrome,换成webdriver.Firefox()
# driver.maximize_window()    # 最大化浏览器窗口
# driver.implicitly_wait(8)   # 设置隐式时间等待
#
# driver.get("https://www.baidu.com")  # 地址栏输入百度地址
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")  # 搜索输入框输入Selenium
# driver.find_element_by_xpath("//*[@id='su']").click()  #点击百度一下按钮
#
# # 导入time模块，等待2秒
#
# time.sleep(2)
# # 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# # 这里采用了相对元素定位方法/../
# # 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。
# /html/body/div[1]/div[1]/div/div[1]/div/form/span[1]
# /html/body/div[1]/div[5]/div[1]/div[3]/div[2]/h3/a
# driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()
# # driver.quit()
# import  random
# from selenium.webdriver.common.keys import  Keys
#
# driver=webdriver.Firefox()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("http://www.baidu.com/")
# source=driver.find_element_by_id("su")
# targe=driver.find_element_by_name("tj_trnews")
# # nums=random.randint(1,5)
# nums=3
# if nums == 1:
#     ActionChains(driver).context_click(source).perform()
#     print("鼠标右击【百度一下】按钮")
# elif nums == 2:
#     ActionChains(driver).double_click(source).perform()
#     print("鼠标双击【百度一下】按钮")
# elif nums == 3:
#     ActionChains(driver).drag_and_drop(targe,source).perform()
#     print("拖动【百度一下】按钮")
# elif nums==4:
#     ActionChains(driver).move_to_element(source).perform()
#     print("鼠标悬停在【百度一下】按钮上")
# elif nums == 5:
#     ActionChains(driver).click_and_hold(source).perform()
#     print("在【百度一下】按钮上点击鼠标左键")
# else:
#     print("An error has occurred")
#
# # print("警告信息：",driver.switch_to_alert().text())
# # alert=driver.switch_to_alert()
# alert=driver.switch_to.alert()
# print("alert:",alert)

import  random
# # l=[]
# a=[1,3,4]
# l=random.choice([1,5,6])
# print(l)
# a=random.choice('12345678')
# if  (a == 1) || ( a == 2) :
#     print(a)
# else:
#     print('22222222')
#
# a={1,5,6}
# if bUN
import requests
from selenium import  webdriver
import time
#登录
def login(driver,userid,password):
    driver.get("https://github.com/login")
    driver.implicitly_wait(15)
    driver.find_element_by_id("login_field").send_keys(userid)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("commit").click()

#核对登入用户名  avatar
def check_username(driver,username):
    time.sleep(3)
    # # 点右上角设置
    # driver.find_element_by_css_selector(".HeaderNavlink.name.mt-1").click()
    # time.sleep(3)
    # uservalue =driver.find_element_by_class_name("css-truncate-target").text
    # driver.find_element_by_link_text()
    # # uservalue = driver.find_element_by_css_selector(".css-truncate-target").text
    #点右上角设置:                       body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > summary > span
    driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0 > details > summary > span").click()
    #获取用户名
    getname = driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0 > details > details-menu > div.header-nav-current-user.css-truncate > a > strong").text
    print("getname:",getname)
    if getname == username:
        print("check username is right:")
    else:
        print("check username is fail:")
    # driver.find_element_by_xpath("//*[@id="user-links"]/li[3]/details/details-menu/div[1]/a/strong").json
#user-links > li:nth-child(3) > details > details-menu > div.header-nav-current-user.css-truncate > a > strong
def logout(driver):
    '''退出github'''
    time.sleep(3)
    # 点右上角设置
    driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0 > details > summary > span").click()
    driver.find_element_by_css_selector(".dropdown-item dropdown-signout").cleck()
    print("退出")
    driver.quit()

if __name__ == "__main__":
    driver=webdriver.Firefox()
    login(driver,"hehewzq0131","it789123")
    # driver.find_element_by_link_text()
    # driver.find_elements_by_css_selector("strong.css-truncate-target")
    username = "hehewzq0131"
    check_username(driver,username)
    # logout(driver)
    driver.quit()
