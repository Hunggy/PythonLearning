import requests

url = "https://api.adviceslip.com/advice"
try:
    resp = requests.get(url)
    data = resp.json()        # 转成字典
    print(data["slip"]["advice"])  # 按键取值

except requests.exceptions.RequestException:
    print("网络出错，请检查连接")