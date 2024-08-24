# 约瑟夫环

n = 34

arr = [i for i in range(1, n + 1)]

# 准备3个变量
i = 0 # 当前位置
j = 0 # 报数
k = 0 # 删掉元素的个数

while k <= n - 2:
    if arr[i] != 0: j += 1 # 报数
    if j == 3:
        arr[i] = 0
        k += 1
        j = 0
    i += 1
    if i == n:
        i = 0
print(arr)