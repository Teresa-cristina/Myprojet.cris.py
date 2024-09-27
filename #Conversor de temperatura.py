GRAU = int(input("Digite a temperatura:"))
SISTEMA = input("Celsius / Kelvin / Fahrenheit?")

if SISTEMA == "Celsius":
    # Criar as 2 fórmulas para converter em Kelvin e Fahrenheit...
    print("O valor em Celsius:", GRAU)
    print("A conversão para Kelvin:", KELVIN)
    print("A conversão para Fahrenheit", FAHRENHEIT)
elif SISTEMA == "Kelvin":
    # Criar as 2 fórmulas para converter em Celsius e Fahrenheit...
    print("O valor em Kelvin:", GRAU)
    print("A conversão para Celsius:", CELSIUS)
    print("A conversão para Fahrenheit:", FAHRENHEIT)
elif SISTEMA == "Fahrenheit":
    # Criar as 2 fórmulas para converter em Celsius e Kelvin...
    print("O valor em Fahrenheit:", GRAU)
    print("A conversão em Celsius:", CELSIUS)  
    print("A conversão para Kelvin:", KELVIN)
else:
    print("Sistema inexistente...")     