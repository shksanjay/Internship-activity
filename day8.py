# while loops 
'''i=1
while i<6:
    print(i)
    i+=1
'''
# break statement 
'''i=1
while i<6:
    print(i)
    if  i==4:
     break
    i+=1'''

# continue statement 
'''i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)'''
'''i=0
while i<=9:
    print(i)
    i+=1'''
'''
i=0
while i<=9:
    i+=1
    if i==5:
        continue
        
    print(i)
    '''
# example 
'''seconds = 5
while seconds > 0:
    print(seconds)
    seconds -= 1

print("Time up!")
'''

'''password=""
while password != "admin111":
    password=input('enter password:')
    
print("access granted")
'''

# nested while loop 

'''i=1
while i<=3:
    j=1
    while j<=2:
        print(i,j)
        j+=1
    i+=1

'''

# WAP to print numbers from 1 to 10 using a while loop.
'''i=0
while i<11:
    print(i)
    i+=1'''
    
# WAP to print all even numbers between 1 and 20 using while.
'''i=2
while i<=20:
    if i%2==0:
        print(i)
    
        i+=2 '''
        
# WAP to print numbers from 10 to 1 in reverse order.
'''num=10
while num>0:
    print(num)
    num-=1'''

# WAP to calculate the sum of first n natural numbers using while.

# for loops 
'''books=["math","account",'science']
for x in books:
    print(x)'''
    
'''for x in "apple":
    print(x)
    if x=="p":
        break'''
        
# break in for loop 
'''clubs=["rma",'fcb','atm']
for x in clubs:
  
    if x=="fcb":
        break 
    print(x)
        
clubs=["rma",'fcb','atm']
for x in clubs:
    print(x)
    if x=="fcb":
     break    
    
        '''
        
# contiinue in for loop 
'''cars=["volk","thar","g wagon"]
for x in cars:
    if x=='volk':
        continue
    print(x)'''
# the range()in for loop 

'''for x in range(2,9,2):
    print(x)'''
    
# else in for loop

'''for x in range(0,20,2):
    print(x)
else:
    print("finished")'''

# WAP to print “Hello” 5 times using while.
'''itr=1
while itr<=5:
    print("hello")
    itr+=1'''


    
