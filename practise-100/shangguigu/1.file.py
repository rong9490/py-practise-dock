# 打开文件: 路径+名称
f = open('./test.txt')
# 读取文件: 具柄
context = f.read()
print(context)
# 关闭文件
f.close()