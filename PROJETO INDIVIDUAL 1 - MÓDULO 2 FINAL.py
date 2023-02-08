'''

Aluno: Matheus Barbosa Furtado
SENAC - RESILIA - PROJETO INDIVIDUAL 1 DO MÓDULO 2:

Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
de um candidato com uma vaga de acordo com seu resultado nas etapas do
processo seletivo.

Para isso foi criado um teste que devolve uma string no seguinte formato:
eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em
uma das etapas do processo - entrevista, teste teórico, teste prático e
avaliação de soft skills).

Criar com Python uma lista para armazenar esses resultados
(e outros resultados que quiser no mesmo formato, o código
precisa funcionar para qualquer lista que seja inserida nesse
formato) e depois uma função que busca o candidato de
acordo com os critérios digitados pelo usuário.
'''


sair = 'sim' #Variavel sair, que será utilizada no comando de looping onde terá a função de criar um (stop), no looping sendo solicitado pelo usuário.

candidatos = [] #Lista vazia, onde seráo adicionados os nomes dos candidatos, e suas respectivas notas nos testes.

def cadastro_cand():

    sair = 'sim'  # Variavel sair, que será utilizada no comando de looping onde terá a função de criar um (stop), no looping sendo solicitado pelo usuário.

    while (sair == 'sim'): #Comando de looping que tem a função de cadastrar os candidatos,e sai assim que o usuário digita algo que não 'sim'.
        print('Digite o nome do candidato: ') #Primeiro print da sequência, pedindo ao usuário para digitar o nome do candidato.
        candidato = input() #aqui há uma variavel candidato, onde vai ser armazenados os nomes dos candidatos a partir do (input), e passado posteriormente para uma lista.
        print('Digite a nota da entrevista: ') #O segundo print, que pede a primeira nota da ENTREVISTA.
        ex = float(input()) #Aqui a primeira váriavel relacionadas as notas, que por sua vez será digitada pelo usuário a partir do (input)
        print('Digite a nota do teste teórico: ') #Print solicitando a nota do teste teórico, que será recebida pela váriavel embaixo.
        tx = float(input()) #A váriavel da nota do teste teórico, que é digitada pelo usuário a partir do (input).
        print('Digite a nota do teste prático: ') #Print com mensagem solicitando a nota do teste prático.
        px = float(input()) #Variavel que recebe a nota do teste prático, que será digitada pelo usuário a partir do (input)
        print('Digite a nota da avalição de soft skills') #Print com mensagem solicitando a nota da avaliação de soft skills.
        sx = float(input()) #Variavel que recebe a nota da avaliação de soft skills, a partir do (input)
        cand = [candidato,  ex, tx, px,sx] #Lista dentro do while, que são armazenados todos os dados solicitados acima, um de cada vez. Ou seja, a cada passagem do looping!

        candidatos.append(cand) #função de lista (append), pra adicionar todos os valores, que caem na lista (cand) com as informações dos candidatos e coloca esses valores, ao final da lista fora do while (candidatos).
        sair = input('Digite sim para continuar e não para sair: ') #variavel sair para ser modificada dentro do looping. Perguntando com (input), se o usuário deseja sair caso digite (sim), o loopíng é executado mais uma vez.

print('*'*50) #print apenas para organizar o código na hora da execução.



def avaliacao():

    print('*'*50) #print apenas para organizar o código na hora da execução.
    print('Digite a nota mínima da entrevista desejada para o candidato: ') #Print com mensagem solicitando a nota miníma desejada pelo avaliador, na entrevista.
    e1 = float(input()) #variavel que recebe a nota miníma desejada pelo avaliador, na entrevista a partir do (input)
    print('Digite a nota mínima do teste teórico desejada para o candidato: ') #Print com mensagem solicitando a nota miníma desejada pelo avaliador, no teste teórico.
    t1 = float(input())  #variavel que recebe a nota miníma desejada pelo avaliador, no teste teórico a partir do (input)
    print('Digite a nota mínima no teste prático desejada para o candidato: ') #Print com mensagem solicitando a nota miníma desejada pelo avaliador, no teste prático.
    p1 = float(input())  #variavel que recebe a nota miníma desejada pelo avaliador, no teste prático a partir do (input)
    print('Digite a nota mínima da avaliação de soft skills desejada para o candidato: ') #Print com mensagem solicitando a nota miníma desejada pelo avaliador, na avaliação de soft skills.
    s1 = float(input())  #variavel que recebe a nota miníma desejada pelo avaliador, na avaliação de soft skills a partir do (input)
    nota_minima = [e1, t1, p1, s1] #lista contendo todas as notas mínimas solicitadas pelo avaliador
    print('*'*50) #print apenas para organizar o código na hora da execução.

    for x in candidatos: #estrutura de repetição for, que busca os valores dentro da lista (candidatos) de um em um.
            # condicional (if), que faz testes para saber qual candidato tem notas equivalentes com as que o avaliador sugeriu como mínimas nos testes.
            if (float(x[1]) >= nota_minima[0]) and (float(x[2]) >= nota_minima[1]) and (float(x[3]) >= nota_minima[2]) and (float(x[4]) >= nota_minima[3]):
                print('*' * 50) #print apenas para organizar o código na hora da execução.
                print('o candidato que corresponde as especificações de notas desejadas é:', '\nnome: ',x[0].title(),'\nnotas: ', 'e' + str(x[1]) + '_' + 't' + str(x[2]) + '_' + 'p' + str(x[3]) + '_' + 's' + str(x[4]))
                #Print, que organiza uma mensagem dizendo o(s), candidatos com as respectivas notas solicitadas pelo avaliador.


cadastro_cand()
avaliacao()

























