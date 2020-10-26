
# name = input('What is your name?\n')
# print('Hi, %s.' % name)

#Var izmantot, gan "", gan ''
print("Hello world!")
print('Hello world!', end='\n\n')

#Vienā līnijā
var1 = 'Hello'
var2 = "world"

print(var1, end=" ")
print(var2)

#1 veids
var1 = 'Hello'
var2 = "world"

print(var1 + ' ' + var2)

#2 veids
var1 = 'Hello'
var2 = " world"

print(var1 + var2)

#3 veids
var1 = 'Hello'
var2 = "world"

print(var1, var2)

#Teksta mainīgā lielums
print(len(var1))

#Piekļuve
print("var1[0]:", var1[0])
print("var1[1:5]: " + var1[1:5])

#Pēdējais burts
print(var2[-1])

#Viss līdz pēdējam burtam
print(var2[:-1])

#Pārbayde
print(var2)

#Viss ar soli 1
print(var2[::1])

#Viss ar soli 2
print(var2[::2])

#Apgriezt otrādāk
print(var2[::-1])

#Mainīgā maiņa
var1 = var1 + ', ' + "I'm glad to see you"
print(var1)

#Teksta reizināšana
print((var1 + ' ') * 3)

print(var2.upper())
print(var2.lower())
print(var1.split())
print(var1.split('o'))

#Vecākā formatēšanas metode
print("Mēs te - %s - kaut ko ieliksim" %'kaut kas')
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %('kaut kas', 'nu, vēl'))

x, y = 'kaut kas', 'nu, vēl'
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %(x, y))

x, y = 'kaut \tkas', 'nu, vēl'
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %(x, y))

#Jaunāka metode
print("Teksta ievietošana ar .format metodi: {}" .format ('Hey, Tev izdevās!'))

print('{0} {1}'.format('Hello', 'world'))
print('{1} {0}'.format('Hello', 'world'))
print('{1} {1}'.format('Hello', 'world'))

print('{a} {a}'.format(a='Hello', b='world'))

#f strings, python 3.6+
vards = "Saulcerīte"
print(f"Viņa teica, ka viņas vārds ir {vards}.")
