# ProjetoDeLFA
Implementação de um automato finito deterministico 

## Proposta

A proposta do projeto é criar uma implementação de automato onde o usuario deve cadastrar um automato finito deterministico indicando os estados, transições de cada estado e estados finais e inicial

Alem do cadastro o usuário podera testar se uma palavra pertence ao automato cadastrado, 
Verificar os estados equivalentes a partir do metodo de minimização.

O cadastro do automato foi feito por meio de um json representado pelo seguinte:

```json

{
    "alfabeto":["a","b"],
    "listaTransicoes":{"q1": {"a":"q2", "b": "q3"}, "q2": {"a":"q1", "b":"q2"}, "q3": {"a":"q3","b":"q3"} },
    "estadoInicial":"q1",
    "estadoFinal":"q3"
    

}
```

## Metodos
A classe principal do projeto é a denominada automato, nela constam todos os metodos de criação, teste, e minimização do automato

A classe estado serve apenas pra abstrair os estados e guarda as transições que cada estado possui

Vamos aos metodos:
1. Classe Automato

    1. createAutomato() : 
        Esse metodo é responsavel pela criação dos objetos estados;
    2. recuperarEstadoPorNome() :
        Esse metodo retorna um Estado a partir do nome do mesmo;
    3. testPalavraAlfabeto() :
        Nesse metodo é feito um teste para verificar se todas as letras da palavra a ser testada estão presentes no alfabeto do automato;
    4. testarAutomato() :
        Nesse metodo é feito o teste para verificar se a palavra pertence ao conjunto de palavras do automato

2. Classe Estado
   
   1. mover() : 
        Esse metodo recebe como parametro uma letra da palavra e retorna o estado que a letra leva a partir do estado em que o metodo é chamado