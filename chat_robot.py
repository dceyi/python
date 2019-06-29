#!/user/bin/env python3
# -*- coding: utf-8 -*-

# import os
# import sys
import urllib.request
import urllib.parse
import time

def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定回复，对非特定问题进行智能回复

    参数描述：
    question 聊天内容或问题

    返回值：str， 回复内容
    '''

    if "你叫什么名字" in question:
        answer = "我叫DC"
    elif "你多少岁" in question:
        answer = "18"
    elif "你是MM还是GG" in question:
        answer = "你猜啊"
    elif "聊天结束" in question:
        answer = "好的，再见。下次再找我玩鸭！"
        exit()
    else:
        try:
            # 调用NLP接口实现智能恢复
            params = urllib.parse.urlencode({b'msg': question.encode()}).encode()  #接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",params, method="POST")  # 创建请求
            answer = urllib.request.urlopen(req).read().decode()  # 调用接口（即向目标服务器发出HTTP请求，并获取服务器的的响应数据）
        except Exception as e:
            answer = "AI机器人出现故障！（原因: %s）" % e

    return answer


 # 测试get_robot_reply   
if __name__ == '__main__':
    # print(get_robot_reply("你叫什么名字"))
    # print(get_robot_reply("武汉明天天气如何"))
    # print(get_robot_reply("你是男是女"))
    while True:
        data = input("\n我说:")
        print("\n小魔仙说: %s" % get_robot_reply(data))
        time.sleep(0.1)