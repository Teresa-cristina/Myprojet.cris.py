# Solução do Eclipse solar...
HORA = input("Qual a hora de chegada?")
ESTADO = input("Qual é o estado (RJ/SP/MG/ES)? ")
DIA = input("O dia está claro(S/N)?")

if HORA == "15:25h" and ESTADO == "RJ" and DIA == "S":
 print("Eclipse total!")
elif HORA > "15:20h" and HORA> "13:30h":
  if ESTADO == "RJ" or ESTADO == "SP" or ESTADO == "MG" or ESTADO == "ES":
     if DIA == "S" :
        print("Eclipse Parcial!")
else:
    print("Não deu para ver o eclipse...")         





