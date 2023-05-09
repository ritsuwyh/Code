# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# #获取数据
# def get_data(): 
#     data = load_iris().data
#     label = load_iris().target
#     df = pd.DataFrame(data)
#     df.columns = [load_iris().feature_names]
#     df['label'] = label

#     df = df.loc[label != 2,:] #做二分类，舍弃掉第三类鸢尾花

#     X = df[load_iris().feature_names]
#     Y = df['label']

#     return X.values,Y.values

# #为了实现矩阵相乘所以将X添加第一个维度，置为1
# def data_mat(x_origin):

#     return np.hstack((x_origin,np.ones((len(x_origin),1))))

# #sigmoid函数
# def sigmoid(x):
#     return 1/(1+np.exp(-x))

# #最后模型输出，其实也是sigmoid函数
# # def model(x,w):
# #     return 1 / (1 + np.exp(-x.dot(w)))

# def predict(x_test,y_test,w):
# 	#两种计算方法
#     #第一种wx+b与0的关系
    
#     y_predict = x_test.dot(w)
#     #! bool索引
#     y_predict[y_predict >= 0] = 1
#     y_predict[y_predict < 0] = 0
	
#     #第二种方法模型输出>= 0.5 或者 < 0.5
#     # y_predict  = model(x_test,w)
#     # y_predict[y_predict >= 0.5] = 1
#     # y_predict[y_predict < 0.5] = 0
#     #! 其实就是一个判断准确率函数
#     return accuracy_score(y_test,y_predict)


# if __name__ == '__main__':
#     X,Y = get_data()
#     print(X)#! 二维数组
#     print(Y)#! 多行一列的二维数组
#     #! 这个思路跟 my_lr 很相近
    
#     x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3) #将数据集划分为训练集和验证集
#     #! KNN具体实现里面有这个的实现 利用随机数

#     x_train = data_mat(x_train) #矩阵化
#     x_test = data_mat(x_test)

#     EPOCHS = 1000 #迭代次数
#     #W = np.array([0]*(x_train.shape[1]))#! W 是未知数向量
    
#     W=np.zeros((x_train.shape[1],1))
#     #初试化W和b，注意b以及包含在w内，所以W的维度为特征数+1
#     lr = 0.1 #学习率
#     print(W.shape)
#     print(sigmoid(x_train.dot(W)).shape)
#     print(x_train.shape)
    
#     for epoch in range(EPOCHS): 
#         #梯度下降学习参数
#         # print(sigmoid(x_train.dot(W)))
#         W = W - lr * ( x_train.T.dot ( (sigmoid(x_train.dot(W)) - y_train) )        )   
#         print(W)
#     print(W)
#     #对测试集进行测试
#     result = predict(x_test,y_test,W)
#     print('Predict_ACC：{}'.format(result))
    
    
    
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#获取数据
def get_data(): 
    data = load_iris().data
    label = load_iris().target
    df = pd.DataFrame(data)
    df.columns = [load_iris().feature_names]
    df['label'] = label

    df = df.loc[label != 2,:] #做二分类，舍弃掉第三类鸢尾花

    X = df[load_iris().feature_names]
    Y = df['label']

    return X.values,Y.values

#为了实现矩阵相乘所以将X添加第一个维度，置为1
def data_mat(x_origin):
    mat = []
    for d in x_origin:
        mat.append([1.0, *d])
    return np.array(mat)

#sigmoid函数
def sigmoid(x):
    return 1/(1+np.exp(-x))

#最后模型输出，其实也是sigmoid函数
def model(x,w):
    return 1 / (1 + np.exp(-x.dot(w)))

def predict(x_test,y_test,w):
	#两种计算方法
    #第一种wx > 0或者 <0
    y_predict = x_test.dot(w)
    y_predict[y_predict >= 0] = 1
    y_predict[y_predict < 0] = 0
	
    #第二种方法模型输出>= 0.5 或者 < 0.5
    # y_predict  = model(x_test,w)
    # y_predict[y_predict >= 0.5] = 1
    # y_predict[y_predict < 0.5] = 0
    
    return accuracy_score(y_test,y_predict)


if __name__ == '__main__':
    X,Y = get_data()
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3) #将数据集划分为训练集和验证集

    x_train = data_mat(x_train) #矩阵化
    x_test = data_mat(x_test)

    EPOCHS = 100 #迭代次数
    W = np.array([0]*(x_train.shape[1])) #初试化W和b，注意b以及包含在w内，所以W的维度为特征数+1
    lr = 0.1 #学习率
    for epoch in range(EPOCHS): 
        #梯度下降学习参数
        W = W - lr * np.mean((sigmoid(x_train.dot(W)) - y_train.squeeze()) * x_train.T, axis=1)

    #对测试集进行测试
    print(W)
    result = predict(x_test,y_test,W)
    print('Predict_ACC：{}'.format(result))


