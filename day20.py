# crud operation in python
'''students=["ram ",'shyam','hari']
students.append('amit')

students[1]='abisekh'


students.remove('hari')
print(students)'''

'''employees=[]
employees.append('amit')
employees.append('abisekh')

# read


# update(changing)
employees[1]='hari'

employees.remove('hari')

print(employees)
'''

# using dictionary

'''employee={'name':'sajan','age':22}

employee['department']='HR'
print(employee)'''

# crud using file handling
'''with open ('employee.txt','w')as f:
    f.write('sanjay,21\n Ram,22')

with open('employee,txt','r') as f:
    print(f.read())
'''

#contract management
contract=[]
def create_contract():
    id=int(input("Enter your id:"))
    name=str(input("Enter your name:"))
    email=str(input("Enter your email:"))
    contract.append({"id":id,"name": name, "email": email})
    print("Contract created")

def read_contract():
    if not contract:
        print("No records found")
        return
    for c in contract:
        print(f"ID:{c['id']}|Name:{c['name']}|Email:{c['email']}"   )


def update_contact(name,new_email):
    id=int(input("Enter your id to update:"))
    for c in contract:
        if c["id"]==id:
            c["name"]=input("Enter your name:")
            c["email"]=input("Enter your email:")
            return

    print("Students Not found!")


while True:
    print("\n---- STUDENT MANAGEMENT SYSTEM ----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_contract()
    elif choice == "2":
        read_contract()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid  choice")