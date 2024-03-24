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
# https://www.geeksforgeeks.org/python-tuples/
# unlike lists, tuples are immutable - they can't be modified after being created.
tuple1 = ()
print(tuple1)
tuple2 = ('a', 'b', 'c')
print(tuple2)
print(tuple2[0])
print(tuple2[-1])
tuple3 = (1, 2, 3)
print(tuple3)
tupleNest = (tuple2, tuple3)
print(tupleNest)
print(tupleNest[0][0])
list1 = [1, 2, 3, 4]
tupleFromList = tuple(list1)
print(tupleFromList)




# BOOLEAN TYPE
# capitalize! True & False
# non-boolean objects can be evaluated in a boolean context
print(type(True))
print(type(False))

# SET TYPE
# https://www.geeksforgeeks.org/python-sets/
set1 = set()
print(set1)
set2 = set("stringSetElt")
print(set2)
list3 = [1, 2, 2, 3, 3, 3]
setFromList = set(list3)
print(setFromList)
setMixedTypes = set([1, 2, "three", False, False, True])
print(setMixedTypes)
set4 = set([1, 2, 3, 4, 5, 5])
# in keyword
print(1 in set4)
print(7 in set4)
for i in set4:
    print(i, end=" ")
print("...")

# DICTIONARY TYPE
# https://www.geeksforgeeks.org/python-dictionary/
dict1 = {}
print(dict1)
dict2 = dict()
print(dict2)
dict3 = {1: "foo", 2: "bar", 3: "foobar"}
print(dict3)
dict4 = dict([("foo", 1), ("bar", 2), ("foobar", 3)])
print(dict4)
dict5 = dict({1: "foo", 2: "bar", 3: "foobar"})
print(dict5)
# index with []
print(dict4["foo"])
# get by key
print(dict4.get("bar"))
dictNested = {1: {11: 111, 111: 1111}, 2: {22: 222, 222: 2222}}
print(dictNested)
print(dictNested[1][11])
dictUpdate = {1: "foo", 2: "bar", 3: "foobar"}
dictUpdate[1] = "newValue!"
print(dictUpdate)
# deleting elt with del keyword
del(dictUpdate[3])
print(dictUpdate)



