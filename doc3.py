#Aluno aprovavado ou reprovado?
N1 = float(input("1a. nota: "))
N2 = float(input("2a. nota: "))
N3 = float(input("3a. nota: "))
N4 = float(input("4a. nota: "))

#Calculo da media final...
MEDIA = (N1 + N2 + N3 + N4)/4

#Verificação se aprovavado ou não...
if MEDIA >= 6:
    print("Estudante aprovado!")
else:
    print("Estudante reprovado!")
print("A media dele é:",MEDIA)

    
