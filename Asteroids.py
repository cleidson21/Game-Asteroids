'''Autor: Cleidson Ramos de Carvalho
Componente Curricular: MI - Algoritmos I
Concluido em: 25/04/2021
Declaro que este código foi elaborado por mim de forma individual e não
contém nenhum trecho de código de outro colega ou de outro autor, tais
como provindos de livros e apostilas, e páginas ou documentos
eletrônicos da Internet. Qualquer trecho de código de outra autoria que
não a minha está destacado com uma citação para o autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para
fins de avaliação'''

# Programa Principal
from random import randint
from blessed import Terminal
from funcoes import Nave_Principal, tiros, meteoros, Pontuacao_tempo_real, Bater_meteoro, Tela_de_jogo

recorde1 = recorde2 = recorde3 = 0
nome1 = nome2 = nome3 = ' '
nivel = 0.1

term = Terminal()
print(f"{term.home}{term.white_on_black}{term.clear}")
print('\n\n              ASTERIODS\n')
menu_principal = input('[1] JOGAR\n[2] RECORDES\n[3] SOBRE\n[4] SAIR\n ')

while menu_principal != '4':

    if menu_principal == '1':  # Menu de opção "JOGAR"

        centro = 3
        tiro = volta = volta_nivel = pontuacao = acerta = 0
        contador_asteroides = 10
        aleatorio_meteoro = randint(0, 6)

        while True:

            with term.cbreak(), term.hidden_cursor():

                # Entrada do teclado com Blessed
                entrada = term.inkey(timeout=nivel)

                # Limpeza de tela
                print(term.clear)

                # Área do Jogo e Resete de funções na tela
                coluna = []
                for i in range(25):
                    linha = []
                    for j in range(8):
                        linha.append('         ')
                    coluna.append(linha)

                # Nave principal em posições na matriz_central
                Nave_Principal(coluna, centro)

                # função dos tiros da nave
                tiro, centro, aleatorio_meteoro, acerta = tiros(coluna, tiro, centro, aleatorio_meteoro, volta,
                                                                        acerta)

                # Função responsavel pela criação e eliminação do meteoro
                aleatorio_meteoro, volta, acerta, pontuacao, contador_asteroides = meteoros(coluna, linha, aleatorio_meteoro, volta, acerta, pontuacao, contador_asteroides)

                # resete do tiro a cada rodada
                tiro = 0
                acerta = 0
                # contador de Loops
                volta += 1
                # contador resposavel pelo aumento de dificuldade
                volta_nivel += 1

                # Pontuacao em tempo real na tela
                Pontuacao_tempo_real(coluna, centro, pontuacao, contador_asteroides)

                # Meteoro bater na nave
                contador_asteroides = Bater_meteoro(coluna, centro, contador_asteroides)

                # Saída do Game com as atualizações de acordo com as instruções
                Tela_de_jogo(coluna)

                # Aumento de dificuldade do game
                if volta_nivel % 300 == 0 and nivel >= 0.03:
                    nivel -= 0.01

                # Geração de meteoro a cada 50 loops
                if volta % 50 == 0:  
                    aleatorio_meteoro = randint(0, 6)
                    volta = 0

                # Direcional da nave para direita
                if entrada.name == 'KEY_RIGHT':
                    if centro < 6:
                        centro += 1
                # Direcional da nave para esquerda
                elif entrada.name == 'KEY_LEFT':
                    if centro > 0:
                        centro -= 1
                # Condicional para os tiros
                elif entrada == ' ':
                    tiro = 1
            # Condicional de Saída
            if entrada.name == 'KEY_ESCAPE':
                break
            # Sessão de gravação de Pontuação por derrota
            if contador_asteroides == 0: 

                print(term.clear)
                print('\n\n     GAME OVER!!!  \n\n')
                print(f'Pontuação: {pontuacao}')
                nome = input('Jogador -> ')
                recordes = pontuacao

                if recordes > recorde1:
                    recorde3 = recorde2
                    recorde2 = recorde1
                    recorde1 = recordes
                    nome3 = nome2
                    nome2 = nome1
                    nome1 = nome

                elif recordes > recorde2:
                    recorde3 = recorde2
                    recorde2 = recordes
                    nome3 = nome2
                    nome2 = nome

                elif recordes > recorde3:
                    recorde3 = recordes
                    nome3 = nome

                break

    elif menu_principal == '2': # Menu de opção "Recordes"

        print(term.clear)
        resposta = ' '
        while resposta != 'S':
            print('\n\n              RECORDES\n\n')
            print('Nº |      JOGADOR       |       RECORDE      \n')

            print(f'1º |{nome1:^20}|{recorde1:^20}')

            if recorde2 > 0:
                print(f'2º |{nome2:^20}|{recorde2:^20}')

            if recorde3 > 0:
                print(f'3º |{nome3:^20}|{recorde3:^20}')

            resposta = input('\n\n\n\nDeseja ir ao menu Principal? [S/N] ').upper()
            print(term.clear)


    elif menu_principal == '3':# Menu de opção "Sobre"
        resposta1 = ' '
        while resposta1 != 'S':
            print(term.clear)
            print('\n\n              SOBRE\n')
            print('''INSTRUÇÕES:\n\n- Objetivo:\n\n  A missão do jogo é destruir os meteoros que surgem aleatoriamente no 
topo da tela e destrui-lo antes que alcançe a base da tela ou antes que
acerte a nave. Para isso projeteis podem ser atirados para destrui-los,
aumentando a pontuação.\n\n- Movimentação: \n\n  As setas direcionais LEFT (<-) e RIGHT (->), movem a nave para esquerda
e para direita, respectivamente, podendo posicionar-se na direção do
meteoro antes de atirar.\n\n- Tiros:\n\n  Apertando a Barra de espaço, projeteis são lançados da posição atual da
nave para o top da tela e se encontrar alguns detrito no caminho ele o
destroi.\n\nAlém disso, a jogatina pode ser encerrada a qualquer momento pressionando
a tecla ESC.\n\n\nDESENVOLVEDOR:\n\nEste protótico do jogo ASTERIODS foi desenvolvido pelo estudante Cleidson
Ramos de Carvalho no 1º semestre do curso de Engenharia de Computação
como resultado do Problema 02 proposto pelo Professor Rafael Tosta Santos.''')
            resposta1 = input('\n\n\n\nDeseja ir ao menu Principal? [S/N] ').upper()

    print(term.clear)
    print('\n\n              ASTERIODS\n')
    menu_principal = input('[1] JOGAR\n[2] RECORDES\n[3] SOBRE\n[4] SAIR\n ')
