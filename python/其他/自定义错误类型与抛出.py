class your_error(ValueError):
    def __init__(self, name):
      self.name = name
        
def mye( level ):
    if level < 1:
        raise your_error("Invalid level!")
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)
finally:
    pass