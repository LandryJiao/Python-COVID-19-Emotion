import os,csv
import shutil

path = 'C:/Users/a5011/Desktop/毕设_微博情感分析/毕设_微博情感分析/code/step4_wId_themeClassify/环球时报微博id/'
path2 = 'C:/Users/a5011/Desktop/毕设_微博情感分析/毕设_微博情感分析/code/step4_wId_themeClassify/'

if not os.path.exists('themeClassify/1_工作失职'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/1_工作失职')
if not os.path.exists('themeClassify/2_患病治愈'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/2_患病治愈')
if not os.path.exists('themeClassify/3_支援建设'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/3_支援建设')
if not os.path.exists('themeClassify/4_防护'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/4_防护')
if not os.path.exists('themeClassify/5_谣假瞒'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/5_谣假瞒')
if not os.path.exists('themeClassify/6_政府措施'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/6_政府措施')
if not os.path.exists('themeClassify/7_期盼疫情'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/7_期盼疫情')
if not os.path.exists('themeClassify/8_学业复工'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/8_学业复工')
if not os.path.exists('themeClassify/9_致敬一线'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/9_致敬一线')
if not os.path.exists('themeClassify/10_病毒研究'):  # 检查是否存在文件夹
    os.mkdir('themeClassify/10_病毒研究')

csv_file = open('环球时报_predict.csv',encoding='utf-8')  # 打开csv文件
csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
empty = []

for one_line in csv_reader_lines:
    if  one_line[1] == '1_工作失职':
		shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/1_工作失职')
	elif one_line[1] == '2_患病治愈':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/2_患病治愈')
    elif one_line[1] == '3_支援建设':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/3_支援建设')
    elif one_line[1] == '4_防护':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/4_防护')
    elif one_line[1] == '5_谣假瞒':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/5_谣假瞒')
    elif one_line[1] == '6_政府措施':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/6_政府措施')
    elif one_line[1] == '7_期盼疫情':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/7_期盼疫情')
    elif one_line[1] == '8_学业复工':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/8_学业复工')
    elif one_line[1] == '9_致敬一线':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/9_致敬一线')
    elif one_line[1] == '10_病毒研究':
        shutil.move(path+str(one_line[0])+'.csv', path2+'themeClassify/10_病毒研究')
    
        
    else:
        empty.append(one_line[0])

print(empty)
