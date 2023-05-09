

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class my_linear_regression(object):
    def __init__(self,df:pd.DataFrame):
        '''
        传入的是训练集
        假设最后一列是目标列
        '''
        self.df=df
        self.x=self._get_x()
        self.y=self._get_y()
        
        self._normalize_feature()#! 如果想更改原来的数据 那么也可以直接self.df=normalize_feature(self.df)


        self.untrained_theta = np.zeros((self.x_norm.shape[1],1))
        self.alpha=0.01
        
    def _normalize_feature(self):
        '''
        归一化
        :param X:
        :return:
        '''
        mu = np.mean(self.x, axis=0)
        # ddof的设置，会改变标准差的结算结果，因为总体误差和样本误差的计算公式不一样
        #标准差
        sigma = np.std(self.x, axis=0, ddof=1)
        
        self.mu=mu
        self.sigma=sigma
        
        
        #! 为了不出现nan
        for i in range(len(sigma)):
            if sigma[i]==0:
                sigma[i]=1
        x_norm = (self.x-mu)/ sigma


        
        #todo 加为1的特征
        ones = np.ones((x_norm.shape[0], 1))
        x_norm=np.c_[ones,x_norm]
        
        self.x_norm=x_norm


        
    # def umnormalize(self):
    #     self.final_theta=self.final_theta*
    
    def _get_x(self)->np.ndarray: 
        '''
        获取特征列
        '''
        return self.df.iloc[:, 0:-1].values  # 这个操作获取所有的特征列(即排除了target列)，返回 ndarray,不是矩阵
    
    def _get_y(self)->np.ndarray:
        """
        假设最后一列是目标列
        获取目标列

        """
        #! 与[:,-1]不同！#!!!!!!!!!!!!!!!!!!!!!!!
        
        return self.df.iloc[:,len(self.df.columns)-1 :len(self.df.columns)].values # df.iloc[:, -1]是指df的最后一列
    
    def _lr_cost(self,theta, x: np.ndarray, y: np.ndarray):
        '''
        可主动调用这个函数，传入未知数向量
        可用于在测试集上对模型进行评估 (使用均方误差)
        param theta: 维度是R(n)，是线性回归的参数
        param x: 维度是R(m*n)，m为样本数，n为特征数
        param y:维度是R(m)
        return: cost
        '''
        m = x.shape[0]  # m为样本数
        # 计算每个样本的每个特征与对应参数的乘积
        inner = x.dot(theta) - y  # x.dot(theta)等价于np.dot(x,theta)，inner的维度是R(m*1)

        square_sum = np.dot(inner.T, inner)#! 等号右侧其实就是计算了平方的和
        
        cost = square_sum / (2 * m)
        return cost[0][0]
    

    def _gradient(self,theta, x:np.ndarray, y: np.ndarray):
        '''
        :param theta: 维度是R(n)，是线性回归的参数
        :param x: 维度是R(m*n)，m为样本数，n为特征数
        :param y: 维度是R(m)
        :return:维度是R(n+1,1)，即与参数向量theta同维度
        '''
        m = x.shape[0]
        inner = np.dot(x.T, (np.dot(x, theta) - y))#dot中第二个参数是差值向量
        return inner / m

    # 批量梯度下降函数
    def _batch_gradient_decent(self,theta, x, y, epoch, alpha):
        '''
        :param theta: 维度是R(n)，是线性回归的参数
        :param X: 维度是R(m*n)，m为样本数，n为特征数
        :param y: 维度是R(m)
        :param epoch: 处理的轮数
        :param alpha: 学习率，即梯度下降更新公式里的alpha
        :return: 拟合线性回归,返回最终的未知数向量和每次的误差
        '''
    
        cost_data = [self._lr_cost(theta, x, y)]#! 记录每次移动之后的代价值 我们目的是通过可视化 来找到最小的cost所对应的theta
        _theta = theta.copy()  # 拷贝一份，不和原来的theta混淆

        for _ in range(epoch):

            
            #! 公式
            _theta = _theta - alpha * self._gradient(_theta, x, y)
            
            #! 记录cost
            cost_data.append(self._lr_cost(_theta, x, y))

        return _theta, cost_data
    
    
    
    def show_to_choose_alpha(self,epoch=50):
        '''
        step1 通过观察图像选择较好的学习率
        (可省略此步骤，若省略则使用默认的0.01学习率)
        ''' 
        
        # 产生不同的学习率
        base = np.logspace(-1, -5, num=4) #指定起始及结束值，并指定个数，默认以10为底。该方法的详细用法见参考文章
        # print(base)
        candidate = np.sort(np.concatenate((base, base*3)))
        # print(candidate)


        fig, ax = plt.subplots(figsize=(16, 9)) # 生成画布
        # 遍历每一个学习率
        for alpha in candidate:
            # 使用当前学习率拟合数据，计算迭代过程中的代价值
            _, cost_data = self._batch_gradient_decent(self.untrained_theta, self.x_norm, self.y, epoch, alpha)
            # 绘制当前学习率之下的代价值的变化情况
            ax.plot(np.arange(epoch+1), cost_data, label=alpha)

        ax.set_xlabel('epoch', fontsize=18)
        ax.set_ylabel('cost', fontsize=18)
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        ax.set_title('learning rate', fontsize=18)
        plt.show()
        
        self.alpha=eval(input('请输入选择的学习率:'))
        
        

        
        
    
    def train(self,epoch=500):
        '''
        step2:训练模型 
        
        epoch:训练次数
        alpha:学习率
        默认训练500次
        学习率0.01
        返回最终未知数向量(第一个分量为常数的值)
        '''
        
        self.final_theta,self.cost_data= self._batch_gradient_decent(self.untrained_theta,self.x_norm,self.y,epoch,self.alpha)
        
        return self.final_theta,self.cost_data#! 是为了给调用者看的
    
    def model_check(self,test_data:pd.DataFrame):
        '''
        传入测试集并汇报均方误差
        '''
        _=my_linear_regression(test_data)
        
        print('模型在测试集上均方误差为:',self._lr_cost(self.final_theta,_.x_norm,_.y))
        
    
    
    def show_training_process(self):


        # final_theta,cost_data=self.get_result(epoch,alpha)
        #! 为了防止重复调用 直接变成属性
        print('学习率为:',self.alpha)
        print('最终的系数向量即final_theta为(第一个数是截距):',self.final_theta)
        # final_theta 即为结果 查看最终的参数向量值（由于特征超过两个，就无法用二维平面图来直观查看拟合的曲线了）        
        plt.xlabel('epoch')
        plt.ylabel('cost')
        plt.plot(range(len(self.cost_data)),self.cost_data)#! 已知x y轴 进行画曲线图
        plt.show()   
        
#这里要注意路径中的斜杠,和我们从文件属性中复制出来的方向不一致。这真是一个非常不方便的地方。那我们有没有方法解决呢?当然是有的。

    def predict(self,df: pd.DataFrame):
        # arr=(arr-self.mu)/self.sigma
        
        # arr = np.concatenate((np.ones((1,)), arr))
        temp=my_linear_regression(df)
        result = temp.x_norm.dot(self.final_theta)
        print('预测结果为:',result)
        
        
    
    
    
data=pd.read_csv('D:/vscode/python/数据建模/机器学习/有监督学习/线性回归/boston2.csv')

data_train=data[:200].copy()

my_lr=my_linear_regression(data_train)

#! 看图找到合适的学习率
my_lr.show_to_choose_alpha()

#! 训练
my_lr.train()

#! 输出训练结果
my_lr.show_training_process()


#! 预测模型在测试集合上的准确率

my_lr.model_check(data[200:400].copy())

print('===============================================')
#! 传入数据 输出预测值

my_lr.predict(data[:20].copy())



