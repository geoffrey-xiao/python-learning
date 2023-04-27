import shutil

# 复制文件，可重命名 copy2() copyfile()
# shutil.copy('./1.txt','./aaa/a.txt')

# 复制文件夹，新复制的文件夹必须不存在
# shutil.copytree('./aaa','./b')

# 删除文件夹
# shutil.rmtree('./b')

# move() 移动文件到指定文件夹 可用来修改文件或者文件夹名称

shutil.move('./aaa/aaa.txt','./bb')