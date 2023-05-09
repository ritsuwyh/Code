from math import log
import operator
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt #计算数据集的香农公式 #新建数据集合
def creatDataSet():

    data = [
         ['Sunny', 'Hot', 'High', 'Weak', 'No'],
         ['Sunny', 'Hot', 'High', 'Strong', 'No'],
         ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
         ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
         ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
         ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
         ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
         ['Sunny', 'Mild', 'High', 'Weak', 'No'],
         ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
         ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
         ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
         ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
         ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
         ['Rain', 'Mild', 'High', 'Strong', 'No'],
     ]
    labels = ['Outlook', 'Temperature', 'Humidity', 'Wind']  # 5个特征

    return data,labels

def xiangnong(dataSet):
     #返回数据集行数
     numEntries=len(dataSet)
     #保存每个标签（label）出现次数的字典
     labelCounts={}
     #对每组特征向量进行统计
     for featVec in dataSet:
         currentLabel=featVec[-1]                     #提取标签信息
         if currentLabel not in labelCounts.keys():   #如果标签没有放入统计次数的字典，添加进去
             labelCounts[currentLabel]=0
         labelCounts[currentLabel]+=1                 #label计数

     shannonEnt=0.0                                   #经验熵
     #计算经验熵
     for key in labelCounts:
         prob=float(labelCounts[key])/numEntries      #选择该标签的概率
         shannonEnt-=prob*log(prob,2)                 #利用公式计算
     return shannonEnt


 #对数据集进行划分

def SplitData(dataSet,axis,value):
     #创建返回的数据集列表
     retDataSet=[]
     #遍历数据集
     for featVec in dataSet:
         if featVec[axis]==value:
             #去掉axis特征
             reduceFeatVec=featVec[:axis]
             #将符合条件的添加到返回的数据集
             reduceFeatVec.extend(featVec[axis+1:])
             retDataSet.append(reduceFeatVec)
     #返回划分后的数据集
     return retDataSet

 #选择最好的数据集划分方式

def ChoosebestSplitData(data):
     numFeatures = len(data[0]) - 1  # 获取样本集中特征个数，-1是因为最后一列是label
     baseEntropy = xiangnong(data)  # 计算根节点的信息熵
     bestInfoGain = 0.0  # 初始化信息增益
     bestFeature = -1  # 初始化最优特征的索引值
     for i in range(numFeatures):  # 遍历所有特征，i表示第几个特征
         featList = [example[i] for example in  data]  # 将dataSet中的数据按行依次放入example中，然后取得example中的example[i]元素，即获得特征i的所有取值
         uniqueVals = set(featList)  # 由上一步得到了特征i的取值，比如[1,1,1,0,0]，使用集合这个数据类型删除多余重复的取值，则剩下[1,0]
         newEntropy = 0.0
         for value in uniqueVals:
             subDataSet = SplitData(data, i, value)  # 逐个划分数据集，得到基于特征i和对应的取值划分后的子集
             prob = len(subDataSet) / float(len(data))  # 根据特征i可能取值划分出来的子集的概率
             newEntropy += prob * xiangnong(subDataSet)  # 求解分支节点的信息熵
         infoGain = baseEntropy - newEntropy  # 计算信息增益
         if (infoGain > bestInfoGain):  # 对循环求得的信息增益进行大小比较
             bestInfoGain = infoGain
             bestFeature = i  # 如果计算所得信息增益最大，则求得最佳划分方法
     return bestFeature  # 返回划分属性（特征）
 #该函数使用分类名称的列表，然后创建键值为ClassList中唯一的数据字典，字典对象存储了ClassList中每个类标签出现的评率，最后利用operator操作键值排序
 #字典，并返回出现次数最多的分类名称。
def moretype_con(classList):
     classCount={}#主要是存储每个类标签出现的评率
     for i in classList:
         if i not  in classList.keys(): classCount[i]=0 # 如果一次也没有，次数就赋值为0
         classCount+=1
         sorted_classCount=sorted(classCount.iteriterms(),key=operator.itemgetter(1),reverse=True)
     return  sorted_classCount
 #创建树
