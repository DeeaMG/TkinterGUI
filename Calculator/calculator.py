"""
	CALCULATOR GUI
"""

from tkinter import *
from math import sqrt, factorial

class Calculator:
    operators = ['+', '-', '*', '/']

    def __init__(self):
        self.expresion_string = ''
        self.LoadWindow()

    def LoadWindow(self):
		# Creates the window with it's features.
        self.wndBoard = Tk()
        self.wndBoard.title('CALCULATOR')
        self.wndBoard.configure(background='gray87')
        self.wndBoard.geometry('450x500')
		
        self.textHolderCalculations = StringVar()
        self.textHolderResults = StringVar()
        self.last_num_pos_list = []
		
		# Creates the entry for the calculations.
        self.wndEntry = Entry(self.wndBoard, font=('Courier New', 18, 'bold'), textvar=self.textHolderCalculations, bd=0,
                              bg='gray87', justify='right')
        self.wndEntry.place(width=60, height=25)
        self.wndEntry.pack(fill=X)
		
		# Creates the entry for the calculations results.
        self.resultsEntry = Entry(self.wndBoard, font=('Courier New', 22, 'bold'), textvar=self.textHolderResults, bd=0,
                                  bg='gray87', justify='right')
        self.resultsEntry.place(width=60, height=25)
        self.resultsEntry.pack(fill=X)

        # Define buttons.
        # Numbers.
        button_number_1 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('1'), text='1', font=('Courier New', 16, 'bold'))
        button_number_2 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('2'), text='2', font=('Courier New', 16, 'bold'))
        button_number_3 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('3'), text='3', font=('Courier New', 16, 'bold'))
        button_number_4 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('4'), text='4', font=('Courier New', 16, 'bold'))
        button_number_5 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('5'), text='5', font=('Courier New', 16, 'bold'))
        button_number_6 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('6'), text='6', font=('Courier New', 16, 'bold'))
        button_number_7 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('7'), text='7', font=('Courier New', 16, 'bold'))
        button_number_8 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('8'), text='8', font=('Courier New', 16, 'bold'))
        button_number_9 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('9'), text='9', font=('Courier New', 16, 'bold'))
        button_number_0 = Button(self.wndBoard, padx=40, pady=30, bd=0, bg='gray80',
                                 command=lambda: self.LoadToggleButton('0'), text='0', font=('Courier New', 16, 'bold'))

        # Operations.
        addition 		  = Button(self.wndBoard, padx=16, pady=30, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('+'), text='+', font=('Courier New', 20))
        substraction 	  = Button(self.wndBoard, padx=16, pady=30, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('-'), text='-', font=('Courier New', 20))
        multiplication 	  = Button(self.wndBoard, padx=16, pady=30, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('*'), text='×', font=('Courier New', 20))
        division 		  = Button(self.wndBoard, padx=16, pady=30, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('/'), text='÷', font=('Courier New', 20))
        factorial 		  = Button(self.wndBoard, padx=10, pady=26, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('n!'), text='n!', font=('Courier New', 14))
        square_root 	  = Button(self.wndBoard, padx=10, pady=25, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('sqrt'), text='√', font=('Courier New', 20))
        number_squared    = Button(self.wndBoard, padx=5, pady=26, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('**2'), text='x^2', font=('Courier New', 14))
        number_cubed 	  = Button(self.wndBoard, padx=5, pady=26, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('**3'), text='x^3', font=('Courier New', 14))
        pi 				  = Button(self.wndBoard, padx=16, pady=25, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('3.14'), text='π', font=('Courier New', 14))
        floating_point    = Button(self.wndBoard, padx=9, pady=24, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('.'), text='.', font=('Courier New', 20))
        open_paranthesis  = Button(self.wndBoard, padx=9, pady=24, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('('), text='(', font=('Courier New', 20))
        close_paranthesis = Button(self.wndBoard, padx=10, pady=24, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton(')'), text=')', font=('Courier New', 20))
        backspace 		  = Button(self.wndBoard, padx=63, pady=10, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('del'), text='⌫', font=('Courier New', 14))
        clear 			  = Button(self.wndBoard, padx=63, pady=2, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('C'), text='C', font=('Courier New', 20))
        equal 			  = Button(self.wndBoard, padx=10, pady=24, bd=0, bg='gray80',
                                   command=lambda: self.LoadToggleButton('='), text='=', font=('Courier New', 20))


        # Display buttons.
        # Numbers.
        button_number_1.place(x=57 , y=308)
        button_number_2.place(x=165, y=308)
        button_number_3.place(x=273, y=308)
        button_number_4.place(x=57 , y=213)
        button_number_5.place(x=165, y=213)
        button_number_6.place(x=273, y=213)
        button_number_7.place(x=57 , y=118)
        button_number_8.place(x=165, y=118)
        button_number_9.place(x=273, y=118)
        button_number_0.place(x=165, y=403)

        # Operations.
        pi.place(x=2, y=417)
        clear.place(x=57, y=66)
        equal.place(x=273, y=403)
        factorial.place(x=3, y=333)
        addition.place(x=381, y=67)
        division.place(x=381, y=391)
        square_root.place(x=2, y=67)
        backspace.place(x=219, y=66)
        number_cubed.place(x=2, y=249)
        number_squared.place(x=2, y=165)
        substraction.place(x=381, y=175)
        multiplication.place(x=381, y=283)
        floating_point.place(x=328, y=403)
        open_paranthesis.place(x=57, y=403)
        close_paranthesis.place(x=110, y=403)

        self.wndBoard.mainloop()

    def ClearEntry(self):
        self.expresion_string = ''
        self.textHolderCalculations.set('')
        self.textHolderResults.set('')

    def SqrtAndFactorial(self, func):
		'''
			When the radical or factorial buttons are pressed the function gets the last number after the last operator.
			If there are not other operations, than the radical/factorial are put to the last number. 
			Othewise if there is no numbers added, then the button does nothing.
			param: none
			return: none
		'''
        if self.expresion_string:
            for i in self.expresion_string:
                if i in self.operators and i != '.':
                    self.last_num_pos_list.append(self.expresion_string.rfind(i))
            if self.last_num_pos_list and len(self.last_num_pos_list) != 0:
                self.last_number = self.expresion_string[self.last_num_pos_list[-1] + 1:]
                self.operation = self.expresion_string[:self.last_num_pos_list[-1] + 1]
                if func == 'sqrt':
                    self.textHolderCalculations.set(self.operation + '√(' + self.last_number + ')')
                    self.expresion_string = self.operation + 'sqrt(' + self.last_number + ')'
                elif func == 'n!':
                    self.textHolderCalculations.set(self.operation + '(' + self.last_number + ')!')
                    self.expresion_string = self.operation + 'factorial(' + self.last_number + ')'
            else:
                if func == 'sqrt':
                    self.textHolderCalculations.set('√' + self.expresion_string )
                    self.expresion_string = 'sqrt(' + self.expresion_string + ')'
                elif func == 'n!' and ('.' not in self.expresion_string):
                    self.textHolderCalculations.set(self.expresion_string + '!')
                    self.expresion_string = 'factorial(' + self.expresion_string + ')'
        self.last_num_pos_list = []

    def LoadToggleButton(self, button):
        # Equal.
        if button == '=':
            if len(self.expresion_string) == 0:
                return
            elif self.expresion_string and (self.expresion_string[ -1 ] in self.operators):
                self.result_operations = str(eval(self.expresion_string[ :-1 ]))
            else:
                self.result_operations = str(eval(self.expresion_string))
            self.expresion_string = self.result_operations
            self.textHolderCalculations.set('')
            self.textHolderResults.set(self.result_operations)

        # Clear all.
        elif button == 'C':
            self.ClearEntry()

        # Backspace/delete.
        elif button == 'del':
            self.expresion_string = self.expresion_string[:-1]
            self.textHolderCalculations.set(self.expresion_string)

        # Square root and factorial.
        elif button == 'sqrt' or button == 'n!':
            if len(self.expresion_string) == 0 or (self.expresion_string[-1] in self.operators):
                return
            elif self.expresion_string[ 0 ] in self.operators:
                self.textHolderCalculations.set('Invalid input')
                self.expresion_string = ''
            elif self.expresion_string:
                if button == 'sqrt':
                    self.SqrtAndFactorial('sqrt')
                elif button == 'n!':
                    self.SqrtAndFactorial('n!')

        # pi
        elif button == '3.14':
            if self.expresion_string and self.expresion_string[-1] not in self.operators:
                return
            else:
                self.expresion_string += button
                self.textHolderCalculations.set(self.expresion_string)

        # Float button.
        elif button == '.':
            if len(self.expresion_string) == 0:
                self.ClearEntry()
            elif '3.14' in self.expresion_string:
                self.textHolderCalculations.set(self.expresion_string)
            else:
                self.expresion_string += button
                self.textHolderCalculations.set(self.expresion_string)

        # Squared/cubed.
        elif button == '**2' or button == '**3':
            if len(self.expresion_string) == 0 and (button == '**2' or button == '**3'):
                return
            elif self.expresion_string[0] == '-' or self.expresion_string:
                if button == '**2':
                    self.expresion_string = '(' + self.expresion_string + ')' + '**2'
                elif button == '**3':
                    self.expresion_string = '(' + self.expresion_string + ')' + '**3'
            else:
                for i in self.expresion_string:
                    if i in self.operators:
                        self.last_num_pos_list.append(self.expresion_string.rfind(i))
                if self.last_num_pos_list and len(self.last_num_pos_list) != 0:
                    self.last_number = self.expresion_string[self.last_num_pos_list[ -1 ] + 1:]
                    self.operation = self.expresion_string[:self.last_num_pos_list[ -1 ] + 1]
                    self.expresion_string = self.operation + '(' + self.last_number + ')' + button
            self.textHolderCalculations.set(self.expresion_string)

        # General.
        else:
            if len(self.expresion_string) == 0 and button in self.operators:
                return
            elif self.expresion_string and self.expresion_string[-1] == ')' and button not in self.operators:
                return
            elif self.expresion_string and (self.expresion_string[-1] in self.operators) and (button == '**2' or button == '**3'):
                return
            elif button in self.operators and self.expresion_string and self.expresion_string[-1] in self.operators:
                temp_expresion_string = list(self.expresion_string)
                temp_expresion_string[-1] = button
                self.expresion_string =  ''.join(temp_expresion_string)
            else:
                self.expresion_string += button

            self.textHolderCalculations.set(self.expresion_string)

            # Auto calculation
            try:
                if (self.expresion_string[-1] in self.operators):
                    result_operations = str(eval(self.expresion_string[:-1]))
                else:
                    result_operations = str(eval(self.expresion_string))
                self.textHolderResults.set(result_operations)
            except SyntaxError:
                print('Eval function can\'t evaluate the operation yet.')

calculator = Calculator()