# Charlie Say AS - Level Computing

# Davenant Foundation School

# SADS (Sunshine Ameatur Dramatic Society) Have asked for a system, that can help
# Their performances that they put on, as they put on a 3rd performance in the year
# This program will allow them to put on the 3rd performance by processing
# Majority of the bookings , customers and revenue queries.

# For Clearing the screen, which can only be done in the command window
# This module allopws gathering information from the operating system - This is used in the os.environ.get code.
import os
# SQLite , is a software library that runs off the SQL Database Engine
import sqlite3
# For closing down the program, in the command line
from time import sleep
#This is used in checking wether or not seats are available. 
from itertools import groupby


#This function is for displaying the main menu, NOT Choosing the options in the menu.
def menu():
#The os.enviorn retrieves the username of the logged in user.
    print "____________________________________________"
    print "|-------------------MENU-------------------|"
    #os.environ.get is getting information from the operating system, in this case its getting the username
    #so the system looks more user-friendly.
    print "|     Hi " + os.environ.get("USERNAME") + " welcome to the SADS menu     |"
    print "|------------------------------------------|"       
    print "|     1 - Add New customer details         |"
    print "|     2 - Edit customer details            |"
    print "|     3 - View customer details            |"
    print "|     4 - Show Available seats             |"
    print "|     5 - Book a new seat                  |"
    print "|     6 - Show Income                      |"
    print "|     7 - Exit                             |"
    print "--------------------------------------------"
    print "| In the choice box below, please put the  |"
    print "| number of the page you want to visit     |"
    print "|------------------------------------------|"
    global choice
    choice = raw_input("| Choice: ")
    print "|------------------------------------------|"
    #The os.system('cls') code is used throughout the program to clear the screen in the command line.
    os.system('cls')
    
