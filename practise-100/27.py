import datetime

date_sale ={}

with open('./files/date_sale_data.txt') as fin:
    is_first_line = True
    for line in fin:
        line = line[:-1]
        if is_first_line:
            title_date, title_sale = line.split(' ')
            is_first_line = False
            continue
        date, sale = line.split(' ')
        date_sale[date] = float(sale)

print(date_sale)

# 遍历找到其n天前的日期
n = 3

def get_diff_days(date, n):
    curr_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    timedelta = datetime.timedelta(days=-n)
    return (curr_date + timedelta).strftime('%Y-%m-%d')

for date, sale in date_sale.items():
    dateN = get_diff_days(date, n)
    saleN = date_sale.get(dateN, 0) # 可能不存在
    if saleN == 0:
        # print(date, sale, 0)
        continue
    # 求周同比
    n_diff_rate = round(100 * (sale - saleN) / saleN, 2)
    print(date, sale, dateN, saleN, f'{n_diff_rate}%')
