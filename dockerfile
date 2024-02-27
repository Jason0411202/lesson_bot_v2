# 使用 Python 官方提供的官方 Docker 鏡像作為基礎鏡像
FROM python:3.11

# 設置工作目錄
WORKDIR /usr/src/app

# 將本地目錄下的所有文件都拷貝到容器的工作目錄下
COPY . .

# 安裝依賴
RUN pip install --no-cache-dir beautifulsoup4 numpy requests python-dotenv easyocr


# 暴露應用程式需要的端口
EXPOSE 80

# 執行 Python 腳本
CMD ["python", "bot.py"]
