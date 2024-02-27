# 使用 Python 官方提供的基礎映像
FROM python:3.11

# 安裝必要的系統套件和工具
RUN apk --no-cache add build-base

# 設置工作目錄
WORKDIR /usr/src/app

# 將本地目錄下的所有文件都拷貝到容器的工作目錄下
COPY . .

# 安裝依賴
RUN pip install --no-cache-dir beautifulsoup4 numpy requests python-dotenv \
    && pip install --no-cache-dir easyocr==1.7.0 \
    && apk del build-base

# 暴露應用程式需要的端口
EXPOSE 80

# 執行 Python 腳本
CMD ["python", "bot.py"]
