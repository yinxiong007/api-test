'''fr.read()           #读取所有内容
    fr.readline()       #读取一行
    fr.readlines()      #读取所有文件内容，返回一个list
    #以上三个命令在大文件时慎用，会把内容读到内存中，占用大内存
    fr.seek(0)          #当前文件指针位置在0位
    fr.writelines(["a","b"])    #把列表写入文件'''

import getpathInfo
import os
import gzip
path = getpathInfo.get_Path()
print(path)
caseListFile = os.path.join(path, "caselist.txt")
print(caseListFile)
fb = open(caseListFile)
#print(fb.readlines()) #读取文件所有行,返回一个list
caseList = []
for value in fb.readlines():
       data = str(value)
       if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
           caseList.append(data.replace("\n", ""))
           print(caseList)

for case in caseList:
    case_name = case.split('/')[-1]
    print(case_name+'.py')

'''''#修改文件
with open(caseListFile,'r+') as f:
    re = f.read()
    new_re = re.replace('app','user')
    f.seek(0)
    f.truncate()
    f.write(new_re)
    #f.flush()
    print(new_re)

str = '#user'
print(not str.startswith('#'))'''

