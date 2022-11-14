from random import randint

naval_player = []
class boat:
    def __init__(self, l, c, player):
        self.l = l - 1
        self.c = c - 1
        if player:
            self.tab = naval_player
        else:
            self.tab = naval_bot
    def submarino(self, sentido):
        self.s = sentido
        if self.s == 1: 
            if size_tab - self.l <= 3 or self.c >= size_tab or self.c < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c": 
                    return True
                else:
                    self.tab[self.l][self.c] = '🛶'
                    self.tab[self.l + 1][self.c] = '🛶'
                    self.tab[self.l + 2][self.c] = '🛶' 
                    return False              
        else:
            if size_tab - self.c <= 3 or self.l >= size_tab or self.l < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c":
                    return True
                else:
                    self.tab[self.l][self.c] = '🛶'
                    self.tab[self.l][self.c + 1] = '🛶'  
                    self.tab[self.l][self.c + 2] = '🛶'  
                    return False
    def patrulha(self, sentido):
        self.s = sentido
        if self.s == 1: 
            if size_tab - self.l <= 2 or self.c >= size_tab or self.c < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c": 
                    return True
                else:
                    self.tab[self.l][self.c] = '🚣'
                    self.tab[self.l + 1][self.c] = '🚣'  
                    return False              
        else:
            if size_tab - self.c <= 2 or self.l >= size_tab or self.l < 0:
                return True
            else:
                if self.tab[self.l][self.c] != self.tab[self.l][self.c + 1]:
                    return True
                else:
                    self.tab[self.l][self.c] = '🚣'
                    self.tab[self.l][self.c + 1] = '🚣'  
                    return False
    def destroyer(self, sentido):
        self.s = sentido
        if self.s == 1: 
            if size_tab - self.l <= 3 or self.c >= size_tab or self.c < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c": 
                    return True
                else:
                    self.tab[self.l][self.c] = '⛵'
                    self.tab[self.l + 1][self.c] = '⛵'
                    self.tab[self.l + 2][self.c] = '⛵' 
                    return False              
        else:
            if size_tab - self.c <= 3 or self.l >= size_tab or self.l < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c":
                    return True
                else:
                    self.tab[self.l][self.c] = '⛵'
                    self.tab[self.l][self.c + 1] = '⛵'  
                    self.tab[self.l][self.c + 2] = '⛵'  
                    return False
    def battleship(self, sentido):
        self.s = sentido
        if self.s == 1: 
            if size_tab - self.l <= 4 or self.c >= size_tab or self.c < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c": 
                    return True
                else:
                    self.tab[self.l][self.c] = '🚤'
                    self.tab[self.l + 1][self.c] = '🚤'
                    self.tab[self.l + 2][self.c] = '🚤'
                    self.tab[self.l + 3][self.c] = '🚤'
                    return False              
        else:
            if size_tab - self.c <= 4 or self.l >= size_tab or self.l < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c":
                    return True
                else:
                    self.tab[self.l][self.c] = '🚤'
                    self.tab[self.l][self.c + 1] = '🚤' 
                    self.tab[self.l][self.c + 2] = '🚤'
                    self.tab[self.l][self.c + 3] = '🚤'
                    return False
    def Aircraft(self, sentido):
        self.s = sentido
        if self.s == 1: 
            if size_tab - self.l <= 5 or self.c >= size_tab or self.c < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c": 
                    return True
                else:
                    self.tab[self.l][self.c] = '🚢'
                    self.tab[self.l + 1][self.c] = '🚢'
                    self.tab[self.l + 2][self.c] = '🚢'
                    self.tab[self.l + 3][self.c] = '🚢'
                    self.tab[self.l + 4][self.c] = '🚢'
                    return False              
        else:
            if size_tab - self.c <= 4 or self.l >= size_tab or self.l < 0:
                return True
            else:
                if self.tab[self.l][self.c] != "\u2b1c" or self.tab[self.l + 1][self.c] != "\u2b1c" or self.tab[self.l + 2][self.c] != "\u2b1c":
                    return True
                else:
                    self.tab[self.l][self.c] = '🚢'
                    self.tab[self.l][self.c + 1] = '🚢'  
                    self.tab[self.l][self.c + 2] = '🚢'
                    self.tab[self.l][self.c + 3] = '🚢'
                    self.tab[self.l][self.c + 4] = '🚢'
                    return False       

