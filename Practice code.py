#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x, y):
        return x + y

def subtract (x, y):
        return x - y


def multiply(x, y):
        return x * y

# Tried Exceptional handling
def divide (x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Cant do divided by Zero")
    
while True:
    
    print("Select Operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("press Q for exit")

    choice = input("Enter your choice: ")
    if choice == "Q" or choice =="q":
          break

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    if choice == '1':
            print(num1, "+", num2,"=", add(num1,num2))

    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))

    elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

    elif choice == "5":
        Exit()

    else:
            print("Invalid Input")


# In[ ]:




