#理解题干 一个细胞分裂第三次就会死亡  上网查找 细胞分裂递归问题 有图解
def all_cell(time):
    def a_cell(time):# 思考每一个细胞的来源 
        if time==1:
            return 1
        else:
            return a_cell(time-1)+b_cell(time-1)+c_cell(time-1)
        
    def b_cell(time):
        if time==1:
            return 0
        else:
            return a_cell(time-1)
        
    def c_cell(time):
        if time==1 or time==2:
            return 0
        else:
            return b_cell(time-1)
    return a_cell(time)+b_cell(time)+c_cell(time)
def main():
    time=eval(input("请输入第几个小时之后:"))
    print(all_cell(time))
main()