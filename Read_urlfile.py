

'''import requests
data=int(input("Enput url file name"))
data=requests.get('https://drive.google.com/file/d/1rpEhCVSytq_AXAiLsXenmrgEAEJOllFC/view')
print(data.text)'''

import urllib.request
# url="https://drive.google.com/file/d/1rpEhCVSytq_AXAiLsXenmrgEAEJOllFC/view"
file=urllib.request.urlopen(url)
decode_line=line.decode("utf-8").strip()
print(decode_line)
