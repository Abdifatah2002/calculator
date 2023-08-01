"""FILE HEADER
//
// Title:  simple calculator
//
//
// Author:   Abdifatah Abdi
// Email:    aaabdi2@wisc.edu
//

"""


#simple calculator
## making div, mutiple, adding, and subs
## is a comment for the what the code does

import math

print("Select an  operation to perform: ")
print ("1. ADD") ##  print is out "1. ADD  is for the ADD
print ("2. Substarct") #print is out "2. Substracts is for SUB
print ("3. multiply") #print is out"3. mutplit is for Mutlpy
print ("4. Divide") # print is out "4. divide". Divide for the

operation = input()

if operation == "1":# code for Add
    num1  = input("Enter the first number:") ## the user enters the first nummber
    num2 = input("Enter the second number:") ## the user enters the second number
    print("The sum is :" + str(int(num1) + int(num2) )) ## then we gonna print it out the num1 + num2

elif operation == "2":#3 code for the SUB
    num1 = input("Enter the first number:")  ## the user enters the first nummber
    num2 = input("Enter the second number:")  ## the user enters the second number
    print("The difference: " + str(int(num1) - int(num2)))


elif operation == "3": ## code for the mutiply
    num1 = input("Enter the first number:")  ## the user enters the first nummber
    num2 = input("Enter the second number:")  ## the user enters the second number
    print("The product is : " + str(int(num1 ) * int(num2)))


elif operation == "4": #code for the div
    num1 = input("Enter the first number:")  ## the user enters the first nummber
    num2 = input("Enter the second number:")  ## the user enters the second number
    print("The quotient: " + str(int(num1) / int(num2)))

else: ## if the user put something else it will print out Invalid Enetry
    print("Invalid Enetry")
