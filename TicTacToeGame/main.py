from time import sleep
from random import choice


class TicTacToeGame:
    startEndRowsList = [[1, 3], [4, 6], [7, 9]]
    posiblePositions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    MAX_ROW = 3
    MAX_COL = 3

    def __init__(self):
        self.game_still_going = True
        self.mainArray = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        self.displayedGrid = [
            ['-|', '-|', '-', '\t\t1|2|3'],
            ['-|', '-|', '-', '\t\t4|5|6'],
            ['-|', '-|', '-', '\t\t7|8|9']
        ]

        # Setting the players (you and the computer).
        self.player1 = input('Choose witch player you want to be X/O: ').upper()
        while self.player1 not in ['X', 'O']:
            self.player1 = input('Choose witch player you want to be X/O: ').upper()

        if self.player1 == 'X':
            self.playerComputer = "O"
            self.currentPlayer = self.player1
        else:
            self.playerComputer = "X"
            self.currentPlayer = self.playerComputer

    # Function so that the computer chooses a random position.
    def ComputerPosition(self):
        position = -1
        hasFound = False

        while not hasFound:
            random_index = choice(self.posiblePositions)
            row, col = self.GetColByIndex(random_index)
            if self.mainArray[row][col] is None:
                position = random_index
                hasFound = True

        return position

    # Get position from the current player(either player1 or playerComputer).
    def GetPosition(self):
        if self.currentPlayer == self.player1:
            position = input('Choose a position from 1 to 9: ')
            if position.isdigit():
                pos = int(position)
                if pos in self.posiblePositions:
                    self.SetColByIndex(pos, self.currentPlayer)
            else:
                self.GetPosition()

        elif self.currentPlayer == self.playerComputer:
            self.SetColByIndex(self.ComputerPosition(), self.currentPlayer)

    # Switch between players.
    def SwitchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.playerComputer
        else:
            self.currentPlayer = self.player1

    # Displays the empty grid, and next to it a grid with possible positions.
    def GridDisplay(self, newLine='\n'):
        result = ''
        for i in self.displayedGrid:
            for j in i:
                result += j
            result += newLine
        print(result)

    # Get's the row and the column from the position the player chose.
    def GetColByIndex(self, position):
        for index, range_list in enumerate(self.startEndRowsList):
            start, end = range_list
            if position >= start and position <= end:
                return index, position - start
        return -1, -1

    # Setting both in the mainArray and in the diplayedGrid the player, on the position he chose.
    def SetColByIndex(self, position, player):
        # Get's the row and the column from the GetColByIndex function based on the player chosen position.
        index, position = self.GetColByIndex(position)

        # If the position is not entered correctly ask's again for position.
        if player == self.player1 and index == -1:
            print("This is a wrong position, please choose one from 1 to 9")
            self.GetPosition()

        # If the position is already filled ask's again for position.
        elif player == self.player1 and self.mainArray[index][position]:
            print("This position is busy, choose another one.")
            self.GetPosition()

        else:
            self.mainArray[index][position] = player

            curString = self.displayedGrid[index][position]
            curString = curString.replace(curString[0], player)
            self.displayedGrid[index][position] = curString

    # Convert the player string into a 3rd list
    def GetPlayerDataTuple(self, player):
        return [player] * 3

    # Checks if is a winner on one of the columns.
    def IsVertical(self, player):
        vertical_cols = []
        for col in range(self.MAX_COL):
            vertical_cols.append([self.mainArray[row][col] for row in range(self.MAX_ROW)])
        return self.GetPlayerDataTuple(player) in vertical_cols

    # Checks if is a winner on one of the rows.
    def IsHorizontal(self, player):
        horizontal_rows = []
        for row in range(self.MAX_ROW):
            horizontal_rows.append([self.mainArray[row][col] for col in range(self.MAX_COL)])
        return self.GetPlayerDataTuple(player) in horizontal_rows

    # Checks if is a winner on one of the diagonals.
    def IsDiagonal(self, player):
        diagonal_1 = [self.mainArray[i][i] for i in range(3)]
        diagonal_2 = [self.mainArray[i][2 - i] for i in range(3)]

        player_data = self.GetPlayerDataTuple(player)
        return player_data == diagonal_1 or player_data == diagonal_2

    # Checks if is a tie between players, count the used slots.
    def IsTie(self):
        count = 0
        for row in self.mainArray:
            for col in row:
                if col:
                    count += 1
        return count == 9

    # Displays who the winner is (if is one) or if is tie and ends the game.
    def CheckWinner(self):
        if self.IsHorizontal(self.currentPlayer) or self.IsVertical(self.currentPlayer) or self.IsDiagonal(
                self.currentPlayer):
            self.GridDisplay()
            print("{} won.".format(self.currentPlayer))
            self.game_still_going = False
        else:
            if self.IsTie():
                self.GridDisplay()
                print('Is tie.')
                self.game_still_going = False

    def PlayGame(self):
        # Main loop.
        while self.game_still_going:
            self.GridDisplay()
            if self.currentPlayer == self.player1:
                print(
                    "_____________\n" +
                    "Is your turn.".format(self.currentPlayer) +
                    "\n_____________"
                )
            elif self.currentPlayer == self.playerComputer:
                result = "_____________\n" + "Is {}'s turn, wait".format(self.currentPlayer)
                print(result, end='')
                for i in range(3):
                    if i == 0:
						sleep(1)
                    print(".", end='')
                    sleep(1)
                print("\n_____________")
            self.GetPosition()
            self.CheckWinner()
            self.SwitchTurn()


game = TicTacToeGame()
game.PlayGame()
