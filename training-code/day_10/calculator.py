
def add(n1,n2):
    return n1+n2

def subtraction(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

operactions = {
'+':add,
'-':subtraction,
'*':multiply,
'/':division
}
while True:
    num1 = int(input('enter the first value?:\n'))
    for symbols in operactions:
        print(symbols)
    operactions_symols = input('pickup an operation from the above line:\n')
    num2 = int(input('enter the second value?:\n'))
    caluculatin_function = operactions[operactions_symols]
    first_answer = caluculatin_function(num1,num2)
    print(f'{num1} {operactions_symols} {num2} = {first_answer}')
    continue_calculation = input("do yo want to continue? type 'yes' to contine or 'no' to exit:\n").lower()
    
    num3 = int(input('enter the new value?: \n'))
    caluculatin_function = operactions[operactions_symols]
    second_answer = caluculatin_function(first_answer,num3)
    print(f'{first_answer} {operactions_symols} {num3} = {second_answer}')
    continue_calculation = input("do yo want to continue? type 'yes' to contine or 'no' to exit:\n").lower()
    if continue_calculation != 'yes': 
       break
    

