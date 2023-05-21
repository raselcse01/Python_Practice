# stack first in last out (lifo)

# books = []
# books.append("c")  
# books.append("d")
# books.append("e")
# books.append("f")
# books.append("g")
# books.append("h")

# books.pop()
# print(books[2])

# books.pop()
# if not books:
#     print("No books")

# print(books)


# Queue fast in fast out
from collections import deque

bank = ['a','b','c']  
bank.popleft()
print(bank)

if not bank:
    print("No person left")

