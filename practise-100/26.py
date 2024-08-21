import datetime

timestamp = 1620747224

date_obj = datetime.datetime.fromtimestamp(timestamp)
date_str = date_obj.strftime('%Y-%m-%d %H:%M:%S')
print(date_str)