import jioeba.posseg as posseg

content = ''
words = []
for word, flag in posseg.cur(content):
    if flag == 'nr':
        print(word, flag)
        words.append(word)

import pandas as pd
print(pd.Series(words).value_counts()[:20])

