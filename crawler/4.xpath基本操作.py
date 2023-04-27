from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul><li><a href="/a/b/jva">java工程师</a></li></ul>
     <ul><li><a href="/a/b/jva">python工程师</a></li></ul>
      <ul><li><a href="/a/b/jva">web工程师</a></li></ul>
</body>
</html>
'''
html = etree.HTML(text)
r = html.xpath('/html/body/ul/li/a/text()')
print(r)
