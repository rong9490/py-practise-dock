# 正则验证日期字符串, 合法

import re

date1 = '2021-05-10'
date2 = '2022/01-32'
date3 = '20220101'
date4 = '2024-10-29 00:00:00'

def date_is_right(date):
    # <re.Match object;>
    return re.match(pattern='^\d{4}-\d{2}-\d{2}$', string=date) is not None

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
