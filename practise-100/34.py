content = '''
    joker9999988888ddd
    真真正1234457677正
    调度的调度的 2221111117977
'''

import re

pattern = r'(\d+)'

result = re.sub(pattern, r'***', content)
print(result)