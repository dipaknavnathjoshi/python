list=[1,2,3,4,5,6,9]
print(list)
print(list[6])
print(type(list))
print(len(list))
print(list[-4:6])
print(list[1:])
if 6 in list:
    print("yes")
else:
    print("no")

# list methods
list=[1,2,7,4,5,3,9,8,5]
list.append(10)
print(list)
list.sort()
print(list.count(5))
list.insert(3,100)
print(list)

l=list.copy()
print(l)
m=[12,234,5,67,8]
print(m)
k=l+m
print(k)
list.extend(m)
print(list)