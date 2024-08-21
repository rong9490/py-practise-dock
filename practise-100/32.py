# 密码验证

import re

def check_pwd(pwd):
    if not 8 <= len(pwd) <= 20:
        return False, '长度不对'
    if not re.findall(r'[a-z]', pwd):
        return False, '需包含小写'
    if not re.findall(r'[A-Z]', pwd):
        return False, '需包含大写'
    if not re.findall(r'[0-9]', pwd):
        return False, '需包含数字'
    if not re.findall(r'[^0-9a-zA-Z]', pwd):
        return False, '需包含特殊字符'
    return True, None

print(check_pwd('#hdddd'))
print(check_pwd('absdddddddddddd'))
print(check_pwd('a293333811'))
print(check_pwd('aA2933@@'))
print(check_pwd('111aaAS@@@@#!'))
print(re.findall(r'[^0-9a-zA-Z]', '111aaAS@@@@#!'))