def createTree(dataSet, labels,featLabels):

     # 取分类标签（是否出去玩：yes or no）
     classList = [example[-1] for example in dataSet]
     # 如果类别完全相同则停止继续划分
     if classList.count(classList[0]) == len(classList):
         return classList[0]
     # 遍历完所有特征时返回出现次数最多的类标签
     if len(dataSet[0]) == 1:
         return majorityCnt(classList)
     # 选择最优特征
     bestFeat = ChoosebestSplitData(dataSet)
     # 最优特征的标签
     bestFeatLabel = labels[bestFeat]
     featLabels.append(bestFeatLabel)
     # 根据最优特征的标签生成树
     myTree = {bestFeatLabel: {}}
     # 删除已经使用的特征标签
     # 得到训练集中所有最优解特征的属性值
     featValues = [example[bestFeat] for example in dataSet]
     # 去掉重复的属性值
     uniqueVals = set(featValues)
     # 遍历特征，创建决策树
     for value in uniqueVals:
        del_bestFeat = bestFeat
        del_labels = labels[bestFeat]
        del (labels[bestFeat])
        myTree[bestFeatLabel][value] = createTree(SplitData(dataSet, bestFeat, value), labels, featLabels)
        labels.insert(del_bestFeat, del_labels)
     return myTree

def getleaf_num(myTree):
     leaf_num=0
     Start = next(iter(myTree))

     Then = myTree[Start]

     for key in Then.keys():
         if type(Then[key]).__name__ == 'dict':
             leaf_num += getleaf_num(Then[key])
         else:
             leaf_num += 1
     return leaf_num

def getTree_Depth(myTree):
     Depth = 0
     Start=next(iter(myTree))
     Then = myTree[Start]
     for key in Then.keys():
         if type(Then[key]).__name__ == 'dict':
             thisDepth =1 + getTree_Depth(Then[key])
         else:
             thisDepth = 1
     if thisDepth>Depth:
        Depth=thisDepth
     return Depth

def plotNode(nodeTxt, centerPt, parentPt, nodeType):                                           #定义箭头格式
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)        #设置中文字体
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',xytext=centerPt, textcoords='axes fraction',va="center", ha="center", bbox=nodeType, arrowprops=dict(arrowstyle="<-"), FontProperties=font)

 """
 函数说明:标注有向边属性值
 """
def plotMidText(cntrPt, parentPt, txtString):
     xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]                                            #计算标注位置
     yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
     createPlot.ax1.text(xMid, yMid, txtString)
 """
 函数说明:绘制决策树
 ​
 Parameters:
     myTree - 决策树(字典)
     parentPt - 标注的内容
     nodeTxt - 结点名
 """
def plotTree(myTree, parentPt, nodeTxt):
     decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # 设置结点格式
     leafNode = dict(boxstyle="round4", fc="0.8")
     #设置叶结点格式
     numLeafs = getleaf_num(myTree)                                                          #获取决策树叶结点数目，决定了树的宽度
     depth = getTree_Depth(myTree)                                                            #获取决策树层数
     firstStr = next(iter(myTree))                                                            #下个字典
     cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)    #中心位置
     plotMidText(cntrPt, parentPt, nodeTxt)                                                    #标注有向边属性值
     plotNode(firstStr, cntrPt, parentPt, decisionNode)                                        #绘制结点
     secondDict = myTree[firstStr]                                                            #下一个字典，也就是继续绘制子结点
     plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD                                        #y偏移
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':                                            #测试该结点是否为字典，如果不是字典，代表此结点为叶子结点
            plotTree(secondDict[key],cntrPt,str(key))                                        #不是叶结点，递归调用继续绘制
        else:                                                                                #如果是叶结点，绘制叶结点，并标注有向边属性值
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

 """
 函数说明:创建绘制面板
 ​
 Parameters:
     inTree - 决策树(字典)
 """
def createPlot(inTree):
     fig = plt.figure(1, facecolor='white')#创建fig
     fig.clf()#清空fig
     axprops = dict(xticks=[], yticks=[])
     createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)#去掉x、y轴
     plotTree.totalW = float(getleaf_num(inTree))#获取决策树叶结点数目
     plotTree.totalD = float(getTree_Depth(inTree))#获取决策树层数
     plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0#x偏移
     plotTree(inTree, (0.5,1.0), '')#绘制决策树
     plt.show()#显示绘制结果
if __name__=='__main__':
     myDat,labels=creatDataSet()
     featLabels = []
     myTree=createTree(myDat,labels,featLabels)
     createPlot(myTree)
