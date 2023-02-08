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

          candidatos.append(cand) 
          sair = input('Digite sim para continuar e não para sair: ')
          
>>Explicando o funciomaneto dessa estrutura: 
> 
