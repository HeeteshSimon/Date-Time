#Import the DateTime Module
import datetime
#import the time zone module
import pytz
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
#Three ways to do dateTime lol
#datetime.date(Y, M, D)
#datetime.time(h, m, s, ms)
#datetime.datetime(Y, M, D, h, m, s, ms)
print(datetime.time(11, 58, 20, 15))
#Created Hour delta to add 10 hrs to current time
hour_delta=datetime.timedelta(hours=10)
#Print It using the 3rd way and added hourdelta to get next day with adding of 10hrs
print(datetime.datetime.now() + hour_delta)
#Checking the Time zone module
datetime_today=datetime.datetime.now(tz=pytz.UTC)
#Pacifice Timezone
datetime_pacific=datetime_today.astimezone(pytz.timezone('US/Pacific'))
#print It
print(datetime_pacific)
#loop to find all TimeZones
for tz in pytz.all_timezones:
    print(tz)
#String Formatting with dates
# 2020-04-16--> April 16,2020
#Use strftime (f=Formatting)
print(datetime_pacific.strftime('%B %d, %Y'))
#April 16,2020-->DateTime Object (2020,04,16)
#Use strptime (p=Parsing)Also for getting object use repr()
datetime_thing=datetime.datetime.strptime('April 16,2020','%B %d,%Y')
print(repr(datetime_thing))
