import datetime

start_date_str = '2021-02-22'
end_date_str = '2021-05-03'

def get_date_ticks(start, end):
    date_ticks_result = []
    while start <= end: # 日期可以直接比较
        date_ticks_result.append(start)
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        days1_timedelta = datetime.timedelta(days=1) # 日期差对象, timedelta
        # 加一天后重新赋值
        start = (start_date + days1_timedelta).strftime('%Y-%m-%d')
    return date_ticks_result

date_ticks = get_date_ticks(start_date_str, end_date_str)
print(date_ticks)