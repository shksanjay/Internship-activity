# built in data types 

'''num1=float(2.11)
num2=float(3.99)
print(num2-num1)'''

'''num1=9
num2=9.1

process=num1*num2

formated_num=f'{process:.3f}'

print(formated_num)'''


'''num1=81
num2=9

output1=(num1%num2)
output2=(num1//num2)

print (output1)

print(type(output1))
'''
'''x=10
y=float(x)

print(y)

a=3.164
b=int(a)

print(b)
'''

'''num=3
square_num=3**2
cube_num=3**3

print("square of a number:",square_num)
print("cube of a number:",cube_num)
'''

'''num1=int(input("enter first  number:"))
num2=int(input('enter second number:'))

sum=num1+num2

print(sum)'''


'''amt=float(input("enter the princple amount:"))
tme=int(input("enter total time:"))
rT=float(input("enter the rate:"))

SI=(amt*tme*rT)//100

print("the simple interest is:",SI)'''

'''import math 
radius=float(input("enter radius:"))

area=math.pi*(radius**2)

print(f'the area of circle is{area:.2f}')

'''

'''num=6

if num%2==0:
 print("Number is even")
else:
 print("number is odd")'''

'''a=5
b=9

a,b=b,a
print("a:",a)
print("b:",b)'''

'''a=5
b=10

temp=a
a=b
b=temp

print("a=",a)
print("b=",b)'''

'''n='this is n'
m='this is m'

temp=n
n=m
m=temp

print("n:",n)
print("m:",m)'''

'''a,b,c=10,5,15

if a>b and a>c:
    print("a is greater")
elif b>c and b>a :
    print("b is greater")
else:
  print("c is greater ")'''

# tuple

'''list=['1','2','3']
list.append(4)
list[0]=8

print(list)'''

'''list=(1,2,3,4,5,1,9,1,8,1)

count_of_one= list.count(1)

count_of_two= list.count(2)

print(f"the number 1 comes {count_of_one} times")

'''


# WAP to create a tuple of 5 elements and print it.
'''a=(1,2,3,4,5,6)
largest_item = max(a)
smallest_item = min(a)

print(f"the largest item is '{largest_item}' ")
'''
'''tuple_list=(1,2,3,4,5,6)

sliced_part= tuple_list[0:2]

print(sliced_part)
'''

# convert tuple into a list 
'''original_tuple =(1,2,3,4,)

temp_list =list(original_tuple)

temp_list.append(5,)
temp_list.extend([7,8])

new_tuple=tuple(temp_list)
print(f"the final tuple is '{new_tuple}'" )
'''
# repeat a tuple 3 time 

# WAP to print numbers from 1 to 10 using range().

'''for number in range(1,11):
    print(number)
'''






































