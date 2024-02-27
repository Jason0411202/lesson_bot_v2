# 使用 Python 官方提供的基礎映像
FROM python:3.11-slim

# 設置工作目錄
WORKDIR /usr/src/app

# 將本地目錄下的所有文件都拷貝到容器的工作目錄下
COPY . .

# 安裝依賴
RUN pip install requests BeautifulSoup4 numpy easyocr python-dotenv

# 暴露應用程式需要的端口
EXPOSE 80

# 執行 Python 腳本
CMD ["python", "bot.py"]
