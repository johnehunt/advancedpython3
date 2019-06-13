import wx
import wx.grid

MAX_ROWS = 25

# Create the Application Object
app = wx.App()

# Now create a Frame (representing the window)
frame = wx.Frame(parent=None, title='Colour Chart')

# Set up grid to be used to display colours
grid = wx.grid.Grid(frame, -1)
grid.CreateGrid(MAX_ROWS, 5)
grid.SetColSize(0, 140)

# Set up the column headings
grid.SetColLabelValue(0, 'RGB')
grid.SetColLabelValue(1, 'Solid')
grid.SetColLabelValue(2, '75%')
grid.SetColLabelValue(3, '50%')
grid.SetColLabelValue(4, '25%')

red = 0
green = 0
blue = 0
add_green = False
add_blue = False

# Generate RGB colours
for i in range(0, MAX_ROWS):
    # Set the colour and text
    grid.SetCellValue(i, 0, 'RGB(' + str(red) + ', ' +  str(green) + ', ' +  str(blue) + ')')
    # Solid version of colour
    grid.SetCellBackgroundColour(i, 1, wx.Colour(red, green, blue))
    # Add a bit of transparency 75%, 50% and 25%
    grid.SetCellBackgroundColour(i, 2, wx.Colour(red, green, blue, alpha=191))
    grid.SetCellBackgroundColour(i, 3, wx.Colour(red, green, blue, alpha=127))
    grid.SetCellBackgroundColour(i, 4, wx.Colour(red, green, blue, alpha=64))
    # Reset RGB values
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