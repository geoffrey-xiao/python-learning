from lxml import etree

html = etree.parse('./yuan.html', etree.HTMLParser())

r = html.xpath('/html/body/ul/li/a/text()')

# 获取页面中所有li里面的数据
r = html.xpath('//li/a/text()')

# 获取class为teacher里面li的数据
a = html.xpath('//div[@class="teacher"]/ul/li/a/text()')
b = html.xpath('//div[@class="teacher"]/ul/li/a/@href')

c = list(zip(a, b))
print(c)
