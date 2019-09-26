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

    while True:
        print("1. - Testar Palavra")
        print("2. - Minimizar Automato")
        print("3. - Finalizar")
        opc = int(input("opcao: "))
        if opc == 1:
            palavra = input("Informe a palavra: ")
            automato.testarAutomato(palavra)
        elif opc == 2:
            automato.minimizacao()
        elif opc == 3:
            break
        else:
            print("Opção invalida")




if __name__ =="__main__":
    main()
