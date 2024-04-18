# Funções do Jogo

def Nave_Principal(coluna, chave):
    coluna[23][chave] = '   /\\    '
    coluna[24][chave] = '  /__\\   '
    return


def tiros(coluna, tiro, chave, meteo, rodada, acerta):
    rodada = rodada // 2
    if tiro != 0:
        if chave != meteo:
            for c in range(22, -1, -1):
                coluna[c][chave] = '   o     '
        elif chave == meteo:
            for c in range(22, rodada, -1):
                coluna[c][chave] = '   o     '
            acerta = 1
    return tiro, chave, meteo, acerta


def meteoros(coluna, linha, meteo, rodada, acerta, pontuacao, aster):
    novo = rodada
    rodada = rodada // 2  #redução para a cada 50 loops o meteoro terminar de cair
    if acerta == 0:
        coluna[rodada][meteo] = '   ***   '
        if rodada > 1:
            coluna[rodada - 1][meteo] = '  *****  '
        if rodada > 2:
            coluna[rodada - 2][meteo] = ' ******* '
        if rodada > 3:
            coluna[rodada - 3][meteo] = '  *****  '
        if rodada > 4:
            coluna[rodada - 4][meteo] = '   ***   '
            if (rodada - 5) == 19:
                aster -= 0.5
    elif acerta == 1:
        for i in range(25):
            for j in range(8):
                linha.append('         ')
            coluna.append(linha)
            novo = 49
        pontuacao += 100
    return meteo, novo, acerta, pontuacao, aster


def Pontuacao_tempo_real(coluna, chave, pontuacao, aster):
    #recordes
    coluna[5][7] = 'PONTUAÇÃO'
    coluna[6][7] = pontuacao
    coluna[8][7] = 'ASTEROIDS'
    coluna[9][7] = round(aster)
    return


def Bater_meteoro(coluna, chave, aster):
    if coluna[22][chave] == '   ***   ' or coluna[22][
            chave] == '  *****  ' or coluna[22][chave] == ' ******* ':
        aster = 0
    return aster


def Tela_de_jogo(coluna):
    for i in range(25):
        for j in range(8):
            print('%s' % coluna[i][j], end='')
        print()
