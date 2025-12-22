import math

def add(input1, input2):
    return input1 + input2

def subtract(input1, input2):
    return input1 - input2

def multiply(input1, input2):
    return input1 * input2

def divide(input1, input2):
    return input1 / input2

def power(input1, input2):
    return input1 ** input2

def root(input1, input2):
    return input1 ** (1 / input2)

print("1. ADD\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Root\n")
while True:
    operation = input("Choose your operation [1,2,3,4,5,6]: ")

    if operation in ['1','2','3','4','5','6']:
        try:
         while True:
            a = float(input("Enter first number: "))
            if a < 0:
                print("invalid!Enter positive number ")
                continue
            break
         if operation != 6:
                b = float(input("Enter second number: "))
                if b<0:
                    print("invalid!Enter positive number")
                    continue
        except ValueError:
            print("Error: Provide valid number")
            continue

        if operation == '1':
            print(f"Result: {add(a, b):.2f}")
        elif operation == '2':
            print(f"Result:, {subtract(a, b):.2f}")
        elif operation == '3':
            print(f"Result: {multiply(a, b):.2f}")
        elif operation == '4':
            print(f"Result: {divide(a, b):.2f}")
        elif operation == '5':
            print(f"Result: {power(a, b):.2f}")
        elif operation == '6':
            print(f"Result: {root(a, b):.2f}")
    else:
        print("Invalid operation. Choose from 1-6.")
        continue

    again = input("Calculate again? (yes/no): ")
    if again == 'no':
        break
