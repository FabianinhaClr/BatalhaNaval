Relatório, Jogo Batalha Naval

import random
Importa a função random que gera dados aleatórios, como o jogador irá jogar sozinho contra o computador, a função ajuda que a máquina espalhe de forma aleatória as embarcações.

linhas = 40
colunas = 40
ex_map = [0] * colunas
fix_mapa = ["\u2B1C"] * colunas
matriz = []
mapa = []
cont = 0
navio = 5
submarino = 7
porta_aviao = 3
cont_navio = 0
cont_sub = 0
cont_port = 0
Variáveis e seus recíprocos valores que serão usados.
O valor do fix_map é o código de um emoji.
ex_map, é o mapa que é exposto na primeira interação com o jogo, antes de começar.

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
As funções irão imprimir o mapa.
O loop irá criar o mapa também. O .append adiciona um item em uma lista. 

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
Os três loops(while) são para gerar de forma aleatória o local dos barco, o submarino e o porta navio.
Em determinada linha e coluna terá um deles. random.randint(0, linhas - 1) =
aleatoriamente(parâmetros da localização) 
matriz[lin][col] = 5  no mapa terá tantas coordenadas para este onjeto, nesse caso serão 5.

while True:
   print("Bem-vindo ao jogo de Batalha Naval! Este jogo foi feito exclusivamente por @Clara_Antonelo.")
   if input("Deseja jogar? ") in ["sim", "SIM", "S", "s", "Sim"]:
       print("OK, vamos lá... Estou empolgada com a sua presença! \n"
             "Irei começar explicando como funciona...")
       print("O mapa do nosso jogo tem tamanho fixo de 40x40, sabendo disto, escolha apenas linhas e colunas que estejam neste intervalo de números.")
       print("Valores do jogo:\n"
             "Acertar um Navio(N), recebe 1 pontinho. \n"
             "Acertar um Submarino(S), recebe 2 pontinho. \n"
             "Acertar um Porta-Avião(P) mostra que você não ta brincando de jogar e está com sorte, recebe 3 pontos.\n"
             "Acertar um Encouraçado(E) recebe 4 pontos."
             "Acertar um Barco Patrulha(P), é um perigo e raro de acontecer, você recebe 10 pontos.")
Menu e início do jogo. O if diz que se o jogador responder uma das coisas que estão entre o colchetes ele irá executar o jogo, se não ele irá parar e trará a mensagem de adeus:
else:
   print("Isto não é um adeus... volte sempre.")
   break

       jogador = input("Como deseja ser chamado durante as interações? ")
Está variavel recebe o valor que será o nome do jogador e irá interagir durante todo o jogo chamando o por este nome.

       def jogo(linha, coluna):
            jog = 0
            if matriz[linha - 1][coluna - 1] == 0:
                matriz[lin_jog - 1][col_jog-1] = "X"
                mapa[lin_jog - 1][col_jog - 1] = "X"
                print("Que pena, aqui não tem nada, você mirou na água!")
            elif matriz[linha - 1][coluna - 1] == 7:
                jog = jog + 1
                matriz[lin_jog - 1][col_jog - 1] = "N"
                mapa[lin_jog - 1][col_jog - 1] = "N"
                print("Eita, voê pegou em cheio um navio! Será que era o Titanic?")
            elif matriz[linha - 1][coluna - 1] == 5:
                jog = jog + 2
                matriz[lin_jog - 1][col_jog - 1] = "S"
                mapa[lin_jog - 1][col_jog - 1] = "S"
                print("Ouvi rumores que este submarino era da Marinha, cuidado!!")
            elif matriz[linha - 1][coluna - 1] == 3:
                jog = jog + 3
                matriz[lin_jog - 1][col_jog - 1] = "A"
                mapa[lin_jog - 1][col_jog - 1] = "A"
                print("Como você é bom neste jogo, Forças Aéreas mandou um abraço ja que você acertou um porta-avião!")
            elif matriz[linha - 1][coluna - 1] == 2:
                jog = jog + 4
                matriz[lin_jog - 1][col_jog - 4] = "E"
                mapa[lin_jog - 1][col_jog - 4] = "E"
                print("ENCOURAÇADO")
            elif matriz[linha - 1][coluna - 1] == 1:
                jog = jog + 10
                matriz[lin_jog - 1][col_jog - 4] = "P"
                mapa[lin_jog - 1][col_jog - 4] = "P"
                print("Barco de patrulha, não sei se foi uma boa ideia!!")
            elif matriz[lin_jog - 1][col_jog - 1] == "X":
                print("Essa posição já foi bombardeada alguma vez, tente novamente!")
            else:
                jog = jog + 0
            return (jog)
Esta função é responsável pela verificação das casas em que o jogador escolheu.
Se a matriz estiver vazia (0) ele adicionará “X”.
Se a matriz estiver com um navio (são 7 deles espalhados por isto matriz == 7) ele irá adicionar um “N”.
Se a matriz estiver com um submarino ( mesma lógica do navio, matriz == 5) ele irá adicionar “S”.
Se a matriz estiver com um porta-avião (mesma lógica, matriz == 3) ele irá adicionar um “A”.
E assim sucessivamente
A variável “jog” conta os pontos do jogador, e cada uma das embarcações contém um determinado valor, se ele for bombardeado o jogador terá tantos pontos.

p_jog123 = 0
contador_navio = 7
contador_port = 3
contador_sub = 5
contador_enc = 2
contador_pat = 1
Variáveis que contém o valor de cada elemento, p_jog(quantidade de pontos do jogador no início)
contador_navio ou sub ou port ou outros diz quantos elementos existem no jogo.

while True:
   print(f"{jogador} vamos lá!!")
   imprime_mapa(mapa, linhas)
   col_jog = int(input("Qual a coluna que você quer jogar? "))
   lin_jog = int(input("Qual a linha que você quer jogar? "))
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
   print(f"{jogador} você tem {p_jog123} pontos")
   print(f"Ainda existem {contador_navio} navio, {contador_port} porta-aviões, {contador_sub} submarinos, {contador_enc} encouraçados e {contador_pat} barco patrulha para você procurar ")
Este loop define o jogo em si, printa o nome do jogador e solicita o começo, imprime o mapa na tela, col_jog = coluna do jogo em que o jogador escolheu, lin_jog = linha para fechar a coordenada.
Jogador123 define que será um int(inteiro) a coordenada e irá somar a quantidade de elementos ainda não combardeados mais tarde. 
p_jog são os pontos, o p_jog será alterado toda vez que ouver um valor em jogador123, ele simaria no valor. pontos receberá pontos + jogador.
IF jogador123 == “.” se na coordenada ouver o determinado valor ele irá diminuir nos parâmetros dados de quantidade de elementos ainda não bombardeados. 
Printa o nome do jogador + a quantidade de pontos gerais, além de quantidade de navio, e demais.

