# i = 1

# while i < 10 :
#     print(i)
#     # i += 1
#     i = i + 1

# print("Program end")

# n = int(input("Enter the value :"))
# sum = 0
# while i <= n:
#     sum = sum + i
#     i = i + 1

# print(sum)


# break continue

# i = 1
# while i <= 100:
#     if i == 20:
#         break
#     print(i)
#     i = i + 1
# print("The end")

i = 1

while i <= 100:

    if i == 20:
        continue
    print(i)
    i = i + 1  
     

print("Hello")

# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# ------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)