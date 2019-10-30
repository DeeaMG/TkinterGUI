

class PlayGame:

    def __init__(self):
        self.matrice = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.result = [[1, 3], [4, 6], [7, 9]]

        self.SetPlayers()

    def SetPlayers(self):
        self.player = input('Choose witch player you want to be X/O: ')
        while self.player.upper() not in ['X', 'O']:
            self.player = input('Choose witch player you want to be X/O: ')

        if self.player == 'X':
            self.player_target = "O"
        else:
            self.player_target = "X"

    def GetColByIndex(self, position):
        for index, range_list in enumerate(self.result):
            start, end = range_list
            if position >= start and position <= end:
                return index, position - start
        return -1, -1

    def SetColByIndex(self, position, player):
        index, position = self.GetColByIndex(position)
        if index == -1:
            print("there's a wrong position, write from 1 to 9")
            return False

        if self.matrice[index][position] is not None:
            print("this position already is busy, choose another one.")
            return False

        self.matrice[index][position] = player
        return True

    # input...
    # if SetColByIndex(input_position, player):
    #    print("You succes blabla at position.")

    def IsVertical(self, player):
        # x[0][0], x[1][0], x[2][0]
        # x[0][1], x[1][1], x[2][1]
        # x[0][2], x[1][2], x[2][2]

        vertical_col_1 = self.matrice[0][0], self.matrice[1][0], self.matrice[2][0]
        vertical_col_2 = self.matrice[0][1], self.matrice[1][1], self.matrice[2][1]
        vertical_col_3 = self.matrice[0][2], self.matrice[1][2], self.matrice[2][2]

        player_data = tuple([player for _ in range(3)])

        if player_data == vertical_col_1 or player_data == vertical_col_2 or player_data == vertical_col_3:
            return True
        return False

    def IsHorizontal(self, player):
        # x[0][0], x[0][1], x[0][2]
        # x[1][0], x[1][0], x[1][0]
        # x[2][0], x[2][0], x[2][0]

        horizontal_row_1 = self.matrice[0][0], self.matrice[0][1], self.matrice[0][2]
        horizontal_row_2 = self.matrice[1][0], self.matrice[1][0], self.matrice[1][0]
        horizontal_row_3 = self.matrice[2][0], self.matrice[2][0], self.matrice[2][0]

        player_data = tuple([player for _ in range(3)])

        if player_data == horizontal_row_1 or player_data == horizontal_row_2 or player_data == horizontal_row_3:
            return True
        return False

    def IsDiagonal(self, player):
        # x[0][0], x[1][1], x[2][2]
        # x[0][2], x[1][1], x[2][0]

        diagonal_1 = self.matrice[1][0], self.matrice[1][0], self.matrice[1][0]
        diagonal_2 = self.matrice[2][0], self.matrice[2][0], self.matrice[2][0]

        player_data = tuple([player for _ in range(3)])

        if player_data == diagonal_1 or player_data == diagonal_2:
            return True
        return False

    # print(tuple(["O" for i in range(3)]))


game = PlayGame()
