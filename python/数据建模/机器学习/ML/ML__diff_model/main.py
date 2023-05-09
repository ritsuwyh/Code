# -*- coding: utf-8 -*-

import random
import csv
import numpy as np
import math
from sklearn.preprocessing import normalize
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)


def GenerateData(data_path):
    with open(data_path, "r", encoding="utf-8") as f:
        data = np.array(list(csv.reader(f))[1:])
    N = data.shape[0]
    X = data[:, :-1].astype(np.float64)
    X = normalize(X, axis=0, norm="max")  # avoid overflow problem

    y = data[:, -1].astype(np.int32).reshape(N, 1)
    test_id = np.random.choice(N, int(0.3 * N), replace=False)
    X_train = np.delete(X, test_id, axis=0)
    y_train = np.delete(y, test_id, axis=0)
    X_test = X[test_id]
    y_test = y[test_id]

    print("Dimension of the feature data in training set:", X_train.shape)
    print("Dimension of the feature data in testing set:", X_test.shape)
    return X_train, y_train, X_test, y_test


def PlotROCs(y_prob_lr, y_prob_tree, y_prob_svm, y_test):
    # %%
    # TODO: Plot the ROCs in one graph
    y_prob = [y_prob_lr, y_prob_tree, y_prob_svm]
    fpr = []
    tpr = []
    roc_auc = []

    for i in range(3):
        temp_fpr, temp_tpr, threshold = roc_curve(y_test, y_prob[i])
        # roc_curve 的第二个参数 Target scores, can either be probability estimates of the positive class, confidence
        # values, or non-thresholded measure of decisions (as returned by “decision_function” on some classifiers).

        # print(y_test.shape)
        # print(y_prob[i].reshape(-1, 1).shape)
        # print(len(temp_fpr))

        fpr.append(temp_fpr)
        tpr.append(temp_tpr)
        temp_roc_auc = auc(temp_fpr, temp_tpr)
        roc_auc.append(temp_roc_auc)
    lw = 2
    plt.figure(figsize=(10, 10))
    color = ['orange', 'blue', 'red']
    name = ['lr', 'tree', 'svm']
    for i in range(3):
        # print(fpr[i])
        # print(tpr[i])

        plt.plot(fpr[i], tpr[i], color=color[i], lw=lw,
                 label='%s model ROC curve (area = %0.4f)' % (name[i], roc_auc[i]))  # 假正率为横坐标，真正率为纵坐标做曲线

    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('三种模型在测试集上的ROC曲线')
    plt.legend(loc="lower right")

    plt.show()
    # %%


# def acc(y_true, y_pred):
#     # print(y_true.shape, y_pred.shape)  # 注意 (100,) 是一个行向量！只有一维
#
#     if y_true.shape != y_pred.shape:
#         print("Dimension error")
#
#     return np.sum(y_true == y_pred) / y_true.shape[0]


def log(model_name, acc_train, acc_test):
    print("%s的训练集精确度为:%0.4f" % (model_name, acc_train))
    print("%s的测试集精确度为:%0.4f" % (model_name, acc_test))


def main(data_path):
    (X_train, y_train, X_test, y_test,) = GenerateData(data_path)
    # %%
    # TODO: Plot the ROCs in one graph

    # 计算acc也可以使用库函数
    # from sklearn.metrics import accuracy_score
    # acc = accuracy_score(y_true,y_pred)

    # lr = sklearn.linear_model.LogisticRegression() 这样写不可以
    lr_clf = LogisticRegression()
    lr_model = lr_clf.fit(X_train, y_train.ravel())  # fit应该传入行向量
    y_train_pred_lr = lr_model.predict(X_train)  # predict函数返回行向量 这里如果使用自己的acc函数就会用到
    y_test_pred_lr = lr_model.predict(X_test)
    acc_train_lr = lr_model.score(X_train, y_train)  # 有的时候可能会遇到维度不对等问题,使用ravel()函数 将列向量展开为行向量
    acc_test_lr = lr_model.score(X_test, y_test)
    log("lr_model", acc_train_lr, acc_test_lr)

    # tree = sklearn.tree.DecisionTreeClassifier(criterion="entropy", random_state=30)
    tree_clf = DecisionTreeClassifier(criterion="gini", max_depth=6, random_state=30)
    tree_model = tree_clf.fit(X_train, y_train.ravel())
    y_train_pred_tree = tree_model.predict(X_train)
    y_test_pred_tree = tree_model.predict(X_test)
    acc_train_tree = tree_model.score(X_train, y_train)
    acc_test_tree = tree_model.score(X_test, y_test)
    log("tree_model", acc_train_tree, acc_test_tree)

    # 发现 gini指数略好于entropy,且峰值都在max_depth=6
    # # 用学习曲线确定最优max_depth取值
    # test = []
    # for i in range(10):
    #     clf = DecisionTreeClassifier(max_depth=i + 1
    #                                       , criterion="entropy"
    #                                       , random_state=30
    #                                       , splitter="random"
    #                                       )
    #     clf = clf.fit(X_train, y_train)
    #     score = clf.score(X_test, y_test)
    #     test.append(score)
    # plt.plot(range(1, 11), test, color="red", label="max_depth")
    # plt.legend()
    # plt.show()
    # # we conclude that max_depth=6 is the best

    svm_clf = svm.SVC(gamma="scale", C=1.0, kernel="rbf", probability=True)
    svm_model = svm_clf.fit(X_train, y_train.ravel())
    y_train_pred_svm = svm_model.predict(X_train)
    y_test_pred_svm = svm_model.predict(X_test)
    acc_train_svm = svm_model.score(X_train, y_train)
    acc_test_svm = svm_model.score(X_test, y_test)
    log("svm_model", acc_train_svm, acc_test_svm)

    # 要区分 pred 和 prob
    # TODO : // scikit - learn.org / stable / modules / generated / sklearn.linear_model.LogisticRegression.html
    # sklearn.linear_model.LogisticRegression predicted probability on test set using logistic regression model
    y_prob_lr = lr_model.predict_proba(X_test)[:, -1]
    # 类别标签是行索引，按行从小到大排列,predict_proba返回的是一个 n 行 k 列的数组， 第 i 行 第 j 列上的数值是模型预测 第 i 个预测样本#为某个标签的概率，并且每一行的概率和为1。
    # print(y_prob_lr.shape) 是 2列的数组
    # 在本题目中是0,1标签 所以第二列是样本为positive的概率

    # predicted probability on test set using tree model
    y_prob_tree = tree_model.predict_proba(X_test)[:, -1]
    # print(y_prob_tree)

    # predicted probability on test set using svm model
    y_prob_svm = svm_model.predict_proba(X_test)[:, -1]
    # %%

    PlotROCs(y_prob_lr, y_prob_tree, y_prob_svm, y_test)


if __name__ == "__main__":
    set_seed(6)
    data_path = "data.csv"
    main(data_path)
