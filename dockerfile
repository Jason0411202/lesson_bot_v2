# 使用輕量級的基礎鏡像
FROM python:3.11-alpine AS builder

# 設置工作目錄
WORKDIR /usr/src/app

# 安裝依賴
RUN apk --no-cache add build-base \
    && pip install --no-cache-dir beautifulsoup4 numpy requests python-dotenv easyocr \
    && apk del build-base

# 第二階段，使用更小的基礎鏡像
FROM python:3.11-alpine

# 設置工作目錄
WORKDIR /usr/src/app

# 從第一階段複製依賴
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# 複製其他文件
COPY . .

# 暴露應用程式需要的端口
EXPOSE 80

# 執行 Python 腳本
CMD ["python", "bot.py"]
