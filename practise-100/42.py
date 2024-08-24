# 矩阵加法

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]

z = x.copy()

for i in range(len(x[0]) - 1):
    for j in range(len(y[0]) - 1):
        z[i][j] = x[i][j] + y[i][j]

print(z)