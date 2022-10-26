import requests
import json
url='https://fanyi.baidu.com/sug'
aa=input("请输入：")
data={'kw':aa}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
a=requests.post(url,data=data,headers=headers)
b=a.json()
c=aa+'.json'
fp=open(c,'w',encoding='utf-8')     #fp-文件参数
json.dump(b,fp=fp,ensure_ascii=False)
