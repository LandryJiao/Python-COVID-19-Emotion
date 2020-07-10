import requests

requests.packages.urllib3.disable_warnings()

from lxml import etree

from datetime import datetime, timedelta

from threading import Thread

import csv

from math import ceil

import os, time

import re
from time import sleep
from random import randint

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie': ''''''
}

result_headers = [
    '评论者主页',
    '评论者昵称',
    '评论者性别',
    '评论者所在地',
    '评论者微博数',
    '评论者关注数',
    '评论者粉丝数',
    '评论内容',
    '评论获赞数',
    '评论发布时间',
]


def parse_time(publish_time):
    publish_time = publish_time.split('来自')[0]
    if '刚刚' in publish_time:
        publish_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    elif '分钟' in publish_time:
        minute = publish_time[:publish_time.find('分钟')]
        minute = timedelta(minutes=int(minute))
        publish_time = (datetime.now() -
                        minute).strftime('%Y-%m-%d %H:%M')
    elif '今天' in publish_time:
        today = datetime.now().strftime('%Y-%m-%d')
        time = publish_time[3:]
        publish_time = today + ' ' + time
    elif '月' in publish_time:
        year = datetime.now().strftime('%Y')
        month = publish_time[0:2]
        day = publish_time[3:5]
        time = publish_time[7:12]
        publish_time = year + '-' + month + '-' + day + ' ' + time
    else:
        publish_time = publish_time[:16]
    return publish_time


def getPublisherInfo(url):
    try:
        res = requests.get(url=url, headers=headers, verify=False)
        html = etree.HTML(res.text.encode('utf-8'))
        head = html.xpath("//div[@class='ut']/span[1]")[0]
        head = head.xpath('string(.)')[:-3].strip()
        keyIndex = head.index("/")
        nickName = head[0:keyIndex - 2]
        sex = head[keyIndex - 1:keyIndex]
        location = head[keyIndex + 1:]

        footer = html.xpath("//div[@class='tip2']")[0]
        weiboNum = footer.xpath("./span[1]/text()")[0]
        weiboNum = weiboNum[3:-1]
        followingNum = footer.xpath("./a[1]/text()")[0]
        followingNum = followingNum[3:-1]
        followsNum = footer.xpath("./a[2]/text()")[0]
        followsNum = followsNum[3:-1]
        print(nickName, sex, location, weiboNum, followingNum, followsNum)
        return nickName, sex, location, weiboNum, followingNum, followsNum
    except Exception as e:
        print('Error: ', e)


def get_one_comment_struct(comment):
    # xpath 中下标从 1 开始
    try:
        userURL = "https://weibo.cn/{}".format(comment.xpath(".//a[1]/@href")[0])

        content = comment.xpath(".//span[@class='ctt']/text()")
        # '回复' 或者只 @ 人
        if '回复' in content or len(content) == 0:
            test = comment.xpath(".//span[@class='ctt']")
            content = test[0].xpath('string(.)').strip()

            # 以表情包开头造成的 content == 0,文字没有被子标签包裹
            if len(content) == 0:
                content = comment.xpath('string(.)').strip()
                content = content[content.index(':') + 1:]
        else:
            content = content[0]

        praisedNum = comment.xpath(".//span[@class='cc'][1]/a/text()")[0]
        praisedNum = praisedNum[2:praisedNum.rindex(']')]

        publish_time = comment.xpath(".//span[@class='ct']/text()")[0]

        publish_time = parse_time(publish_time)
        nickName, sex, location, weiboNum, followingNum, followsNum = getPublisherInfo(url=userURL)

        return [userURL, nickName, sex, location, weiboNum, followingNum, followsNum, content, praisedNum, publish_time]
    except Exception as e:
        print('Error: ', e)
        print('被检测，等候10分钟继续(2)')
        time.sleep(600)


def write_to_csv(result, isHeader=False):  # 写入csv文件
    with open('comment/' + weiboId + '.csv', 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        if isHeader == True:
            writer.writerows([result_headers])
        writer.writerows(result)
    print('已成功将{}条评论写入{}中'.format(len(result), 'comment/' + weiboId + '.csv'))


def run(weiboId):  # 主程序
    res = requests.get('https://weibo.cn/comment/{}'.format(weiboId), headers=headers, verify=False)
    print('https://weibo.cn/comment/{}'.format(weiboId))

    try:
        commentNum = re.findall("评论\[.*?\]", res.text)[0]
        commentNum = int(commentNum[3:len(commentNum) - 1])
        print(commentNum)
        pageNum = ceil(commentNum / 10)
        print(pageNum)
    except Exception as e:
        print('Error: ', e)
        print('被检测，等候10分钟继续(3)')
        time.sleep(600)

    for page in range(pageNum):

        result = []

        res = requests.get('https://weibo.cn/comment/{}?page={}'.format(weiboId, page + 1), headers=headers,
                           verify=False)

        html = etree.HTML(res.text.encode('utf-8'))

        try:
            comments = html.xpath("/html/body/div[starts-with(@id,'C')]")
        except Exception as e:
            print('Error: ', e)
            print('被检测，等候10分钟继续(4)')
            time.sleep(600)

        print('第{}/{}页'.format(page + 1, pageNum))

        for i in range(len(comments)):
            result.append(get_one_comment_struct(comments[i]))

        if len(result) == 0:
            break

        if page == 0:
            try:
                write_to_csv(result, isHeader=True)
            except Exception as e:
                print('Error: ', e)
        else:
            try:
                write_to_csv(result, isHeader=False)
            except Exception as e:
                print('Error: ', e)

        sleep(randint(1, 5))


if __name__ == "__main__":

    if not os.path.exists('comment'):  # 检查是否存在文件夹
        os.mkdir('comment')

    csv_file = open('id.csv',encoding='utf-8')  # 打开csv文件
    csv_reader_lines = csv.reader(csv_file)  # 逐行读取csv文件
    date = []  # 创建列表准备接收csv各行数据
    sum_line = 0  # 记录总行数

    for one_line in csv_reader_lines:
        date.append(one_line)  # 将读取的csv分行数据按行存入列表‘date’中
        sum_line = sum_line + 1  # 统计行数

    i = 1  # 遍历标记
    while i < sum_line:
        weiboId = str(date[i][0])
        weiboId = re.sub(r'%EF%BB%BF', '', weiboId)  # 处理头字母编码错误
        print('第{}/{}项 ID:{}'.format(i + 1, sum_line, weiboId))  # 访问列表date中的数据验证读取成功
        i = i + 1
        run(weiboId)  # 运行主程序
