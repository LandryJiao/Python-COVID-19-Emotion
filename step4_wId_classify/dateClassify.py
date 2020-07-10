import csv
import os
import re

path = 'allComments'
filelist = os.listdir(path)  # 存储了所有的csv文件名
lines = 0
for filename in filelist:
    newpath = path + "\\" + filename  # 代表绝对路径
    reader = csv.reader(open(newpath, "r", encoding='utf-8'))  # 读取csv文件

    for item in reader:  # 读取每一行
        if item[1] == '评论者昵称':
            continue
        filename = item[9]
        # print(filename)
        searchObj = re.match(r'2020/(.*)/(.*) .*', filename, re.M | re.I)
        if searchObj:
            name =  str(searchObj.group(1)+'.'+searchObj.group(2))
            fo = open('dateClassify\\'+name+'.csv', "a+", encoding='utf-8')
        else:

            searchObj = re.match(r'2020-0(.*)-(.*) .*', filename, re.M | re.I)
            name = str(searchObj.group(1) + '.' + searchObj.group(2))
            fo = open('dateClassify\\'+name+'.csv', "a+", encoding='utf-8')
        item[1] = re.sub(r',', "，", item[1])
        item[7] = re.sub(r',', "，", item[7])
        fo.write(item[0]+','+item[1]+','+item[2]+','+item[3]+','+item[4]+','+item[5]+','+item[6]+','+item[7]+','+item[8]+','+item[9])
        fo.write('\n')
        lines += 1  # 提示进程
        if lines % 10000 == 0:
            print('处理', lines, '条')
print("finish")
