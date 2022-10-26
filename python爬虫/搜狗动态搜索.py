import requests
url='https://www.sogou.com/web?'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
aa=input('请输入：')
a={'query':aa}
b=requests.get(url,params=a,headers=headers)
filename=aa+'.html'
#print(filename)
with open(filename,'w',encoding='utf-8') as f1:
    f1.write(b.text)
