content = '''
    2021/05/26
2021.05.25
        05-23-2021  05/26/2022
        
'''

import re

content = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3', content)
content = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r'\1-\2-\3', content)
content = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\2-\1', content)
content = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\2-\1', content)

print(content)