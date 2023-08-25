import base64
import requests
import time
from html_parse import html_parse
import consts



def main():
    url = consts.Url+consts.UrlEnd_shanghai

    while True:
        # Get image
        imageData = html_parse.query_page(
            url=url
        )
        if len(imageData) < 100:
            print("get image failed, next")
            continue

        decoded = base64.b64decode(imageData)

        submit_form(captchaText="test")

        time.sleep(5)
        #output img
        




def submit_form(captchaText):
    url = "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "captchaText": captchaText,  # 替换为你要提交的验证码文本
        "rebooking": "",
        "token": "",
        "lastname": "",
        "firstname": "",
        "email": "",
        "locationCode": "shan",
        "realmId": "96",
        "categoryId": "558",
        "openingPeriodId": "",
        "date": "",
        "dateStr": "",
        "action:appointment_showMonth": "Continue"
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # 检查请求是否成功
    print(response.content)

    # 处理响应数据
    # ...


if __name__ == "__main__":
    main()

