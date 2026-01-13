employee =[]

def create_employee():

    name=str(input("Enter employee name: "))
    age=int(input("Enter employee age: "))
    emp_id=int(input("Enter employee id: "))

    employee.append({'name':name,'age':age,'emp_id':emp_id})
    print('employee data created')

def read_employee():
    if not  employee:
        print('employee not exist')
        return
    for emp in employee:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Emp_id: {emp['emp_id']}")

def update_employee():
    name_to_update=input('enter employee name to update:')
    for emp in employee:
        if emp['name'] == name_to_update:
            emp['name'] = input("Enter new name: ")
            emp['age'] = input("Enter new age: ")
            emp['emp_id'] = input("Enter new employee id: ")
            print("Employee updated successfully!\n")
            return
    print("Employee not found.\n")

def menu():
    while True:
        print("Employee Management System ")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employee()
        elif choice == "3":
            update_employee()

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")



menu()


