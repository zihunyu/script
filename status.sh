#!/bin/bash

for i in {bdip-tomcat,bdip-oauth2,gateway,redis,rabbitmq,nacos}
  do
   count=`ps -ef |grep $i | grep -v grep |wc -l`
   if [ $count -eq 0 ];then
	sh /shell/token.sh $i
   fi
done