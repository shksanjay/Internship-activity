# function args and kwargs 
'''def function(*kids):
    print("the youngest child is"+ kids[2])
function("jetha","maila","saila")'''


# accessing individual arguments from *args 
'''def function(*args):
    print("Type:",type(args))
    print("first argument:",args[0])
    print("first argument:",args[1])
    print("first argument:",args[2])
    
function("messi",'neymar','ronaldo')'''

'''def funct(greeting,*names):
    for name in names:
        print(greeting,name)
        
funct("hello",'ram')'''

# *args example

'''def new_func(*numbers):
    total=0
    for num in numbers:
     total+=num
    return total
    
print(new_func(1,2,3))
print(new_func(10,20,30))
print(new_func(9))'''

# finding maximum value 

'''def function(*numbers):
    if len(numbers)==0:
        return None 
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num

print(function(3,6,11,9,22))
        '''

# **kwargs to accpet any number of keyword arguments 
'''def my_function(**kid):
    print("his last name is "+kid["fname"])
my_function(fname="rabin",lname="shrestha")
'''

# using kwargs with regular argument 

'''def function(username,**details):
    print("Username:",username)
    print("additional details:")
    for key,value in details.items():
        print("",key+":",value )
        
function("sanjay111",age=25,city="oslo")'''

'''def my_function(title,*args,**kwargs):
    print("title:",title)
    print("positional argument:",args)
    print("keyword arguments:",kwargs)
my_function("user info","emil","Ram",age=24)'''

# unpacking arguments 
'''def function(a,b,c):
    return a+b+c
numbers=[1,2,3]
result=function(*numbers)
print(result)'''

'''def func(fname,lname):
    print("hello",fname,lname)

person={"fname":"shyam",'lname':'shakya'}
func(**person)
'''

'''def sum_all(*args):
    total=0
    for num in args:
        total+= num
    return total 
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))
'''
'''
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
print_info(name='Alice',age=30,city='new york')
'''
       
       
'''def create_profile(**kwargs):
    profile = {
        "name": kwargs.get("name", "Unknown"),
        "age": kwargs.get("age", 0),
        "email": kwargs.get("email", ""),
    }
    return profile

user1 = create_profile(name="Bob", age=25)
user2 = create_profile(name="Charlie", email="charlie@example.com")
                '''  
                
# using both togther 
'''def complete_function(a,b,*args,**kwargs):
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"args:{args}")
    print(f'kwargs:{kwargs}')

complete_function(1,2,3,4,5,name='alice',age=24)'''

'''def multiply(a,b,c):
    return a*b*c
numbers=[2,3,4]
print(multiply(*numbers))

def greet (name,message):
    return f"{message},{name}!"

params={'name':'alice',"message":"hello"}
print(greet(**params))'''
