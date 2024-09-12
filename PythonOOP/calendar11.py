# # Write a python program to display calendar
import calendar

# get the year
year = int(input("Please enter the year: "))
month = int(input("Enter the month: "))

# get the month and the year from the calender module
cal = calendar.month(year, month)

print(cal)

