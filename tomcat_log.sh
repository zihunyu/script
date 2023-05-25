#!/bin/sh
#将每天的日志进行分割，并且删除15天以前的日志

#日志文件所在的位置
source_home=/data/bdip5.0/bdip-tomcat/logs
#分割后日志文件所在的位置
dest_home=/data/bdip5.0/bdip-tomcat/logs

#将分割后的日志按照年月份命名
data_time=`date +'%Y-%m-%d'`
cp -p $source_home/catalina.out $dest_home/catalina.out-$data_time

#清空原来的日志
echo '' > $source_home/catalina.out

#删除15天前的日志
find /data/bdip5.0/bdip-tomcat/logs/ -name "*.out*" -mtime +15 |xargs rm