arr = [i for i in range(1, 11)]
arr2 = [0 for i in range(1, 11)]

move_size = 6

# range左闭右开
for i in range(0, len(arr)):
    val = arr[i]
    print(f'val={val}')
    arr2[i - move_size] = val

print(arr)
print(arr2)