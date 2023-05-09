
#自己实现PCA
import numpy as np
# PCA算法
# • 设有m条D维数据构成X，目标为压缩到d维：
# – 将每个样本中⼼化（零均值化）
# – 计算协⽅差矩阵X.dot(X.T)
# - 对协⽅差矩阵做特征值分解 
# – 最⼤的d个特征值所对应的特征向量构成投影矩阵W


def pca(X,k):#k is the components you want 列数降到多少列
    #mean of each feature
    m,n = np.shape(X)
    #!print(X[:,0]) 以行向量形式输出第1列

    mean=np.mean(X,axis=0)#! 计算每一列的平均值 
    #normalization
    norm_X=X-mean #!利用广播机制 列上面的每一个元素都减去该列上的平均值
    
    #scatter matrix 协方差矩阵
    scatter_matrix=np.dot(np.transpose(norm_X),norm_X)
    
    #Calculate the eigenvectors and eigenvalues
    # x=np.linalg.eig(scatter_matrix)
    # print(x)
    # (array([37.7067455 ,  1.62658783]), array([[ 0.8549662 , -0.51868371],
    #   [ 0.51868371,  0.8549662 ]]))
    eig_val, eig_vec = np.linalg.eig(scatter_matrix)
    
#     v: 代表特征向量
# 返回值v是一个array类型的数据，其维度和方阵的维度是相同的，对于一个m x m的方阵，v的维度也为m x m，v中包含m个特征向量，每个特征向量的长度为m，v[:,i]对应特征值为w[i]的特征向量，特征向量是进行单位化（除以所有元素的平方和的开方）的形式。

    # print(eig_val)
    # print('-----')
    # print(eig_vec)
    
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(n)]
    # sort eig_vec based on eig_val from highest to lowest
    eig_pairs.sort(reverse=True)
    # select the top k eig_vec
    feature=np.array([ele[1] for ele in eig_pairs[:k]])#! 即为矩阵P
    #get new data
    data=np.dot(norm_X,np.transpose(feature))
    return data

X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])

print(pca(X,1))

##用sklearn的PCA
from sklearn.decomposition import PCA
import numpy as np
X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca=PCA(n_components=1)
pca.fit(X)
print(pca.transform(X))

