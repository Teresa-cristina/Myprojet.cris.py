
print("Vou montar a marmita com 5 alimentos")
MARMITA = [ "feijão", "arroz", "legumes", "salada", "carne"]
print("Eis,a nossa recomendação:",MARMITA)

RESPOSTA = input("Quer montar uma marmita diferente(S/N)?")
if RESPOSTA == "S":
    for X in range(len (MARMITA)):
        print(f'Digite o {X+1} o. item cardápio:') 
        MARMITA[X] = input()
        print("A marmita montada foi:", MARMITA)
        print("Os três primeiros itens foram:", MARMITA[0:3])
        print("O último item da marmita foi:", MARMITA[-1])
    else:
        print("Ok. Você decide")    
    








