import numpy as np
import scipy
a = np.array([[10,7],[9,1]])
b=np.sort(a)
b[0][0]=0
print(b)
print(a)