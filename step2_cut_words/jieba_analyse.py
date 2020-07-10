import csv
import os
import jieba.analyse
import re
from jieba import analyse
from weibo_preprocess_toolkit import WeiboPreprocess

tfidf = analyse.extract_tags
path = "../step4_wId_classify/dateClassify"  # 所有csv文件所在的文件夹
filelist = os.listdir(path)  # 存储了所有的csv文件名
lines = 0
commends = []
stopwords = {}.fromkeys([line.rstrip() for line in open('dict/Stopword.txt', encoding='utf-8')])
preprocess = WeiboPreprocess()
csv.field_size_limit(500 * 1024 * 1024)
# 预处理、分词、
for filename in filelist:
    newpath = path + "\\" + filename  # 代表绝对路径
    reader = csv.reader(open(newpath, "r", encoding='utf-8'))  # 读取csv文件

    for item in reader:  # 读取每一行
        if item[7] == '评论内容':  # 判断头行
            continue

        lines += 1  # 提示进程
        if lines % 10000 == 0:
            print('处理', lines, '条')

        text = item[7]  # 选择评论数据
        text = preprocess.preprocess(text)
        text = re.sub(r'[a-zA-Z0-9]', "", text)
        text = re.sub(r'组图', "", text)
        text = re.sub(r'回复.*', "", text)
        text = re.sub(r'原图', "", text)
        text = re.sub(r',', "，", text)
        text = re.sub(r'①||②||③||④||⑤||⑥||⑦||⑧||⑨||⑩', "", text)
        text = re.sub(r'\n', "", text)


        # seg = jieba.cut(text)
        #
        # result = []
        # for i in seg:  # 去停用词
        #     if i not in stopwords:
        #         result.append(i)

        fo = open("data_full.dat", "a+", encoding='utf-8')
        # fo = open("cache/" + filename, "a+", encoding='utf-8')
        fo.write(text) #改

        # for j in result:
        #     fo.write(j)
        #     fo.write(' ')

        fo.write('\n')
        fo.close()




# 提取关键词
# for line in open("data_full.dat", encoding='utf-8'):
#
#     text = line
#
#     keywords = tfidf(text, allowPOS=('ns', 'nr', 'nt', 'nz', 'nl', 'n', 'vn', 'vd', 'vg', 'v', 'vf', 'a', 'an', 'i'))
#
#     result = []
#
#     for keyword in keywords:
#         result.append(keyword)
#
#     fo = open("data_keywords.dat", "a+", encoding='utf-8')  # 存放分词数据
#
#     for j in result:
#         fo.write(j)
#         fo.write(' ')
#
#     fo.write('\n')
#     fo.close()
print("Keywords Extraction Done!")