def newdetails():
    os.system('cls')
    print "____________________________________________"       
    print "|---------Add new customer details---------|"
    print "|------------------------------------------|"
    #Here i am declaring a new array for the user to input new customer details into the system.
    newdetails=[0,1,2,3,4,5,6,7,8]
    newdetails[0] = raw_input("|Customer ID: ")
    while True:
        #Newdetails[1] is the forename in the customer table.
        newdetails[1] = raw_input("|Forename: ")
        #This is a presence check, if no input is detected it will go to the else statement below.
        if newdetails[1] != None:
            break
        else:
            print "|------------------------------------------|"
            print "|You didnt put anything in! Try again      |"
            print "|------------------------------------------|"
    while True:
        #Newdetails[2] is the surname in the customer table.
        newdetails[2] = raw_input("|Surname: ")
        #This again is another presence check, if no input is detected it will resort to the else statement below.
        if newdetails[2] != None:
            break
        else:
            print "|------------------------------------------|"
            print "|You didnt put anything in! Try again      |"
            print "|------------------------------------------|"
    while True:
        #Newdetails[3] is address line 1 in the customer table
        newdetails[3] = raw_input("|Address Line 1: ")
        #This validation is a length check, it will only accept inputs from 5 - 30 Letters.
        if len(newdetails[3]) > 30:
            print "|------------------------------------------|"
            print "|Your input was over 30 Letters try again  |"
            print "|------------------------------------------|"
        elif len(newdetails[3]) < 5:
            print "|------------------------------------------|"
            print "|Your input was under 5 Letters try again  |"
            print "|------------------------------------------|"
        else:
            break
    while True:
        #Newdetails[4] is address line 2 in the customer table
        newdetails[4] = raw_input("|Address Line 2: ")
        #This validation is the exact same as address line 1.
        if len(newdetails[4]) > 30:
            print "|------------------------------------------|"
            print "|Your input was over 30 Letters try again  |"
            print "|------------------------------------------|"
        elif len(newdetails[3]) > 1 and len(newdetails[3]) < 5:
            print "|------------------------------------------|"
            print "|Your input was under 5 Letters try again  |"
            print "|------------------------------------------|"
        else:
            break
    while True:
        #newdetails[5] is the city in the customer table
        newdetails[5] = raw_input("|City: ")
        #This validation is another presence check, if nothing is input into the program, it will resort to the
        #else statement
        if newdetails[5] != None:
            break
        else:
            print "|------------------------------------------|"
            print "|You didnt put anything in! Try again      |"
            print "|------------------------------------------|"
    while True:
        #newdetails[6] is the postcode in the customer table
        newdetails[6] = raw_input("|Postcode: ")
        #this validation is another length check, as UK Postcodes can only be 8 characters, it only accepts a length
        #of 8 characters.
        if len(newdetails[6]) < 8:
            print "|------------------------------------------|"
            print "|Your input was not 8 letters              |"
            print "|Postcodes in the UK Are only 8 Letters!   |"
            print "|Try again!                                |"
            print "|------------------------------------------|"
        elif len(newdetails[6]) > 8:
            print "|------------------------------------------|"
            print "|Your input was not 8 letters              |"
            print "|Postcodes in the UK Are only 8 Letters!   |"
            print "|Try again!                                |"
            print "|------------------------------------------|"
        else:
            break
    while True:
        #newdetails[7] is the telephone number in the customer table
        newdetails[7] = raw_input("|Telephone: ")
        #This validation check is for the telephone, as telephone numbers can only be 11 Characters, so the program will only accept 11 characters as a telephone number.
        if len(newdetails[7]) > 11:
            print "|------------------------------------------|"
            print "|Your input was over 11 Letters try again  |"
            print "|------------------------------------------|"
        elif len(newdetails[7]) < 11:
            print "|------------------------------------------|"
            print "|Your input was under 11 Letters try again |"
            print "|------------------------------------------|"
        else:
            break
    while True:
        #newdetails[8] is the email in the email in the customer table
        newdetails[8] = raw_input("|E-Mail: ")
        atsign = '@'
        #a presence check is used here to check wether there is an @ sign in the input.
        if atsign in newdetails[8]:
            break
        else:
            print "|------------------------------------------|"
            print "|You didnt put in a @ ! Try again          |"
            print "|------------------------------------------|"
    while True:
        print "|------------------------------------------|"
        choice = raw_input("|Do you want to confirm? Y/N : ")
        print "|------------------------------------------|"  
        if choice == "Y":
            #sqlite.connect connects the program to the database file
            conn = sqlite3.connect('SADS.db')
            #This creates a cursor which allows all the commands to be executed
            cur = conn.cursor()
            #This code is adding the new customers details through the array into the customer table in the SADS.db file.
            cur.execute("INSERT INTO customers (CustID,Surname,Forename,Address1,Address2,City,Postcode,Telephone,EMail) VALUES (?,?,?,?,?,?,?,?,?)", (newdetails[0],newdetails[1],newdetails[2],newdetails[3],newdetails[4],newdetails[5],newdetails[6],newdetails[7],newdetails[8]))
            #This code esentially saves the change. It commits the changes.
            conn.commit()
            print "|------------------------------------------|"
            print "|Confirmed, and added                      |"
            print "|------------------------------------------|"
            break
        elif choice == "N":
            #This is if someone sees an error, and dont want to confirm the details. Though they have to add each
            #Detail in again.
            print "|------------------------------------------|"
            print "|Not added - Press enter to return to      |"
            print "|Main menu                                 |"
            print "|------------------------------------------|"
            raw_input("")
            os.system('cls')
            mainprogram()
            break
        else:
            print "|------------------------------------------|"
            print "|You didn't type 'Y' or 'N' Try again!     |"
            print "|Press enter to return to confirmation     |"
            print "|------------------------------------------|"
    while True:
        print "|Do you want to:                           |"
        print "|1 - Book seats                            |"
        print "|2 - Return to menu                        |"
        print "|In the choice box below, please put the   |"
        print "|number of the page you want to visit      |"
        print "|------------------------------------------|"
        choice = raw_input("| Choice: ")
        print "|------------------------------------------|"
        if choice == "1":
            bookseat()
            break
        elif choice == "2":
            mainprogram()
            break
        else:
            print "|------------------------------------------|"
            print "|You didn't type in 1 or 2! Try again      |"
            print "|Press enter to try again                  |"
            print "|------------------------------------------|"
            raw_input("")
            os.system('cls')
        os.system('cls')

