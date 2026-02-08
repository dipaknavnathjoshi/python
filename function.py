def adds(a,b):
    print(a+b, "\n" , a*b)

adds(2,3)

def inp():
    en=input("enter data: ")
    for i in en:
        print(i)

inp()

def count(nm):
    count=0
    nm=input("enter name: ")
    for i in nm:
        count+=1
        return count
count()
    
vae="sai"
print(len(vae))
print(vae.__reversed__)
for i in vae:
    print(i)

nm="dipak"
print(nm[::-1])
list=list(nm)
print(list)