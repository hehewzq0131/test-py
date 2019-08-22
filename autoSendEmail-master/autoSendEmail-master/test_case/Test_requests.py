import http.client
import requests
import unittest
import json



#连接接口IP端口
# coon=http.client.HTTPConnection('http://180.167.180.52:11080')

# data={"brokerId":"10003"}
# url='http://180.167.180.52:11080/exchangeApi/user/login?brokerId=10003'
# res=requests.get(url,header)
# print(res.content().read)
# res=coon.request("GET","/exchangeApi/user/login",data,headers='header')

class somedata(unittest.TestCase):
    def setUp(self):
        self.url='http://180.167.180.52:11080/exchangeApi/user/login?brokerId=10003'
        self.headers={
                "Accept":"application/json, text/javascript, */*; q=0.01",
                "Accept-Encoding":"gzip, deflate",
                "accept-language":"zh-CN",
                "authorization":"account-no=hehewzq2009@163.com,login-password=it789123",
                "Content-Type":"application/json; charset=UTF-8",
                "Host":"180.167.180.52:11080",
                "Proxy-Connection":"keep-alive",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                "Referer":"http://180.167.180.52:11080/cn/login.html",
                "X-Requested-With":"XMLHttpRequest",
                "Cookie":"_ga=GA1.1.747534054.1540865057; _gid=GA1.1.860184762.1545187528"
        }

    # 登录接口
    def test_aalogin(self):
        res=requests.get(url=self.url,headers=self.headers)
        rep=res.content.decode('utf-8')
        # print("test_login result:",json.loads(rep))
        print('登录接口获取token:',res.json()["data"]["token"])
        return res.json()["data"]["token"]
    # 查询身份认证信息
    def test_authentication(self):
        url1='http://180.167.180.52:11080/exchangeApi/certification/overseas/basic-authentication-info?brokerId=10003'
        token=self.test_aalogin()
        headers1={
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "authorization":'token='+ token,
            "Content-Type":"application/json; charset=UTF-8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Referer":"http://180.167.180.52:11080/cn/account.html"
        }
        # print('headers1',json.dumps(headers1))
        res=requests.get(url=url1,headers=headers1)
        rep=res.content.decode('utf-8')
        print("身份认证信息:", res.text)
        print("身份认证信息:",json.loads(rep))

    #修改银行卡支付方式的信息
    def test_setpayconfig(self):
        req={
            "bank":"北京壹号",
            "subBank":"北京壹号分行",
            "name":"豆豆",
            "acnumber":"123456789",
            "brokerId":10003
        }
        token=self.test_aalogin()
        headers2={
                "Accept":"*/*",
                "Accept-Encoding":"gzip, deflate, sdch, br",
                "Accept-Language":"zh-CN,zh;q=0.8",
                "Connection":"keep-alive",
                "authorization":"token=" + token + ',pay-password=it789123',
                "Host":"www.baidu.com",
                "Content-Type":"application/json; charset=UTF-8",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
                "Referer":"https://www.baidu.com/duty/privacysettings.html"
        }
        print('headers2',json.dumps(headers2))
        con=requests.post(url='http://180.167.180.52:11080/c2cApi/payconfig/c2cbank-config',json=req,headers=headers2)
        print('银行卡支付方式的信息',con.content.decode('utf-8'))
        # print('ceshi',con.json())

if __name__ == "__main__":
    unittest.main()

