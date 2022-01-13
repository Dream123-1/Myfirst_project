import requests

url = "www.baidu.com"

response = requests.get(url)

print(response.text)



