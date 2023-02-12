numb1 = int(input("first number please:"))
numb2 = int(input("second number please:"))


def sum():
    return numb1 + numb2

def minus():
    result = numb1 - numb2
    if(result < 0):
        result = result * -1
    return result

def multiply():
    return numb1 * numb2

def division():
     return numb1 / numb2


print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

choose = int(input("what do you prefer?  "))

def eleccion(choose):
    if(choose == 1):
        print(sum())
    elif(choose == 2):
        print(minus())
    elif(choose == 3):
        print(multiply())
    elif(choose == 4):
        print(division())  
    else:
        print("please use an input valid")

eleccion(choose)

   