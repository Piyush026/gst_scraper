import requests

# url = 'https://httpbin.org/ip'
# proxy = "5.61.58.211:4037:BR"
# response = requests.get(url, proxies={"http": proxy, "https": proxy})
# print(response.json())
# proxy_list = []
def proxylist():
    url = "http://proxy.link/list/get/e40abb7f2ead053db343dd8e82e04ad7?geo=true"
    response = requests.get(url)
    proxy_list = (response.text.split('\n'))
    print(proxy_list)
    return proxy_list
# print(proxy_list)
# print(proxy_list)
# for x in proxy_list:
#     print(x)