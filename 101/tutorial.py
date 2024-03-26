# https://docs.python.org/3/tutorial/
# TUTORIAL NOTES

# import sys
# sys.argv[0]
# 
# >>> interactive mode (from a TTY/REPL)
# 
# https://docs.python.org/3/tutorial/introduction.html
# 
# / division vs // floor division (discards fractional part)
# % modulo operator (remainder of division)
# ** power x ** 2 x squared
# + string concat
# strings are immutable
# 
# id() built-in function that returns unique id of an object (integer representing memory address of object)
# 
# = assignment never copies data.
# list1 = [1, 2, 3]
# list2 = list1
# id(list2) == id(list1) >>> True (variable list2 refers to existing list)
# 
# slice operations return a new list containing requested elements
# list3 = list1[:] >>> list3 is a shallow copy
# 
# list1 = [1, 2, 3]
# list2 = list1
# print(id(list2) == id(list1))
# list3 = list1[:]
# print(list3)
# print(id(list3) == id(list1))
# 
# assignment to slices is possible
# 
# letters = ['a', 'b', 'c', 'd']
# letters[1:3] = ['B', 'C']
# print(letters)
# # len() function built-in (strings and lists)
# print(len(letters))
# # clear entire list
# letters[:] = []
# print(letters)
# 
# multi-assignment Fibonnaci example
# a, b = 0, 1
# while a < 50:
#     print(a)
#     a, b = b, a + b
# 
# multi-arg print() example
i = 256 * 256
print('the value of i is', i)
# 
# https://docs.python.org/3/tutorial/controlflow.html
# 
# if..elif..elif..elif..else is a substitute for switch/case statements in other langs
# x = int(input("Enter an integer: "))
# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# elif x == 1:
#     print('one')
# else:
#     print('greater than 1')
# 
# for simply iterates over items of any sequence (lacks control over iteration+halting step such as in C)
# words = ['foo', 'bar', 'foobar']
# for w in words:
#     print(w, len(w))
# 
# beware of modifying a collection while iterating over it. 
# 2 alternate strategies involve iterating over a copy or creating a new collection
# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# 
# iterating over sequence of numbers can be accomplished with range()
# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)

# for i in range(-10, -100, -30):
#     print(i)
# 
# To iterate over the indices of a sequence, you can combine range() and len() 
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
# # 
# # ... or the enumerate() function
# for i, v in enumerate(a):
#     print(i, v)
# 
# range() returns an iterable - gives your the successive items of a sequence when you iterate over it
# print(range(4))
# print(sum(range(4)))
# 
# while loop
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1 
# 
# break & continue statements
# else clauses on loops (FOR and WHILE can have ELSE clauses - reached if loop wasn't terminated by a BREAK)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
# 
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
# 
# PASS statement - does nothing! good for minimal classes or function/clause placeholder
# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
#
class MyEmptyClass:
    pass
# 
def initlog(*args):
    pass   # Remember to implement this!
# 
# MATCH statement
# similar flow to a switch statement
# pattern matching behavior similar to Rust or Haskell
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404: # multiple literals combined
            return "Not allowed"
        case _: # _ is wildcard - never fails to match
            return "Something's wrong with the internet"
# 
# MATCh patterns can unpack/assign/bind variables
# point is an (x, y) tuple
point = (5, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
# 
# further using MATCH assignments to capture attributes into variables
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
# 
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
# 
# if clause known as GUARD added to a pattern
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")        
# 
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 
# 
# 
# 
# 
# 
# 