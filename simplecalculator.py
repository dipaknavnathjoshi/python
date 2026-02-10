print("simple calculator")
 
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
print("choose operation")
print("1. addition (+)")
print("2. substraction (-)")
print("3. multiplication (*)")
print("4. division (/)")
print("5. modulus (%)")
print("6. square (**)")
     
def cal(operation):   
    if operation=="1":
        print(f"addition : {num1}+{num2} : ",num1+num2)
    elif operation=="2":
        print(f"substraction : {num1}-{num2} : ",num1-num2)
    elif operation=="3":
        print(f"multiplication : {num1}*{num2} : ",num1*num2)
    elif operation=="4":
        print(f"division : {num1}/{num2} : ",num1/num2)
    elif operation=="5":
        print(f"substraction : {num1}%{num2} : ",num1%num2)
    elif operation=="6":
        if num1==num2:
            print(f"square : {num1}**{num2} : ",num1**num2)
        else:
            print("given number are not same :: enter same number")
    else:
        print("Invalid Input")
    
cal(operation=input("choose operations : (1/2/3/4/5/6) : "))
 
    