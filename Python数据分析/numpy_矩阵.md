# 创建矩阵(numpy中矩阵运算是针对矩阵中每一个元素的)
## 使用mat函数
    import numpy as np
    matr1=np.mat('1,2,3;4,5,6;7,8,9')
    print(matr1)
    '''
    [[1 2 3]
    [4 5 6]
    [7 8 9]]
    '''
## 使用matrix函数
    matr1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(matr1)
## 使用bmat函数创建（分布矩阵，将小矩阵创建成大矩阵）
    import numpy as np
    matr1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    matr2=matr1*3
    arr3=np.bmat('matr1 matr2;matr1 matr2')
    print(arr3)
    '''
    [[ 1  2  3  3  6  9]
    [ 4  5  6 12 15 18]
    [ 7  8  9 21 24 27]
    [ 1  2  3  3  6  9]
    [ 4  5  6 12 15 18]
    [ 7  8  9 21 24 27]]
    '''
## 查看矩阵属性
    import numpy as np
    matr1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(matr1)
    print(matr1.T) #矩阵的转置
    '''
    [[1 2 3]
    [4 5 6]
    [7 8 9]]
    [[1 4 7]
    [2 5 8]
    [3 6 9]]
    '''
    print(matr1.H) #矩阵的共轭转置
    print(matr1.I) #返回逆矩阵
    print(matr1.A) #返回二维数组视图
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

