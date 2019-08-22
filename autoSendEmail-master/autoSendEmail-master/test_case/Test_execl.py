#__author__ = 'lenovo'
import xlrd
import os
# C:\Users\lenovo\Desktop\111111.xlsx
# D:\study\python\autoSendEmail-master\autoSendEmail-master\data\test0001.xlsx
# dat111 = xlrd.open_workbook(r "C:\Users\lenovo\Desktop\111111.xlsx")[1]
# data = xlrd.open_workbook(r 'C:\Users\lenovo\Desktop\111111.xlsx') [1]

print('当前目录路径：',os.getcwd())
print('上个目录路径:',os.path.abspath('..'))   #获取当前工作的父目录 ！注意是父目录路径
print('获取当前文件的目录路径:',os.path.abspath('Test_execl.py'))
# data=xlrd.open_workbook(r 'os.path.abspath('Test_execl.py')')
prepaths=os.path.abspath('..')
execl_path=os.path.join('D:\study\python\autoSendEmail-master\autoSendEmail-master\data','test0001.xlsx')
print('data dir:',execl_path)
data =  xlrd.open_workbook(logfile=execl_path,verbosity=0)
data.read