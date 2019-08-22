import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import  Select
import  unittest

# Browser=webdriver.chrome()
class Test_baidu(unittest.TestCase):
    def setUp(self):
        self.Browser=webdriver.Firefox()
        self.Browser.implicitly_wait(10)
        # self.Browser.maximize_window()
        #设置浏览器窗口大小
        # self.Browser.set_window_size(1080,800)
        # Browser.get('https://www.baidu.com/')
        self.url='https://www.baidu.com/'
        self.verificationErrors=[]  #脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert=True  #是否继续接受下一个警告#
        # 搜索用例
    def test_baidu_search(self):
        Browser=self.Browser
        Browser.get(self.url)
        Browser.find_element_by_id("kw").send_keys("你好")
        time.sleep(3)
        Browser.find_element_by_id("kw").clear()
        backspace=Browser.find_element_by_name("wd").send_keys("大豆")
        #退格删除1个字符
        Browser.find_element_by_name("wd").send_keys(Keys.BACK_SPACE)
        # Browser.find_element_by_id("su").click()
        Browser.find_element_by_id("su").submit()
            #设置全集操作超时时间
        # Browser.implicitly_wait(10)
        # print('titel:',Browser.title)
        time.sleep(2)
        Browser.quit()
     #百度搜索页设置
    def test_baidu_search_shezhi(self):
        Browser=self.Browser
        Browser.get(self.url+'gaoji/preferences.html')
        nr=Browser.find_element_by_id("nr")
        nr.find_element_by_xpath("//option[@value='20']").click()
        time.sleep(2)
        Browser.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        n=Browser.switch_to_alert()
        n.accept()
        Browser.quit()
    #高级搜索
    def test_baidu_gaoji_search(self):
        Browser=self.Browser
        Browser.get(self.url+'gaoji/advanced.html')
        Browser.find_element_by_name("q1").send_keys("上海")
        Browser.find_element_by_name("q2").send_keys("世纪远游")
        Browser.find_element_by_xpath("//input[@value='百度一下']").click()
        time.sleep(3)
        Browser.quit()

    def test_down(self):
        self.Browser.quit()
        self.assertEqual([],self.verificationErrors)
        '''
        test_down 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出浏览器等。
        self.assertEqual([], self.verificationErrors) 是个难点，
        对前面verificationErrors方法获得的列表进行比较；如查verificationErrors的列表不为空，输出列表中的报错信息。
        '''


if __name__ =="__main__":
    unittest.main()

