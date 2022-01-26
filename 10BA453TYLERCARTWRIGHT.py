import sys
import math #allows the code to use special commands like the math .ceil
import csv #allows the code to open csv files for the shop

#TASK 1`

def gtin8(): #created function for if repeat is needed
    while True: #needed to let the base exception know when to interrupt the code
        try:#allows use of except

            code1 = input("Enter a 7 digit number: ")#allows user to enter a 7 digit number
            while len(code1) != 7:#checks if the number entered is 7 digits long
                print("This is not a valid option try again!")#displayed to the user as a string
                code1 = input("Enter a 7 digit number: ")#allows user to enter a 7 digit number
            codelist = []#creates a list to use in creating a gtin
            for i in code1:#each digit is entered into the list separately
                codelist.append(i)#creates a different section of the list for every entered digit

            code1y = int(codelist[0])*3 + int(codelist[1])*1 + int(codelist[2])*3 + int(codelist[3])*1 + int(codelist[4])*3 +int(codelist[5])*1  + int(codelist[6])*3#multiplies the appropriate digit and then adds the answers together
            roundup = int(math.ceil(code1y/10)) * 10 #find the nearest multiple of ten to code 1

            checkdig = (roundup-code1y) #finds check digit

            print ("This number,",checkdig,", is your check digit.")#prints what your check digit is
            print ("Your full GTIN-8 code is" ,(str(code1))+(str(checkdig)))#prints what your gtin is
            menu()#takes you back to menu]
            break #disrupts the code
        except BaseException:#gives the code something new to carry out after the disruption
            print("Error! Try Again!!!")#displayed as a string
   

def check(): #creates another function for if repeating is needed
    while True:#need to let the base exeception know when to interrupt the code
        try:#allows use of except
            
            code2 = input("Enter an 8 digit number: ")#allows user to enter a 8 digit number
            while len(code2) != 8:#checks if the number entered is 7 digits long
                print("Error! Try Again!!!")#displayed to the user as a string
                code2 = input("Enter an 8 digit number: ")#allows user to enter a 7 digit number
            codelist2 = []#creates a list to use in checking a gtin
            for i in code2: #puts each digit in the list by its self
                codelist2.append(i)#creates a different section of the list for every entered digit
            checksum = int(codelist2[0]*3) + int(codelist2[1]*1) + int(codelist2[2]*3) + int(codelist2[3]*1) + int(codelist2[4]*3) + int(codelist2[5]*1) + int(codelist2[6]*3) + int(codelist2[7]*1)#multiplies by the appropriate digit and then adds the answers together
            if checksum % 10 == 0: #finds if there is a remainder in dividing checksum by 10
                print ("this is a valid code") #if checksum is a multiple of 10 it is valid
            else:#for if the code isnt valid
                print ("This is not a valid GTIN-8 code") #if it isnt then it is invalid
            menu()#takes you back to menu
            break #disrupts the code
        except BaseException:#gives the code something new to carry out after the disruption
            print("Error! Try Again!!!")#displayed as a string
        

def readfile(f):#this subroutine opens the file
    csvFile = csv.reader(f)#"
    tempArray = []#"
    for row in csvFile:#"
        tempArray.append(row)#"
        print("Product: ", row[1])
        print("Barcode: ",row[0])
        print("Price: ",row[2])
        print("PLEASE NOTE --- Stock Level: ",row[3])
        print(" ")
        f.close#"
    return tempArray#


#TASK 2

def products():#creates another function for if repeating is needed

    print("  *  *  *  *  *  Shop Items  *  *  *  *  *  ")#this is used to make the shop look pretty
    print(" ")#aesthetics
    itemsdata = readfile(open("Items.csv"))#this finds the excel file and carries out readfile

    shoppinglist = [] #creates empty shopping list
    carryon = True #this helps the menu loop to start
    totalc = 0 #this makes it so that the total bill is nothing at the start
    pnf = ("Product Not Found") #this is useful for when you enter an incorrect barcode

    while carryon is True: #this makes it so if you say yes to carry on at the end of the code, it will start again here
        itemfound = False #says that an item hasnt been found yet
        searchItem = input("enter a gtin 8 number: ")#tells user to enter an 8 digit barcode
        while len(searchItem) != 8 and not searchItem.isdigit():#makes sure the user is only allowed to enter numbers that are 8 digit
                print("This is not a valid option try again!")#if it is invalid then this ius told to the user
                searchItem = input("Enter a gtin 8 number: ")#gets user to input a new number
        for items in itemsdata: #reads the itemsdata list (csv file)
            if items[0] == searchItem:#checks to see if the searched barcode matches up in the file
                itemfound = True#if so, an item is now found
                quan = input("How many do you want: ")#asks user how many of the item they want
                if quan.isalpha():
                    while quan.isalpha() or len(quan) == 0:#checks if the input has letters or is null
                        print("Please enfer a number which is valid!")#displayed to user
                        print("Stock Level: ",items[3])#tells user the stock level
                        quan = input("How many do you want: ")#asks again
                elif quan.isdigit():
                    while int(quan) > int(items[3]):
                        print("We may not have that many in stock, or your input is invalid!")#displayed to user
                        print("Stock Level: ",items[3])#tells user the stock level
                        quan = input("How many do you want: ")#asks again
                totcost = int(quan)*int(items[2])#multiplies price and quantity to get total cost
                items[3] = int(items[3]) - int(quan)#finds the new shop quantity
                shoppinglist.append([searchItem,items[1],quan,totcost])#adds new data to the shopping list
                totalc = totalc + totcost#finds total cost of all the items bought (if multiple)
                updateCSV(itemsdata)
        if itemfound == False:#if the item isnt found then this part of the code takes place
            shoppinglist.append([searchItem,pnf,"",""])#adds blank data to the shopping list
        valid = False
        while valid == False:
            carry = input("do you want to enter another code: ")#asks if the user wants to buy new items
            if carry.lower() == "yes":#if yes the code restarts
                carryon = True#carries on loop
                valid = True
            elif carry == "no" or carry == "No":#if no the code exits too menu
                carryon = False#ends loop
                valid = True
            else:
                print("This is not a valid input!")
    for item in shoppinglist:#for each items in the shopping list, the information about it is displayed
        print("Barcode: ", item[0]," product:",item[1]," quantity:",item[2],"price: £",item[3])#the shopping list displayed
    print("Total cost of order:   £",totalc)#total cost displayed

    
    menu()#takes you to the menu
    

