import wx

class Counter:
    def __init__(self, string):
        self.label = string

    def __str__(self):
        return self.label


# Set up Counter Globals
X = Counter('X')
O = Counter('O')


class TicTacToeButton(wx.Button):
    """ Version of a button that knows its
    position within a grid layout"""

    def __init__(self, parent=None, label=None, row=0, col=0):
        super().__init__(parent=parent, label=label)
        self.row = row
        self.col = col


class TicTacToeFrame(wx.Frame):
    """ A Frame that holds a TicTacToe game"""
    def __init__(self):
        super(TicTacToeFrame, self).__init__(parent=None,
                                             title='TicTacToe App',
                                             size=(250, 100))
        self.button_grid = []
        self.board = Board()
        self.first_player = Player(self.board)
        self.first_player.counter = X
        self.second_player = Player(self.board)
        self.second_player.counter = O
        self.next_player = self.first_player
        self.setup_display()


    def setup_display(self):
        # Create the panel to contain the widgets
        panel = wx.Panel(self)
        # Create the GridSizer to use with the Panel
        grid_sizer = wx.GridSizer(3, 3, 1, 1)
        panel.SetSizer(grid_sizer)

        for row_position in range(0, 3):
            row = []
            for col_position in range(0, 3):
                button = TicTacToeButton(panel, label=' ', row=row_position, col=col_position)
                button.Bind(wx.EVT_BUTTON, self.button_handler)
                row.append(button)
                grid_sizer.Add(button)
            self.button_grid.append(row)

    def button_handler(self, event):
        button_clicked = event.EventObject
        if button_clicked.GetLabel() != ' ':
            dialog = wx.MessageDialog(None,
                                      'Cell is already in use',
                                      'Cell Message',
                                      wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()
        else:
            move = Move(self.next_player.counter, button_clicked.row, button_clicked.col)
            self.make_a_move(move)
            finished = False
            if self.board.check_for_winner(self.next_player):
                self.show_winner_message(self.next_player)
                finished = True
            if finished == False and self.board.is_full():
                print('Game is a Tie')
                self.show_tie_message()
                finished = True
            if finished:
                print('Goodbye')
                wx.Exit()
            if self.next_player == self.first_player:
                self.next_player = self.second_player
            else:
                self.next_player = self.first_player

    def make_a_move(self, move):
        self.board.add_move(move)
        row = self.button_grid[move.x]
        row[move.y].SetLabel(move.counter.label)

    def show_winner_message(self, winner):
        dialog = wx.MessageDialog(None,
                                  'The winner is ' + str(winner),
                                  'Winner',
                                  wx.OK)
        dialog.ShowModal()

    def show_tie_message(self):
        dialog = wx.MessageDialog(None,
                                  'The game is a tie',
                                  'No Winner',
                                  wx.OK)
        dialog.ShowModal()


class Move:
    """ Represents a move made by a player """

    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter

    def __str__(self):
        return 'Move(' + str(self.x) + ', ' + str(self.y) + ')'


class Player:
    """ Class representing a Player and their counter """

    def __init__(self, board):
        self.board = board
        self._counter = None

    @property
    def counter(self):
        """ Represents Players Counter - may be X or Y"""
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    def __str__(self):
        return '[' + str(self.counter) + ']'


class Board:
    """ The ticTacToe board"""

    def __init__(self):
        # Set up the 3 by 3 grid of cells
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # List of lists
        self.separator = '\n' + ('-' * 11) + '\n'

    def __str__(self):
        row1 = ' ' + str(self.cells[0][0]) + ' | ' + str(self.cells[0][1]) + ' | ' + str(self.cells[0][2])
        row2 = ' ' + str(self.cells[1][0]) + ' | ' + str(self.cells[1][1]) + ' | ' + str(self.cells[1][2])
        row3 = ' ' + str(self.cells[2][0]) + ' | ' + str(self.cells[2][1]) + ' | ' + str(self.cells[2][2])
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self, move):
        """ A a move to the board """
        row = self.cells[move.x]
        row[move.y] = move.counter

    def is_empty_cell(self, row, column):
        """ Check to see if a cell is empty or not"""
        return self.cells[row][column] == ' '

    def cell_contains(self, counter, row, column):
        """ Check to see if a cell contains the provided counter """
        return self.cells[row][column] == counter

    def is_full(self):
        """ Check to see if the board is full or not """
        for row in range(0, 3):
            for column in range(0, 3):
                if self.is_empty_cell(row, column):
                    return False
        return True

    def check_for_winner(self, player):
        """ Check to see if a player has won or not """
        c = player.counter
        return (  # across the top
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 0, 1) and self.cell_contains(c, 0, 2)) or
                # across the middle
                (self.cell_contains(c, 1, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 1, 2)) or
                # across the bottom
                (self.cell_contains(c, 2, 0) and self.cell_contains(c, 2, 1) and self.cell_contains(c, 2, 2)) or
                # down the left side
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 0) and self.cell_contains(c, 2, 0)) or
                # down the middle
                (self.cell_contains(c, 0, 1) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 1)) or
                # down the right side
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 2) and self.cell_contains(c, 2, 2)) or
                # diagonal
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 2)) or
                # other diagonal
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 0)))


class MainApp(wx.App):

    def OnInit(self):
        frame = TicTacToeFrame()
        frame.Show()
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
