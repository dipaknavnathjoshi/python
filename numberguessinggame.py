import random

number=random.randint(1,100)
attempts=0
print("Wellcome to the Number Guessing Game!")
while True:
    GuessingNumber=input("Guess the Number : ")
    if  not GuessingNumber.isdigit():
        print("Please enter a number")
        attempts+=1
        continue
    GuessingNumber=int(GuessingNumber)
    if GuessingNumber==number:
        print("You guessing the right number. Number is: ",number)
        attempts+=1
        print("your attempts is : ",attempts)

        break
    elif GuessingNumber>number:
        print("you guessing number is to high")
        attempts+=1
    elif GuessingNumber<number:
        print("you guessing number is to low")
        attempts+=1
    