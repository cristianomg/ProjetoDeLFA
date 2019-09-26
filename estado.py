class Estado:
    def __init__(self, nome, alfabeto, funcaoTransicao, tipoDeEstado):
        self.nome = nome
        self.funcaoTransicao = funcaoTransicao
        self.alfabeto = alfabeto
        self.ehEstadoFinal = tipoDeEstado

    #a partir de uma letra movimenta para o proximo estado que a função de transição indica
    def mover(self, letra):   
        return self.funcaoTransicao[letra]

    def __str__(self):
        return self.nome

    def __rep__(self):
        return self.__str__()