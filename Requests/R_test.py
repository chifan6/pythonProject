import requests

url = "https://www.glnc.edu.cn/"
result = requests.get(url)
print(result.content.decode())
file = open("test.txt","w",encoding='utf-8')
context = str(result)
file.write(result.content.decode())

file.close()

