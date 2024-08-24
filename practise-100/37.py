import jieba
import re

content = re.sub(r'[\s. ...,]]', '')
print(jieba.cur(content))
