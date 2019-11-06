from tkinter import *


class GameWindow:
    MAX_ROW: int = 3
    MAX_COL: int = 3

    def __init__(self):
        self.gameWnd = None

        self.buttList = []
        self.player1 = ''
        self.player2 = ''
        self.playerComputer = ''
        self.currentPlayer = ''
        self.onClick = False
        self.game_still_going = True

       # self.GetPlayers()

    def PlayGame(self, button):
        self.SetButtTxtOnClick(button)
        self.SwitchTurn()

    def SetGrid(self):
        canvas = Canvas(self.gameWnd, width=300, height=300, highlightthickness=0, bg="PaleGreen1")
        canvas.pack()

        # Vertical lines.
        canvas.create_line(100, 1, 100, 300, fill="black")
        canvas.create_line(200, 1, 200, 300, fill="black")

        # Horizontal lines.
        canvas.create_line(1, 100, 300, 100, fill="black")
        canvas.create_line(1, 200, 300, 200, fill="black")

        self.buttonPos1 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos1))
        self.buttonPos2 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos2))
        self.buttonPos3 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos3))
        self.buttonPos4 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos4))
        self.buttonPos5 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos5))
        self.buttonPos6 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos6))
        self.buttonPos7 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos7))
        self.buttonPos8 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos8))
        self.buttonPos9 = Button(self.gameWnd, padx=40, pady=38, bd=0, bg='PaleGreen1', activebackground='PaleGreen1',
                                 command=lambda: self.PlayGame(self.buttonPos9))

        self.buttonPos1.place(x=2, y=2)
        self.buttonPos2.place(x=102, y=2)
        self.buttonPos3.place(x=202, y=2)
        self.buttonPos4.place(x=2, y=102)
        self.buttonPos5.place(x=102, y=102)
        self.buttonPos6.place(x=202, y=102)
        self.buttonPos7.place(x=2, y=202)
        self.buttonPos8.place(x=102, y=202)
        self.buttonPos9.place(x=202, y=202)

        self.buttList = [
            [self.buttonPos1, self.buttonPos2, self.buttonPos3],
            [self.buttonPos4, self.buttonPos5, self.buttonPos6],
            [self.buttonPos7, self.buttonPos8, self.buttonPos9]
        ]

    def SetFirstPlayer(self, text):
        self.OnClickFlag()
        if self.onClick:
            self.player1 = text
            print('player1 is : %s' % self.player1)

        self.SetPlayers()

    def SetSecondPlayer(self, answer):
        self.gameWnd = Tk()
        self.gameWnd.title('X and O Game')
        self.gameWnd.configure(background='light blue')
        self.gameWnd.geometry('300x300')

        if answer[0].upper() == 'Y':
            self.player2 = self.secondPlayer
        elif answer[0].upper() == 'N':
            self.playerComputer = self.secondPlayer
        print('player2 is : %s\nplayerComputer is: %s' % (self.player2, self.playerComputer))
        self.SetGrid()

    def SetPlayers(self):
        if self.player1 == 'X':
            self.secondPlayer = 'O'
            self.currentPlayer = self.player1
        elif self.player1 == 'O':
            self.secondPlayer = 'X'
            self.currentPlayer = self.secondPlayer

    def OnClickFlag(self):
        if not self.onClick:
            self.onClick = True

    def SetButtTxtOnClick(self, button):
        self.OnClickFlag()

        if not button.cget('text') and self.onClick:
            button.configure(text=self.currentPlayer)

        # Checks if after pressing button player wins.
        self.CheckWinner()

    def SwitchTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.secondPlayer
        else:
            self.currentPlayer = self.player1

    def CheckWinner(self):
        if self.CheckWinOnCols() or self.CheckWinOnRows() or self.CheckWinOnDiagonals():
            print('Yeeey')
            self.gameWnd.destroy()
            PlayAgain(self.currentPlayer, self)

        elif self.IsTie():
            print('TIE')
            self.gameWnd.destroy()
            PlayAgain(None, self)

    def IsTie(self):
        count = 0
        for row in self.buttList:
            for col in row:
                if col.cget('text'):
                    count += 1
        return count == self.MAX_COL * self.MAX_ROW

    def CheckWinOnCols(self):
        checkColsList = []
        for col in range(self.MAX_COL):
            checkColsList.append([self.buttList[row][col].cget('text') for row in range(self.MAX_ROW)])
        return GetPlayerDataList(self.currentPlayer) in checkColsList

    def CheckWinOnRows(self):
        checkColsList = []
        for row in range(self.MAX_ROW):
            checkColsList.append([self.buttList[row][col].cget('text') for col in range(self.MAX_COL)])
        return GetPlayerDataList(self.currentPlayer) in checkColsList

    def CheckWinOnDiagonals(self):
        diagonal_1 = [self.buttList[i][i].cget('text') for i in range(3)]
        diagonal_2 = [self.buttList[i][2 - i].cget('text') for i in range(3)]
        player_data = GetPlayerDataList(self.currentPlayer)
        return player_data == diagonal_1 or player_data == diagonal_2


