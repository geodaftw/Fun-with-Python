#!/usr/bin/python3

import sqliteTest

sqliteTest.CreateDB()
#sqliteTest.CheckAgent()
#sqliteTest.AddAgent()
#sqliteTest.ChangeAgentName()
#print("First alphaNumeric Random String is  ", sqliteTest.RandomAgentID(8#))
#sqliteTest.AllDatabaseEntries()
#sqliteTest.DeleteAllEntries()

choice = input("What do you want to do?\n" + \
        "Type 1 to Add Agent\n" + \
        "Type 2 to Print All Entries\n" + \
        "Type 3 to Delete All Entries\n" + \
        "Type 4 to Change Agent Name\n")

if choice == '1':
    sqliteTest.AddAgent()
elif choice == '2':
    sqliteTest.AllDatabaseEntries()
elif choice == '3':
    sqliteTest.DeleteAllEntries()
elif choice == '4':
    sqliteTest.ChangeAgentName()
else:
    print("Invalid Choice")
