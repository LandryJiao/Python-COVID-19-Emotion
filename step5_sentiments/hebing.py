import csv,re
import os
# from weibo_preprocess_toolkit import WeiboPreprocess

path = '../step1_comments_spider/data/整理完成/新京报/'
empty = []
csv_file1 = open('seg.csv',encoding='utf-8')  # 打开csv文件
csv_file2 = open('seg.csv',encoding='utf-8')  # 打开csv文件
csv_reader_lines1 = csv.reader(csv_file1)  # 逐行读取csv文件
csv_reader_lines2 = csv.reader(csv_file2)  # 逐行读取csv文件
# preprocess = WeiboPreprocess()
for one_line1 in csv_reader_lines1:
    with open('learn.csv', 'a+') as w:
        text = re.sub(r'[a-zA-Z0-9]', "", str(one_line1))
        text = re.sub(r'!', "", text)
        text = re.sub(r'\[', "", text)
        w.write(text)
        w.write("\n")