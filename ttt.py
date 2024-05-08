#SUPER TIC TAC TOE
a = [['_','_','_'],['_','_','_'],['_','_','_']]
b = [['_','_','_'],['_','_','_'],['_','_','_']]
c = [['_','_','_'],['_','_','_'],['_','_','_']]
d = [['_','_','_'],['_','_','_'],['_','_','_']]
e = [['_','_','_'],['_','_','_'],['_','_','_']]
f = [['_','_','_'],['_','_','_'],['_','_','_']]
g = [['_','_','_'],['_','_','_'],['_','_','_']]
h = [['_','_','_'],['_','_','_'],['_','_','_']]
i = [['_','_','_'],['_','_','_'],['_','_','_']]
game = [a,b,c,d,e,f,g,h,i]


def show():
    print("\n")
    print(a[0],'   ',b[0],'   ', c[0])
    print(a[1],'   ',b[1],'   ' ,c[1])
    print(a[2],'   ',b[2],'   ' ,c[2])
    print("\n")
    print(d[0],'   ',e[0],'   ',f[0])
    print(d[1],'   ',e[1],'   ',f[1])
    print(d[2],'   ',e[2],'   ',f[2])
    print("\n")
    print(g[0],'   ',h[0],'   ',i[0])
    print(g[1],'   ',h[1],'   ',i[1])
    print(g[2],'   ',h[2],'   ',i[2])


show()
turn = 1
flag = True
clear = True

def replace(player,block):
    global turn
    if 0 < select <= 3:
        block[0][select-1] = player
    elif 3 < select <= 6:
        block[1][select-4] = player
    elif 6 < select <= 9:
        block[2][select-7] = player
    else:
        print("not a valid position")
    show()


def won(player):
    if player == 'O':
        for i in range(3):
            for j in range(3):
                block[i][j] = '1'
        print(f"player 1 won this block")

    else:
        for i in range(3):
            for j in range(3):
                block[i][j] = '2'
        print(f"player 2 won this block")
    show()
def whole_win1():
    global block
        # column
    if (game[0][0][0] == game[3][0][1] == game[6][0][2] == '1') or (game[1][1][0] == game[4][1][1] ==game[7][1][2] == '1') or (game[2][2][0] == game[5][2][1] == game[8][2][2] == '1'):
        print("player 1 won the match")
        exit()
    #rows
    if (game[0][0][0] == game[1][0][1] == game[2][0][2] == '1') or (game[3][1][0] == game[4][1][1] ==game[5][1][2] == '1') or (game[6][2][0] == game[7][2][1] == game[8][2][2] == '1'):
        print("player 1 won the match")
        exit()
    #diagonals
    if (game[0][0][0] == game[4][1][1] == game[8][2][2] == '1') or (game[2][0][2] == game[4][1][1] == game[6][2][0] == '1'):
        print("player 1 won the match")
        exit()
def whole_win2():
    global block
    # column
    if (game[0][0][0] == game[3][0][1] == game[6][0][2] == '2') or (game[1][1][0] == game[4][1][1] == game[7][1][2] == '2') or (game[2][2][0] == game[5][2][1] == game[8][2][2] == '2'):
        print("player 2 won the match")
        exit()
    # rows
    if (game[0][0][0] == game[1][0][1] == game[2][0][2] == '2') or (game[3][1][0] == game[4][1][1] == game[5][1][2] == '2') or (game[6][2][0] == game[7][2][1] == game[8][2][2] == '2'):
        print("player 2 won the match")
        exit()
    # diagonals
    if (game[0][0][0] == game[4][1][1] == game[8][2][2] == '2') or (game[2][0][2] == game[4][1][1] == game[6][2][0] == '2'):
        print("player 2 won the match")
        exit()
def win(player, block):
    global turn,clear
    # checking for column
    for i in range(3):
        if block[0][i] == block[1][i] == block[2][i] == player:
            won(player=player)
            whole_win1()
            whole_win2()
    # checking for rows
    if (block[0][0] == block[0][1] == block[0][2] == player) or (block[1][0] == block[1][1] == block[1][2] == player) or (block[2][0] == block[2][1] == block[2][2] == player):
        won(player=player)
        whole_win1()
        whole_win2()
    # checking for diagonal
    if (block[0][0] == block[1][1] == block[2][2] == player) or (block[0][2] == block[1][1] == block[2][0] == player):
        won(player=player)
        whole_win1()
        whole_win2()


def block_selection(select):
    global block
    for i in range(9):
        if select == i + 1:
            block = game[i]


val = bool


def con(block):
    global val
    for i in range(3):
        if 0 < select <= 3:
            if block[i][select-1] == '_':
                val = True
            else:
                print("the position or the block is already taken")
                break
        elif 3 < select <= 6:
            if block[1][select - 4] == '_':
                val = True
            else:
                print("the position or the block is already taken")
                break
        elif 6 < select <= 9:
            if block[2][select - 7] == '_':
                val = True
            else:
                print("the position or the block is already taken")
                break
        return val

def check1(block):
    global select,clear
    if 0 < select <= 3:
        if block[0][select-1] == '1':
            print("this block is already taken")
            return clear == False
    elif 3 < select <= 6:
        if block[1][select-4] == '1':
            print("this block is already taken")
            return clear == False
    elif 6 < select <= 9:
        if block[2][select-7] == '1':
            print("this block is already taken")
            return clear == False
def check2(block):
    global select,clear
    if 0 < select <= 3:
        if block[0][select-1] == '2':
            print("this block is already taken")
            return clear == False
    elif 3 < select <= 6:
        if block[1][select-4] == '2':
            print("this block is already taken")
            return clear == False
    elif 6 < select <= 9:
        if block[2][select-7] == '2':
            print("this block is already taken")
            return clear == False

block = e
print("player 1 to play in block 5")
while flag:
    if turn % 2 != 0:
        select = int(input(f"player 1(O):position "))
        if con(block=block):
            replace(player='O', block=block)
            win(player='O', block=block)
            if check1(block=game[select-1])==False or check2(block=block)==False:
                fda = int(input("enter the block:"))
                block = game[fda - 1]
                select = int(input('enter the position:'))
                turn += 1
                print(f"player 2 to play in block {select}")
            else:
                block_selection(select=select)
                turn += 1
                print(f"player 2 to play in block {select}")


    else:
        select = int(input(f"player 2(X):position"))
        if con(block=block):
            replace(player='X', block=block)
            win(player='X', block=block)
            if check1(block=game[select-1])==False or check2(block=block)==False:
                fda = int(input("enter the position:"))
                block = game[fda - 1]
                select = int(input('enter the block:'))
                turn += 1
                print(f"player 1 to play in block {select}")
            else:
                block_selection(select=select)
                turn += 1
                print(f"player 1 to play in block {select}")
