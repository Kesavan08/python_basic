#creating variables
a=5
b="hello"
print(a)
print(b)

#Casting an Variable
x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

#get the type
a=5
b=10
print(type(x))
print(type(y))

#Assign multiple variable to many values
a,b,c="a","b","c"
print(a)
print(b)
print(c)

#one value to multiple variables
x=y=z="hello"
print(x)
print(y)
print(z)

#Global variable
a="hi"
def fun():
    print("i will say "+a)
fun()

#Create varible inside a function
a="hi"
def fun():
    a="hello"
    print("i will say "+a)
fun()
print("i will say"+a)

#global keyword
def fun():
    global a
    a="hi"
fun()
print("i will say "+a)


