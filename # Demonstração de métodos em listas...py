INSS = ["Maria", "Manoel", "José","Isabela"]
print("Eis, a fila do INSS:", INSS)

NOVO = input("Inpira mais uma pessoa:")
INSS.append(NOVO)
print("Conferindo a nova lista:", INSS)

print("Vou tirar a última pessoa desta lista...")
ESPECIAL = INSS.pop()

print("Agora, vou colocá-la na frente de todos!")
INSS.insert(0, ESPECIAL)
print("Conferindo a lista.", INSS)

print("Maria não gostou e reclamou...")
INSS.remove("Maria")
print("E agora,ela saiu 'pe da vida'", INSS)

print("Para não ter mais reclamações,vamos atender...")
INSS.sort()

print("Onde está nova pessoa chamada", ESPECIAL,"?")
print("Ela agora ficou na posição", INSS.index(ESPECIAL)+1,"!")