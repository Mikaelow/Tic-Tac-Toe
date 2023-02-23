
def table():
    l1 = [' ', ' ', ' ']
    l2 = [' ', ' ', ' ']
    l3 = [' ', ' ', ' ']
    return [l1, l2, l3]

def resoults(my_table):
    for line in my_table:
        if line == ['X','X','X']:
            return True
        elif line == ['O','O','O']:
            return True
        else: pass
    for i in range(0,3):
        if my_table[0][i]=='X' and my_table[1][i]=='X' and my_table[2][i]=='X':
            return True
        elif my_table[0][i]=='O' and my_table[1][i]=='O' and my_table[2][i]=='O':
            return True
        else: pass
    if my_table[0][0] == 'X' and my_table[1][1] == 'X' and my_table[2][2] == 'X':
        return True
    elif my_table[0][0] == 'O' and my_table[1][1] == 'O' and my_table[2][2] == 'O':
        return True

def showingTable(my_table):
    for linia in my_table:
        print('|'.join(linia))



def choseOfPlayerA(my_table):
    while True:
        chose = list(input('Player A choose position '))
        a = int(chose[0])-1
        b = int(chose[1])-1
        if a in range(0, 3) and b in range(0, 3) and my_table[a][b] == ' ':
            my_table[a][b] = 'X'
            return False
        else: print('Wrong char')



def choseOfPlayerB(my_table):
    while True:
        chose = list(input('Player B choose position '))
        a = int(chose[0]) - 1
        b = int(chose[1]) - 1
        if a in range(0, 3) and b in range(0, 3) and my_table[a][b] == ' ':
            my_table[a][b] = 'O'
            return False
        else:
            print('Wrong')


def theGame():
    my_table = table()
    showingTable(my_table)
    while True:
        choseOfPlayerA(my_table)
        showingTable(my_table)
        if resoults(my_table)==True:
            print('Won player A')
            break
        choseOfPlayerB(my_table)
        showingTable(my_table)
        resoults(my_table)
        if resoults(my_table) == True:
            print('Won player B')
            break
# Check
theGame()
