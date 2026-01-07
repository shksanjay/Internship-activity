'''class father:
    def skill1(self):
        print("father's skill: driving")
        
class mother:
    def skill2(self):
        print("mother's skill: Cooking")
        
class child(father,mother):
    pass
c=child()
c.skill1()
c.skill2() '''

# method resolution order for multiple inheritance 
'''class father:
    def skill(self):
        print("father's skill: driving")
        
class mother:
    def skill(self):
        print("mother's skill: Cooking")
        
class child(father,mother):
    pass

c=child()
c.skill()'''

# diamond problem 

'''class A:
    def show(self):
        print('class a ')
class B(A):
    def show(self):
        print('class b')
        super().show()

class C(A):
    def show(self):
        print('class c')
        super().show()

class D(B,C):
    def show(self):
        print('class d')
        super().show()
d=D()
d.show()'''


# multilevel inheritance 
'''class Network:
    def connectivity(self):
        return'network connected'
    
class Network_5g(Network):
    def fast_connectivity(self):
        return'it provide fast connecction '
    
class Network_5g_wifi(Network_5g):
    def fast_and_stable_connection(self):
        return "is is fast and stable"
    
network_object = Network_5g_wifi()
print(network_object.connectivity())        
print(network_object.fast_connectivity())   
print(network_object.fast_and_stable_connection ())'''  

# method overriding 

'''class parent:
    def show(self):
        print('this is parent class ')

class child(parent):
    def show (self):
        print('this is child class ')
        
obj=child ()
obj.show()'''


# calling parent method using super()
'''class parent:
    def show(self):
        print('study till 8')
        
class child(parent):
    def show(self):
        super().show()
        print('study till 7')
        
obj= child()
obj.show()
        '''
        
        
# method overriding in multilevel inheritance 

'''class father:
    def show (self):
        print('take mother permission')
        
class mother(father):
    def show(self):
        print("take father's permission ") 
        
class child(mother):
    def show (self):
        print("doesnt takes permission ")
        
obj=child()
obj.show()'''

# abstraction method 
'''from abc import ABC,abstractmethod 

class vehicle(ABC):
    @abstractmethod
    def start(self):
     print('220hp')

class Car (vehicle):
    def start(self):
        print('car starts')

c=Car()
c.start()'''

'''from abc import ABC,abstractmethod 
class demo(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return 
    def method2(self):
        print("concrete method")
        
class concreteclass(demo):
    def method1(self):
         super().method1()
         return '''

    


