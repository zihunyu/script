#coding:utf-8
import json
import requests
import sys
import os
import time


url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=276fa48******60e-6f6bfc938704'

headers={"Content-Type":"application/json;charset=utf-8"}

def msg(text):
    json_text= {
        "msgtype":"text",
        "at":{

            "isAtall":"true"
        },
        "text":{
            "content": text
        }
    }

    print(requests.post(url,json.dumps(json_text),headers=headers).content)

if __name__ == '__main__':
    data = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    text = "发布平台: " + "5.0后端" + "\n" + "环境: " + "生产环境" +"\n" + "发布时间: " + time.strftime("%Y-%m-%d", time.localtime()) + " " + time.strftime("%H:%M", time.localtime()) + "\n"  
    msg(text)