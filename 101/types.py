# https://www.geeksforgeeks.org/python-data-types/

# NUMERIC TYPE
# int
b = 50 
print(type(b))

# float
c = 12.3 
print(type(c))

# complex
d = 5 + 4j
print(type(d))

# SEQUENCE TYPE
# string
a = "stringType"
print(type(a))

e = '''Some "quotes"'''
f = '''multi
    line
    fun'''

g = "a b c d ef"
gList = g.split()
print(gList)
print(g[0])
# last char (negative indexing)
print(g[-1])
# 2nd to last char
print(g[-2])

# list
# https://www.geeksforgeeks.org/python-lists/
listOne = [1, 2, 3.1, "four", {}]
print(type(listOne))
print(len(listOne))
listOne.append(6)
# range is [x, y)
for i in range(1, 4):
    listOne.append(i)
listOne.insert(0, 'starter')
listOne.extend(['some', 'ending', 'stuff'])
print(listOne)
listOne.reverse()
print(listOne)
listOne.remove('starter')
# pop last elt
lastElt = listOne.pop()
print(lastElt)
print(listOne)
# pop at 0th index
zerothElt = listOne.pop(0)
print(zerothElt)
print(listOne)
#slicing/advanced indexing
sliceList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sliceList[2:])
print(sliceList[:4])
print(sliceList[2:4])
print(sliceList[1::2])
print(sliceList[:-4])
print(sliceList[-3:-1])
print(sliceList[::-1])
#list comprehension
# newList = [ expression(element) for element in oldList if condition]
oddSquare = [x**2 for x in range(1,11) if x % 2 == 1]
print(oddSquare)
# above list comprehension similar to below for loop:
oddSquare2 = []
for x in range(1,11):
    if x % 2 == 1:
        oddSquare2.append(x**2)
print(oddSquare2)


# tuple

# BOOLEAN TYPE

# SET TYPE

# DICTIONARY TYPE

# BINARY TYPE


