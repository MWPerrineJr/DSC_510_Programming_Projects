#DSC 510
# Week 4
# Programming Assignment
# Author Michael Perrine
# 9/20/2024


print("Welcome to Cables Unlimited.\n ")

company = input("What is the name of your company?\n ")

print("Hello, " + company + ", Welcome to Cables Unlimited.\n ")

cable_feet = int(input("How many feet of fiber optic cable do you need?\n "))

if cable_feet > 500:
    amount_foot = (input(float(.50)))

elif cable_feet > 250:
    amount_foot = (input(float(.70)))

elif cable_feet > 100:
    amount_foot = (input(float(.80)))

else:
    amount_foot = (input(float(.87)))


def material_calculator(cable_feet, amount_foot):

    receipt= cable_feet * amount_foot

    print("${:,}".format(receipt))


material_calculator(250,.8)

print("Thank you," + company + ", We'll get you order out now.\n")
