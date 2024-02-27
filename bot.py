import json
import os
import sys
import time
from bs4 import BeautifulSoup
import numpy as np
import requests
from dotenv import load_dotenv
import easyocr

# 從.env文件中載入環境變數
load_dotenv()
ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
PAYLOAD = os.getenv('PAYLOAD')

print(PAYLOAD)

payload = json.loads(PAYLOAD)

def getSessionID():
    failCounter=0
    while(1):
        try:
            # 獲取驗證碼圖片的 URL 及 PHPSESSID
            captcha_image_url = 'https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/captcha.php'
            session = requests.Session()
            captcha_image_response = session.get(captcha_image_url)

            # 取得回應中的cookies
            cookies = session.cookies

            # 輸出所有cookies的名稱和值
            for cookie in cookies:
                print("Cookie名稱:", cookie.name)
                print("Cookie值:", cookie.value)
            
            # 寫入圖片
            with open('captcha.png', 'wb') as f:
                f.write(captcha_image_response.content)

            # 載入圖片並用 EasyOCR 辨識
            reader = easyocr.Reader(['en'])  # 指定要識別的語言，這裡設定了繁體中文和英文
            result = reader.readtext('captcha.png')
            captcha_Text = result[0][1]
            print("captcha_Text: ", captcha_Text)

            # 送出登入請求
            url = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/bookmark.php"
            data = {
                'version': '0',
                'id': ACCOUNT,
                'password': PASSWORD,
                'term': 'on',
                'm': '0',
                'captcha_input': captcha_Text
            }
            cookies = {
                'PHPSESSID': cookies['PHPSESSID']
            }

            # 發送 POST 請求
            session = requests.Session()
            response = session.post(url, data=data, cookies=cookies)
            response.encoding='utf-8'
            print(response.text)
            
            # 取得 response 中的 session_id，若成功則返回，失敗則重試
            soup = BeautifulSoup(response.text, 'html.parser')
            meta = soup.find('meta', {'http-equiv': 'refresh'})
            content = meta['content']
            session = content.split('URL=bookmark.php?session_id=')[1]
            print("login: ", session)
            return session
        except:
            failCounter+=1
            if failCounter>500: # 失敗次數超過500次則退出程式
                print("captcha fail too many times, exit.")
                sys.exit()

def main():
    url = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/Add_Course01.cgi" # request URL
    while(1):
        sessionid = getSessionID()
        for i in range(len(payload)):
            payload[i]['session_id'] = sessionid

        try:
            for i in range(150//len(payload)):
                for j in range(len(payload)):
                    print(payload[j])
                    response = requests.post(url, data=payload[j]) # 發送POST請求
                    response.encoding = 'utf-8'
                    print("響應內容:", response.text) # 印出請求的狀態碼和內容
                    print("本次登入第", i+1, "輪搶課")
                    if "衝堂" in response.text:
                        print("回應中包含 '衝堂', 已搶到課程")

                    time.sleep(0.2)
        except:
            print("發生錯誤，重新開始")
            continue

main()