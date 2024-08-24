arr = [83, -110, 27, 220, -34, 12, 256, -122]

max_pair = (0, arr[0])
min_pair = (0, arr[0])

for i in range(0, len(arr) - 1):
    cell = arr[i]
    if cell < min_pair[1]:
        min_pair = (i, cell)
    if cell > max_pair[1]:
        max_pair = (i, cell)

arr[max_pair[0]], arr[min_pair[0]] = arr[min_pair[0]], arr[max_pair[0]]
print(max_pair, min_pair)
print(arr)
