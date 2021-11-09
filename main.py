x = input("Podaj pierwsza liczbe do przedzialu: ")
y = input("Podaj druga liczbe do przedzialu: ")

x = int(x)
y = int(y)

print(f'({x},{y})')
print("===============")

wieksza = max(x,y) #48
mniejsza = min(x,y) #7

if(wieksza != (int(mniejsza)*int(wieksza/mniejsza))):
    razy = int(wieksza/mniejsza) 
    mnozona = int(mniejsza) 
    calosc = int(wieksza/mniejsza)*int(mniejsza)
    reszta = int(wieksza-calosc) 
    print(f'{wieksza} = {razy} * {mnozona} + {reszta}') 
    while(reszta != 0):
        wieksza = mnozona
        razy = int(wieksza/reszta)
        mnozona = reszta
        reszta = wieksza-razy*mnozona
        print(f'{wieksza} = {razy} * {mnozona} + {reszta}')
    print(mnozona)
else:
    print(mniejsza)

print("~~~~~~~~~~~~~~~~~")

while(x!=y):
    if(x>y):
        x=x-y
        print(x)
    else:
        y=y-x
        print(y)
print(f'{x} - {y}')