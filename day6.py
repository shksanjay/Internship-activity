# nested dictionary 


'''employ1={
        "name":"samrat",
        "Id":"9990"
 }
employ2={
        "name":"smaran",
        "Id":"1996"
}
employ3={
    "name":"abinash",
        "Id":"220"
    }
register_dict= {
    "employ1": employ1,
    "employ2":employ2,
    "employ3":employ3
}
for x in register_dict:
 print(x)'''
 
 
#  loop if else
'''a=input("enter a num")
b=input("enter second number")
if b>a:
    print("b is greater than a ")
else:
    print("a is greater than b")
    '''
    
'''num1 = 15
if num1>0:
    print("the  number is positive")
    '''
'''age =18
if age>=18:
    print("eligible for license")
    print("eligible for voting")
    '''
    
'''is_present=True
if is_present:
    print("Sanjay is present in the class")'''

# WAP to check if a number is positive or negative.

'''num=bool(input("enter a number:"))
if num>0:
    print("number is pos")
else:
    print("number is neg ")'''
    
'''num=6
if num%2==0:
    print("num is even")
else:
    print("num is odd")
'''

'''age=int(input("enter your age"))
if age>=18:
    print("u are eligible for voting")
else:
    print("u are not eligible")
'''

'''num1=-5
num2=5
if num1==num2:
    print("number is equal")
else:
    print("number is unequal")
'''

'''num=int(input("enter a number"))
if num%5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible")
'''
# WAP to print “Pass” if marks are ≥ 40, otherwise print “Fail”.
'''marks=41
if marks>=40:
    print("Passed")
else:
    print("failed")     '''
# WAP to check if a character is a vowel or consonant.

'''val="aeiou" 
value=input("enter a char:")
if value in val:
    print("value is vowel")
else:
    print('value is consonant')
        '''
# WAP to check if a number is greater than 10.
'''num=10
if num>11:
    print('num is greater')
else:
    print('num is smaller')
'''

# The Elif Keyword
'''a=20
b=22
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b is equal ")
    '''
    

# multiple elif statement
'''score=int(input("enter your marks"))
if score>=90:
    print("grade:A")
elif score>=80:
    print("grade:B")
elif score>=70:
    print("grade:C")   
elif score>=60:
    print("grade d")'''
    
'''name='hello'
if len(name)>0:
    print(f"welcome,{name}!")
else:
    print("this field should be completed")'''
    
    # WAP to find the largest of three numbers.
    
'''a,b,c=11,12,13
if a>b & a>c:
    print('a is largest')
elif b>a & b>c:
    print("b is largest")
else:
    print("c is largest")'''
    
'''
WAP to display a grade based on marks:

90+ = A

75–89 = B

50–74 = C

Below 50 = Fail'''
'''marks=int(input('enter your marks:'))
if marks>=90:
    print("grade a")
elif marks>=75 and marks<89:
    print("grade b")
elif marks>=50 and marks<=74:
    print("grade c")
else:
    print("failed")'''


    
# WAP to check if a person is child, teenager, adult, or senior citizen
'''age=int(input("enter your age "))
if age>=3 and age<=12:
    print("your are a child ")
elif age>=13 and age <=19:
    print("your are a teenager")
elif age>=20 and age<=59:
    print("your are a adult")
elif age>=60:
    print("your are a senior citizen ")
'''
# WAP to check if a character is uppercase, lowercase, digit, or special symbol.

'''ch=input("enter a character")
if 'A' <= ch <='Z':
    print('Uppercase Letter')
elif 'a' <= ch <='z':
    print('Lowercase letter')
elif '0' <= ch <='9':
    print('digit')
else:
    print('Special letter')'''
    
# WAP to check if a number is divisible by both 3 and 7.
'''num=int(input("enter a number "))
if num%3==0 & num%7==0:
    print('the number is divisible by both 3 and 7')
else:

    print('not divisible ')'''
    
# WAP to check whether a number is single-digit, double-digit, or three-digit.

'''num=int(input('enter a number'))
if 0<= num <=9:
    print('single digit')
elif 00<= num <=99:
    print("double digit ")
else:
    print("triple digit ")'''
    
    
while True:
    year = int(input("Enter the year to check: "))

    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")

    choice = input("Do you want to check again? (y/n): ").lower()
    if choice != 'y':
        print("Exiting program...")
        break
