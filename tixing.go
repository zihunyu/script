package pkg

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
)

type Message struct {
	MsgType string `json:"msgtype"`
	Text    struct {
		Content string `json:"content"`
	} `json:"text"`
}

func QiyeWeChat(next string) {
	// 企业微信机器人 webhook 地址
	webhookUrl := "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=98****996-4004-a874-e9b443a3976a"

	// 要发送的消息
	message := Message{
		MsgType: "text",
		Text: struct {
			Content string `json:"content"`
		}{Content: next},
	}

	// 将消息编码成 JSON 格式
	messageJson, err := json.Marshal(message)
	if err != nil {
		fmt.Println("Failed to marshal message:", err)
		return
	}

	// 发送 HTTP POST 请求
	resp, err := http.Post(webhookUrl, "application/json", bytes.NewReader(messageJson))
	if err != nil {
		fmt.Println("Failed to send request:", err)
		return
	}
	defer resp.Body.Close()

	// 处理响应
	if resp.StatusCode != http.StatusOK {
		fmt.Println("Failed to send message, status code:", resp.StatusCode)
		return
	}

}
