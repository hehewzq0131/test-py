import configparser
import  os
import codecs

cf=configparser.ConfigParser()
# curfolder=os.path.dirname(os.path.abspath('.'))
# curfolder = os.getcwd()
# print('curfolder:',curfolder)
# conf_foleder = curfolder + '\config\ConfigParserceshi.ini'
conf_foleder = os.getcwd() + '\config\ConfigParserceshi.ini'
# print('conf_foleder:',conf_foleder)
cf.read(conf_foleder,encoding='utf-8')

# file_path= r'D:\study\python\autoSendEmail-master\autoSendEmail-master\test_case\config\ConfigParserceshi.ini'
# cf.read(file_path,encoding="utf-8")
#返回所有的section
s = cf.sections()
print("section:",s)

# 列表 展示， 元素以key值为元祖形式显示
print("*"* 70 )
cf.options('mysql')
o1 = cf.options("mysql")
print("options:mysql",o1)
o2 = cf.options("个人信息")
print("options:个人信息",o2)
o3 = cf.options("add")
print("options:add",o3)
o4 = cf.options("del")
print("options:del",o4)

# 列表形式展示，元素值包括key 和 value，以元祖形式显示
print("*" * 70)
v1 = cf.items("mysql")
print("items:mysql",v1)
v2 = cf.items("个人信息")
print("items:个人信息",v2)
v3 = cf.items("add")
print("items:add",v3)
v4 = cf.items("del")
print("items:del",v4)


#  结果：key: value
print("*" * 70)
db_host = cf.get("mysql","db_host")
db_port = cf.getint("mysql","db_port")
db_user = cf.get("mysql","db_user")
db_pass = cf.get("mysql","db_pass")

my_name = cf.get("个人信息","name")
my_age = cf.get("个人信息","age")
my_address = cf.get("个人信息","address")
my_tel = cf.get("个人信息","tel")

print("db_host:",db_host)
print("db_port:",db_port)
print("db_user:",db_user)
print("db_pass:",db_pass)
print("")
print("my_name:",my_name)
print("my_age:",my_age)
print("my_address:",my_address)
print("my_tel:",my_tel)

print("*" * 60)
#添加[add]
#cf.add_section("addd")
#cf.write(open("ConfigParser.conf","w"))

if cf.has_section("addd"):
    print("有了 [addd] 了!")
else :
    print("没有 [addd] !!现在开始写入:")
    cf.add_section("addd")
    cf.set("addd","addd1","addd1的值")
    cf.set("addd","addd2","addd2的值")
    cf.write(open("config/ConfigParserceshi.ini","w",encoding='utf-8'))
    print("[addd] 写入完成")

#删除一个option
#cf.remove_opetion("del","del2")
#cf.write(open("ConfigParser.conf","w"))
if cf.has_option("del","del2"):
    print("有del2,现在开始删除:")
    cf.remove_option("del","del2");
    cf.write(open("config/ConfigParserceshi.ini","w",encoding='utf-8'))
    print(" [del]下的 del2 已经被删除!")
else:
    print(" [del]下没有 del2了")

#删除section[dele]
#cf.remove_section("dele")
#cf.write(open("ConfigParser.conf","w"))
if cf.has_section("dele"):
    print("有 [dele] 了，开始删除：")
    cf.remove_section("dele")
    cf.write(open("config/ConfigParserceshi.ini","w",encoding='utf-8'))
    print("删除 [dele] 成功")
else:
    print("没有[dele],不需处理！")

if cf.has_section("baidu"):
    print("有 baidu 的 section:")
else:
    cf.add_section("baidu")
    cf.set("baidu","baiduwangpan","big red")
    cf.set("baidu","baidutieba","little  house")
    cf.write(open("config/ConfigParserceshi.ini","w",encoding='utf-8'))
    print("[baidu] write complete")
#修改一个option
#使用set()和新增加一样，这里不再写了
#cf.set("section","option","新值")
