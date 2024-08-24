arr = [1, 2, 3, 4, 5, 8, 77, 122] # 实现reverse逆序
size = len(arr)
for i in range(0, (size - 1) >> 1):
    arr[i], arr[size - i - 1] = arr[size - i - 1], arr[i]
print(arr)