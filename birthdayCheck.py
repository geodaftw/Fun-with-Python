#! python3.
# Check someone's birthday and tell us how long until their birthday
# Written by: Eric Guillen

from datetime import *
import csv

# Get Today's Date
today = date.today()
print("[+] Important Days Calculator")
print("[+] Today: " + today.strftime('%A, %b %d, %Y'))

bday = csv.DictReader(open("dates.csv"))

bdayList = dict()
for ud in bday:
    bdayList[ud.pop('name')] = ud

print("")
'''
print("Here's a list of Birthdays we have: ")
for i, j in bdayList.items():
    print(str(i) + ': ' + str(j['Date']))
'''

# Loop through the bdayList, extract date values and put them into variables
# Calculate today and calculate how many days until the day is reached
for i, j in bdayList.items():
    dob_data = str(j['Date']).split("-")
    dobMonth = int(dob_data[0])
    dobDay = int(dob_data[1])
    thisYear = int(today.strftime('%Y'))

    nextBirthday = date(thisYear,dobMonth,dobDay)
    if today<nextBirthday:
        gap = (nextBirthday - today).days
        print("[+] " + str(i) + ": " + str(gap) + " days")
    elif today == nextBirthday:
        print("[+] Today is " + str(i) + "'s Day! Time to celebrate!")
    else:
        nextBirthday = date(thisYear+1,dobMonth,dobDay)
        gap = (nextBirthday - today).days
        print("[+] " + str(i) + ": " + str(gap) + " days")


