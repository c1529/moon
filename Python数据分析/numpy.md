numpy提供两个基本对象：ndarray(是存储单一数据类型的多维数组)和ufunc(对数组进行处理的函数)
## 创建一维数组
    import numpy as np
    arr1=np.array([1,2,3,4])
    print(arr1)
## 创建二维数组
    import numpy as np
    arr2=np.array([[1,2,3,4],[4,5,6,7]]) ** 二维数组两个【】 **
    print(arr2)
##  查看数组属性
    import numpy as np
    arr2=np.array([[1,2,3,4],[4,5,6,7],[12,15,16,14]])
    print(arr2.shape)  #查看数组结构，返回的是（3，4）
    print(arr2.dtype)  #查看数组类型，返回值是int32
    print(arr2.size)   #查看数组中元素的个数，返回值是12
    print(arr2.itemsize)  #查看数组每个元素的大小
##  改变数组shape属性
    arr2.shape=4,3
    print(arr2)
    '''输出如下:
    [[ 1  2  3]
    [ 4  4  5]
    [ 6  7 12]
    [15 16 14]]
    '''
##  创建数组
   ### 使用arange函数创建数组
    arr3=np.arange(0,1,0.1)
    print(arr3) #输出 [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9] 
    #arange符合左闭右开，即从0开始，取不到1
   ### 使用linspace函数创建函数
    arr3=np.linspace(0,1,12)
    print(arr3)
    '''
    [0.         0.09090909 0.18181818 0.27272727 0.36363636 0.45454545
    0.54545455 0.63636364 0.72727273 0.81818182 0.90909091 1.        ]
    '''



























