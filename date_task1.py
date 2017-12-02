from datetime import datetime, date, timedelta


date_str = "01/01/17 12:10:03.234567"
date_from_str = datetime.strptime(date_str,"%m/%d/%y %H:%M:%S.%f")
print(date_from_str)

today = date.today()
delta_day = timedelta(days=1)
yesterday = today - delta_day
delta_month = timedelta(365/12)
month_ago = today - delta_month
print("Сегодня {}, а вчера было {}, а месяц назад было {}".format(today,yesterday,month_ago))