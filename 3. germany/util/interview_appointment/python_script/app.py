import base64
import requests
import time
from datetime import datetime
import logging
import os
from html_parse import html_parse
from ddddocr_util import pp
from file_util import file_util
from file_util import file_name_util
from logs import log
import consts

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
logger.addHandler(log.get_log_file_handler())

def main():
    config = consts.ShanghaiConfig
    url = config["url"] #consts.Url+consts.UrlEnd_shanghai
    # data str: 23.10.2023
    config["dateStr"] = '02.10.2023'

    while True:
        session = requests.Session()
        # Get image
        imageData = html_parse.query_page(session=session,url=url)
        if len(imageData) < 100:
            print("get image failed, next")
            continue

        decoded = base64.b64decode(imageData)
        file_util.write_file_to_folder("img.jpg", decoded, "./img")

        # Parse code
        code = pp.ocr_img(decoded)
        if code == '' or len(code)!= 6:
            print("ocr code len not 6, next")
            time.sleep(3)
            continue
        
        time.sleep(15) # this gap is needed by the page, or the page response 'code not write'

        for i in range(0,2): 
            # show month
            html = submit_form(session=session,captchaText=code,config=config)
            file_util.write_file_to_folder("after_post.html", html, "./img")

            if html is '':
                continue

            str_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # if has avaiable
            if 'Bitte geben Sie hier den Text ein, den Sie im Bild über diesem Feld sehen' in html.decode('utf-8'):
                print(str_time+"【验证码错误】"+config["locationCode"])
                logger.info("【验证码错误】"+config["locationCode"])
                break
            elif html.decode('utf-8').count('onclick="return startCommitRequest();"') > 2:
                print(str_time+"【有坑位！】"+config["locationCode"])
                logger.info("【有坑位！】"+config["locationCode"])
                file_util.write_file_to_folder(code+"_"+file_name_util.hash_verification_code(code)+".jpg", decoded, "./img_ok")
                break
            else:
                # 字符串不存在于response.content中
                print(str_time+"【无】"+config["locationCode"])
                logger.info("【无】"+config["locationCode"])
                # file_util.write_file_to_folder(code+"_"+file_name_util.hash_verification_code(code)+".jpg", decoded, "./img_ok")
                break
        
        #time.sleep(1)
        #output img
        




def submit_form(session:requests.Session,captchaText:str,config):
    url = "https://service2.diplo.de/rktermin/extern/appointment_showMonth.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        # "captchaText": captchaText,  # 替换为你要提交的验证码文本
        "rebooking": "",
        "token": "",
        "lastname": "",
        "firstname": "",
        "email": "",
        "locationCode": config['locationCode'],
        "realmId": config['realmId'],
        "categoryId": config['categoryId'],
        "openingPeriodId": "",
        "date": "",
        "dateStr": config["dateStr"],
        "action:appointment_showMonth": "Continue"
    }
    if captchaText is not "":
        data["captchaText"] = captchaText


    try:
        response = session.post(url, headers=headers, data=data,timeout=5)
        response.raise_for_status()  # 检查请求是否成功
    except:
        print("request failed, please check")
        return ""
    return response.content

    # 处理响应数据
    # ...


if __name__ == "__main__":
    main()




