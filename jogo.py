
import random

linhas = 5
colunas = 5
ex_map = [0] * colunas
fix_mapa = ["\u2B1C"] * colunas
matriz = []
mapa = []
cont = 0
navio = 5
submarino = 7
porta_aviao = 3
encouracado = 2
patrulha = 1
cont_navio = 0
cont_sub = 0
cont_port = 0
cont_enc = 0
cont_pat = 0

def imprime_mapa(mat, L):
    cont = 0
    while cont < L:
        print(mat[cont])
        cont = cont + 1

while cont < linhas:
    matriz.append(ex_map.copy())
    mapa.append(fix_mapa.copy())
    print(matriz[cont])
    cont = cont + 1

while cont_navio < navio:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    matriz[lin][col] = 5
    cont_navio = cont_navio + 1

while cont_sub < submarino:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 1):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 7
    cont_sub = cont_sub + 1

while cont_port < porta_aviao:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 5) or (matriz[lin][col] == 7):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 3
    cont_port = cont_port + 1

while cont_enc < encouracado:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 5) or (matriz[lin][col] == 7) or (matriz[lin][col] == 3):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 2
    cont_enc = cont_enc + 1

while cont_pat < patrulha:
    lin = random.randint(0, linhas - 1)
    col = random.randint(0, colunas - 1)
    while (matriz[lin][col] == 5) or (matriz[lin][col] == 7) or (matriz[lin][col] == 3) or (matriz[lin][col] == 2):
        lin = random.randint(0, linhas - 1)
        col = random.randint(0, colunas - 1)
    matriz[lin][col] = 1
    cont_pat = cont_pat + 1

while True:
    print("Bem-vindo ao jogo de Batalha Naval! Este jogo foi feito exclusivamente por @Clara_Antonelo.")
    if input("Deseja jogar? ") in ["sim", "SIM", "S", "s", "Sim"]:
        print("OK, vamos l??... Estou empolgada com a sua presen??a! \n"
              "Irei come??ar explicando como funciona...")
        print("O mapa do nosso jogo tem tamanho fixo de 40x40, sabendo disto, escolha apenas linhas e colunas que estejam neste intervalo de n??meros.")
        print("Valores do jogo:\n"
              "Acertar um Navio(N), recebe 1 pontinho. \n"
              "Acertar um Submarino(S), recebe 2 pontinho. \n"
              "Acertar um Porta-Avi??o(P) mostra que voc?? n??o ta brincando de jogar e est?? com sorte, recebe 3 pontos.\n"
              "Acertar um Encoura??ado(E) recebe 4 pontos."
              "Acertar um Barco Patrulha(P), ?? um perigo e raro de acontecer, voc?? recebe 10 pontos.")

        jogador = input("Como deseja ser chamado durante as intera????es? ")

        def jogo(linha, coluna):
            jog = 0
            if matriz[linha - 1][coluna - 1] == 0:
                matriz[lin_jog - 1][col_jog-1] = "X"
                mapa[lin_jog - 1][col_jog - 1] = "X"
                print("Que pena, aqui n??o tem nada, voc?? mirou na ??gua!")
            elif matriz[linha - 1][coluna - 1] == 7:
                jog = jog + 1
                matriz[lin_jog - 1][col_jog - 1] = "N"
                mapa[lin_jog - 1][col_jog - 1] = "N"
                print("Eita, vo?? pegou em cheio um navio! Ser?? que era o Titanic?")
            elif matriz[linha - 1][coluna - 1] == 5:
                jog = jog + 2
                matriz[lin_jog - 1][col_jog - 1] = "S"
                mapa[lin_jog - 1][col_jog - 1] = "S"
                print("Ouvi rumores que este submarino era da Marinha, cuidado!!")
            elif matriz[linha - 1][coluna - 1] == 3:
                jog = jog + 3
                matriz[lin_jog - 1][col_jog - 1] = "A"
                mapa[lin_jog - 1][col_jog - 1] = "A"
                print("Como voc?? ?? bom neste jogo, For??as A??reas mandou um abra??o ja que voc?? acertou um porta-avi??o!")
            elif matriz[linha - 1][coluna - 1] == 2:
                jog = jog + 4
                matriz[lin_jog - 1][col_jog - 4] = "E"
                mapa[lin_jog - 1][col_jog - 4] = "E"
                print("ENCOURA??ADO")
            elif matriz[linha - 1][coluna - 1] == 1:
                jog = jog + 10
                matriz[lin_jog - 1][col_jog - 4] = "P"
                mapa[lin_jog - 1][col_jog - 4] = "P"
                print("Barco de patrulha, n??o sei se foi uma boa ideia!!")
            elif matriz[lin_jog - 1][col_jog - 1] == "X":
                print("Essa posi????o j?? foi bombardeada alguma vez, tente novamente!")
            else:
                jog = jog + 0
            return (jog)

        p_jog123 = 0
        contador_navio = 7
        contador_port = 3
        contador_sub = 5
        contador_enc = 2
        contador_pat = 1

        while True:
            print(f"{jogador} vamos l??!!")
            imprime_mapa(mapa, linhas)
            col_jog = int(input("Qual a coluna que voc?? quer jogar? "))
            lin_jog = int(input("Qual a linha que voc?? quer jogar? "))
            jogador123 = int(jogo(lin_jog, col_jog))
            matriz[lin_jog - 1][col_jog - 1] = "X"
            p_jog123 = p_jog123 + jogador123
            if jogador123 == 1:
                contador_navio = cont_navio - 1
            if jogador123 == 2:
                contador_sub -= 1
            if jogador123 == 3:
                contador_port -= 1
            if jogador123 == 4:
                contador_enc -= 1
            if jogador123 == 10:
                contador_pat -= 1
            print(f"{jogador} voc?? tem {p_jog123} pontos")
            print(f"Ainda existem {contador_navio} navio, {contador_port} porta-avi??es, {contador_sub} submarinos, {contador_enc} encoura??ados e {contador_pat} barco patrulha para voc?? procurar ")

    else:
        print("Isto n??o ?? um adeus... volte sempre.")
        break

