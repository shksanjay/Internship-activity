# intersection()

'''set1={1,2,3}
set2={3,4,5,1}

set3=set1.intersection(set2)
print(set3)'''

'''set1={2,4,5,6}
set2={7,8,9,2,4}

set3=set1 & set2
print(set3)
'''

# intersection  update
'''set1={1,2,3,4}
set2={4,5,6,7,1}

set1.intersection_update(set2)

print(set1)'''

'''set1={'apple','1','banana',}
set2={'1','google','apple','2','true'}
set3=set1.intersection(set2)

print(set3)'''

# difference or  -

'''set1={'apple','1','banana',}
set2={'1','google','apple','2','true'}
set3=set1 - set2

print(set3)'''

'''n = {1, 2, 3, 4}
m = {3, 4}

n.difference_update(m)
print(n)

print("new one")

a = {1, 2, 3, 4}
b = {3, 4}

c = a.difference(b)
print(c)
print(a)
'''

# symmetric difference present itam not present in both sides 


'''set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
'''

'''set1={'madrid','barca','athletic '}
set2={'madrid','chelsea',"tottnem"}

set1.symmetric_difference(set2)

print(set1)'''

'''# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)'''

# frozensets

'''x=frozenset({"apple","banana","cherry"})
print(x)
print (type(x))'''

'''fs=frozenset({1,2,5})
cp=fs.copy()

print(cp)'''


'''a=frozenset({1,2,3,4})
b=frozenset({3,4,5})

print(a.difference(b))
print(a-b)'''

'''frozen set intersections '''

'''a=frozenset({1,2,3,4,5})
b=frozenset({1,2,6,7,8})

print(a.intersection(b))
print(a &b)'''

#to check the two frozenset have intersection 
'''
a=frozenset({5,6})
b=frozenset({1,2,3,4})

print(a.isdisjoint(b))
'''

# issubset()

'''a=frozenset([1,2,3,4,5])
b=frozenset([1,2,3,4])
print(b.issubset(a))

print(b<a)
'''
# superset()
'''a=frozenset([1,2,3])
b=frozenset({1,2,3,4,5})

print(a.issuperset(b))
print(b>=a)
print(b>a)'''

# symmetric diiference

'''a=frozenset({1,2,3,4})

b=frozenset({2,3,4})

print(a^b)


'''
# union 
'''a=frozenset({1,2,3})
b=frozenset([4,5,6])

print(a|b)
'''


# DICTIONARY

'''newdict={"brand":"Yamaha",
         "model":"xsr",
         "year":"2024"
         }
print(newdict)'''

'''playdict={"Club":"realmadrid","Nationality":"England"
          ,"Name":"TAA"
          ,"Name":"Marcel"}
print(playdict)

print(len(playdict))
'''

'''thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))
'''

# using dict() constructor 
# hdict=dict(name ="john cena", 
#            age="66",country="new zealand")




# x= hdict.get("name")

# print(x)


# keys()

'''newdict=dict (name="sanjay", grade="7th sem",
              country="nepal")

x=newdict.keys()

print(x)'''

# add items in dict

'''car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()

print(x)

car["color"]="black"

print(x)
'''
# get values 

'''car = {
 "brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(['model']='ford')
x=car.values()
print(x)

dict={"item":"pen","price":"40","color":"black"}
x=dict.keys()
print(x)

dict["brand"]= "sepaha"

print(x)'''

'''car= {
    'brand':'ford',
    'model':'mustang',
    'year':1999
    
}

car.update({"color":"red"})


print(car)'''

# pop()

'''dict={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dict.pop("year")
print(dict)'''

# popitem removes last inserted item 
'''thisdict = {
  "brand": "Ford",
  "year": 1964,
  "model": "Mustang"
  
}
thisdict.popitem()
print(thisdict)'''

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict)'''

# clear
'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)'''

# loop

'''thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x,y in thisdict.items():
    print(x,y)
'''

'''dict={
    'item':'burger',
    'price':'44'
}
newdict=dict.copy()

for x,y in newdict.items(): 
 print(x,y)'''
 
'''dict={
    'item':'burger',
    'price':'44'
}

newdict=dict()
print(newdict)'''



