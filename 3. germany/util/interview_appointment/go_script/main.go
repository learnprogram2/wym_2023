package main

import (
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	"wangyiming/interview_appointment/ocr"
	"wangyiming/interview_appointment/web"
)

func main() {
	os.ErrInvalid
	ocr.Init()

	for true {
		// get image:
		imageData := web.QueryPage()
		if len(imageData) < 100 {
			fmt.Println("get image failed, next")
			continue
		}
		decoded, err := base64.StdEncoding.DecodeString(imageData)
		if err != nil {
			fmt.Printf("decode base64 image data err:%v\n", err)
			continue
		}
		fmt.Println(decoded)
		err = ioutil.WriteFile("output.jpg", decoded, 0644)
		if err != nil {
			fmt.Println("写文件出错:", err)
			os.Exit(1)b
		}

		// ocr scan
		//err = ocr.OcrCli.SetImageFromBytes(decoded)
		//if err != nil {
		//	fmt.Printf("ocr set image failed err:%v\n", err)
		//	continue
		//}
		//text, err := ocr.OcrCli.Text()
		//if err != nil {
		//	fmt.Printf("ocr parse text err:%v\n", err)
		//	continue
		//}
		//fmt.Println("ocr result" + text)
		//time.Sleep(time.Second * 5)
	}

	
}
