# python decorator and scope 
'''def myfunc():
    x=300
    print(x)
myfunc'''

'''def func():
    x=999
    def innerfunc():
        print(x)
    innerfunc()
func()'''

# global scope

# variable created oustside of a function

'''x=20
def func():
    print(x)
func()
print(x)
'''

'''x=440
def func():
    x=555
    print(x)
func()
print(x)
'''


# function indepth 
'''def function():
    # example code
    print("function")
function()'''

# simple function code


def evenodd(x,y):
    
    if (x,y%2==0):
        return "even"
    else:
        return "Odd"
x=int(input("enter a number:"))
y=int(input("enter a number:"))

print(evenodd(x,y))


