import base64
import requests
import re



def query_page(url):
    # Send POST request to get HTML page
    response = requests.post(url,
                             headers={
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                                 "Content-Type": "application/x-www-form-urlencoded"
                             }, data={})
    if response.status_code != 200:
        print("POST request failed:", response.status_code)
        return ""

    html = response.text
    imageTag, imageData = extract_captcha_info(html)
    if imageTag == "" or imageData == "":
        print("Failed to extract captcha information")
        return ""

    # print("Captcha image data:", imageData)
    return imageData


def extract_captcha_info(html):
    captchaDivRegex = re.compile(r"url\('data:image\/\w+;base64,([^']+)'\)")
    match = captchaDivRegex.search(html)
    if match and len(match.groups()) == 1:
        return match.group(0), match.group(1)
    return "", ""