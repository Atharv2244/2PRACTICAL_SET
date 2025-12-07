#Q2.1
Day=int(input("Enter a number between 1-7 to see which day come:"))

match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("ThurSday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Wornge Choice")

#Q2.2
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

print("1.Add , 2.Subtract , 3.Mlituply , 4.Divishion")
Choice=int(input("Enter your choice"))

match Choice:
    case 1:
        print(num1,"+",num2,"=",num1+num2)
    case 2:
        print(num1,"-",num2,"=",num1-num2)
    case 3:
        print(num1,"/",num2,"=",num1/num2)
    case 4:
        print(num1,"x",num2,"=",num1*num2)
    case _:
        print("Enter right choice")