import csv
import os

path = 'predictnon'
filelist = os.listdir(path)  # 存储了所有的csv文件名
anger = []
disgust = []
fear = []
happiness = []
like = []
sadness = []
surprise = []
null =[]

for filename in filelist:
    newpath = path + "\\" + filename  # 代表绝对路径
    reader = csv.reader(open(newpath, "r", encoding='utf-8'))  # 读取csv文件
    angercount = 0
    disgustcount = 0
    fearcount = 0
    happinesscount = 0
    likecount = 0
    sadnesscount = 0
    surprisecount = 0
    nullcount = 0
    for item in reader:  # 读取每一行
        if item[1] == 'anger':
            angercount = angercount + 1
        if item[1] == 'disgust':
            disgustcount = disgustcount + 1
        if item[1] == 'fear':
            fearcount = fearcount + 1
        if item[1] == 'happiness':
            happinesscount = happinesscount + 1
        if item[1] == 'like':
            likecount = likecount + 1
        if item[1] == 'sadness':
            sadnesscount = sadnesscount + 1
        if item[1] == 'surprise':
            surprisecount = surprisecount + 1
        if item[1] == 'nulls':
            nullcount = nullcount + 1
    anger.append(angercount)
    disgust.append(disgustcount)
    fear.append(fearcount)
    happiness.append(happinesscount)
    like.append(likecount)
    sadness.append(sadnesscount)
    surprise.append(surprisecount)
    null.append(nullcount)


print(anger)
print(disgust)
print(fear)
print(happiness)
print(like)
print(sadness)
print(surprise)
print(null)