class IndexException(Exception):
    """
    这个异常是操作下标不对（可能是越界或类型不对），可以终止程序或忽略
    """
    pass


class FilterException(Exception):
    """
    这个异常是排序过程中发生了错误
    """
    pass


class TimeSequenceException(Exception):
    """
    这个异常是前后时间顺序不对，可以修复（对进行排序）
    """
    pass


class InvalidOperationException(Exception):
    """
    这个错误是发生了非法操作时产生的
    """
    pass


class InvalidObjectException(Exception):
    """
    这个异常是操作符或操作过程中有不合法的对象
    """
    pass
