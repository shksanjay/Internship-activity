# python shorthand if 
'''a=10
b=9

if a>b:print("a is greater than b ")
'''

# one line if else 

'''a=6
b=4
print('A') if a>b else print('b')'''
'''a,b=5,6
print('A')if a>b else print('B') '''
'''
a=7 
b=6

if a>b:print("a is greater than b")'''

# Assign a value with if else 

'''a=10
b=20
c=a if a>b else b
print('bigger is ',c)'''

# multiple condition on one line 
'''a=int(input ("enter first number"))
b=int(input ("enter second number"))

print("a") if a>b else print("equals") if a==b else print("b")'''

'''x=20
y=17
max_value = x if x>y else y
print('max value:',max_value)'''

'''age=5
msg="adult" if age>=18 else "minor"
print(msg)'''
 
#  setting a default value 
'''
username="cristiano ronaldo "
show_name= username if username else "guest"
print('welcome,',show_name)
'''


'''a = 2
b = 5
print("YES") if a>b else print("NO")'''


# logical operators 
'''a=220
b=33
c=500
if a>b or a>c:
    print('one condition is true')
'''

# not operator

'''a=330
b=220
if not a>b:
    print("a is NOT greater than b") 
    
    

m=22
n=44
if not m==n:
 print("m is not equal to n")
'''

# combining multiple operators 
'''age=68
is_student=False 
has_disc_code=False
if (age < 18 or age> 65 ) and not  is_student or has_disc_code:
    print("discount applied!!")
else:
    print("discount not applied")'''
    
'''temperature=26
is_raining =False
is_weekend =True
if(temperature>20 and not is_raining) or is_weekend:
    print("great")'''
    
'''username ="Sanjay"
password="9869"
is_verified= False

if username and password and is_verified:
    print("logged in ")
else:
    print('ko ho ta be')'''

# range checking with logical operator 

'''score =101

if score >=0 and score <=100:
    print('valid ')
else:
    print('not valid ')'''
    
# Nested if 
'''x=19
if x>10:
    print("above 10")
    if x>20:
        print(" and also above 20")
    else:
        print("but not above 20 ")
'''
# checking multiple condition with nesting 

'''age=int(input("enter  your age :"))
has_license=False

if age>= 18:
    if has_license:
        print("you can drive ")
    else:
        print("you need a license ")
else:
    print("you cannot acquire license ")
        '''
        
        # score 60 att 80
'''       pass with goo standing
    pass but missing assignment 
pss but low attndence 
fail'''
'''marks = int(input("enter your score"))
attendence =int(input("enter your attendence"))
is_submitted=False

if marks>=60:
    if attendence>=80:
        if is_submitted:
            print("passed with good standing ")
        else:
            print("passed but assignment missing")
    else:
        print("passed but low attendence ")
else:
    print("failed")
            '''

# login validation with nested checks 
'''username ="Emil"
password="123456"
is_active=False
if username:
    if password:
        if is_active:
            print("login succed")
        else:
            print("account is not active ")
    else:
        print("password required")
else:
    print("username required")
    '''
# pass statement 

'''a=33
b=11
if b>a:
    pass'''

'''age=14
if age< 18:
    pass
else:
    print("access granted")
'''

# match 
'''Your_day=int(input("enter your day "))
match Your_day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case _:
        print('nothing')'''
        
# use of pipe operator
'''day_num=int(input("enter day number :"))
match day_num:
    case 1|2|3|4|5:
        print("today is a weekday")
    case 6|7:
        print("weekends")
    case _:
        print('error boii')
    '''

# if statement as guards 

'''month =4
day=1
match day:
    case 1|2|3|4 if month ==4:
        print("day in april")
    case 1|2|3|4 if month ==5:
        print("day in may")
    case _:
     print("no match ")
            '''
 # WAP to use pass in an empty if statement.
'''a=3
b=5
if a>b:
    pass
else:
    print('b is greater')
            '''
'''num=3
for i in num:
    i==5
    print('number is equal ')
else:
    pass
          '''  
