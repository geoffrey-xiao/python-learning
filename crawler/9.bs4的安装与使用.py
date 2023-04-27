from bs4 import BeautifulSoup

text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title abc="123">豆瓣首页</title>
</head>
<body>
    <ul><li id="java"><a href="/a/b/jva">java工程师</a></li></ul>
    <li><a href="/a/b/jva">python工程师</a></li>
    <li><a href="/a/b/jva" class="web">web工程师</a></li></ul>
</body>
</html>
'''
# 1.通过tag标签获取文本
soup = BeautifulSoup(text, 'lxml')
r = soup.title
# 只返回找到的第一个元素
r = soup.li
r = soup.title['abc']
# print(r)

# 2. 通过搜索获取页面元素 find find_all
# find 只返回第一个 find_all 返回所有
r = soup.find_all('a')

r = soup.find(id="java")
# print(r)

# 3.通过css选择器,返回的是列表

r = soup.select('li')
r = soup.select('#java')
r = soup.select('.web')

r = soup.select('a,title')
print(r)
