a = "Hello"

print(a)

# ----------------------
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# ----------------------

a = "Hello, World!"
print(a[1])

# ----------------------


for x in "banana":
  print(x)


# ----------------------
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# ----------------------
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
