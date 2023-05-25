#coding=utf-8
import schedule
import time
import os


def job():
    num = os.system("ps -ef | grep main.js | grep -v grep |wc -l")
    if num == 0:
        os.system("/usr/bin/nohup /usr/bin/node /data/bdip5.0/websock/lmv_rtc/main.js &")


schedule.every().minute.at(":01").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)