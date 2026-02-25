d,m,y = map(int,input("Nhap ngay thang nam: ").split())
import datetime
date = datetime.date(y,m,d)
prev_day = date - datetime.timedelta(days=1)
print(prev_day.day, prev_day.month, prev_day.year)