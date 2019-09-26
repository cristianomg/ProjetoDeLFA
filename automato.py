from estado import Estado
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
    
    def verificaSeEstadoFinal(self, estado):
        if estado in self.__fim:
            return True
        else:
            return False

    #cria todos os estados e seta as transições neles
    def createAutomato(self):
        for estado, funcaoTransicao in self.__listaTransicoes.items():
            newEstado = Estado(estado, self.__alfabeto, funcaoTransicao, self.verificaSeEstadoFinal(estado))
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
            if inicio.ehEstadoFinal:
                print("Palavra aprovada")
            else:
                print("Palavra recusada")
        else:
            print("A Palavra não pertence ao alfabeto do automato.")

    #cria uma matriz triangular com os estados do automato
    def criarMatrizTriangular(self):
        colunas = self.__estados.copy()[:-1]
        linhas = self.estados.copy()[1:]
        matriz = {}
        for x in colunas:
            linha = {}
            for y in linhas:
                linha.update({y.nome:None})
            matriz.update({x.nome:linha})
            linhas = linhas[1:]
        return matriz    
    #printa a matriz de minimização em forma de uma matriz triangular 
    def printarMatriz(self, matriz):
        colunas = self.__estados.copy()[:-1]
        linhas = self.estados.copy()[1:]
        impressao = []
        for j in linhas:
            linha = []
            for x in matriz.values():
                for key, value in x.items():
                    if j.nome == key:
                        linha.append(value)
            impressao.append(linha)
        print()
        for pos , item in enumerate(impressao):
            valores = "  ".join(item)
            print("{:^2}  {}".format(linhas[pos].nome, valores))
        colunas = " ".join(map(lambda x: x.nome, colunas))
        string = " "*3
        print("{:^3}{}".format(string, colunas))
    
    # minimiza o automato e retorna a matriz de minimização a qual mostra quais os estados equivalentes 
    def minimizacao(self):
        minimizacao = False
        matrizMinimizacao = self.criarMatrizTriangular()
        while minimizacao is False:
            minimizacao = True
            for coluna, linhas in matrizMinimizacao.items():
                for linha, valor in linhas.items():      
                    if valor == None:
                        listaTestes = []
                        testeColuna = self.recuperarEstadoPorNome(coluna)
                        testeLinha = self.recuperarEstadoPorNome(linha)
                        marcou = False
                        for x in self.__alfabeto:
                            testeColuna =  self.recuperarEstadoPorNome(testeColuna.mover(x))
                            testeLinha = self.recuperarEstadoPorNome(testeLinha.mover(x))
                            listaTestes.append((testeColuna, testeLinha))
                            if (testeColuna.ehEstadoFinal != testeLinha.ehEstadoFinal):
                                linhas[linha] = "X"
                                marcou = True
                                break
                            elif (testeColuna.ehEstadoFinal == True and testeLinha.ehEstadoFinal == True):
                                linhas[linha] = "Eq"
                                marcou = True
                                break
                        if not marcou:
                            linhas[linha] = listaTestes
                    elif type(valor) == list:
                        minimizacao = False
                        for pos, letra in enumerate(self.__alfabeto):
                            item = valor[pos]
                            testeColuna = self.recuperarEstadoPorNome(item[0].mover(letra))
                            testeLinha = self.recuperarEstadoPorNome(item[1].mover(letra))
                            if (testeColuna.ehEstadoFinal != testeLinha.ehEstadoFinal):
                                linhas[linha] = "X"
                                marcou = True
                                break
                            elif (testeColuna.ehEstadoFinal == True and testeLinha.ehEstadoFinal == True):
                                linhas[linha] = "Eq"
                                marcou = True
                                break
        self.printarMatriz(matrizMinimizacao)


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