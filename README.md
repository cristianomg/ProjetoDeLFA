# ProjetoDeLFA
Implementação de um automato finito deterministico 

## Proposta

A proposta do projeto é criar uma implementação de automato onde o usuario deve cadastrar um automato finito deterministico indicando os estados, transições de cada estado e estados finais e inicial

Alem do cadastro o usuário podera testar se uma palavra pertence ao automato cadastrado, 
Verificar os estados equivalentes a partir do metodo de minimização.

O cadastro do automato foi feito por meio de um json representado pelo seguinte:

```json

{
    "alfabeto":["0","1"],
    "listaTransicoes":{"q0": {"0": "q1", "1": "q2"},
                       "q1": {"0": "q3", "1": "q4"},
                       "q2": {"0": "q3", "1": "q4"},
                       "q3": {"0": "q1", "1": "q4"},
                       "q4": {"0": "q4", "1": "q4"} },
                       
    "estadoInicial":"q0",
    "estadoFinal":["q4"]
    

}
```
Para configurar o automato, edite o arquivo automato.json

Para rodar o programa execute o arquvio main.py

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
    5. criarMatrizTriangular() : A partir os estados do automato o metodo gera uma matriz triangular onde as linhas possuem os vertices começando do segundo ate o ultimo e as colunas do primeiro ate o penultimo
    6. minimizacao() : Minimiza o automato e retorna a matriz de minimização a qual mostra quais os estados equivalentes 
    7. printarMatriz() : Printa a matriz de minimização em forma de uma matriz triangular. 
    8. MarcaEstadosNaoFinais : Marca na matriz os estados distinguintes dos estados finais a partir da palavra vazia
    9. Verifica se todos estados foram marcados com X ou com Eq e retorna True caso marcados

2. Classe Estado
   
   1. mover() : 
        Esse metodo recebe como parametro uma letra da palavra e retorna o estado que a letra leva a partir do estado em que o metodo é chamado