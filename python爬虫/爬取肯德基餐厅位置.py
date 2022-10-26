import json
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
aa=input("请输入一个城市")
data={'cname':'',
        'pid':'',
        'keyword':aa,
        'pageIndex':'1',
        'pageSize':'10'}
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
response=requests.post(url,data=data,headers=headers)
data=response.json()
c=aa+'的肯德基门店位置.json'
fp=open(c,'w',encoding='utf-8')
json.dump(data,fp=fp,ensure_ascii=False)
