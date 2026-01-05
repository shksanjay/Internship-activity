'''class bank:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary =salary 
b1=bank('sanjay',19,0.1,20000)
print(b1.name)
print(b1.age)
print(b1.id)
print(b1.salary)'''
# encapsulation 

'''class bank:
    def __init__(self,balance ):
        
        self.balance=balance '''
        
# abstraction 

# car.start()

# inheritance 

'''class animal:
    def sound(self):
        print("bark sound")

class Dog(animal):
    pass
'''

# polymorphism
'''class Dog:
    def sound (self):
        print('bark')

class cat:
    def sound(self):
        print('meow')'''
        
# calling one method from another method 

'''class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return "hello,"+self.name
    def welcome(self):
        message=self.greet()
        print(message+"wlcome")
p1=person("ram")
p1.welcome()
    '''
    
    
# class properties 

'''class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
D=car('bmw','g class')
print(D.brand)
print(D.model)
'''

# modify properties 
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("ankit",33)

p1.age=34
print(p1.age)'''

# delete properties 

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("ankit",33)
del p1.age
print(p1.name)
    '''
    
# class properties vs instance properties 

'''class person:
    lastname="shakya"
    def __init__(self,name):
        self.name=name
p1=person("emil")
p2=person("ram")

               
person.lastname="kc"

print(p1.name+p1.lastname)
print(p2.lastname)'''

# add properties 
'''class person:
    def __init__(self,name):
        self.name=name
p1=person('vini')

p1.age=44
p1.home='bkt'

print(p1.name)
print(p1.age)
print(p1.home)'''


# class methods 

'''class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello my name is "+self.name)
p1=person('sanjay')
p1.greet'''

# method  with parameter 
'''class calculator:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
calc=calculator()
print(calc.add(4,3))
print(calc.multiply(4,3))'''

'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        return f"{self.name} is {self.age}years old"
p1=person('ram',22)
print(p1.get_info())'''

# methods modifying properties 

'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 2
    print(f"Happy birthday! You are now {self.age}")
    
p1=Person('sanjay',22)
p1.celebrate_birthday()'''

# __str__method

'''class person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}  {self.age}  "
        
p1 =person('sanja',66)
print(p1)
'''

# delete method 

'''class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello")
p1=Person("sanjay")

del Person.greet
p1.greet()'''

# inheritance 

'''class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def print_name(self):
        print (self.firstname ,self.lastname)
    
x=Person("ram","kc")


class Student(Person):
    def __init__(self, firstname, lastname,):
       super().__init__(firstname,lastname)

    def welcome(self):
        print('welcome',self.firstname,self.lastname,'to')
'''

# polymorphism 
'''class car:
    def __init__(self,brand):
        self.brand=brand
    
    def move(self):
        print("drive")
        
class boat:
    def __init__(self,brand):
        self.brand=brand
    
    def move(self):
        print('sail')
        
class plane:
    def __init__(self,brand):
        self.brand=brand
    
    def move(self):
        print('fly')
        
car1=car('ford')
boat1=boat('lambo')
plane1=plane('airlines')

for x in(car1,boat1,plane1):
    x.move()'''

# inheritance class polymorphisim 
'''class vehicle:
    def __init__(self,name):
        self.name=name
    
    def move(self):
        print('move')
        
class car(vehicle):
    def move(self):
        print('ride')
        
class boat(vehicle):
    def move(self):
        print('sail')
        
car1=car('ford')
boat1=boat('lambo')

for x in (car1,boat1):
    x.move()
'''
        


        
        
    