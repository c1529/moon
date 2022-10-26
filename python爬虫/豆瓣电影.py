import requests
import json
url='https://movie.douban.com/j/chart/top_list?'
param={'type': '17','interval_id':'100:90','action':'','start':'0','imit':'99'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
res=requests.get(url=url,params=param,headers=headers)
list_data=res.json()
fp=open('./豆瓣.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
//初步清洗一下
for data in list_data:
    print(data['title'])
