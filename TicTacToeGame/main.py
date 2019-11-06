from time import sleep
from random import choice


class TicTacToeGame:
    START_END_ROWS_LIST: list = [[1, 3], [4, 6], [7, 9]]
    POSSIBLE_POSITIONS : list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    MAX_ROW: int = 3
    MAX_COL: int = 3

    XO_LIST = ['X', 'O']

    TRANSLATE_DICT: dict = {
        'WIN_TIE_MSG_LIST'        : ["{} won.", 'Is tie.'],
        'PLAYER_TURN_MSG'         : ["_____________\n", "{} turn.\n{} moves.", "\n_____________"],
        'COMPUTER_TURN_MSG'       : ["_____________\n", "Is {}'s turn, wait", "\n_____________"],
        'GET_NAME_MSG'            : 'Enter your name: ',
        'CHOOSE_PLAYER_MSG'       : 'Choose which player you want to be X/O: ',
        'ASK_FOR_POS_MSG'         : 'Choose a position from 1 to 9: ',
        'PLAY_WITH_FRIEND_MSG'    : 'Do you want to play with a friend? (YES/NO) ',
        'PLAY_AGAIN_MSG'          : 'Do you want to play again? (YES/NO) ',
        'GOODBYE_MSG'             : 'Thank you for playing this game.',
        'POS_ERR_MSG_LIST'        : ['This is a wrong position, please choose one from 1 to 9',
                                     'This position is busy, choose another one.'
                                     ]
    }

    for msgName, msgValue in TRANSLATE_DICT.items():
        locals().update({msgName: msgValue})

    def __init__(self):
        self.player1:          str = ''
        self.player2:          str = ''
        self.playerComputer:   str = ''
        self.player1Name:      str = ''
        self.player2Name:      str = ''

        self.game_still_going: bool = True
        self.mainArray:        list = [
                  [None, None, None],
                  [None, None, None],
                  [None, None, None]
        ]

        self.displayedGrid:    list = [
                  ['-|', '-|', '-', '\t\t1|2|3'],
                  ['-|', '-|', '-', '\t\t4|5|6'],
                  ['-|', '-|', '-', '\t\t7|8|9']
        ]

    def PlayGame(self):
        self.SetPlayers()

        while self.game_still_going:
            self.GridDisplay()
            self.ShowTurn()
            self.LoadPosition()
            self.CheckWinner()
            self.SwitchTurn()

    def SetPlayers(self):
        self.player1Name = input(self.GET_NAME_MSG)
        self.player1 = input(self.CHOOSE_PLAYER_MSG).upper()
        while self.player1 not in self.XO_LIST:
            self.player1 = input(self.CHOOSE_PLAYER_MSG).upper()

        if self.player1 == self.XO_LIST[0]:
            self.secondPlayer = self.XO_LIST[1]
            self.currentPlayer = self.player1
        else:
            self.secondPlayer = self.XO_LIST[0]
            self.currentPlayer = self.secondPlayer

        self.SetSecondPlayer()

    def SetSecondPlayer(self):
        question = input(self.PLAY_WITH_FRIEND_MSG)

        if question[0].upper() == 'Y':
            self.player2Name = input(self.GET_NAME_MSG)
            self.player2 = self.secondPlayer
        else:
            self.playerComputer = self.secondPlayer

    def GridDisplay(self, newLine='\n'):
        result = ''
        for i in self.displayedGrid:
            for j in i:
                result += j
            result += newLine
        print(result)

    def ShowTurn(self):
        if self.currentPlayer == self.player1 or self.currentPlayer == self.player2:
            print(self.PLAYER_TURN_MSG[0] +
                  self.PLAYER_TURN_MSG[1].format(self.GetName(), self.currentPlayer) +
                  self.PLAYER_TURN_MSG[2]
                  )
        elif self.currentPlayer == self.playerComputer:
            result = self.COMPUTER_TURN_MSG[0] + self.COMPUTER_TURN_MSG[1].format(self.currentPlayer)
            print(result, end='')
            for i in range(3):
                if i == 0:
                    sleep(1)
                print(".", end='')
                sleep(1)
            print(self.COMPUTER_TURN_MSG[2])

    def LoadPosition(self):
        if self.currentPlayer == self.player1 or self.currentPlayer == self.player2:
            position = input(self.ASK_FOR_POS_MSG)
            if position.isdigit():
                pos = int(position)
                if pos in self.POSSIBLE_POSITIONS:
                    self.SetColByIndex(pos, self.currentPlayer)
            else:
                self.LoadPosition()
        else:
            self.SetColByIndex(self.GetComputerPos(), self.currentPlayer)

    def CheckWinner(self):
        if self.CheckIfWinOnRows(self.currentPlayer) or self.CheckIfWinOnCols(self.currentPlayer) or self.CheckIfWinOnDiagonals(self.currentPlayer):
            self.GridDisplay()
            print(self.WIN_TIE_MSG_LIST[0].format(self.GetName()))
            self.game_still_going = False
            self.PlayAgain()
        elif self.CheckIfTie():
            self.GridDisplay()
            print(self.WIN_TIE_MSG_LIST[1])
            self.game_still_going = False
            self.PlayAgain()

    def SwitchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.secondPlayer
        else:
            self.currentPlayer = self.player1

    def PlayAgain(self):
        answer = input(self.PLAY_AGAIN_MSG)
        if answer[0].upper() == 'Y':
            print('\n\n\n')
            playAgain = TicTacToeGame()
            playAgain.PlayGame()
        elif answer[0].upper() != 'Y':
            print(self.GOODBYE_MSG)

    # Setting both in the mainArray and in the diplayedGrid the player, on the position he chose.
    def SetColByIndex(self, position, player):
        # Get's the row and the column from the GetColByIndex function based on the player chosen position.
        index, position = self.GetColByIndex(position)

        # Ask's again for position.
        if (player == self.player1 or player == self.player2) and index == -1:
            print(self.POS_ERR_MSG_LIST[0])
            self.LoadPosition()

        elif (player == self.player1 or player == self.player2) and self.mainArray[index][position]:
            print(self.POS_ERR_MSG_LIST[1])
            self.LoadPosition()

        # Changes elements from mainArray and displayedGrid (from position [index][position]) with the current player.
        else:
            self.mainArray[index][position] = player

            curString = self.displayedGrid[index][position]
            curString = curString.replace(curString[0], player)
            self.displayedGrid[index][position] = curString

    def GetName(self):
        if self.currentPlayer == self.player1:
            return self.player1Name
        elif self.player2Name:
            return self.player2Name
        else:
            return self.currentPlayer

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

    def CheckIfTie(self):
        count = 0
        for row in self.mainArray:
            for col in row:
                if col:
                    count += 1
        return count == self.MAX_COL * self.MAX_ROW

    def CheckIfWinOnCols(self, player):
        checkColsList = []
        for col in range(self.MAX_COL):
            checkColsList.append([self.mainArray[row][col] for row in range(self.MAX_ROW)])
        return GetPlayerDataList(player) in checkColsList

    def CheckIfWinOnRows(self, player):
        checkRowsList = []
        for row in range(self.MAX_ROW):
            checkRowsList.append([self.mainArray[row][col] for col in range(self.MAX_COL)])
        return GetPlayerDataList(player) in checkRowsList

    def CheckIfWinOnDiagonals(self, player):
        diagonal_1 = [self.mainArray[i][i] for i in range(3)]
        diagonal_2 = [self.mainArray[i][2 - i] for i in range(3)]
        player_data = GetPlayerDataList(player)
        return player_data == diagonal_1 or player_data == diagonal_2

def GetPlayerDataList(player):
    return [player] * 3


game = TicTacToeGame()
game.PlayGame()
