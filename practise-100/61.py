# 杨辉三角

line_size = 15

lines = list()
for i in range(0, line_size):
    lines.append([])
    for j in range(0, i + 1):
        if j == 0 or j == i:
            # line.append(str(1).rjust(2, '0'))
            lines[i].append(1)
        else:
            # 通过上一行的计算
            # val = int(lines[i - 1][j]) + int(lines[i - 1][j - 1])
            # line.append(str(val).rjust(2, '0'))
            lines[i].append(lines[i - 1][j] + lines[i - 1][j - 1])

for i in lines:
    print(i)