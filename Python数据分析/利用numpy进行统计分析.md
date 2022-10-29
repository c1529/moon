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
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
