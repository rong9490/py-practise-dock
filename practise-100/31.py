# 提取邮箱地址

article = '''
            在《时间简史》第一章开头，讲述了这样一个故事：曾经有一位著名的科学家在一次天文学演讲中，描述了地球是如何围绕着太阳公转的，而太阳又
            是如何围绕着星系公转的。当演Username@126.com讲结束之际，一位太太站起来说到：你讲的是一派胡言。
            support@68abc.com
            实际上，世界是由一pythnin-ab@123.com
            pyzzz-666@sina.net
            只大乌龟驮在背上的。而这xxxxxxxx@126.com只乌
            龟又站在另一只更大的乌龟背上，它们就像这样一只驮着一只组成了一座无限巨大的乌龟塔。abceee@hejj.cn
'''

import re

# pattern = re.compile(r'''
#     [a-zA-Z0-9_-]+          # 匹配用户名部分
#     @                       # 匹配 @ 符号
#     [a-zA-Z0-9]{1,4}       # 匹配域名部分（1到4个字母或数字）
#     \.                      # 匹配点（.）
#     (com|cn|net)           # 匹配结尾部分（com、cn 或 net）
# ''', re.VERBOSE)  # 使用 VERBOSE 模式

# TODO 这里的捕获有问题

pattern = re.compile(r'''
    [a-zA-Z0-9_-]+          # 用户名部分
    @                       # @ 符号
    [a-zA-Z0-9]{1,4}       # 域名部分（1到4个字母或数字）
    \.                      # 点（.）
    (com|cn|net|org|info|biz|[a-z]{2,8})  # 支持多个后缀
''', re.VERBOSE)  # 使用 VERBOSE 模式

results = pattern.findall(article)

for res in results:
    print(res)