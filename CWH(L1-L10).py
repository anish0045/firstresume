print("Hello World",end=" ")
print("Hello World2")

print("my,\nname\tis\"anish\abakshi\r")

var1="hello python"
var2="4"
var3="36.7"
print(type(var2))
print(var1+var2)

print(10*"Hello World\n")

mystr="I love python"
print(mystr[2:6])
print(len(mystr))
print(mystr[0:13])  #prints(I love Python)
print(mystr[0:66])  #prints(I love Python)
print(mystr[:13])
print(mystr[13:])
print(mystr[0:13:2])
print(mystr[::])
print(mystr[::222]) #extended slicing
print(mystr[::-1])
print(mystr[::-2])

a="Anish is a good boy"
print(a.isalnum())   #error code
a="Anishisagoodboy"
print(a.isalnum())  
a="Anishisagoodboy"
print(a.isalpha())  #isalpha is true when spaces are not present
a="Anish is a good boy"
print(a.endswith("boy"))
print(a.count("i"))
print(a.lower())
print(a.replace("is","was"))
print(a.replace("good","bad"))
a="anishisagoodboy"
print(a.capitalize()) #capitalizes the first letter
print(a.find("is"))
print(a.upper())

v=[2, 14, 26, 37, 45]
print(v.pop())  #adds at end
print(v.insert(1,29))

a=1
b=8
a, b=b, a
print(a, b)


