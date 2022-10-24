## 创建矩阵
 ### 使用mat函数
  import numpy as np
  matr1=np.mat('1,2,3;4,5,6;7,8,9')
  print(matr1)
  '''
  [[1 2 3]
  [4 5 6]
  [7 8 9]]
  '''
 ### 使用matrix函数
  matr1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
  print(matr1)
 ### 使用bmat函数（分块矩阵，将小矩阵变成大矩阵）
 import numpy as np
 matr1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
 matr2=matr1*3
 arr3=np.bmat('matr1 matr2;matr1 matr2') #里面元素可以是二维数组
 print(arr3)
 '''
 [[ 1  2  3  3  6  9]
 [ 4  5  6 12 15 18]
 [ 7  8  9 21 24 27]
 [ 1  2  3  3  6  9]
 [ 4  5  6 12 15 18]
 [ 7  8  9 21 24 27]]
 '''
 
 