def cria_tab():
    l = []
    for i in range(40):
        #l.append(0)
        l.append("\u2b1c") #quadrado branco "nos vamos usar esse"
        #l.append("\u25FD") quadrado pequeno
        #l.append("\u25A1") quadrado bem queno
        #l.append(u"\u2b1b") quadrado preto
        #l.append(u"\U0001F7E5") quadrado vermelho
    for i in range(40):
        naval_player.append(l[:])

naval_bot = []
def cria_tab_bot():
    l = []
    for i in range(40):
        l.append('\u2b1c')
    for i in range(40):
        naval_bot.append(l[:])

naval_botF = []
def cria_bot_fake():
    l = []
    for i in range(40):
        l.append(u"\u2b1b")
    for i in range(40):
        naval_botF.append(l[:])

cria_tab()
cria_bot_fake()
cria_tab_bot()
size_tab = len(naval_player)

Boats = ["submarino[1]🛶","barco de patrulha[2]🚣", "destroyer[3]⛵","encouraçado[4]🚤", "porta-aviões[5]🚢"]

def print_tab():
    print("   Seu tabuleiro                                                                           Tabuleiro do Inimigo")
    for a in range(40):
        if a < 9:
            print(a + 1, end=' ')
        else:
            print(a + 1, end='')
        for i in range(40):
            if i == 39:
                print(naval_player[a][i], end=' | ')
            else:
                print(naval_player[a][i], end='')
        j = 0
        if i == 39 and j < 39:
            for j in range(40):
                if j == 39:
                    print(naval_botF[a][j],a + 1)
                else:
                    print(naval_botF[a][j], end='')
            
def player_position():
    print(f"Escolha qual barco você quer posicionar")
    for x in range(len(Boats)): 
        print(Boats[x])
        if x == 0:
            s = int(input("Escolha se você quer seu barco na Vertical(1) ou Horizontal(2): ")) 
            while s > 2:                         
                print("Digite 1 ou 2")
                s = int(input("Vertical(1) ou Horizontal(2): "))
            print("Digite a Coluna e a linha e coluna que você quer posicionar o barco")
            c = int(input("Coluna: "))
            l = int(input("Linha: "))
            sub = boat(l, c, True)
            after = 0
            while sub.submarino(s):
                if after > 0:
                    print("Casa ocupada ou posição invalida")
                    while s > 2: s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    c = int(input("Coluna: "))
                    l = int(input("Linha: "))                      
                    sub = boat(l, c, True)
                after = 1
            print_tab()
        elif x == 1: 
            s = int(input("Escolha se você quer seu barco na Vertical(1) ou Horizontal(2): ")) 
            while s > 2:                         
                print("Digite 1 ou 2")
                s = int(input("Vertical(1) ou Horizontal(2): "))
            c = int(input("Coluna: "))
            l = int(input("Linha: "))
            patrulha = boat(l, c, True)
            after = 0
            while patrulha.patrulha(s):
                if after > 0:
                    print("Casa ocupada ou posição invalida")
                    s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    while s > 2: 
                        print("Digite 1 ou 2")
                        s = int(input("Vertical(1) ou Horizontal(2): "))
                    c = int(input("Coluna: "))
                    l = int(input("Linha: "))                      
                    patrulha = boat(l, c, True)
                after = 1
            print_tab()
        elif x == 2:
            s = int(input("Escolha se você quer seu barco na Vertical(1) ou Horizontal(2): ")) 
            while s > 2:                         
                print("Digite 1 ou 2")
                s = int(input("Vertical(1) ou Horizontal(2): "))
            print("Digite a Coluna e a linha e coluna que você quer posicionar o barco")
            c = int(input("Coluna: "))
            l = int(input("Linha: "))
            destroyer = boat(l, c, True)
            after = 0
            while destroyer.destroyer(s):
                if after > 0:
                    print("Casa ocupada ou posição invalida")
                    s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    while s > 2: s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    c = int(input("Coluna: "))
                    l = int(input("Linha: "))                      
                    destroyer = boat(l, c, True)
                after = 1
            print_tab()
        elif x == 3:
            s = int(input("Escolha se você quer seu barco na Vertical(1) ou Horizontal(2): ")) 
            while s > 2:                         
                print("Digite 1 ou 2")
                s = int(input("Vertical(1) ou Horizontal(2): "))
            print("Digite a Coluna e a linha e coluna que você quer posicionar o barco")
            c = int(input("Coluna: "))
            l = int(input("Linha: "))
            battle = boat(l, c, True)
            after = 0
            while battle.battleship(s):
                if after > 0:
                    print("Casa ocupada ou posição invalida")
                    s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    while s > 2: s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    c = int(input("Coluna: "))
                    l = int(input("Linha: "))                      
                    battle = boat(l, c, True)
                after = 1
            print_tab()
        elif x == 4:
            s = int(input("Escolha se você quer seu barco na Vertical(1) ou Horizontal(2): ")) 
            while s > 2:                         
                print("Digite 1 ou 2")
                s = int(input("Vertical(1) ou Horizontal(2): "))
            print("Digite a Coluna e a linha e coluna que você quer posicionar o barco")
            c = int(input("Coluna: "))
            l = int(input("Linha: "))
            air = boat(l, c, True)
            after = 0
            while air.Aircraft(s):
                if after > 0:
                    print("Casa ocupada ou posição invalida")
                    while s > 2: s = int(input("Escolha se você quer seu barco na vertical(1) ou Horizontal(2): "))
                    c = int(input("Coluna: "))
                    l = int(input("Linha: "))                      
                    air = boat(l, c, True)
                after = 1
            print_tab()

