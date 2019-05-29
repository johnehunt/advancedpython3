import wx
import wx.grid

MAX_ROWS = 25

# Create the Application Object
app = wx.App()

# Now create a Frame (representing the window)
frame = wx.Frame(parent=None, title='Colour Chart')

# Set up grid to be used to display colours
grid = wx.grid.Grid(frame, -1)
grid.CreateGrid(MAX_ROWS, 4)
grid.SetColSize(1, 140)
grid.SetColLabelValue(0, 'Colour')
grid.SetColLabelValue(1, 'RGB')
grid.SetColLabelValue(2, 'Transparent')
grid.SetColLabelValue(3, 'alpha value')

red = 0
green = 0
blue = 0
add_green = False
add_blue = False

# Generate RGB colours
for i in range(0, MAX_ROWS):
    grid.SetCellBackgroundColour(i, 0, wx.Colour(red, green, blue))
    grid.SetCellValue(i, 1, 'RGB(' + str(red) + ', ' +  str(green) + ', ' +  str(blue) + ')')
    grid.SetCellBackgroundColour(i, 2, wx.Colour(red, green, blue, alpha=127))
    grid.SetCellValue(i, 3, '127')
    red = red + 30
    if red > 255:
        red = 0
        add_green = True
    if add_green:
        green = green + 30
    if green > 255:
        green = 0
        red = 0
        add_blue = True
    if add_blue:
        blue = blue + 30


# Run the GUI application
frame.Show()

# Start the event loop
app.MainLoop()