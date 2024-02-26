import json
import os
import sys
import time
import requests
from dotenv import load_dotenv

# 從.env文件中載入環境變數
load_dotenv()
ACCOUNT = os.getenv('ACCOUNT')
PASSWORD = os.getenv('PASSWORD')
PAYLOAD = os.getenv('PAYLOAD')

print(PAYLOAD)

payload = json.loads(PAYLOAD)

def getSessionID():
    # @蘇 幫我寫這段
    return ""

url = "https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/Add_Course01.cgi" # request URL
while(1):
    payload['session_id'] = getSessionID()

    for i in range(100):
        response = requests.post(url, data=payload) # 發送POST請求
        response.encoding = 'utf-8'
        print("響應內容:", response.text) # 印出請求的狀態碼和內容
        if "衝堂" in response.text:
            print("回應中包含 '衝堂'，退出程式")
            sys.exit()

        time.sleep(5)
