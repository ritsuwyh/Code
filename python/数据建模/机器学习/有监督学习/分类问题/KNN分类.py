

#!https://wenku.baidu.com/view/fbc23ddfadf8941ea76e58fafab069dc502247bb.html
#!https://blog.csdn.net/xiaoyoupei/article/details/122888826
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_excel('./datasets/my_films.xlsx')
#提取特征数据
feature = df[['Action Lens','Love Lens']]
#提起标签数据
target = df['target']

#数据集切分
x_train,x_test,y_train,y_test = train_test_split(feature,target,test_size=0.1,random_state=2020)

#创建算法模型对象
#n_neighbors == knn中的k
knn = KNeighborsClassifier(n_neighbors=3)
#训练模型:特征数据必须是二维的
knn.fit(x_train,y_train)

knn.predict(x_test)
print('模型分类结果：',knn.predict(x_test))
print('真实的结果：',y_test)

# 结果：
# 模型分类结果： ['Action' 'Action']
# 真实的结果： 2    Action
# 1    Action
# Name: target, dtype: object
# 学习曲线寻找最优的k值
# 穷举不同的k值
import matplotlib.pyplot as plt
ks = np.arange(3,150,5)
scores = []
for k in ks:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    score = knn.score(x_test,y_test)
    scores.append(score)
scores = np.array(scores)
plt.plot(ks,scores)
plt.xlabel('k')
plt.ylabel('score')
