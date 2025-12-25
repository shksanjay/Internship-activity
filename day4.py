
# WAP to print numbers from 1 to 10 using range().

'''for number in range(2,21):
 print (number)
 '''
 
#  wap to print num from 10 to 1 in reverse using range()
'''for i in range(10,0,-1):
    print(i)
    '''
'''
for i in range(1,31):
    if i%3==0:
        print(i)   '''
        
#WAP to find the sum of numbers from 1 to 50 using range().
'''total=0
 
for num in range(1,51):
    total +=num
    print(total)'''

# using built in function sum()
'''total = sum(range(1,51))
print("sum of from 1 to 51 is:",total)'''

# WAP to create a list of numbers using range() and print it.
'''number=list(range(1,11))
print(number)'''

# WAP to print all numbers from 1 to 20 except multiples of 5 using range().
'''for num in range(1,21):
    if num%5!=0:
     print(num)
     '''
# WAP to print numbers from 0 to 50 with a step of 5 using range().

'''for number in range(0, 51, 5): 
    # start stop step
    print(number)'''
      
     
# WAP to generate a tuple from a range() of numbers.

'''number_tuple=tuple(range(10))    
print(number_tuple)'''

# WAP to check if a number is in a range() of numbers from 1 to 100.  

'''num1=int(input("enter a number:"))

for n in range(1,101):
     if n==num1:
      print("the number is in range",num1)
      break
else:
 print('the number is not in range')
     '''
    
# sets
# example of sets'''*unordered,unchangeable,duplicates not allowed'''


 
 
 
'''thisset={"apple","banana","kiwi"}
print(thisset)

myset={"bike","car",'lambo'}
print(myset)'''
# True ra 1 same item vantancha ani False ra 0 autai 


'''thisset = {"apple", "banana", "cherry",   2,True}

print(len(thisset))'''

'''set={True,False,"99",'30',19,'sanjay',}
print(type(set))'''

# use of set constructor set()


'''new_set=set([1,2,3,4,5,5])
print(new_set)'''

# WAP to create a set of 5 numbers and print it.

'''set={1,2,3,4,5,5}
print(set)

set={1,2,3,4,5,5}
new=append.(set)
print(new)'''

# access items 
# USE OF LOOP THROUGH THE SET AND PRINT THE VALUES 
'''set={"oman","porto","levante"}
for i in set:
 print(i)'''
 
#  output=porto
#         levante
#         oman

# check if item in the set 
'''new=set(("rabin","sabin","bipul"))
print("rabin" in new)
'''


'''set={'1','2','3','4'}

for x in set:
    print(x)
'''

'''print("9" not in set)'''


# add item in the set . #add()

'''Car_set={"lambo","mercedes","ferrari"}

Car_set.add("Volkswagen")

for x in Car_set:
    
 print(x)
 break 
print (f'the new added item in the set is{"Volkswagen"}.')'''

# update item of set2 in set 1
'''Set1={1,2,3,4,5,6}
Set2={7,8,9}
Set1.update(Set2)



print(Set1)'''

# Add update item from any iterable ie - list tuple dictionary

'''set={1,2,3,4,5}
list=(5,6)
tuple=[7,8,1]

set.update(list)
set.update(tuple)

print(set)
'''

# remove item in set-remove(),discard()

'''set={"rabin","sabin","don lee"} 


set.pop("rabin")

print(set)
'''
# remove will throw error if item is not present in the list while discard

# pop() takes no argument and remove random item 

'''thisset={"apple","banana","john"}

x=thisset.pop()

print(x)

print(thisset)'''

'''set={1,2,3,4,5}

x=set.pop()

print(x)

print(set)
'''

# clear() will clear the set 
'''new_set={12,3,4,5,6}

new_set.clear()

print(new_set)'''

# del will delete the set
'''thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)'''

# loop items

'''set={"apple","banana"}

for x in set:
    print(x)
'''

# join sets
'''
set1 ={"a","b",'c'}
set2={1,2,3}
set3={7,8,9}
set4={11,12,13}
set5= set1|set2|set3|set4

print(set5)'''

# join set and tuple using union 

'''x={1,2,3}
tuple=[4,5,6]

z=x.union(tuple)
print(z)'''


# update()

'''s={1,2,3}
c={4,5,6}
s.update(c)

print(s)'''


 
'''a=("a",'b','c')
for x in a:
 print(x)
'''

