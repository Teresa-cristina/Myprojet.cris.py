# Demonstração de operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã?")
print("Dormir / estudar / planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar/treinar/trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você precisa d que vai fazer!")
else:
    if MANHA == "dormir" or TARDE == "jogar":
        print("Você está disperdiçando seu dia!")
    elif MANHA =="estudar" or TARDE == "treinar":
        print("Que bom! Você irá se aperfeiçoar!") 
    elif MANHA =="planejar" and TARDE == "Trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinamos estas ações...")  

print("Tenha um bom dia!")          


















