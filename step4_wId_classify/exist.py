import csv
import os
import shutil

path = '../step1_comments_spider/data/整理完成/新京报/'
empty = []
csv_file = open('新京报.csv',encoding='utf-8')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
for one_line in csv_reader_lines:
    if os.path.exists(path+str(one_line[0])+'.csv'):  # 检查是否存在文件
        # shutil.move(path+str(one_line[0])+'.csv', 'C:/Users/a5011/Desktop/毕设_微博情感分析/毕设_微博情感分析/code/step1_comments_spider/data/copy')
        continue
    else:empty.append(one_line[0])
print(empty)