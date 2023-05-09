# Painting类，暂时还没想好是按照函数或者按照类来建立
# 但是先将几个主要的函数构建出来，留待第四节课使用
import pandas as pd
from account import Account


class Painting:
    pass


def AnnualAnalysis(Analysis_Object: Account):
    """
    根据Analysis_Object（一年的统计数据），生成折线图。具体而言，可以分析十二个月四种Type数量的统计变化
    :param Analysis_Object:
    :return:
    """
    pass


def MonthTypeAnalysis(Analysis_Object: Account):
    """
    根据Analysis_Object（统计数据），生成热力图，分析十二个月和各种书的借还之间的热力图
    :param Analysis_Object:
    :return: 成功则没有返回值（会生成图），否则
    """


def YearAnalysis(Analysis_Object:Account):
    """
    根据Analysis_Object（统计数据），生成折线图，分析几年间的总事件数量，总注册用户数量或其他数量
    :param Analysis_Object:
    :return:成功则没有返回值（会生成图），否则
    """
