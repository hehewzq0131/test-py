from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import  time


class TestBaidu(unittest.TestCase):
    def setUp(self):
        browser_engine = BrowerEngine(self)
        self.driver = browser_engine.get_browser()
        print(browser_engine)
        print(self.driver)
        print(browser_engine)

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys("beijeeeeeeeeeeeeing")
        #  element_to_be_clickable(locator)是等待页面元素可见的时候操作
        element = WebDriverWait(self.driver, 0.01).until(EC.element_to_be_clickable((By.ID, "kw")))
        print("hello")
        self.driver.find_element_by_id('kw').send_keys("beijing")
        print("!!!!11")

class BrowerEngine:
    def __init__(self,driver):
        self.driver = driver
    brower_type = 'Firefox'

    def get_browser(self):
        # if self.brower_type == 'Chrome':
        #     driver = webdriver.Chrome("D:/software/python/py3.5.3/Scripts/chromedriver.exe")
        if self.brower_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.brower_type == 'IE':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()
        return driver


if __name__ == '__main__':
    unittest.main()