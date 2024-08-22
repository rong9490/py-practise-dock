import re

content = '''
小码上街买菜
买了1斤黄瓜花了8.1元
买了2斤西红柿花了11.5元
买了3斤花生花了28元
买了14斤大米花了117.2元
'''

for line in content.split('\n'):
    pattern = r'(\d+)斤(.*)花了(\d+(?:\.\d+)?)元'
    match = re.search(pattern, line)
    if match:

        print(f'{match[1]}\t{match[2]}\t{match[3]}')