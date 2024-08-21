import datetime

def get_diff_days(date_str, days):
    # 构造成日期对象
    base_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    # 差异日期
    time_gap = datetime.timedelta(days=days)
    diff_date = base_date - time_gap
    return diff_date.strftime('%Y-%m-%d')

print(get_diff_days('2024-08-20', 200))
print(get_diff_days('2024-08-20', 100))
