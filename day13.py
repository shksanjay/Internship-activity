# file handling 
# print(x)
 
'''try:
    print(x)
except:
    print("exception handled ")
    '''
'''try:
    print(x)
except NameError:
    print("Variable x is not defined ")
except:
    print("smt is wrong")'''
    
# use of else word in 
'''try:
    print('hello')
except:
    print('no')
else:
    print('yes')'''
    
# finally

'''try:
    print(x)
except:
    print("1")
finally:
    print("2")'''
  
# raising exception 
'''x= -9
if x<0:
    raise Exception("please enter number above zero")
'''
'''try:
    value=int(input("enter a number "))
except ValueError:
    print("enter number not char ")'''

'''x='9'

if not type(x) is int:
    raise TypeError("integer only allwed")'''
    
'''try:
    num=int(input("enter a number"))
except ValueError:
    print("Number please!")
else:
    print("you entered:",num)'''
    
'''try:
    num=int(input('enter a number '))
except ValueError:
    print("number only")
finally:
    print("task excuted")'''
    
# multiple except blocks 

'''try:
    result=10/int(input('enter a number'))
except ValueError:
    print("number only ")
except ZeroDivisionError:
    print('cannot divide by zero')
else:
    print('calculation executed')
'''

'''try:
    file=open('data.txt')
except FileNotFoundError:
    print('file not found')
finally:
    print('hello')'''
'''password='1234'
try:
    pin=input(print('Enter pin'))
    if pin!= password:
        raise ValueError('incorrect pin')
    
except ValueError as e:
    print(e)
else:
    print("phone unlocked")'''
    
# python oop


'''class student:
    pass
    
new_car=student()'''

'''class collegue:
    name='abinash'
    age=29'''
    
'''class Team:
    def greet(self):
        print('hello')'''
        
'''class Student:
    def __init__(self, name):
        self.name = name
       
        
    def show(self):
        print("name is",self.name)
            
s1=Student("sanjay")
s1.show()'''
'''
class MyClass:
    x=5
    
p1=MyClass()
p2=MyClass()
p3=MyClass()

print(p2.x)  
print(p1.x)  
print(p3.x)  '''

'''class person:
    pass'''

# python __init__ method 
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("sanjay",29)
print(p1.name,p1.age)'''

'''class Detail:
    def __init__(self,name,age,place,country):
        self.name=name
        self.age=age
        self.place=place
        self.country=country
p1= Detail('Sanjay',21,'sanagaun','nepal')
print(p1.name)
print(p1.age)
print(p1.place)
print(p1.country)'''
 


'''class Player():
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
p1=Player('xavi',55,'mid')
print(p1.name)
print(p1.age)
print(p1.position)
'''








    