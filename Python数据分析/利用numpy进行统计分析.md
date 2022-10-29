## 读写文件（二进制）
### 二进制文件读写
    #save函数以二进制形式的格式保存数据，load函数从二进制的文件读取数据
    #save函数用法np.save(file,arr,allow_pick=Ture,fix_import+Ture)
    #file是文件保存位置，没写则是默认路径,文件扩展名字为.npy
    import numpy as np
    arr1=np.arange(100).reshape(10,10)
    np.save("D:/save_arr1",arr1)
    a=np.load("D:/save_arr1.npy")
    print(a)
### 多个文件存储
    #savez文件扩展名为.npz
    import numpy as np
    arr1=np.arange(100).reshape(10,10)
    arr2=np.arange(100)
    np.savez("D:/savez_arr",arr1,arr2)
    a=np.load("D:/savez_arr.npz")
    print(a['arr_0'])
    print(a['arr_1'])
### 文件读取
    np.load("D"/save_arr1.npy")   #单个文件读取
    a=np.load("D:/savez_arr.npz")   #多个文件读取
    print(a['arr_0'])
    print(a['arr_1])
## 文件存储与读取（savetxt,loadtxt,genformtxt）
### savetxt和loadtxt
    import numpy as np
    arr1=np.arange(0,12,0.5).reshape(4,6)
    np.savetxt('D:/savetxt.txt',arr1)
    a=np.loadtxt('D:/savetxt.txt')
    print(a)
### genfromtxt
    a=np.genfromtxt('D:/savetxt.txt')
## 使用函数进行简单的统计分析
### 使用sort函数进行排序
    import numpy as np
    arr=([1,5,16,11,13])
    arr.sort()
    print(arr)
    '''
    [1, 5, 11, 13, 16]
    '''
    import numpy as np
    arr=np.array([[1,5,3],[6,11,8],[2,10,12]])
    arr.sort(axis=1)#沿横轴排序
    print(arr)
    '''
    [[ 1  3  5]
    [ 6  8 11]
    [ 2 10 12]]
    '''
    arr.sort(axis=0)#沿纵轴排序
    '''
    [[ 1  5  3]
    [ 2 10  8]
    [ 6 11 12]]
    '''
### 使用argsort函数进行排序（返回索引）
    import numpy as np
    arr=np.array([1,5,2,6,12])
    print(arr.argsort())
    '''
    [0 2 1 3 4]
    '''
### 使用lexsort函数进行排序（返回索引）
    import numpy as np
    a=np.array([3,2,6,4,5])
    b=np.array([50,30,40,20,10])
    c=np.array([400,300,600,100,200])
    d=np.lexsort((a,b,c))#多个键值排序时候，按照最后一个函数计算
    print(d)
    print(list(zip(a[d],b[d],c[d])))
    '''
    [3 4 1 0 2]
    [(4, 20, 100), (5, 10, 200), (2, 30, 300), (3, 50, 400), (6, 40, 600)]
    '''
## 去重与重复数组
### 数组内去重
    import numpy as np
    a=np.array(['小明','小黄','小红','小明'])
    print(np.unique(a))
    print(sorted(set(a))) #等价
    '''
    ['小明' '小红' '小黄']
    ['小明', '小红', '小黄']
    '''
### 使用tile函数实现数据重复
    import numpy as np
    a=np.arange(5)
    print(a)
    print(np.tile(a,3))
    '''
    [0 1 2 3 4]
    [0 1 2 3 4 0 1 2 3 4 0 1 2 3 4]
    '''
### 使用repeat函数实现数据重复
    import numpy as np
    a=np.arange(10).reshape(5,2)
    print(a)
    print(a.repeat(2,axis=1))#行重复
    print(a.repeat(2,axis=0))#列重复
    '''
    [[0 1]
    [2 3]
    [4 5]
    [6 7]
    [8 9]]
    [[0 0 1 1]
    [2 2 3 3]
    [4 4 5 5]
    [6 6 7 7]
    [8 8 9 9]]
    [[0 1]
    [0 1]
    [2 3]
    [2 3]
    [4 5]
    [4 5]
    [6 7]
    [6 7]
    [8 9]
    [8 9]]
    '''
### 统计函数的使用
    import numpy as np
    a=np.arange(10).reshape(2,5)
    print(np.sum(a))#计算数组和
    print(a.sum(axis=1))#沿横轴求和
    print(a.sum(axis=0))#沿纵轴求和
    print(np.mean(a))#计算数组平均值
    print(a.mean(axis=1))#沿横轴求平均值
    print(a.mean(axis=0))#沿纵轴求平均值
    '''
    45
    [10 35]
    [ 5  7  9 11 13]
    4.5
    [2. 7.]
    [2.5 3.5 4.5 5.5 6.5]
    '''
    import numpy as np
    a=np.arange(10).reshape(2,5)
    print(np.std(a))#标准差
    print(np.var(a))#方差
    print(np.min(a))#最小值
    print(np.max(a))#最大值
    print(np.argmin(a))#最小值索引
    print(np.argmax(a))#最大值索引
    '''
    2.8722813232690143
    8.25
    0
    9
    0
    9
    '''
### cumsum和cumprod函数的使用
    import numpy as np
    a=np.arange(2,10)
    print(a)
    print(np.cumsum(a))#计算所有元素的累计和
    print(np.cumprod(a))#计算所有元素的累计积
    '''
    [2 3 4 5 6 7 8 9]
    [ 2  5  9 14 20 27 35 44]
    [     2      6     24    120    720   5040  40320 362880]
    '''
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
