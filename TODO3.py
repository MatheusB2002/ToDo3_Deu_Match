# Comecei com a criação de duas listas:
# A "notasCand" é para que eu consiga futuramente comparar os valores já com o formato de inteiro.
# A "candiatos" que recebe Strings para futuramente serem imprimidas no formato que é pedido.
# Fiz essa separação para que eu consiga de forma prática comparar com as notas necessárias para ser aprovado
# e ainda assim conseguir imprimir no formato perfeito pedido.

notasCand = [[5,10,8,8],[10,7,7,8],[8,5,4,9],[2,2,2,1],[10,10,8,9]]
candidatos = ['Candidato 1: e5_t10_p8_s8','Candidato 2: e10_t7_p7_s8','Candidato 3: e8_t5_p4_s9','Candidato 4: e2_t2_p2_s1','Candidato 5: e10_t10_p8_s9',]
aprovados = []
contador = 1
numDoCand = 6
qtdCand = int(input("Digite o número de candidatos à ser cadastrados: "))
notasNecessarias = []


def adicaoDeCand( contador, qtdCand, numDoCand, notasCand, candidatos ):

# Função que adiciona valores em "notasCand" para comparar futuramente e também adiciona os candidatos
# com suas strings para futuramente imprimir os candidatos aprovados e suas strings no formato pedido na atividade. 
# Atribuí aqui um contador para conseguir limitar o while para repetir na quantidades desejadas que são inputadas 
# em "qtdCand" e Também outro contador para numerar os candidatos, organizando na lista "candidatos" da forma que é pedido.

    print('Selecione as notas do candidato com valores de 0 a 10')
    
    while contador <= qtdCand:

        e = int(input(f'Nota da entrevista do candidato {numDoCand}: '))
        
        t = int(input(f'Nota do teste teorico do candidato {numDoCand}: '))
        
        p = int(input(f'Nota do teste prático do candidato {numDoCand}: '))
        
        s = int(input(f'Nota da avaliação de soft skills do candidato {numDoCand}: '))
        

        notasCand.append([e,t,p,s])
        candidatos.append(f'Candidato {numDoCand}: e{e}_t{t}_p{p}_s{s}')
        contador += 1
        numDoCand += 1


def criterios():

# Armazenando critérios necessários para comparação com as notas dos candidatos com o uso do  
# método .append para colocar esses valores dentro da lista "notasNecessárias".

    criterioE = notasNecessarias.append(int(input(f'Digite a nota de corte da entrevista: ' )))
   
    criterioT = notasNecessarias.append(int(input(f'Digite a nota de corte do teste teorico: ')))
   
    criterioP = notasNecessarias.append(int(input(f'Digite a nota de corte do teste prático: ')))
    
    criterioS = notasNecessarias.append(int(input(f'Digite a nota de corte da avaliação de soft skills: ')))


def compara( notasCand, notasNecessarias, aprovados ):

#  Função com um contador em uma estrutura de repetição de comparação onde ela percorre a lista principal de 
# notas "notasCand", entra em cada uma de suas sublistas compara índice por índice com a lista "notasNecessarias". 
# Se o inteiro contido no índice da sublista for maior ou igual ao inteiro contidos no mesmo índice em "notasNecessarias"
# ele adiciona 1 ao contador, se o contador alcançar o valor 4 ao percorrer aquela sublista, a função adicionará em outra
# lista com os aprovados de nome "aprovados" o item da lista "candidatos" de mesmo índice da lista "notasCand". 

    for posicao, notas in enumerate(notasCand):
        count = 0
        for indice,valor in enumerate(notas):
            if valor >= notasNecessarias[indice]:
                count += 1
            if count == 4:
                aprovados.append(candidatos[posicao])

        
def devulgaAprov( aprovados ):

# esta função basicamente imprime de um a um os candidatos contidos em "aprovados".

    print('\n     Os candidatos que atendem à todos os critérios desejados são:     \n')
    [print(i) for i in aprovados]


# Chamada das funções:

adicaoDeCand(contador, qtdCand, numDoCand, notasCand, candidatos)
criterios()
compara(notasCand, notasNecessarias, aprovados)
devulgaAprov( aprovados )
