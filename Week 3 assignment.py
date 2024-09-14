# DSC 510
# Week 3
# Programming Assignment Week 2
# Author Michael Perrine
# 9/12/2024


print ("Welcome to Cables Unlimited.\n ")

Company = input("What is the name of your company?\n ")

print("Hello, "+Company+", Welcome to Cables Unlimited.\n ")

Cable = int(input("How many feet of fiber optic cable do you need?\n "))

if Cable > 100:
    print(Cable * float(.80))

elif Cable > 250:
    print(Cable * float(.70))
    
elif Cable > 500:
    print(Cable * float(.50))

else :
    print(Cable * float(.87))

print ("Thank you,"+Company+", We'll get you order out now.\n")
