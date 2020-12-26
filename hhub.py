import requests

url = 'https://httpbin.org/ip'
proxy = "5.61.58.211:4037:BR"
response = requests.get(url, proxies={"http": proxy, "https": proxy})
print(response.json())
#
# import os
#
# os.system("restart")
