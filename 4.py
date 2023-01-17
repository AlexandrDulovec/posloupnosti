num1=0
num2=1
x=input("KOLÍK ČÍSEL VYPSAT? (ZADÁNÍM LICHÉHO ČÍSLO BUDE VYPSÁNO O JEDNO NAVÍC)")
x=int(x)

if x%2==1:
    x=x+1

x=int(x/2)
for i in range(x):
    print(num1)
    num1=num1+num2
    print(num2)
    num2=num1+num2


input()
