from time import sleep
from random import choice


class TicTacToeGame:
    START_END_ROWS_LIST = [[1, 3], [4, 6], [7, 9]]
    POSSIBLE_POSITIONS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
        self.SetPlayers()

    @staticmethod
    def PlayAgain():
        answer = input('Do you want to play again? (YES/NO) ')
        if answer[0].upper() == 'Y':
            playAgain = TicTacToeGame()
            playAgain.PlayGame()
        elif answer[0].upper() != 'Y':
            print('Thank you for playing this game.')

    @staticmethod
    def GetPlayerDataList(player):
        return [player] * 3

    def PlayGame(self):
        while self.game_still_going:
            self.GridDisplay()
            self.ShowTurn()
            self.LoadPosition()
            self.CheckWinner()
            self.SwitchTurn()

    def SetPlayers(self):
        self.player1 = input('Choose witch player you want to be X/O: ').upper()
        while self.player1 not in ['X', 'O']:
            self.player1 = input('Choose witch player you want to be X/O: ').upper()

        if self.player1 == 'X':
            self.playerComputer = "O"
            self.currentPlayer = self.player1
        else:
            self.playerComputer = "X"
            self.currentPlayer = self.playerComputer

    def GridDisplay(self, newLine='\n'):
        result = ''
        for i in self.displayedGrid:
            for j in i:
                result += j
            result += newLine
        print(result)

    def SwitchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.playerComputer
        else:
            self.currentPlayer = self.player1

    def ShowTurn(self):
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

    def CheckWinner(self):
        if self.CheckIfWinOnRows(self.currentPlayer) or self.CheckIfWinOnCols(self.currentPlayer) or self.CheckIfWinOnDiagonals(
                self.currentPlayer):
            self.GridDisplay()
            print("{} won.".format(self.currentPlayer))
            self.game_still_going = False
            self.PlayAgain()
        else:
            if self.CheckIfTie():
                self.GridDisplay()
                print('Is tie.')
                self.game_still_going = False
                self.PlayAgain()

    # Setting both in the mainArray and in the diplayedGrid the player, on the position he chose.
    def SetColByIndex(self, position, player):
        # Get's the row and the column from the GetColByIndex function based on the player chosen position.
        index, position = self.GetColByIndex(position)

        # Ask's again for position.
        if player == self.player1 and index == -1:
            print("This is a wrong position, please choose one from 1 to 9")
            self.LoadPosition()

        elif player == self.player1 and self.mainArray[index][position]:
            print("This position is busy, choose another one.")
            self.LoadPosition()

        # Changes elements from mainArray and displayedGrid (from position [index][position]) with the current player.
        else:
            self.mainArray[index][position] = player

            curString = self.displayedGrid[index][position]
            curString = curString.replace(curString[0], player)
            self.displayedGrid[index][position] = curString

    # Get position from the current player(either player1 or playerComputer).
    def LoadPosition(self):
        if self.currentPlayer == self.player1:
            position = input('Choose a position from 1 to 9: ')
            if position.isdigit():
                pos = int(position)
                if pos in self.POSSIBLE_POSITIONS:
                    self.SetColByIndex(pos, self.currentPlayer)
            else:
                self.LoadPosition()
        else:
            self.SetColByIndex(self.GetComputerPos(), self.currentPlayer)

    # Get's the row and the column from the position the player chose.
    def GetColByIndex(self, position):
        for index, range_list in enumerate(self.START_END_ROWS_LIST):
            start, end = range_list
            if position >= start and position <= end:
                return index, position - start

        return -1, -1

    def GetComputerPos(self):
        position = -1
        hasFound = False

        while not hasFound:
            random_index = choice(self.POSSIBLE_POSITIONS)
            row, col = self.GetColByIndex(random_index)
            if self.mainArray[row][col] is None:
                position = random_index
                hasFound = True

        return position

    def CheckIfWinOnCols(self, player):
        checkColsList = []
        for col in range(self.MAX_COL):
            checkColsList.append([self.mainArray[row][col] for row in range(self.MAX_ROW)])
        return self.GetPlayerDataList(player) in checkColsList

    def CheckIfWinOnRows(self, player):
        checkRowsList = []
        for row in range(self.MAX_ROW):
            checkRowsList.append([self.mainArray[row][col] for col in range(self.MAX_COL)])
        return self.GetPlayerDataList(player) in checkRowsList

    def CheckIfWinOnDiagonals(self, player):
        diagonal_1 = [self.mainArray[i][i] for i in range(3)]
        diagonal_2 = [self.mainArray[i][2 - i] for i in range(3)]

        player_data = self.GetPlayerDataList(player)
        return player_data == diagonal_1 or player_data == diagonal_2

    def CheckIfTie(self):
        count = 0
        for row in self.mainArray:
            for col in row:
                if col:
                    count += 1
        return count == self.MAX_COL * self.MAX_ROW


game = TicTacToeGame()
game.PlayGame()
