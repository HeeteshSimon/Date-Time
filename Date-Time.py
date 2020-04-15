import datetime
today=datetime.date.today()
print(today)
birthday=datetime.date(1996,5,19)
print(birthday)
alive_days=(today-birthday).days
print(alive_days)