# 使用 Python 官方提供的基礎映像
FROM python:3.11-slim

# 安装 Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr

# 设置環境變數
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

# 設置工作目錄
WORKDIR /usr/src/app

# 将本地目录下的所有文件都拷贝到容器的工作目录下
COPY . .

# 將 ccu.traineddata 拷貝到 /usr/share/tesseract-ocr/4.00/tessdata
COPY ccu.traineddata /usr/share/tesseract-ocr/5/tessdata

# 安装依赖
RUN pip install requests BeautifulSoup4 python-dotenv pytesseract

# 暴露应用程序需要的端口
EXPOSE 80

# 执行 Python 脚本
CMD ["python", "bot.py"]
