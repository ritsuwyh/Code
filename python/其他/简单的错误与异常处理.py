def temp_convert(var):
    try:
        return int(var)
    except ValueError as x:
        print ("参数没有包含数字\n",x)

# 调用函数
temp_convert("xyz")