def GetPlayerDataList(player):
    return [player] * 3


class PlayAgain:
    def __init__(self, currentPlayer, wndGame):
        self.wndGame = wndGame
        self.currentPlayer = currentPlayer
        self.exitWnd = Tk()
        self.exitWnd.title('Play again.')
        self.exitWnd.configure(background='light blue')
        self.exitWnd.geometry('300x200')

        self.onclick = False

        if self.currentPlayer:
            self.WinnerMsg()
        else:
            self.TieMsg()

        self.PlayAgainMsg()

        self.exitWnd.mainloop()

    def TieMsg(self):
        tieMsg = Label(self.exitWnd, text='Is a tie.', font=('Tahoma', 40), background='light blue')
        tieMsg.place(x=65, y=15)

    def WinnerMsg(self):
        congratLabel = Label(self.exitWnd, text='Congratulations!', font=('Tahoma', 25), background='light blue')
        winLabel = Label(self.exitWnd, text='{} won.'.format(self.currentPlayer), font=('Tahoma', 20), background='light blue')

        congratLabel.place(x=30, y=5)
        winLabel.place(x=117, y=50)

    def PlayAgainMsg(self):
        msgLabel = Label(self.exitWnd, text='Do you want to play again?', font=('Tahoma', 17), background='light blue')
        yesButton = Button(self.exitWnd, padx=30, pady=10, bd=1, bg='PaleGreen1', text='Yes', activebackground='PaleGreen2',
                           command=lambda: self.GetResponse(yesButton))
        noButton = Button(self.exitWnd, padx=30, pady=10, bd=1, bg='PaleGreen1', text='No', activebackground='PaleGreen2',
                          command=lambda: self.GetResponse(noButton))

        msgLabel.place(x=10, y=95)
        yesButton.place(x=50, y=140)
        noButton.place(x=160, y=140)

    def OnClickFlag(self):
        if not self.onclick:
            self.onclick = True

    def GetResponse(self, button):
        self.OnClickFlag()
        if self.onclick:
            if button.cget('text') == 'Yes':
                self.exitWnd.destroy()
                SelectPlayer(self.wndGame)
            elif button.cget('text') == 'No':
                self.exitWnd.destroy()

game = GameWindow()

class SelectPlayer:
    def __init__(self, parent):
        self.parent = parent

        self.window = Tk()
        self.window.title('X and O Game')
        self.window.configure(background='light blue')
        self.window.geometry('300x100')

        self.choosePlayerLabel = Label(self.window, text='Which player do you want to be:', font=('Tahoma', 15),
                                       background='light blue')
        self.XButton = Button(self.window, padx=25, pady=5, bd=1, bg='PaleGreen1', text='X', activebackground='PaleGreen2',
                              command=lambda: self.SetFirstPlayer(self.XButton.cget('text')))
        self.OButton = Button(self.window, padx=25, pady=5, bd=1, bg='PaleGreen1', text='O', activebackground='PaleGreen2',
                              command=lambda: self.SetFirstPlayer(self.OButton.cget('text')))
        self.playWithFriendLabel = Label(self.window, text='Do you want to play with a friend?', font=('Tahoma', 14),
                                         background='light blue')
        self.yesButton = Button(self.window, padx=20, pady=5, bd=1, bg='PaleGreen1', text='Yes', activebackground='PaleGreen2',
                                command=lambda: self.SetSecondPlayer(self.yesButton.cget('text')))
        self.noButton = Button(self.window, padx=20, pady=5, bd=1, bg='PaleGreen1', text='No', activebackground='PaleGreen2',
                               command=lambda: self.SetSecondPlayer(self.noButton.cget('text')))

        self.choosePlayerLabel.place(x=2, y=5)
        self.XButton.place(x=70, y=35)
        self.OButton.place(x=160, y=35)

        self.window.mainloop()

    def SetFirstPlayer(self, text):
        self.parent.SetFirstPlayer(text)

        self.choosePlayerLabel.destroy()
        self.XButton.destroy()
        self.OButton.destroy()

        self.playWithFriendLabel.place(x=2, y=5)
        self.yesButton.place(x=70, y=35)
        self.noButton.place(x=160, y=35)

    def SetSecondPlayer(self, answer):
        self.parent.SetSecondPlayer(answer)
        self.window.destroy()


select_player = SelectPlayer(game)