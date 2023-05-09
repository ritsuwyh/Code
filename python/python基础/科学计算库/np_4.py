import numpy as np

# 1
A = np.array([[[0., 1.], [0., 1.], [1., 0.]], [[0., 1.], [1., 1.], [1., 0.]]])
print(A)
print(np.prod(A, axis=0))
print(np.prod(A, axis=1))
# In [5]: %timeit np.prod(A,axis=1)
# 7.15 µs ± 162 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
print(np.prod(A, axis=2))

# 2
lst = [[[0., 1.], [0., 1.], [1., 0.]], [[0., 1.], [1., 1.], [1., 0.]]]
ans = [[1 for i in range(len(lst[0][0]))] for _ in range(len(lst))]

for i in range(len(lst)):
    for j in range(len(lst[0])):
        for k in range(len(lst[0][0])):
            ans[i][k] *= lst[i][j][k]
print(ans)
