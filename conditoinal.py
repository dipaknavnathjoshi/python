# a=int(input("enter your age: "))
# print("you age  is:",a)
# if(a>18):
#     print(" you can drive")
# else:
#     print("can`t drive")

b=int(input("enter your age: "))
if b in range (12,18):
    print("you are learner")
elif (b>=18 and b<=50):  
    print("your are rights to drive")
elif b in range(51,70):
    print("you avoids the driving")
elif(b>71 and b<81):
    print("you not allowed to driving")
else:
    print("you are rest in peace")
