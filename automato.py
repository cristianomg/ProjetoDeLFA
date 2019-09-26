from estado import Estado
from estadoMinimizacao import EstadoMinimizacao
class Automato:
    def __init__(self, alfabeto, listaTransicoes, inicio, fim):
        self.__estados = []
        self.__alfabeto = alfabeto
        self.__listaTransicoes = listaTransicoes
        self.__inicio = inicio
        self.__fim = [fim]

    @property
    def estados(self):
        return self.__estados
    #cria todos os estados e seta as transições neles
    def createAutomato(self):
        for estado, funcaoTransicao in self.__listaTransicoes.items():
            newEstado = Estado(estado, self.__alfabeto, funcaoTransicao)
            self.__estados.append(newEstado)

    #recupera o objeto estado a partir do nome 
    def recuperarEstadoPorNome(self, nome):
        for estado in self.__estados:
            if estado.nome == nome:
                return estado

    #testa se todas as letras da palavra estão entre as letras do alfabeto
    def testPalavraAlfabeto(self, listaPalavra):
        for x in listaPalavra:
            if x not in self.__alfabeto:
                return False
        return True

    #testa se a palavra pertence ao alfabeto do automato
    def testarAutomato(self, palavra):
        palavra = list(palavra)
        if self.testPalavraAlfabeto(palavra):
            inicio = self.recuperarEstadoPorNome(self.__inicio)
            estados = []
            estados.append(inicio.nome)
            for letra in palavra:
                inicio = self.recuperarEstadoPorNome(inicio.mover(letra))
                estados.append(inicio.nome)
            estados = "; ".join(estados)
            print("Estados utilizados pela palavra: " + estados)
            if inicio.nome in self.__fim:
                print("Palavra aprovada")
            else:
                print("Palavra recusada")
        else:
            print("A Palavra não pertence ao alfabeto do automato.")

    def criarMatrizTriangular(self):
        colunas = self.__estados.copy()[:-1]
        linhas = self.estados.copy()[1:]
        matriz = []
        for x in colunas:
            linha = {}
            for y in linhas:
                linha.update({y.nome:None})
            matriz.append({x.nome:linha})
            linhas = linhas[1:]
        for x in matriz:
            print(x)
        return matriz    

        #   for x in enumerate(self.__estados):


    #retorna a representaçaõ do automato
    def __str__(self):
        retorno = []
        for x, y in self.__listaTransicoes.items():
            var = x+":"+ str(y)
            retorno.append(var)
        retorno = "\n".join(retorno)
        return retorno
    
    def __repr__(self):
        return self.__str__()