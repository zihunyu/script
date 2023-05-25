#! /bin/bash
text=$1
curl 'https://oapi.dingtalk.com/robot/send?access_token=dbcde7*****e1efb4a1e0539f2046fa0c3c1643d6add11af14ecd1edaa578e' \
   -H 'Content-Type: application/json' \
   -d '{"msgtype": "text", 
        "text": {
             "content": "'"平台：生产bdip主服务
$text 服务挂了！！！ 需要尽快恢复。
"'"
        },
  "at":{
  "atMobiles":[
  "'"$1"'"
],
  "isAtAll":false
}
      }'