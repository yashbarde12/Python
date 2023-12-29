# datetime module
#--------------------------------------------------------
import datetime
#--------------------------------------------------------
print("-----datetime.datetime.now()-----")
today_with_time = datetime.datetime.now()
print(today_with_time) # 2023-12-29 19:27:44.065409  
#--------------------------------------------------------
print("-----datetime.date.today()-----")
today_without_time = datetime.date.today()
print(today_without_time) # 2023-12-29
#--------------------------------------------------------
print("-----strftime-----")
# Types
# first 3 letters of weekday
print(today_with_time.strftime("%a")) # Fri

# complete name of weekday
print(today_with_time.strftime("%A")) # Friday

# number of weekday(monday is 1, tuesday is 2...)
print(today_with_time.strftime("%w")) # 5

# day of month
print(today_with_time.strftime("%d")) # 29

# first 3 letters of month
print(today_with_time.strftime("%b")) # Dec

# complete name  of month
print(today_with_time.strftime("%B")) # December

# 2 digits of year
print(today_with_time.strftime("%y")) # 23

# 4 digits of year
print(today_with_time.strftime("%Y")) # 2023

# represent the zero-padded hour (00-23) of a datetime object.
print(today_with_time.strftime("%H")) # 19 # because now time is 7:43 PM 

# represent the zero-padded minute (00-59) of a datetime object.
print(today_with_time.strftime("%M")) # 46 # because now time is 7:46 PM

# represent the zero-padded second (00-59) of a datetime object.
print(today_with_time.strftime("%S")) # 23

# Formating date
print(today_with_time.strftime("%d/%b/%Y")) # 29/Dec/2023
print("Today with time is :",today_with_time.strftime("%A %H:%M")) # Today with time is : Friday 20:10
#--------------------------------------------------------
# getting information from random date
print("-----information from random date-----")

# (year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
random_date = datetime.datetime(2023,12,23,13,45,30,35650) 
print(random_date) # 2023-12-23 13:45:30.035650

print(random_date.strftime("%A")) # Saturday
print("Year :", random_date.year) # Year : 2023
print("Month:", random_date.month) # Month: 12
print("Day  :", random_date.day) # Day  : 23
print("Hour  :", random_date.hour) # Hour  : 13
print("Minute:", random_date.minute) # Minute: 45
print("Second:", random_date.second) # Second: 30
print("Micro second:", random_date.microsecond) # Micro second: 35650

# x = datetime.date(2023,11,31) # ValueError: day is out of range for month
x = datetime.date(2023,12,31)
print(x) # 2023-12-31
#--------------------------------------------------------
# diff between 2 dates
print("-----Difference between 2 dates-----")

d1 = datetime.date(2023,12,4)
d2 = datetime.date(2023,12,6)
d3 = d2 - d1
d4 = d1 - d2
print(d3) # 2 days, 0:00:00
print(d4) # -2 days, 0:00:00

d5 = datetime.datetime(2023,12,4,13,45,30,35650)
d6 = datetime.datetime(2023,12,6,14,46,30,35650)
print(d6-d5) # 2 days, 1:01:00
#--------------------------------------------------------
#--------------------------------------------------------