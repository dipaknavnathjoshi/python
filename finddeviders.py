n = int(input("entern : "))
print([i for i in range(1, n + 1) if n % i == 0])

num=int(input("enter number: "))
print(num)
for i in range(1, num + 1):
    if num % i == 0:
        print(i)