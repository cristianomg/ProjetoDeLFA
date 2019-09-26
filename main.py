import json
from automato import Automato
def main ():
    with open('automato.json') as f:
        data = json.load(f)

    alfabeto = data["alfabeto"]
    listaTransicoes = data["listaTransicoes"]
    estadoInicial = data["estadoInicial"]
    estadoFinal = data["estadoFinal"]
    automato = Automato(alfabeto, listaTransicoes, estadoInicial, estadoFinal)

    automato.createAutomato()
    automato.testarAutomato("abbaababbbbbb")




if __name__ =="__main__":
    main()
