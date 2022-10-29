## 读写文件
### 二进制文件读写
    //save函数以二进制形式的格式保存数据，load函数从二进制的文件读取数据
    //save函数用法np.save(file,arr,allow_pick=Ture,fix_import+Ture)
    //file是文件保存位置，没写则是默认路径
    import numpy as np
    arr1=np.arange(100).reshape(10,10)
    np.save("D:/save_arr1",arr1)
    a=np.load("D:/save_arr1.npy")
    print(a)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