def availablity():
    os.system('cls')
    #This part of the program shows what seats are available, the seat layout as shown has no interaction
    #with the database, it just is a text way of showing what it is in the specification.
    print "|_______________________________________________________________________|"
    print "||____________________________SEAT LAYOUT________________________________\ "
    print "|                                                                         \ "
    print "|---------------------L--(15) 14 13 12 11 10 09 08 07 06 05 04 03 02 (01)-|"
    print "|-----(19)18 17 (16)--K--(15) 14 13 12 11 10 09 08 07 06 05 04 03 02 (01)-|"
    print "|-(19) 18 17 16 (15)--J--(14) 13 12 11 10 09 08 07 06 05 04 03 02(01)-----|"
    print "|-(19) 18 17 16 (15)--H--(14) 13 12 11 10 09 08 07 06 05 04 03 02(01)-----|"
    print "|-(19) 18 17 16 (15)--G--(14) 13 12 11 10 09 08 07 06 05 04 03 02(01)-----|"
    print "|-(20) 19 18 17 (16)--F--(15) 14 13 12 11 10 09 08 07 06 05 04 03 02 (01)-|"
    print "|-(20) 19 18 17 (16)--E--(15) 14 13 12 11 10 09 08 07 06 05 04 03 02 (01)-/"
    print "|-(19) 18 17 16 (15)--D--(14) 13 12 11 10 09 08 07 06 05 04 03 02(01)----/"
    print "|-----(17)16 15 (14)--C--(13) 12 11 10 09 08 07 06 05 04 03 02(01)------/"
    print "|-----(16)15 14 (13)--B--(12) 11 10 09 08 07 06 05 04 03 02(01)--------/"
    print "|--------(14)13 (12)--A--(11) 10 09 08 07 06 05 04 03 02(01)----------/"
    print "|____________________________________________________________________/"
    print "|                                                                    |"
    print "|                            |Stage|                                 |"
    print "|____________________________________________________________________|"
    #These instructions are clear and percise.
    print "|This is the layout of the seats in the theatre. The actual available|"
    print "|seats on the next screen, will not be in the same layout as above   |"
    print "|--------------------------------------------------------------------|"
    print "|Below type what day you want to check on                            |"
    print "|Type F for Friday and S for Saturday (Capitals ARE Needed!)         |"
    print "|--------------------------------------------------------------------|"
    global choice 
    while True:
        choice = raw_input("|Choice: ")
        if choice == "F":
            conn = sqlite3.connect('SADS.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM seats WHERE Day = 'F' AND Booked = 'N' AND Disabled = 'N'")
            #This is for displaying available seats. It takes a letter say 'A' and puts it into a row with all the
            #other records that have the same letter in the table, such as A1,A2 then the next line B1,B2
            for letter, rows in groupby(cur, key=lambda r: r[0][0]):
                print '|'.join([r[0] for r in rows])
            cur.execute("SELECT * FROM seats WHERE Day = 'F' AND Booked = 'N' AND Disabled = 'Y'")
            #This merely retrieves the disabled seats, but doesnt group it. It just prints them all out in a linear
            #Statement in the order they are in the database table
            print '|Disabled seats available : ','| '.join([r[0] for r in cur] ) ,"|"
            print "|------------------------------------------|"
            print "|Please press enter to return to the menu  |"
            print "|------------------------------------------|"
            raw_input("")
            break
        elif choice == "S":
            conn = sqlite3.connect('SADS.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM seats WHERE Day = 'S' AND Booked = 'N' AND Disabled = 'N'")
            for letter, rows in groupby(cur, key=lambda r: r[0][0]):
                print '|'.join([r[0] for r in rows])
            cur.execute("SELECT * FROM seats WHERE Day = 'S' AND Booked = 'N' AND Disabled = 'Y'")
            print '|Disabled seats available : ','| '.join([r[0] for r in cur] ) ,"|"
            print "|------------------------------------------|"
            print "|Please press enter to return to the menu  |"
            print "|------------------------------------------|"
            raw_input("")
            break
        else:
            print "|------------------------------------------|"     
            print "|You didnt put 'F' Or 'S'! Please try again|"
            print "|Press enter to return to the choice       |"
            print "|------------------------------------------|"
            raw_input("")
            os.system('cls')
    os.system('cls')

def editdetails():
    print "____________________________________________"
    print "|--------------Editing Details-------------|"
    print "|------------------------------------------|"
    os.system('cls')
    conn = sqlite3.connect('SADS.db')
    cur = conn.cursor()
    print "|------------------------------------------|"
    print "|Does the customer know their user ID?     |"
    choice = raw_input("|Y/N : ")
    print "|------------------------------------------|"
    if choice == "N":
            number = raw_input("|What is their Telephone number? : ")
            #This gets the row that has the telephone number that was input in the line above.
            cur.execute("SELECT * FROM customers WHERE Telephone = (?)", (number,))
            row = cur.fetchone()
            print "|Customer ID : " , row[0]
            print "|Forename : " , row[1]
            print "|Surname : " , row[2]
            print "|Address Line 1 : " , row[3]
            print "|Address Line 2 : " , row[4]
            print "|City : " , row[5]
            print "|Postcode : " , row[6]
            print "|Telephone number : " , row[7]
            print "|E-Mail : " , row[8]
            print "|------------------------------------------|"
            print "|What field would you like to change?      |"
            print "|1 - Telephone                             |"
            print "|2 - Email                                 |"
            print "|3 - Address                               |"
            print "|------------------------------------------|"
            choice = raw_input("|Please put choice here : ")
            if choice == "1":
                print "|------------------------------------------|"
                print "|Current telephone number :", row[7]
                print "|------------------------------------------|"
                while True:
                    phonechange = raw_input("|Change telephone number to : ")
                    #This is a length check, as phone numbers in the UK Without the +44 Region code, are
                    #only 11 Characters.
                    if len(phonechange) > 11:
                        print "|------------------------------------------|"
                        print "|Your input was over 11 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(phonechange) < 11:
                        print "|------------------------------------------|"
                        print "|Your input was under 11 Letters try again |"
                        print "|------------------------------------------|"
                    else:
                        break
                print "|------------------------------------------|"
                #This updates the telephone number, where the inital entered telephone number was in the row.
                cur.execute("UPDATE customers SET Telephone=? WHERE Telephone = (?)", (phonechange,number,))
                conn.commit()
            elif choice == "2":
                print "|------------------------------------------|"
                print "|Current Email :", row[8]
                print "|------------------------------------------|"
                while True:
                    emailchange = raw_input("|E-Mail: ")
                    #Presence check.
                    if emailchange != None:
                        break
                    else:
                        print "|------------------------------------------|"
                        print "|You didnt put anything in! Try again      |"
                        print "|------------------------------------------|"
                print "|------------------------------------------|"
                cur.execute("UPDATE customers SET email = (?) WHERE Telephone = (?)", (emailchange,number,))
                conn.commit()
            elif choice == "3":
                os.system('cls')
                print "|------------------------------------------|"
                print "|Current Address Line 1 : " , row[3]
                print "|Current Address Line 2 : " , row[4]
                print "|Current City : " , row[5]
                print "|Current Postcode : " , row[6]
                print "|------------------------------------------|"
                while True:
                    ad1change = raw_input("|Change Address Line 1 to : ")
                    #An check of 5 to 30 characters, because i believe that a address cant be longer than 30 characters
                    #Nor under 5 characters
                    if len(ad1change) > 30:
                        print "|------------------------------------------|"
                        print "|Your input was over 30 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(ad1change) < 5:
                        print "|------------------------------------------|"
                        print "|Your input was under 5 Letters try again  |"
                        print "|------------------------------------------|"
                    else:
                        break
                while True:
                    ad2change = raw_input("|Change Address Line 2 to : ")
                    #The same with this, but some people do not have a second address line so i allowed for a blank input
                    if len(ad2change) > 30:
                        print "|------------------------------------------|"
                        print "|Your input was over 30 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(ad2change) > 1 and len(newdetails[3]) < 5:
                        print "|------------------------------------------|"
                        print "|Your input was under 5 Letters try again  |"
                        print "|------------------------------------------|"
                    else:
                        break
                while True:
                    citychange = raw_input("|Change City to : ")
                    #Another presence check, as a city name can be very long.
                    if citychange != None:
                        break
                    else:
                        print "|------------------------------------------|"
                        print "|You didnt put anything in! Try again      |"
                        print "|------------------------------------------|"
                while True:
                    postcodechange = raw_input("|Change Postcode to : ")
                    if len(postcodechange) < 8:
                        print "|------------------------------------------|"
                        print "|Your input was not 8 letters              |"
                        print "|Postcodes in the UK Are only 8 Letters!   |"
                        print "|Try again!                                |"
                        print "|------------------------------------------|"
                    elif len(postcodechange) > 8:
                        print "|------------------------------------------|"
                        print "|Your input was not 8 letters              |"
                        print "|Postcodes in the UK Are only 8 Letters!   |"
                        print "|Try again!                                |"
                        print "|------------------------------------------|"
                    else:
                        break
                print "|------------------------------------------|"
                conn = sqlite3.connect('SADS.db')
                cur = conn.cursor()
                #This updates all the inputs where the first nubmer was input
                cur.execute("UPDATE customers SET Address1=? WHERE Telephone = (?)", (ad1change,number,))
                cur.execute("UPDATE customers SET Address2=? WHERE Telephone = (?)", (ad2change,number,))
                cur.execute("UPDATE customers SET City=? WHERE Telephone = (?)", (citychange,number,))
                cur.execute("UPDATE customers SET Postcode=? WHERE Telephone = (?)", (postcodechange,number,))
                conn.commit()
    elif choice == "Y":
        #this is all the same as above, just the custid is the WHERE Command instead.
            custid = raw_input("What is their ID? : ")
            cur.execute("SELECT * FROM customers WHERE CustID = (?)", (custid,))
            row = cur.fetchone()
            print "|Customer ID : " , row[0]
            print "|Forename : " , row[1]
            print "|Surname : " , row[2]
            print "|Address Line 1 : " , row[3]
            print "|Address Line 2 : " , row[4]
            print "|City : " , row[5]
            print "|Postcode : " , row[6]
            print "|Telephone number : " , row[7]
            print "|E-Mail : " , row[8]
            print "|------------------------------------------|"
            print "|What field would you like to change?      |"
            print "|1 - Telephone                             |"
            print "|2 - Email                                 |"
            print "|3 - Address                               |"
            print "|------------------------------------------|"
            choice = raw_input("Please put choice here : ")
            if choice == "1":
                print "|------------------------------------------|"
                print "|Current telephone number :", row[7]
                print "|------------------------------------------|"
                while True:
                    phonechange = raw_input("|Change telephone number to : ")
                    if len(phonechange) > 11:
                        print "|------------------------------------------|"
                        print "|Your input was over 11 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(phonechange) < 11:
                        print "|------------------------------------------|"
                        print "|Your input was under 11 Letters try again |"
                        print "|------------------------------------------|"
                    else:
                        break
                print "|------------------------------------------|"
                cur.execute("UPDATE customers SET Telephone=? WHERE CustID = (?)", (phonechange,custid,))
                conn.commit()
            elif choice == "2":
                print "|------------------------------------------|"
                print "|Current Email :", row[8]
                print "|------------------------------------------|"
                while True:
                    emailchange = raw_input("|E-Mail: ")
                    if emailchange != None:
                        break
                    else:
                        print "|------------------------------------------|"
                        print "|You didnt put anything in! Try again      |"
                        print "|------------------------------------------|"
                print "|------------------------------------------|"
                cur.execute("UPDATE customers SET email = (?) WHERE CustID = (?)", (emailchange,custid,))
                conn.commit()
            elif choice == "3":
                os.system('cls')
                print "|------------------------------------------|"
                print "|Current Address Line 1 : " , row[3]
                print "|Current Address Line 2 : " , row[4]
                print "|Current City : " , row[5]
                print "|Current Postcode : " , row[6]
                print "|------------------------------------------|"
                while True:
                    ad1change = raw_input("|Change Address Line 1 to : ")
                    if len(ad1change) > 30:
                        print "|------------------------------------------|"
                        print "|Your input was over 30 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(ad1change) < 5:
                        print "|------------------------------------------|"
                        print "|Your input was under 5 Letters try again  |"
                        print "|------------------------------------------|"
                    else:
                        break
                while True:
                    ad2change = raw_input("|Change Address Line 2 to : ")
                    if len(ad2change) > 30:
                        print "|------------------------------------------|"
                        print "|Your input was over 30 Letters try again  |"
                        print "|------------------------------------------|"
                    elif len(ad2change) > 1 and len(newdetails[3]) < 5:
                        print "|------------------------------------------|"
                        print "|Your input was under 5 Letters try again  |"
                        print "|------------------------------------------|"
                    else:
                        break
                while True:
                    citychange = raw_input("|Change City to : ")
                    if citychange != None:
                        break
                    else:
                        print "|------------------------------------------|"
                        print "|You didnt put anything in! Try again      |"
                        print "|------------------------------------------|"
                while True:
                    postcodechange = raw_input("|Change Postcode to : ")
                    if len(postcodechange) < 8:
                        print "|------------------------------------------|"
                        print "|Your input was not 8 letters              |"
                        print "|Postcodes in the UK Are only 8 Letters!   |"
                        print "|Try again!                                |"
                        print "|------------------------------------------|"
                    elif len(postcodechange) > 8:
                        print "|------------------------------------------|"
                        print "|Your input was not 8 letters              |"
                        print "|Postcodes in the UK Are only 8 Letters!   |"
                        print "|Try again!                                |"
                        print "|------------------------------------------|"
                    else:
                        break
                print "|------------------------------------------|"
                conn = sqlite3.connect('SADS.db')
                cur = conn.cursor()
                cur.execute("UPDATE customers SET Address1=? WHERE CustID = (?)", (ad1change,custid,))
                cur.execute("UPDATE customers SET Address2=? WHERE CustID = (?)", (ad2change,custid,))
                cur.execute("UPDATE customers SET City=? WHERE CustID = (?)", (citychange,custid,))
                cur.execute("UPDATE customers SET Postcode=? WHERE CustID = (?)", (postcodechange,custid,))
                conn.commit()
    print "|------------------------------------------|"
    print "|Edited! Please press enter to return to   |"
    print "|The main menu                             |"
    print "|------------------------------------------|"  
    raw_input("")
    os.system('cls')
                               
def viewdetails():
    os.system('cls')
    print "|__________________________________________|"
    print "|----------------View Details--------------|"
    print "|------------------------------------------|"
    print "|1 - Search with Customer ID               |"
    print "|2 - Search with Telephone number          |"
    print "|------------------------------------------|"
    choice = raw_input("|Choice: ")
    if choice == "1":
        while True:
            IDSearch = raw_input("|What is their ID? : ")
            conn = sqlite3.connect('SADS.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM customers WHERE CustID = (?)",(IDSearch,))
            if IDSearch:
                row = cur.fetchone()
                CustID = row[0]
                print "|------------------------------------------|"
                print "|Customer ID : " , row[0]
                print "|Forename : " , row[1]
                print "|Surname : " , row[2]
                print "|Address Line 1 : " , row[3]
                print "|Address Line 2 : " , row[4]
                print "|City : " , row[5]
                print "|Postcode : " , row[6]
                print "|Telephone number : " , row[7]
                print "|E-Mail : " , row[8]
                print '|Do you want to see what seats', row[1] , "Has booked?"
                choice = raw_input("|Choice Y/N : ")
                if choice == 'Y':
                    cur.execute("SELECT * FROM seats WHERE CustID = (?)", (CustID,))
                    rowseat = cur.fetchone()
                    if rowseat:
                        print "|Seats booked:" , rowseat[0]
                        break
                    else:
                        #instead of showing an error message and crashing the progam. This prevents that
                        #And says what the error is.
                        print "|------------------------------------------|"
                        print row[1] , "Has not booked any seats"
                        break
                elif choice == 'N':
                    break
                else:
                    print "|------------------------------------------|"
                    print "|You didnt put Y or N in!                  |"
                    print "|------------------------------------------|"
            else:
                print "|------------------------------------------|"
                print "|That USER ID is not in the table!         |"
                print "|------------------------------------------|"
    elif choice == "2":
        while True:
            PhoneSearch = raw_input("|What is their telephone number? : ")
            conn = sqlite3.connect('SADS.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM customers WHERE Telephone = (?)",(PhoneSearch,))
            if PhoneSearch:
                row = cur.fetchone()
                CustID = row[0]
                print "|------------------------------------------|"
                print "|Customer ID : " , row[0]
                print "|Forename : " , row[1]
                print "|Surname : " , row[2]
                print "|Address Line 1 : " , row[3]
                print "|Address Line 2 : " , row[4]
                print "|City : " , row[5]
                print "|Postcode : " , row[6]
                print "|Telephone number : " , row[7]
                print "|E-Mail : " , row[8]
                print '|Do you want to see what seats', row[1] , "Has booked?"
                choice = raw_input("|Choice Y/N : ")
                if choice == 'Y':
                    cur.execute("SELECT * FROM seats WHERE CustID = (?)", (CustID,))
                    rowseat = cur.fetchone()
                    if rowseat:
                        print "|Seats booked:" , rowseat[0]
                        break
                    else:
                        print "|------------------------------------------|"
                        print row[1] , "Has not booked any seats"
                        break
                elif choice == 'N':
                    break
                else:
                    print "|------------------------------------------|"
                    print "|You didnt put Y or N in!                  |"
                    print "|------------------------------------------|"
            else:
                print "|------------------------------------------|"
                print "|That telephone number is not in the table!|"
                print "|------------------------------------------|"
        print "|------------------------------------------|"
        print("|Please select an option:                  |")
        print("|1 - Return to menu                        |")
        print("|2 - Book seats                            |")
        print("|3 - Edit details                          |")
        choice = raw_input("|Please put choice here : ")
        print "|------------------------------------------|"
    if choice == "1":
        mainprogram()
    elif choice == "2":
        availablity()
    elif choice == "3":
        editdetails()
    os.system('cls')



def bookseat():
    while True:
        print "____________________________________________"
        print "|--------------Booking Seats---------------|"
        print "|------------------------------------------|"
        os.system('cls')
        print "|------------------------------------------|"  
        print "|1 - Look at available seats               |"
        print "|2 - Book seats                            |"
        print "|------------------------------------------|"  
        choice = raw_input("|Choice : ")
        if choice == "1":
            availablity()
        elif choice == "2":
            conn = sqlite3.connect('SADS.db')
            cur = conn.cursor()
            print "|------------------------------------------|"
            print "|What day would you like to book on?       |"
            print "|Type F for Friday and S for Saturday      |"  
            choice = raw_input("|Day: ")
            print "|------------------------------------------|"
            if choice == "F" or "f":
                bookseats = [0,1]
                print "|------------------------------------------|"
                bookseats[0] = raw_input("|Choice (Capital Letters are needed!) : ")
                bookseats[1] = raw_input("|What is their user ID? : ")
                cur.execute("SELECT * FROM seats WHERE Booked='N'")
                row = cur.fetchone()
                if row != None and row[2] == "F":
                    booked = 'B'
                    cur.execute("UPDATE seats SET CustID=?, Booked=? WHERE Seat_name=? AND Day='F'", (bookseats[1],booked,bookseats[0],))
                    conn.commit()
                    print "|------------------------------------------|"
                    print "|Seat Number:" , bookseats[0]  ,"Is now booked!          |"
                    print "|------------------------------------------|"
                    cur.execute("SELECT * FROM seats WHERE Booked='B' AND CustID= ? AND Day='F'", (bookseats[1],))
                    rows = cur.fetchall()
                    for row in rows:
                        if row[4] == bookseats[1] and row[2] == 'F':
                            total = row[1] + row[1]
                            print("|Cost of booking: "),  u"\xA3", int(row[1]) , "        |"
                            break
            elif choice == "S" or "s":
                bookseats = [0,1]
                print"What seats would you like to book?"
                bookseats[0] = raw_input("|Choice (Capital Letters are needed!) : ")
                bookseats[1] = raw_input("|What is their user ID? : ")
                cur.execute("SELECT * FROM seats WHERE Booked='N'")
                row = cur.fetchone()
                if row[2] == "S":
                    booked = 'B'
                    cur.execute("UPDATE seats SET CustID=?, Booked=? WHERE Seat_name=? AND Day='S'", (bookseats[1],booked,bookseats[0],))
                    conn.commit()
                    print "|------------------------------------------|"
                    print "|Seat Number:" , bookseats[0]  ,"Is now booked!          |"
                    print "|------------------------------------------|"
                    cur.execute("SELECT * FROM seats WHERE Booked='B' AND CustID= ? AND Day='S'", (bookseats[1],choice))
                    rows = cur.fetchall()
                    for row in rows:
                        if row[4] == bookseats[1] and row[2] == 'S':
                            total = row[1] + row[1]
                            print("|Cost of booking: "),  u"\xA3", int(row[1]) , "        |"
                            break
        else:
            print "|------------------------------------------|"
            print "| You didnt put 1 or 2, Try again!         |"
            print "|------------------------------------------|"        
    print "|------------------------------------------|"
    print "|------------------------------------------|"
    print "|1 - Return to booking menu                |"
    print "|2 - Return to main menu                   |"
    print "|------------------------------------------|"
    print "| In the choice box below, please put the  |"
    print "| number of the page you want to visit     |"
    print "|------------------------------------------|"
    choice = raw_input("|Choice : ")
    if choice == "1":
        bookseat()
    elif choice == "2":
        mainprogram()
    os.system('cls')
    
def income():
    os.system('cls')
    print "____________________________________________"
    print "|------------------INCOME------------------|"
    print "|------------------------------------------|"
    conn = sqlite3.connect('SADS.db')
    cur = conn.cursor()
    Fri_Total = 0
    Sat_Total = 0
    cur.execute("SELECT * FROM seats")
    rows = cur.fetchall()
    for row in rows:
        if row[3] == 'B' and row[2] == 'F':
            Fri_Total = Fri_Total + row[1]
        elif row[3] == 'B' and row[2] == 'S':
            Sat_Total = Sat_Total + row[1]
    print "|Friday Total : " , u"\xA3", float(Fri_Total)
    print "|Saturday Total : " , u"\xA3", float(Sat_Total)
    Final_Total = Fri_Total + Sat_Total
    print "|Total Income : " , u"\xA3", float(Final_Total)
    print("|Press enter to return to menu             |")
    print "|------------------------------------------|"    
    raw_input("")
    os.system('cls')
    
def wrongnumber():
    os.system('cls')
    print "|------------------------------------------|"     
    print "| You didnt put an option between 1 and 7! |"
    print "| Please press enter to return to the menu |"
    print "|------------------------------------------|"
    raw_input("")
    os.system('cls')

def mainprogram():
    os.system('cls')
    while True:
        menu()
        if choice == "1":
            newdetails()    
        elif choice == "2":
            editdetails()
        elif choice == "3":
            viewdetails()       
        elif choice == "4":
            availablity()     
        elif choice == "5":
            bookseat()       
        elif choice == "6":
            income()
        elif choice == "7":
            os.system('cls')
            print "|------------------------------------------|"  
            print "|-----------------GOODBYE------------------|"
            print "|------------------------------------------|"  
            sleep(4)
            break
        else:
            wrongnumber()

mainprogram()
