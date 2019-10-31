result = [[1, 3], [4, 6], [7, 9]]
posiblePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
displayedGrid = [['-|', '-|', '-', '\t\t1|2|3'], ['-|', '-|', '-', '\t\t4|5|6'], ['-|', '-|', '-', '\t\t7|8|9']]

matrice = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


# player = 'X'
# player_target = "O"
currentPlayer = "X"
game_still_going = True

def GetPosition():
    position = int(input('Choose a position from 1 to 9: '))

    if position in posiblePositions:
        return SetColByIndex(position, currentPlayer)


def SwichTurn():
    global currentPlayer
    if currentPlayer == "O":
        currentPlayer = "X"
    else:
        currentPlayer = "O"

    return currentPlayer

def GridDisplay():
    # print(displayedGrid)
    for i in displayedGrid:
        for j in i:
            print(j, end='')
        print()
    print()


def GetColByIndex(position):
    for index, range_list in enumerate(result):
        start, end = range_list
        if position >= start and position <= end:
            return index, position - start
    return -1, -1


def SetColByIndex(position, player):
    index, position = GetColByIndex(position)
    if index == -1:
        print("This is a wrong position, enter a numer from 1 to 9")
        GetPosition()

    if matrice[index][position] is not None:
        print("this position already is busy, choose another one.")
        GetPosition()

    matrice[index][position] = player
    if position == 2:
        displayedGrid[index][position] = player
    else:
        displayedGrid[index][position] = player + '|'

def IsVertical(player):
    # x[0][0], x[1][0], x[2][0]
    # x[0][1], x[1][1], x[2][1]
    # x[0][2], x[1][2], x[2][2]

    vertical_col_1 = matrice[0][0], matrice[1][0], matrice[2][0]
    vertical_col_2 = matrice[0][1], matrice[1][1], matrice[2][1]
    vertical_col_3 = matrice[0][2], matrice[1][2], matrice[2][2]
    # print('column_1: {}\ncolumn_2: {}\ncolumn_3{}'.format(vertical_col_1, vertical_col_2, vertical_col_3))

    player_data = tuple([player for _ in range(3)])

    if player_data == vertical_col_1 or player_data == vertical_col_2 or player_data == vertical_col_3:
        return True
    return False


def IsHorizontal(player):
    # x[0][0], x[0][1], x[0][2]
    # x[1][0], x[1][0], x[1][0]
    # x[2][0], x[2][0], x[2][0]

    horizontal_row_1 = matrice[0][0], matrice[0][1], matrice[0][2]
    horizontal_row_2 = matrice[1][0], matrice[1][1], matrice[1][2]
    horizontal_row_3 = matrice[2][0], matrice[2][1], matrice[2][2]
    # print('row_1: {}\nrow_2: {}\nrow_3{}'.format(horizontal_row_1, horizontal_row_2, horizontal_row_3))

    player_data = tuple([player for _ in range(3)])

    if player_data == horizontal_row_1 or player_data == horizontal_row_2 or player_data == horizontal_row_3:
        return True
    return False


def IsDiagonal(player):
    # x[0][0], x[1][1], x[2][2]
    # x[0][2], x[1][1], x[2][0]

    diagonal_1 = matrice[0][0], matrice[1][1], matrice[2][2]
    diagonal_2 = matrice[0][2], matrice[1][1], matrice[2][0]
    # print('diagonal_1: {}\ndiagonal_2: {}'.format(diagonal_1, diagonal_2))
    player_data = tuple([player for _ in range(3)])

    if player_data == diagonal_1 or player_data == diagonal_2:
        return True
    return False

def IsTie():
    busyPosCounter = 0
    for row in matrice:
        for col in row:
            if col is not None:
                busyPosCounter += 1
    if busyPosCounter == 9:
        return True

# print(tuple(["O" for i in range(3)]))
def CheckWinner():
    global game_still_going
    if IsHorizontal(currentPlayer) or IsVertical(currentPlayer) or IsDiagonal(currentPlayer):
        GridDisplay()
        print("{}'s won.".format(currentPlayer))
        game_still_going = False
    else:
        if IsTie():
            GridDisplay()
            print('Is tie.')
            game_still_going = False

while game_still_going:
    GridDisplay()
    print("Is {}'s turn.".format(currentPlayer))
    GetPosition()
    CheckWinner()
    SwichTurn()
