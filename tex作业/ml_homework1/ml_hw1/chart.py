import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# epoch,acc,loss,val_acc,val_loss
x_axis_data = [0, 0, 0.2, 0.4, 0.4, 0.6, 0.8, 1]  # (0,0)必有
y_axis_data = [0, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1]
# 画图

plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=1, label='ROC')  # '
for a, b in zip(x_axis_data, y_axis_data):
    plt.text(a, b, str(b), fontsize=8)  # ha='center', va='top'
plt.legend()  # 显示上面的label
plt.xlabel('TPR')
plt.ylabel('FPR')  # accuracy
plt.ylim(0, 1)  # 仅设置y轴坐标范围
plt.xlim(0, 1)
plt.show(block=True)

print(0.2 * 0.25 + 0.2 * 0.5 + 0.4 * 0.75 + 0.2 * 1)
