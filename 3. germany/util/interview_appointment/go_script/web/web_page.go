package web

import (
	"fmt"
	"io"
	"net/http"
	"regexp"
	"strings"
)

func QueryPage() string {
	// 发送POST请求获取HTML页面
	url := "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=shan&realmId=96&categoryId=558"
	resp, err := http.Post(url, "application/x-www-form-urlencoded", strings.NewReader(""))
	if err != nil {
		fmt.Println("POST请求失败:", err)
		return ""
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("读取响应失败:", err)
		return ""
	}

	// 解析HTML页面
	html := string(body)
	imageTag, imageData := extractCaptchaInfo(html)
	if imageTag == "" || imageData == "" {
		fmt.Println("无法提取验证码信息")
		return ""
	}

	fmt.Println("验证码图片数据:", string(imageData))
	return imageData
}

// 提取验证码div的ID和style URL
func extractCaptchaInfo(html string) (string, string) {
	//
	captchaDivRegex := regexp.MustCompile(`url\('data:image\/\w+;base64,([^']+)'\)`)
	match := captchaDivRegex.FindStringSubmatch(html)
	if len(match) == 2 {
		return match[0], match[1]
	}
	return "", ""
}
