 #Avaliação de um filme e ou serie de TV...
print("Digite o nome do filme ou série:")
FILME = input()
print("A. Pessímo")
print("B. Ruim")
print("C. Razoável")
print("D. Bom")
print("E. Nenhuma das opções ")
NOTA = int(input())

match ESTADO:
    case "A":
        print("Péssimo")
    case "B":
        print("Ruim")
    case "c":
        print("Razoável")
    case "D":
        print("Bom")
    case "E":
        print("Nenhuma das opções")
    case _:
        print("Opção não reconhecida") 
        
            
        
