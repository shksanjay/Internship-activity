# function 
'''def run():
    print("hello called from a fucntion")
    # indentation required 
run()
run()
run()
'''

# function that returns a value 

'''def get_greetings():
    
  return "fucntion called hello"

message=get_greetings()

print(message)'''



# simple function 

'''def function():
    print('First function called')
    
function()'''

# function with parameter

'''def add(a,b):
    print(a+b)
    
add(4,6)'''
# funtion that returns the value 
'''def square (x):
    return x*x
result=square(9)

print(result)'''


'''    
def square(x):
    print(x*x) 

square(9)'''

# function with default 
'''def greet(name="sanjay"):
    print("hello",name)
greet()
greet("nischal vai")
'''
# function with multiple return

'''def calc(a,b):
    return a+b,a*b,a-b


r,n,s=calc(4,8)


print(r,n,s)'''

# using return value directly
'''def get_greetings():
    return "hello"

print(get_greetings())
'''
'''
def func():
    pass'''

# ✅ Basic Function Questions

# WAP to create a function that prints “Hello World”.
'''
def basic():
    print("Hello world")
    
basic()
'''


# WAP to create a function that prints “Hello World”.

'''name=input("enter name")
def function():
    print(f"hello,{name}")
function()
'''


# WAP to create a function that returns the sum of two numbers.

'''def add(a,b):
    return(a+b)
sum=add(4,6)
print(sum)'''

# WAP to create a function that returns the square of a number.

'''def square(x):
    return(x*x)
result=square(9)
print(result)'''

# WAP to create a function that checks if a number is even or odd

'''def func(num):
    if num %2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("enter a number:"))

result=func(num)
print(f"{num} is {result}")
'''

# arguments 

'''def function(fname):
    print(fname )
function("sanjay")
function("sanjeev")
function("smaran")'''

'''# parameter and argument 
def function(name):
    #name is parameter 
    print(name)
function("emil")
#emil is an argument 
'''

'''def func(fname,lname):
    print(fname,lname)
func("sann","shakya")
'''
 
# default parameter values

'''def new_func(name="mate"):
    print("hello",name)
    
new_func('sanjay')
new_func('rabin')
new_func('')
new_func('sabin')'''

'''def function(name="portugal"):
    print("nationality",name)
function("spain")
function("germany")
function("poland")
function()'''

# keywords argument
'''def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
'''


'''def my_func(vehicle,name):
    print("i have a ",vehicle)
    print("My", vehicle + " brand's name is ",name)
my_func(name="volkswagen",vehicle="car")'''

# positional arguments 
'''def function(animal,name):
    print("i have a ",animal)
    print("it's name is ",name)
function("dog","dawg")'''


# mixing positonal and keyword arguments 
'''def function(animal,age, name):
    print("i have a",age,"year old",animal,"named",name)
function("dog",name="guddu pandit",age=9)'''


# passing different data types 


'''def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)'''

'''def func(players):
    for player in players:
        print(player)
my_players=["rabin","sabin","birke"]
func(my_players)
'''

# sending a dictioanry as an argument

'''def func(persons):
    print("Name",persons["name"])
    print("Age",persons["age"])
my_person={"name":"rabin","age":29}
func(my_person)'''

# return values
'''def function(x,y):
    return x-y
result=function(5,9)
print(result)'''

# return a list 
'''def my_function():
    return["ovan","microwave","mixer"]
fruits=my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])'''

# return tuple
'''def tuple():
    return(10,30)
x,y=tuple()
print("x:",x)
print("y:",y)'''

# postional only arguments
'''def function(name,/):
    # ,/ use gareko bela ma keyword argument use garna milena(=)
    print("hey",name)
# function(name="sabin")
function("sabin ")'''
        


# keyword only argument 

'''def function(*,name):
    print("hello",name)
function(name="sakiram")
'''
# combining positional only and keyword only

'''def my_function(a,b,/,*,c,d):
    return a+b+c+d

result=my_function(5,6,c=7,d=1)
print(result)'''


    








 
