print("~~~~~~~~~~~~MINI CALCULATOR~~~~~~~~~~~~~")


num1=float(input("enter the first number here: "))
num2=float(input("enter the second number here: "))

print("press1 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

choice=int(input("enter your choice from 1-4: "))

if choice==1:
   print("the addition of given two number is",num1+num2)
elif choice==2:
    print("the substraction of given two number is",num1-num2)
elif choice==3:
    print("the multiplication of given two number is",num1*num2)
elif choice==4:
    print("the division of given two number is",num1/num2)
else:
   print("invalid input")
