import zipfile
import os
import shutil
# 压缩指定文件
# with zipfile.ZipFile('exam.zip','w') as myzip:
#     myzip.write('./1.txt')
# myzip.write(('./2.txt'))

# 解压文件 默认压缩模式 不压缩文件
# with zipfile.ZipFile('exam.zip','r') as myzip:
# myzip.extractall('./')

# 修改压缩模式

# with zipfile.ZipFile('all.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
#     arr = os.listdir('./')
#     for i in arr:
#         # print(i)
#         myzip.write(i)

# 用shutil压缩文件 zip tar
shutil.make_archive('all2','zip','./')

