from lxml import  etree


html='''
<head>
  <meta charset="UTF-8">
  <title>安间公寓管理系统</title>
  <meta http-equiv="pragma" content="no-cache">
  <meta http-equiv="cache-control" content="no-cache">
  <meta http-equiv="expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <link rel="icon" href='/favicon.ico' type="image/x-icon" />

'''
parse= etree.HTML(html)
node=parse.xpath("//head")
for p in node:
    print(p.attrib,p.text)
