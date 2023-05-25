#coding=utf-8

import schedule
import time
import os



def job():
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    os.system("/usr/bin/mydumper -u root -p ****** -P 3306 -G -R -E -h 192.168.240.42 -B ecology -o /home/data/db_bak/" + date)



#schedule.every().minute.at(":01").do(job)   #每分钟的第一秒执行
schedule.every().day.at("01:00").do(job)   #每天01:00执行
while True:
    schedule.run_pending()
    time.sleep(1)