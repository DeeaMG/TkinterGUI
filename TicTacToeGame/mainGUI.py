from tkinter import *


class GameWindow:

    MAX_ROW: int = 3
    MAX_COL: int = 3

    def __init__(self):
        self.gameWnd = Tk()
        self.gameWnd.title('X and O Game')
        self.gameWnd.configure(background='light blue')
        self.gameWnd.geometry('300x300')
        self.onClickText = StringVar()
        self.player1 = 'X'
        self.player2 = 'O'
        self.game_still_going = True
        self.currentPlayer = self.player1
        self.onClick = False

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

        self.gameWnd.mainloop()

    def PlayGame(self, button):
        self.SetButtTxtOnClick(button)
        self.SwitchTurn()

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
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def CheckWinner(self):
        if self.CheckWinOnCols() or self.CheckWinOnRows() or self.CheckWinOnDiagonals():
            print('Yeeey')
            self.gameWnd.destroy()

        elif self.IsTie():
            print('TIE')
            self.gameWnd.destroy()

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

game = GameWindow()