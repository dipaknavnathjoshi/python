# String functions
name="dipak"  #strings are immutable 
print(name.upper())
print(name.lower())
a="!!john!!!!!!!!!!"
print(a)
print(a.rstrip("!")) #remove specific character
n="sakshi ravin ram"
print(n.replace("sakshi","radha"))
print(n.split(" ")) #converting into list
s="wellcome my code journEy"
print(s)
print(s.capitalize()) #first latter convert into capital and fix human error
tr1="wellcome to travelling"
print(tr1,len(tr1))
print(tr1.center(50))
print(tr1.count("e")) #counting latter
st="wellcome!!"
print(st.endswith("!"))

t="hello im dipak and im very honest man"
print(t.index("e")) 
print(t.find("e")) 

str="wellcometotheconsole"
print(str.isalnum())

str="Wellcomemyfeeds"
print(str.isalpha())
str="wellcomemyfeeds\n"
print(str.islower())
print(str.upper())
t="   "
print(t.isspace())
h="Wellcome my journey, i really proud of me bequase nobady compares my strengths and will power"
print(h.swapcase()) 
print(h.lower()) 
print(h.startswith("wellcome"))
print(h)
h="Wellcome My Journey, I Really Proud Of Me Bequase Nobady Compares My Strengths And Will Power"
print(h.istitle())

num1=int(input("enter number first: "))
num2=int(input("enter number second: "))
print(num1+num2)
