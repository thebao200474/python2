d,m,y = map(int,input("Nhap ngay thang nam: ").split())
import datetime
date = datetime.date(y,m,d)
next_day = date + datetime.timedelta(days=1)
print(next_day.day, next_day.month, next_day.year)