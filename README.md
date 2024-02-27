# 使用教學
## 填寫環境變數
* 於專案根目錄中創建一個名為 .env 的檔案
* 填寫登入選課系統的帳密 (不要加引號)
* 填寫選課系統 request payload (JSON list 格式)
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
ACCOUNT=你的帳號

# 選課系統密碼
PASSWORD=你的密碼

# 選課系統 request payload
PAYLOAD=[{"session_id":"你的 session_id","dept":"5304","grade":"3","cge_cate":"","cge_subcate":"","page":"1","e":"0","m":"0","SelectTag":"1","5303111_01":"2","5303213_01":"2","5303221_01":"2","5303229_01":"1","5303233_01":"1","5303234_01":"2","course":"5303239_01","5303239_01":"2"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"2","cge_subcate":"6","page":"1","e":"0","m":"0","SelectTag":"1","7201002_01":"3","7204003_01":"3","7204004_01":"3","7303022_01":"3","7407033_01":"3","7500004_01":"3","7500021_01":"3","course":"7500021_02","7500021_02":"3","7501019_01":"3","7502002_01":"3"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"2","cge_subcate":"1","page":"2","e":"0","m":"0","SelectTag":"1","7304030_02":"3","7304031_01":"3","7304031_02":"3","7304033_01":"3","7304034_01":"3","7304034_02":"3","7304035_01":"3","7304036_01":"3","course":"7304038_01","7304038_01":"3","7304041_01":"3"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"2","cge_subcate":"6","page":"2","e":"0","m":"0","SelectTag":"1","7503012_01":"3","7503019_01":"3","course":"7506011_01","7506011_01":"3","7506012_01":"3","7506012_02":"3","7506014_01":"3","7506014_02":"3","7507003_01":"3","7507008_01":"3","7507026_01":"3"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"2","cge_subcate":"6","page":"2","e":"0","m":"0","SelectTag":"1","course":"7503012_01","7503012_01":"3","7503019_01":"3","course":"7506011_01","7506011_01":"3","7506012_01":"3","7506012_02":"3","7506014_01":"3","7506014_02":"3","7507003_01":"3","7507008_01":"3","7507026_01":"3"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"1","cge_subcate":"4","page":"1","e":"0","m":"0","SelectTag":"1","7301023_01":"3","7301027_01":"3","7301036_01":"3","7301036_02":"3","course":"7301036_03","7301036_03":"3","7301037_01":"3","7301037_02":"3","7301039_01":"3","7301041_01":"3","7301043_01":"3"},{"session_id":"你的 session_id"","dept":"I001","grade":"1","cge_cate":"2","cge_subcate":"5","page":"2","e":"0","m":"0","SelectTag":"1","7405019_01":"3","7406015_01":"3","7406018_01":"3","course":"7406018_02","7406018_02":"3","7406032_01":"3","7406032_02":"3","7406035_01":"3","7406036_01":"3"}]
```

# 執行程式
1. 在電腦上安裝 docker
2. 輸入以下指令
windows
```
docker run --env-file .env -d jason0411202/lessonbot-window
```

linux
```
docker run --env-file .env -d jason0411202/lessonbot-linux
```
# 版本資訊
* Python 3.11.3
```
absl-py                       2.0.0
aiohttp                       3.8.4
aiosignal                     1.3.1
annotated-types               0.6.0
anyio                         4.2.0
asgiref                       3.6.0
asttokens                     2.4.0
astunparse                    1.6.3
async-generator               1.10
async-timeout                 4.0.2
attrs                         23.1.0
audioread                     3.0.1
backcall                      0.2.0
beautifulsoup4                4.12.2
blinker                       1.7.0
bs4                           0.0.1
cachetools                    5.3.0
certifi                       2022.12.7
cffi                          1.15.1
charset-normalizer            3.1.0
chromedriver-autoinstaller    0.6.2
click                         8.1.7
colorama                      0.4.6
comm                          0.1.4
contourpy                     1.1.1
cycler                        0.12.0
debugpy                       1.8.0
decorator                     4.4.2
discord                       2.2.3
discord.py                    2.2.3
distro                        1.9.0
Django                        4.2
easyocr                       1.7.1
et-xmlfile                    1.1.0
exceptiongroup                1.1.1
executing                     2.0.0
filelock                      3.9.0
Flask                         3.0.0
flatbuffers                   23.5.26
fonttools                     4.43.0
frozenlist                    1.3.3
fsspec                        2023.4.0
func-timeout                  4.3.5
gast                          0.5.4
google-api-core               2.11.0
google-api-python-client      2.86.0
google-auth                   2.26.2
google-auth-httplib2          0.1.0
google-auth-oauthlib          1.0.0
google-cloud-aiplatform       1.39.0
google-cloud-bigquery         3.16.0
google-cloud-core             2.4.1
google-cloud-resource-manager 1.11.0
google-cloud-storage          2.14.0
google-crc32c                 1.5.0
google-pasta                  0.2.0
google-resumable-media        2.7.0
googleapis-common-protos      1.59.0
grpc-google-iam-v1            0.13.0
grpcio                        1.60.0
grpcio-status                 1.60.0
h11                           0.14.0
h5py                          3.9.0
httpcore                      1.0.2
httplib2                      0.22.0
httpx                         0.26.0
idna                          3.4
imageio                       2.31.6
imageio-ffmpeg                0.4.9
ipykernel                     6.25.2
ipython                       8.16.1
itsdangerous                  2.1.2
jedi                          0.19.1
Jinja2                        3.1.2
joblib                        1.3.2
jupyter_client                8.3.1
jupyter_core                  5.3.2
keras                         2.14.0
kiwisolver                    1.4.5
lazy_loader                   0.3
libclang                      16.0.6
librosa                       0.10.1
llvmlite                      0.41.1
Markdown                      3.4.4
MarkupSafe                    2.1.2
matplotlib                    3.8.0
matplotlib-inline             0.1.6
ml-dtypes                     0.2.0
moviepy                       1.0.3
mpmath                        1.3.0
msgpack                       1.0.7
multidict                     6.0.4
mysql-connector-python        8.3.0
nest-asyncio                  1.5.8
networkx                      3.2.1
ninja                         1.11.1.1
numba                         0.58.1
numpy                         1.26.0
oauthlib                      3.2.2
openai                        1.9.0
opencv-python                 4.8.1.78
opencv-python-headless        4.9.0.80
openpyxl                      3.1.2
opt-einsum                    3.3.0
outcome                       1.2.0
packaging                     23.2
pandas                        2.1.1
parso                         0.8.3
pickleshare                   0.7.5
Pillow                        10.0.1
pip                           23.1.2
platformdirs                  3.11.0
pooch                         1.8.0
proglog                       0.1.10
prompt-toolkit                3.0.39
proto-plus                    1.23.0
protobuf                      4.22.3
psutil                        5.9.5
pure-eval                     0.2.2
pyasn1                        0.5.0
pyasn1-modules                0.3.0
pyclipper                     1.3.0.post5
pycparser                     2.21
pydantic                      2.5.3
pydantic_core                 2.14.6
Pygments                      2.16.1
pyparsing                     3.0.9
pypinyin                      0.49.0
pypng                         0.20220715.0
PySocks                       1.7.1
pytesseract                   0.3.10
python-bidi                   0.4.2
python-dateutil               2.8.2
python-dotenv                 1.0.0
pytz                          2023.3.post1
pywin32                       306
PyYAML                        6.0.1
pyzmq                         25.1.1
Qart                          0.0.1
qrcode                        7.4.2
radian                        0.6.8
rchitect                      0.4.4
requests                      2.29.0
requests-oauthlib             1.3.1
rime                          2.0.0
rsa                           4.9
scikit-image                  0.22.0
scikit-learn                  1.3.2
scipy                         1.11.3
seaborn                       0.13.1
selenium                      4.12.0
setuptools                    65.5.0
shapely                       2.0.2
six                           1.16.0
sklearn                       0.0.post11
sniffio                       1.3.0
sortedcontainers              2.4.0
soundfile                     0.12.1
soupsieve                     2.4.1
soxr                          0.3.7
sqlparse                      0.4.4
stack-data                    0.6.3
sympy                         1.12
tabulate                      0.9.0
tensorboard                   2.14.1
tensorboard-data-server       0.7.1
tensorflow                    2.14.0
tensorflow-estimator          2.14.0
tensorflow-intel              2.14.0
tensorflow-io-gcs-filesystem  0.31.0
termcolor                     2.3.0
threadpoolctl                 3.2.0
tifffile                      2023.9.26
torch                         2.1.2+cu118
torch-tb-profiler             0.4.3
torchaudio                    2.1.2+cu118
torchvision                   0.16.2+cu118
tornado                       6.3.3
tqdm                          4.65.0
traitlets                     5.11.2
trio                          0.22.0
trio-websocket                0.10.2
typing_extensions             4.8.0
tzdata                        2023.3
uritemplate                   4.1.1
urllib3                       1.26.15
vertexai                      0.0.1
wcwidth                       0.2.8
Werkzeug                      3.0.0
wheel                         0.41.2
wrapt                         1.14.1
wsproto                       1.2.0
yarl                          1.9.2
```