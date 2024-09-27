ESTADO = input(" Rio, São Paulo, Minas (RJ / SP / MG)?")

match ESTADO: 
    case "RJ":
        CLUBE = input(("Flamengo,Fluminense,Vasco, Botafogo"))
        if CLUBE == "FLUMINENSE":
           print("Parabéns, você é feliz!")
    