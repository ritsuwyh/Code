import random
import csv
import numpy as np
import math
from tqdm import tqdm
from sklearn.preprocessing import normalize
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
roc_auc = 0

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def GenerateData(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        data = np.array(list(csv.reader(f))[1:])
    N = data.shape[0]
    X = data[:, :-1].astype(np.float64)
    X = normalize(X, axis=0, norm="max")  # avoid overflow problem
    X = np.insert(X, 0, values=1, axis=1)  # insert bias term
    print("Dimension of the feature data:", X.shape)
    y = data[:, -1].astype(np.int32).reshape(N, 1)
    test_id = np.random.choice(N, int(0.25 * N), replace=False)
    X_train = np.delete(X, test_id, axis=0)                         
    y_train = np.delete(y, test_id, axis=0)
    X_test = X[test_id]
    y_test = y[test_id]

    return X_train, y_train, X_test, y_test


def nabla_l(w_old, X, y):
    """
    A function expression for the gradient of l(w) w.r.t. w
    """

    p = 1 / (1 + math.e ** (-X @ w_old))  # 向量取倒数的意义？ 每一个分量先计算 p也是个向量 

    return -X.T @ (y - p)


def nabla_2_l(w_old, X, y):
    """
    A function expression for the Hessian matrix of l(w) w.r.t. w
    """
    # %%
    # TODO: Compute the Hessian matrix of log-likelihood function

    p1 = 1 / (1 + math.e ** (-X @ w_old))  # 分子分母上下同乘了一个 math.e ** (-X @ w_old)
    p0 = 1 / (1 + math.e ** (X @ w_old))

    # print((p1*p0).shape) 注意 p1.T * p 就是求和了！ X.T @ X 也是求和 X.T @ X * (p1.T * p0) 就是求和乘求和 而 求和的乘积并不等于乘积的求和!!!
    return X.T @ ((p1 * p0) * X)  # p1 * p0 是一个 列向量 每一个元素的值为 pi(1-pi) , (p1 * p0) * X ： p1* p0 先进行了矩阵的列扩张形成temp矩阵，temp矩阵再与X矩阵对应位置元素相乘,此时每一个元素的值为xi pi (1-pi)
    # End your code here
    # %%


def Newton_Solver_for_LR(w_old, nabla_l, nabla_2_l, X, y):
    """
    Solving the minimizer for log-likelihood in Logistic Regression((3.27) in the book).
        param nabla_l: function, nabla_l(w) is the gradient of l(w) w.r.t. w
        param nabla_2_l: function, nabla_2_l(w) is the Hessian matrix of l(w) w.r.t. w
        param X, y: parameters in l(w)
        return: optimize one_step for w_new
    """
    # %%
    # TODO: Finish the code here
    w_new = w_old - np.linalg.inv(nabla_2_l(w_old, X, y)) @ nabla_l(w_old, X, y)
    # End your code here
    # %%

    return w_new


class LogisticRegression:
    def __init__(self, iter_num, Solver):
        self.name = "Logistic Regression"
        self.iter_num = iter_num
        self.Solver = Solver

    def train(self, X_train, y_train):
        self.w = np.random.randn(X_train.shape[1], 1)  # initialize w_0
        for _ in tqdm(range(self.iter_num)):  # 迭代的过程
            self.w = self.Solver(
                w_old=self.w,
                nabla_l=nabla_l,
                nabla_2_l=nabla_2_l,
                X=X_train,
                y=y_train,
            )
        return self.w

    def predict(self, X_new):
        # %%
        # TODO: Finish the code here to predict the label for new data
        # Please return the probability vector P(X=1), rather than a 0-1 vector

        y_prob = 1 / (1 + math.e ** (-X_new @ self.w))
        # End your code here
        # %%

        return y_prob

    def evalute(self, X, y):
        # %%
        # TODO: Compute the accuracy when using parameter self.w
        my_result = self.predict(X)
        # print(my_result)
        # print(my_result.shape)
        my_result[my_result>=0.5]=1
        my_result[my_result<0.5]=0
        # for i in range(my_result.shape[0]):
        #     if my_result[i][0] >= 0.5:
        #         my_result[i][0] = 1
        #     else:
        #         my_result[i][0] = 0
        accuracy = np.sum(my_result == y) / my_result.shape[0]
        # print(accuracy)
        # End your code here
        # %%
        return accuracy


def PlotROC(y_prob, y_test):
    # %%
    # TODO: Plot the ROC
    fpr, tpr, threshold = roc_curve(y_test, y_prob)
    # print(y_test.shape,y_prob.shape)
    # print(len(fpr))
    # print(y_prob)
    global roc_auc
    roc_auc = auc(fpr, tpr)

    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.3f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")

    plt.show(block=True)
    # %%


if __name__ == "__main__":
    set_seed(6)
    iter_num = 20
    # data_path = "data.csv"
    data_path="tex作业\ml_homework1\ml_hw1\program\code\data.csv"

    (
        X_train,
        y_train,
        X_test,
        y_test,
    ) = GenerateData(data_path)

    model = LogisticRegression(
        iter_num=iter_num,
        Solver=Newton_Solver_for_LR,
    )
    model.train(X_train=X_train, y_train=y_train)
    # print(model.w)
    # train_acc = model.evalute(X_train, y_train)
    test_acc = model.evalute(X_test, y_test)
    print("Accuracy in test set: %.4f" % test_acc)
    #
    y_prob = model.predict(X_test)
    PlotROC(y_prob, y_test)
    #
    # # %%
    # # TODO: Compute the AUC
    auc_value = roc_auc
    print("AUC in test set: %.4f" % (auc_value))
    #

#TODO 下面的写法非常之优美 充分利用了numpy的性质 索引数组
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import warnings


# def classify(z, threshold):
#     y_pred = z.copy()
#     y_pred[y_pred < threshold] = 0
#     y_pred[y_pred > threshold] = 1
#     return y_pred


#TODO 对于z>0 的数据 用 1 / (1 + np.exp(-z[z > 0])) 代替原数据  z < 0 的 用np.exp(z[z < 0]) / (1 + np.exp(z[z < 0]))代替原数据
# def sigmoid(z):
#     z[z > 0] = 1 / (1 + np.exp(-z[z > 0]))
#     z[z < 0] = np.exp(z[z < 0]) / (1 + np.exp(z[z < 0]))
#     return z


# def predict(model, X, theta):
#     return classify(sigmoid(X @ model), theta)


# def calc_pr(y_pred, y_true):
#     TP, FP, FN = [
#         e.sum() for e in [
#             y_pred[y_true == 1] == 1, y_pred[y_true == 0] == 1, y_pred[
#                 y_true == 1] == 0
#         ]
#     ]
#     return (TP / (TP + FP), TP / (TP + FN))


# def evaluate(y_pred, y_true):
#     p, r = calc_pr(y_pred, y_true)
#     print(f"accuracy:  {(y_true==y_pred).mean()}")
#     print(f"precision: {p}")
#     print(f"recall:    {r}")


# warnings.filterwarnings('ignore', category=RuntimeWarning)
# # data reading
# X_train = pd.read_csv('./ML4_programming/train_features.csv').assign(
#     argumented=1).to_numpy()
# y_train = pd.read_csv('./ML4_programming/train_target.csv').to_numpy()
# X_val = pd.read_csv('./ML4_programming/val_features.csv').assign(
#     argumented=1).to_numpy()
# y_val = pd.read_csv('./ML4_programming/val_target.csv').to_numpy()
# X_test = pd.read_csv('./ML4_programming/test_feature.csv').assign(
#     argumented=1).to_numpy()

# # model training
# epoch = int(800)
# beta = np.full(shape=(X_train.shape[1], 1),
#                fill_value=0.114151919810,
#                dtype=float)
# for i in range(epoch):
#     z = X_train @ beta
#     z[z > 0] = 1 / (1 + np.exp(-z[z > 0]))
#     z[z < 0] = np.exp(z[z < 0]) / (1 + np.exp(z[z < 0]))
#     df = X_train.T @ (z - y_train)
#     beta -= df * 0.05

# # predict & evaluate (question 2(3))
# evaluate(predict(beta, X_val, 0.5), y_val)

# # predict (question 2(4))
# y_pred = predict(beta, X_test, 0.5)
# # predict output
# np.savetxt("./ML4_programming/58121128_1.csv",
#            y_pred,
#            delimiter=',',
#            header="class",
#            fmt="%d")
