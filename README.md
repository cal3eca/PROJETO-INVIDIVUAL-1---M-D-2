# PROJETO-INVIDIVUAL-1---M-D-2
Projeto individual do módulo 2 - SENAC - RESILIA

Esse repositório contem os arquivos que foram utilizados para a realização do projeto indivual 1, do módulo 2.
No curso de Analise de dados do Senac - Botafogo.

Criado por: Matheus Barbosa Furtado.
Data de criação : 07.02.2023

>####PROBLEMA DO PROJETO:
>
>> Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
de um candidato com uma vaga de acordo com seu resultado nas etapas do
processo seletivo.

>####RESOLUÇÃO:
>
>>Um programa que tentei fazer de maneira mais simples possível, utilizando poucas linhas para que ficasse bem clean.

>>O funcionamento do código, se dá no sentido de que: O usuário vai cadastrar os possíveis candidatos, a partir de um conjunto de perguntas feitas a esse usuário, digitando o (nome) do candidato e suas (notas) referente as avaliações. 
De início eu separei em defs as duas operações principais, contendo dentro da def as funções que dão funcionalidade ao código.

    def cadastro_cand():

          sair = 'sim' 

          while (sair == 'sim'):
              print('Digite o nome do candidato: ')
              candidato = input() 
              print('Digite a nota da entrevista: ') 
              ex = float(input()) 
              print('Digite a nota do teste teórico: ') 
              tx = float(input()) 
              print('Digite a nota do teste prático: ') 
              px = float(input())
              print('Digite a nota da avalição de soft skills')
              sx = float(input())
              cand = [candidato,  ex, tx, px,sx] 

              print(str(cand[0]),'e' +str(cand[1])+ '_' + 't' + str(cand[2]) + '_' + 'p' + str(cand[3]) + '_' + 's' +   str(cand[4]))
              candidatos.append(cand) 
              sair = input('Digite sim para continuar e não para sair: ')
          
>>Explicando o funciomaneto dessa estrutura: 
>>Começa com uma váriavel (sair), ja estipulada com a string (sim), para que comece o looping(while).
Em seguida começa o looping(while), dentro dele há 5 váriaveis referentes ao:
(nome do candidato, nota da entrevista, nota do teste teórico, nota do teste prático e nota da entrevista).
Após isso, todos esses dados que são digitados pelo usuário ficam salvos na lista (cand).
depois um print, para esse candidato, com suas respectivas notas no formato solicitado pelo projeto. (ex_tx_px_sx)
seguindo por uma adição a lista principal com (append), e por fim a variavel (sair), para verificar se o usuario quer continuar
cadastrando candidatos, ou se quer passar para a segunda etapa do projeto, a de busca.



>> Na segunda parte do projeto: Criei um menu de buscas para o avaliador.
Utilizando uma funçao def, para guardar todo esse processo que começa a partir de (prints)
solicitando ao avaliador, quais são as notas mínimas em cada etapa do processo seletivo.
salvando todas essas notas em váriaveis diferentes, e colocando em seguida tudo dentro de uma lista.
chamada (nota-minima)

      def avaliacao():

            print('*'*50) 
            print('Digite a nota mínima da entrevista desejada para o candidato: ')
            e1 = float(input()) 
            print('Digite a nota mínima do teste teórico desejada para o candidato: ')
            t1 = float(input()) 
            print('Digite a nota mínima no teste prático desejada para o candidato: ')
            p1 = float(input())
            print('Digite a nota mínima da avaliação de soft skills desejada para o candidato: ')
            s1 = float(input())
            nota_minima = [e1, t1, p1, s1]
            print('*'*50) 


>>Depois desse processo, utilizando o laço de repetição for, essa etapa busca dentro da lista de candidatos, cada valor dentro dela.
Em seguida, utilizando condicionais (if), são feitos testes, que comparam as notas dentro da lista (candidatos), com as notas dentro da lista (nota_minima), caso as notas dentro da primeira lista de candidatos, sejam maiores ou iguais, as solicitadas como mínimas pelo avaliador, o candidato é visto como "aprovado", e é exibido através de um (print) o nome dos candidato(s), aprovados no processo com suas notas.


          for x in candidatos:
                if (float(x[1]) >= nota_minima[0]) and (float(x[2]) >= nota_minima[1]) and (float(x[3]) >= nota_minima[2]) and (float(x[4]) >= nota_minima[3]):
                    print('*' * 50)
                    print('o candidato que corresponde as especificações de notas desejadas é:', '\nnome: ',x[0].title(),'\nnotas: ', 'e' + str(x[1]) + '_' + 't' +  str(x[2]) + '_' + 'p' + str(x[3]) + '_' + 's' + str(x[4]))

>>Para finalizar, como todo esse processos estão dentro de funções def, eu chamo essas funções para que o programa funcione!

      cadastro_cand()
      avaliacao()
