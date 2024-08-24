arr = [1, 4, 6, 9, 17, 22, 49, 110, 0] # 最后需要多一位0站位!
for i in range(0, len(arr) - 1): print(arr[i], end = ' ')
print()

number = int(input('Search:'))

## 核心: 排序, 插入: 从后往前倒序

local = 0
for i in range(len(arr) - 2, -1, -1):
    if number > arr[i]:
        local = i + 1
        break
print(f'local={local}')

for i in range(len(arr) - 1, local - 1, -1):
    arr[i] = arr[i - 1] # 相邻挪动

arr[local] = number # 将数字插入到最后挪位空出的位置
print(arr)