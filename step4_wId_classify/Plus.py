import csv
import os
import re

path = '人民日报/'
empty = []
fo = open("人民日报_full.csv", "a+", encoding='utf-8')
fo.write('微博id,标签,微博正文,评论者昵称,评论者性别,评论者所在地,comments,评论发布时间')
fo.write('\n')
csv_file = open('人民日报.csv',encoding='utf-8')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
for news_line in csv_reader_lines:
    if news_line[1] == '微博正文':
        continue
    csv_file2 = open(path+news_line[0]+'.csv', encoding='utf-8')  # 打开csv文件
    csv_reader_lines2 = csv.reader(csv_file2)  # 逐行读取csv文件
    for comment_line in csv_reader_lines2:
        if comment_line[1] == '评论者昵称':
            continue
        if "回复" in comment_line[7]:
            continue
        if news_line[9] == '1':
            classify = '1_小区隔离，不能出门'
        elif news_line[9] == '2':
            classify = '2_患病治愈'
        elif news_line[9] == '3':
            classify = '3_支援建设'
        elif news_line[9] == '4':
            classify = '4_口罩防护'
        elif news_line[9] == '5':
            classify = '5_造谣售假隐瞒'
        elif news_line[9] == '6':
            classify = '6_国家政府采取措施'
        elif news_line[9] == '7':
            classify = '7_期盼战胜疫情'
        elif news_line[9] == '8':
            classify = '8_开学考试'
        elif news_line[9] == '9':
            classify = '9_致敬一线'
        elif news_line[9] == '10':
            classify = '10_病毒研究'
        elif news_line[9] == '11':
            classify = '11_工作失职'
        comment_line[7] = re.sub(r',', "，", comment_line[7])
        comment_line[9] = re.sub(r',', "，", comment_line[9])
        news_line[1] = re.sub(r',', "，", news_line[1])
        fo.write(news_line[0]+','+classify+','+news_line[1]+','+comment_line[1]+','+comment_line[2]+','+comment_line[3]+','+comment_line[7]+','+comment_line[9])
        fo.write('\n')
fo.close()
print("完成")