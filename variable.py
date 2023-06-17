# multiple variable
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# global variable

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()