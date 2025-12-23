# print('36')
#single line comment uses#
#print number 36
#declare variaable 
# name = "Sabin"
#print name
# print(name) #prints sabin

# command to us comment in windows cntrl +/
""" this is a multiline 
comment """
#win +ctrl+shift+b
'''num1=20
num2=32

sum=num1+num2
print(sum)
#print(product)
'''
# assigneing  single value to a variable 
# employee_name="sanjay"

# print(employee_name)

# assiging multiple values to multiple variables

'''
a,b,c=10,20.15,'sunita'

print( a,b,c )
'''

# assign same value to multiple variable 

# x=y=z=66

# print(x,y,x)

site1 = site2  = 'programiz.com'

print (site1)  # prints programiz.com
print (site2)  # prints programiz.com

"""rule for naming a variable
snake_case
MACRO_CASE
camelCase
CapWords """    
 
# valid variable names
num = 5
Num = 55
print(num) # 5
print(Num) # 55

# PYTHON LITERALS

is_active = True
print(is_active )

value = None #special literal in python
print(value)

# python type conversion implicit conversion
integer_num=10
float_num=10.5
new_num= integer_num+float_num

print("Value:",new_num)
print("type:",type(new_num))

# explicit conversion



num1 = '22.12'
num2 = 10

result = float(num1) + num2
print(result)
print(type(result))

# python print statement

print('goodmorning' ,end=' ')
print("dear client")
print('new year',2026 , 'see yahh' ,sep='.')

name = 'rabin'
num = -65
print(9)
print(name)
print(num)

print('python is' + 'good' )
print('language')


x=9
y=1
print('the value of x is{} and the value of y is {}'.format(x,y))

# python input

number = input ('enter your num: ')
print(number)
print(type(number))
#  convert user input into number

num= float(input('enter num: '))# to be noted
print(num)

print(5+6)

print(10/3)

print(10//3)
 
print(10 ** 2)

# identity operator is and is not used to check if two values are in same location
x3 ='hello'
y3 ='hello'


x2 = [2,3,4]
y2 = [2,3,4]
print(x3 is  y3)

# membership operator "in and not in "
name="sabin bajrahcarya"
print("a"in name)

print("x"in name)

number=[10,25,40]
print('25 'not in number)


record ={'name':'sabin','age':22}
print('name'in record)

print('gender' not in record )

#  python program to split bill amount 

input_amount= float(input('enter the amount:'))
input_friends= int(input('enter number of friends:'))
friend=5
amount=100
total_after_tax=0.20*amount+amount
per_person=total_after_tax/friend

print(per_person)
    
    # python if statement 
number = int(input('Enter a number: '))
if number >=10:
    print('the number is greater ')
    
else:
    print('the number is smaller ')


# python if else statement 

number=int(input('enter num:'))
if number >=0:
    print('the number is positive')
else:
    print('the number is negative ')


# python if elif else statement 

number=int(input('enter number:'))
if number >0:
    print('the number is positive ')
elif number==0:
    print('the number is zero')
else:
    print('the number is negative ')

# python nested if statement 

age=int(input('enter age:'))
if age >=18:
    print('adult  ')
    if age>=21:
     print('eligible for voting')
number=int(input("enter number:"))

if number >= 0:
    if number == 0:
      print('Number is 0')
    
    else:
        print('Number is positive')

else:
    print('Number is negative') 


number=-6

if number>0:print('number is positive ')
else:print('number is negative ')

# Write a function to check whether a student passed or failed his/her examination.

marks=int(input('enter marks:'))
if marks>=40:
    print('passed')
else:
    print('failed')

# python for loop

# for i in range(5):
#     print(i)

for j in range(0,6):
    print(j)

language="python"
for ch in language:
        print(ch)

languages=['python','java','c++']
for lang in languages:
        print(lang)

values= range(0,4)
for val in values:
    print(val)

# break and continue statement 
for i in range(0,10):
    if i==7:
        continue
    print(i)

# nested for loop
for i in range(1,4):
    for j in range(2,4):
        print(i,j)

# pass with conditional statement

n=7
if  n>9:
     pass 
print('hello world')
