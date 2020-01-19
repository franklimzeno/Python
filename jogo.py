def gerarBaralho():
    import random
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['P', 'C', 'E', 'O']
    baralho = []
    for n in range(len(naipes)):
        for v in range(len(valores)):
            baralho.append(valores[v] + '  ' + naipes[n])

    random.shuffle(baralho)
    return baralho

def criarJogadores(numero):
    player = [[0]*5 for i in range(numero)]
    total = [0]*numero
    return player, total

def somaValor(vetor):
    valor = 0
    for i in range(5):
        if vetor[3][:2].strip() == 'J':
            valor = valor + 11
        elif vetor[3][:2].strip() == 'Q':
            valor = valor + 12
        elif vetor[3][:2].strip() == 'K':
            valor = valor + 13
        elif vetor[3][:2].strip() == 'A':
            valor = valor + 14
        else:
            valor = valor + int(vetor[3][:2])

    return valor

def encontrarVencedor(nu_jogadores, nu_rodadas, jogadores, score,cartas):
    historico = [[0]*nu_jogadores for i in range(nu_rodadas)]
    rodada = [0]*nu_rodadas

    for j in range(len(rodada)):
        for i in range(len(jogadores)):
            jogadores[i] = cartas[0:5]
            score[i] = somaValor(jogadores[i])
            del cartas[0:5]
            historico[j][i] = score[i]
    
    vetorizar = []
    
    for k in historico:
        for i in k:
            vetorizar.append(i)
    
    PontMax = max(vetorizar)
    JogVen = 0
    RodVen = 0
    for j in range(len(rodada)):
        for i in range(len(jogadores)):
            if historico[j][i] == PontMax:
                RodVen = j
                JogVen = i
    
    print('Jogador vencendor: '+str(JogVen+1)+' na rodada numero '+str(RodVen+1)+' com pontuacao de '+str(PontMax))

def Jogo():
    print('Entre com o numero de jogadores: ')
    qtd_jogadores = input()
    jogador, total = criarJogadores(int(qtd_jogadores))
    
    maxJogadas = 52/(int(qtd_jogadores)*5)
    baralho = gerarBaralho()
    
    if int(maxJogadas) < 2:
        print('A quanntidade de jogadores nao permite a quantidade minima de rodadas!')
    else:
        if maxJogadas > 4:
            print('Digite o numero de rodada que deseja de 2 a 4')
            rodadas = input()
            if int(rodadas) > 4:
                return print('Numero de rodadas invalidas')
            else:
                encontrarVencedor(int(qtd_jogadores), int(rodadas), jogador, total, baralho)
        else:
            print('Digite o numero de rodada que deseja de 2 a '+str(int(maxJogadas)))
            rodadas = input()
            if int(rodadas) > 4:
                return print('Numero de rodadas invalidas')
            else:
                encontrarVencedor(int(qtd_jogadores), int(rodadas), jogador, total, baralho)
   
 
if __name__ == '__main__':
    Jogo()