#TASK 3        

def updateCSV(tempdata):#starts the new function and brings over the itemsdata
    ofile  = open('items.csv', 'w', newline='')#opens the csv file
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)#sets up the writing to file process

    for item in tempdata:#for each item in the file
        writer.writerow(item)#writes the new quantity to be updated into the csv
    
    ofile.close()#closes file


def StockCSV():#starts new function

    itemsdata = readfile(open('items.csv'))#opens csv file

    reorderinfo = open("reorderinfo.txt","w")
    
    choice3 = input("Do you want to check the stocks? ")#string displayed to ask user
    while len(choice3) !=3 and not choice3.isalpha:
        print("This is not a valid option try again!")
        choice3 = input("Do you want to check the stocks? ")#string displayed to ask user
    if choice3.lower() == "yes":#if th answer is yes then...
        for items in itemsdata:#do this for each item
            if int(items[3]) <= int(items[4]):#if current stock level is lower than reorder level
                reorder = (int(items[5])-(int(items[3])))
                print("WE NEED",reorder," MORE OF THIS ITEM: ",items[0]," ",items[1])#displayed as string
                reorderinfo.write("WE NEED " + str(reorder) + " MORE OF THIS ITEM: "+items[0]+" "+items[1]+"\n")
            else:#if not lower
                print("WE ARE ALL STOCKED UP FOR: ",items[0]," ",items[1])#displyed as string
    elif choice3.lower() == "no":#if the answer is no then...
        print("RETURNING TO MENU... ")#displayed as string and then returns to menu
    else:#if neither...
        print("INVALID OPTION, TRY AGAIN")#displyed as string
        StockCSV()#restarts this part of the code

    reorderinfo.close()
    menu()#goes to menu


def restock():#new function

    itemsdata = readfile(open('items.csv'))#opens csv file

    choice4 = input("Do you want to restock all of the items: ")#question for reader
    if choice4.lower() == "yes":#sees if the user wants to update the csv
        for items in itemsdata:#for each item in file
            if int(items[3]) <= int(items[4]):#if current stock level is less thsn or equal to re order level
                difference = int(items[5])-int(items[3])#difference that needs to be ordered
                items[3] = int(items[3]) + int(difference)
                updateCSV(itemsdata)
                print(" ")
                print("ITEMS RESTOCKED")
    elif choice4.lower() == "no":
        print(" ")
        print("RETURNING TO MENU...")
    else:
        print(" ")
        print("This input is invalid, TRY AGAIN!!!")
        restock()

    menu()
    
   
def menu():#created function for if repeat is needed
    while True:
            print ("                             ")#aesthetics
            print ("* * * * * Main Menu * * * * *")#aesthetics
            print ("                             ")#aesthetics
            print ("What do you want to do: ")#asks user what they want to do
            print (" ")
            print ("1 = Create a GTIN number")#informs user what this choice 1 does
            print ("2 = Checks if your random 8 digit number is valid")#informs user what this choice 2 does
            print ("3 = Open shop")#informs user what this choice 3 does
            print ("4 = Check Stock Level")
            print ("5 = Re Order Stock")
            print ("6 = Quit the program")#informs user what this choice 4 does
            print ("                             ")#aesthetics
            choice = input("Enter your choice: ")#asks user to enter their destination
            while len(choice) != 1 and choice.isalpha:
                print("This is not a real destination")
                choice = input("Enter your choice: ")#asks user to enter their destination
            if choice == "1":#if entered num is 1
                print ("Create a GTIN number: ")#displayed as a string
                gtin8()#takes you corresponding function
            elif choice == "2":#if entered num is 2
                print ("Checking if an 8 digit number is correct: ")#displayed as a string
                check()#takes you corresponding function
            elif choice == "3":#if entered num is 3
                print ("Opening the shop: ")#displayed as a string
                products()#takes you corresponding function
            elif choice == "4":#if entered num is 4
                print ("Opening menu to sort the stock: ")#displayed as a string
                StockCSV()#takes you corresponding function
            elif choice == "5":#if entered num is 4
                print ("Opening menu to re order the stock: ")#displayed as a string
                restock()#takes you corresponding function
            elif choice == "6":#if entered num is 5
                quit()#closes the program
            else:
                menu()


menu()






    





