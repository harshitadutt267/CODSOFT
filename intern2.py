import math
def Add():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a+b
    return c
def Sub():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a-b
    return c
def Mul():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a*b
    return c
def Div():
    a=int(input("enter dividend"))
    b=int(input("enter divisor"))
    c=a/b
    return c
def po():
    a=int(input("enter base"))
    b=int(input("enter exponent"))
    c=a**b
    return c
def Sq():
    a=int(input("enter a number"))
    c=math.sqrt(a)
    
    return c
#while True:
print('MAIN MENU')
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
print('5.exponent')
print('6.square root')
while True:
    x=int(input('enter your choice'))
    match (x):
        case 1:
            z=Add()
            print('sum of two number is',z)
            print('_'*85)
        case 2:
            z=Sub()
            print('difference of two number is',z)
            print('_'*85)
        case 3:
            z=Mul()
            print('multilplicaton of two number is',z)
            print('_'*85)
        case 4:
            z=Div()
            print('quotient of two number is' ,z)
            print('_'*85)
        case 5:
            z=po()
            print('value is',z)
            print('_'*85)
        case 6:
            z=Sq()
            print('square root is',z)
            print('_'*85)
        
