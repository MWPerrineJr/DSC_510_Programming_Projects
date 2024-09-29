#DSC 510
# Week 5
# Programming Assignment
# Author Michael Perrine
# 9/28/2024


# this function is used to calculate math operations such as +,-,*,/

def performCalcuation(operator):

# these values are used to perform the necessary actions

    x_num1 = input(int('Please select a number'))

    x_num2 = input(int('Please select a number'))

# the if statements perform the math calculations

    if operator == '+':

        total = x_num1 + x_num2

        print(f"result of {x_num1} + {x_num2} is : total")

    elif operator == '-':

        total = x_num1 - x_num2

        print(f"result of {x_num1} - {x_num2} is : total")

    elif operator == '*':

        total= x_num1 * x_num2

        print(f"result of {x_num1} * {x_num2} is : total")

    elif operator == '/':

        if operator != 0:

           total= x_num1 / x_num2

           print(f"result of {x_num1} / {x_num2} is : total")

        else:
            print('incorrect!!!, unable to divide by zero')

    else:

        print("Incorrect operation please select +,-,*,/")

# this function is used to calculate the average

def calculateAverage():

    try:
        num_range= int(input("Please select starting number"))
        num_range2= int(input("Please select an ending number"))
        total = num_range + num_range2


        count=0

        for i in range(count):
            count= count + 1

            average= count / total

            print(f"The answer is: {average}")

    except ValueError:
        print("Please enter valid numbers")

def main():

    while True:
        print("Choose a valid operation \n")

        print("To add numbers select 1")

        print("To subtract numbers select 2")

        print("To multiply numbers select 3")

        print("To divide numbers select 4")

        print("To average numbers select 5")

        print("To exit select 6")

        action= input("Please select a number from 1-6 \n")

# this if statement denotes the actions to perform in the respective functions

        if action == 1:
            performCalcuation('+')

        elif action == 2:
            performCalcuation('-')

        elif action == 3:
            performCalcuation('*')

        elif action == 4:
            performCalcuation('/')

        elif action == 5:
            calculateAverage()

        elif action == 6:
            print("Thank you and have a nice day")

        else:
            print("Please make a selection between 1-6")

    if _name_ == "_main_":
        main()






































