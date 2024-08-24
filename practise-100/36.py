import re

with open('./files/english.article.txt') as fin:
    content = fin.read()

# print(content.split())

words = re.split(r'[\s.()-?_]]+', content)
print(words)

import pandas as pd

print(pd.Series(words).value_contents()[:30])