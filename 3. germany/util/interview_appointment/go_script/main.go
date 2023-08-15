package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"regexp"
	"strings"
)

func main() {
	// 发送POST请求获取HTML页面
	url := "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=shan&realmId=96&categoryId=558"
	resp, err := http.Post(url, "application/x-www-form-urlencoded", strings.NewReader(""))
	if err != nil {
		fmt.Println("POST请求失败:", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("读取响应失败:", err)
		return
	}

	// 解析HTML页面
	html := string(body)
	captchaDivID, captchaStyleURL := extractCaptchaInfo(html)
	if captchaDivID == "" || captchaStyleURL == "" {
		fmt.Println("无法提取验证码信息")
		return
	}

	// 获取验证码图片数据
	captchaDataURL := extractCaptchaDataURL(captchaStyleURL)
	if captchaDataURL == "" {
		fmt.Println("无法提取验证码图片数据URL")
		return
	}

	captchaImageBytes, err := fetchCaptchaImage(captchaDataURL)
	if err != nil {
		fmt.Println("获取验证码图片数据失败:", err)
		return
	}

	fmt.Println("验证码图片数据:", string(captchaImageBytes))
}

// 提取验证码div的ID和style URL
func extractCaptchaInfo(html string) (string, string) {
	//
	captchaDivRegex := regexp.MustCompile(`url\('data:image\/\w+;base64,([^']+)'\)`)
	match := captchaDivRegex.FindStringSubmatch(html)
	if len(match) == 3 {
		return match[1], match[2]
	}
	return "", ""
}

// 提取验证码图片数据URL
func extractCaptchaDataURL(styleURL string) string {
	captchaDataURLRegex := regexp.MustCompile(`url\('data:image\/\w+;base64,([^']+)'\)`)
	match := captchaDataURLRegex.FindStringSubmatch(styleURL)
	if len(match) == 2 {
		return match[1]
	}
	return ""
}

// 获取验证码图片数据
func fetchCaptchaImage(captchaDataURL string) ([]byte, error) {
	resp, err := http.Get(captchaDataURL)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return ioutil.ReadAll(resp.Body)

}
