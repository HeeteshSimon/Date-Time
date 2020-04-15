#Import the DateTime Module
import datetime
#Wrote the code to check the working of module-By Checking the Current date
today=datetime.date.today()
#Print It
print(today)
#Checked the B'day Thing-By specifying the DOB
birthday=datetime.date(1996,5,19)
#Print It
print(birthday)
#Checked The no. of days I'm alive-By finding the difference b/w today and DOB,
#Alse, Make sure that it's only returning no. of days not the complete object-By including the "('').days"
alive_days=(today-birthday).days
#Print It
print(alive_days)
#Added 10 days to the current date- You can also subtract it LOL
tdelta=datetime.timedelta(days=10)
#Print It
print(today+tdelta)
#Print todays' Day
print(today.day)
#Print WeekDay of Today's day
#It Returns a number coz, Mon=0 ------Sun=6
print(today.weekday())