def bot_position():
    for i in range(len(Boats)):
        if i == 0: 
            sub = boat(randint(1,40), randint(1,40), False)
            while sub.submarino(randint(1,2)): #8, 3 / 20, 25 / 22, 32 / 1, 14 / 23, 25
                sub = boat(randint(1,40), randint(1,40), False)
        elif i == 1:
            patrulha = boat(randint(1,40), randint(1,40), False)
            while patrulha.patrulha(randint(1,2)):
                patrulha = boat(randint(1,40), randint(1,40), False)
        elif i == 2:
            destroyer = boat(randint(1,40), randint(1,40), False)
            while destroyer.destroyer(randint(1,2)):
                destroyer = boat(randint(1,40), randint(1,40), False)
        elif i == 3:
            battle = boat(randint(1,40), randint(1,40), False)
            while battle.battleship(randint(1,2)):
                battle = boat(randint(1,40), randint(1,40), False)
        else:
            air = boat(randint(1,40), randint(1,40), False)
            while air.Aircraft(randint(1,2)):
                air = boat(randint(1,40), randint(1,40), False)
    print((sub.l, sub.c), (patrulha.l, patrulha.c), (destroyer.l, destroyer.c), (battle.l, battle.c), (air.l, air.c))    
def attack(l, c, tab, tab_f):
    l = l - 1
    c = c - 1
    target = tab[l][c]
    tab_f[l][c] = u"\U0001F7E5"
    print_tab()
    if target == '\u2b1c':
        return False
    else:   
        return True
    
print_tab()

player_position()

bot_position()

def bot_attack(acertosp,acertosb):
    acertosplayer = acertosp
    acertosbot = acertosb
    if attack(randint(1,40), randint(1, 40), naval_player, naval_player):
        bot_attack(acertosplayer, acertosbot)
    else:
        player_attack(acertosplayer, acertosbot)

def player_attack(acertosp,acertosb):
    acertosplayer = acertosp
    acertosbot = acertosb
    l = int(input("Digite a Linha que você quer atacar: "))
    while l > 40: l = int(input("Digite a Linha que você quer atacar: "))
    c = int(input("Digite a Coluna que você quer atacar: "))
    while c > 40:
        c = int(input("Digite a Coluna que você quer atacar: "))
    print(f"Você acertou um {naval_player[l][c]}") 
    if attack(l, c, naval_bot, naval_botF):
        acertosplayer =+ 1
        player_attack(acertosplayer, acertosbot)
    else:
        print("Tiro na água")
        bot_attack(acertosplayer, acertosbot)

player_attack(0,0)
