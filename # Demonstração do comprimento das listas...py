print("Vou almoçar em um restaurante a quilo!")

ORIGINAL = ["arroz","feijão", "batata", "alface","frango"]
print("Eis,a minha comida:",ORIGINAL)
DERIVADA = ORIGINAL
print("Meu amigo irá comer também:", DERIVADA)

print("vou alterar  as opções sem ele ver...")
ORIGINAL.remove("arroz")
ORIGINAL.remove("feijão")
ORIGINAL.remove("alface")
ORIGINAL.remove("picanha")
ORIGINAL.remove("linguiça")

print("Amiguinho,me mostre o que você vai comer?")
print("Claro! Dá uma conferida", DERIVADA)