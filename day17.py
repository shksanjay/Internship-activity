'''f=open('demofile.txt')
print(f.read())'''



'''with open('demofile.txt') as f:
    print(f.read())'''
    
'''f=open('demofile.txt')
print(f.read())
f.close()'''
'''
with open ('demofile.txt') as f:
    print(f.read(3))'''
    
'''with open ('demofile.txt') as f:
    print(f.readline())
    
f=open('demofile.txt')
print(f.read())'''
    
'''with open('demofile.txt') as f :
    print(f.readline())
    print(f.readline())'''
    
'''with open('demofile.txt')as f:
    for x in f:
        print(x)'''
        
# python file write 
'''with open('demofile.txt','a') as f :
    f.write("file has more content now ")
    
with open('demofile.txt') as f :
    print(f.read())'''
    
    # overwrite existing content

'''with open('demofile.txt','w') as d:
    d.write("here comes another content")
with open ('demofile.txt','a')as d:
    d.write('content added here ')

with open('demofile.txt') as d :
    print(d.read())'''
    
    
# /create new file named myfile.txt\



'''with open('myfile.txt','a') as f :
    f.write('new content added ')
    
f=open('myfile.txt','w') 
f.write('overwrited data')

f.close()'''


'''with open('nayafile.txt','w') as f :
  f.write('hello')
  
with open('nayafile.txt')as f:
    print(f.read())'''
    
# f=open('deletefile','x')

# delete file  

# import os
# os.remove('deletefile2')

'''import os 
if os.path.exists('deletefile6'):
    os.remove('deletefile6')
else:
    print('file doesnt exist')'''

'''with open('deletefile7','a') as f:
    f.write("content added ")
    
with open('deletefile7') as f :
    print(f.read())'''
    
# delete a entire folder 
'''import os 
os.rmdir('mfolder')'''

'''file=open('demofile.txt','rb')'''

'''fo=open('demofile.txt','wb')
print('name of the file:',fo.name)
print('opening mode:',fo.mode)
fo.close()'''


'''with open("example.txt", "rb") as file:
   content = file.read()
   print(content)
'''

'''try:
    with open('data.txt','r') as file :
        print(file.read())
except FileNotFoundError:
    print('file not found')'''
    
# checking file existence 
'''import os 
if os.path.exists('myfile.txt'):
    print('file exists')'''
    
'''with open ('example.txt') as u:
  for line in u:
      print(line)'''


'''with open('images.jpeg','rb') as file :
    data=file.read()'''


'''f=open('example.txt','r')

data=f.read()
print(data)

line1=f.readline()
print(line1)  

line2=f.readline()
print(line2)

line3=f.readline()
print(line3)

f.close() '''
'''f=open('demo.txt','a+')
# f.write('abc')
print(f.read())
f.write('abs')
f.close()'''

'''with open('demo.txt','r')as f:
    data=f.read()
    print(data)

with open('demo.txt','w')as f:
    f.write('')'''
