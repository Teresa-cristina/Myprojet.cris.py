# Programa com três valores...
X = int(input("Digite o valor de X:"))
Y = int(input("Digite o valor de Y:"))
Z = int(input("Digite o valor de Z:"))

if X < Y and Y < Z:
    print("Em ordem crescente!")
elif X > Y and Y > Z:
    print("Em ordem decrescente!")
else:
    print("Todos misturados!")       
