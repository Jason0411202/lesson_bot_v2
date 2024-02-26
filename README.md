# 使用教學
## 填寫環境變數
* 填寫登入選課系統的帳密
* 填寫選課系統 request payload
  1. 來到要選的課程頁面，按下 F12，選擇 "網路"
  ![alt text](images/image.png)
  1. 點選要選的課程，按下送出，留意多出來的 .cgi
  ![alt text](images/image-1.png)
  1. 點擊該 .cgi，選擇 "酬載"，複製其中全部的內容
  ![alt text](images/image-3.png)
  1. 請 chatGPT 轉成 JSON 格式後，填入 `PAYLOAD` 變數

範例:
```env
# 選課系統帳號
ACCOUNT="你的帳號"

# 選課系統密碼
PASSWORD="你的密碼"

# 選課系統 request payload
PAYLOAD={"session_id":"你的 session_id","dept":4104,"grade":1,"cge_cate":"","cge_subcate":"","page":1,"e":0,"m":0,"SelectTag":1,"4100003_01":2,"4101023_01":2,"4101024_01":2,"course":"4101032_01","4101032_01":1,"4101032_02":1,"4101034_01":1,"4101034_02":1,"4101034_03":1,"4101034_04":1,"4101035_01":2}
```

# 執行程式
1. 在電腦上安裝 docker
2. 輸入以下指令
```
docker build -t "lessonbot" .
docker run --env-file .env -d lessonbot
```