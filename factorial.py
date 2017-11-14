#factorial.py
# calculates the factorial of a given number


var = 1 
while var == 1 :
    print("This program will calculate the factorial of a given number.")

    x = input("Enter a number: ")
    fact = 1

    for i in range(x):
        fact = fact * (i + 1)

    print(str(x) + "! = " + str(fact))





