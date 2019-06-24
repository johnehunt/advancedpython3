import wx
from abc import abstractmethod

class PyDrawConstants:
    LINE_ID = 100
    SQUARE_ID = 102
    CIRCLE_ID = 103
    TEXT_ID = 104

    SQUARE_MODE = 'square'
    LINE_MODE = 'line'
    CIRCLE_MODE = 'circle'
    TEXT_MODE = 'Text'


class Figure(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=None, size=None, style=wx.TAB_TRAVERSAL):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style)
        self.point = pos
        self.size = size

    @abstractmethod
    def on_paint(self, dc):
        pass


class Square(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos, size=size)

    def on_paint(self, dc):
        dc.DrawRectangle(self.point, self.size)


class Line(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos, size=wx.Size(size, size))
        self.end_point = wx.Point(self.point.x + size, self.point.y + size)

    def on_paint(self, dc):
        dc.DrawLine(pt1=self.point, pt2=self.end_point)


class Circle(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos, size=wx.Size(size, size))
        self.radius = (size - 10) / 2
        self.circle_center = wx.Point(self.point.x + self.radius, self.point.y + self.radius)

    def on_paint(self, dc):
        dc.DrawCircle(pt=self.circle_center, radius=self.radius)


class Text(Figure):
    def __init__(self, parent, pos, size):
        super().__init__(parent=parent, pos=pos, size=wx.Size(size, size))

    def on_paint(self, dc):
        dc.DrawText(text='Text', pt=self.point)


class PyDrawFrame(wx.Frame):
    """ Main Frame responsible for the
    layout of the UI."""

    def __init__(self, title):
        super().__init__(None,
                         title=title,
                         size=(300, 200))

        # Set up the controller
        self.controller = PyDrawController(self)

        # Set up the layout fo the UI
        self.vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.vertical_box_sizer)

        # Set up the menu bar
        self.SetMenuBar(PyDrawMenuBar())

        # Set up the toolbar
        self.vertical_box_sizer.Add(PyDrawToolBar(self),
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL, )


        # Setup drawing panel
        self.drawing_panel = DrawingPanel(self, self.controller.get_mode)
        self.drawing_controller = self.drawing_panel.controller

        # Add the Panel to the Frames Sizer
        self.vertical_box_sizer.Add(self.drawing_panel,
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL)

        # Set up the command event handling for the menu bar and tool bar
        self.Bind(wx.EVT_MENU, self.controller.command_menu_handler)

        self.Centre()


class PyDrawMenuBar(wx.MenuBar):

    def __init__(self):
        super().__init__()
        fileMenu = wx.Menu()
        newMenuItem = wx.MenuItem(fileMenu, wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        newMenuItem.SetBitmap(wx.Bitmap("new.gif"))
        fileMenu.Append(newMenuItem)
        loadMenuItem = wx.MenuItem(fileMenu, wx.ID_OPEN, text="Open", kind=wx.ITEM_NORMAL)
        loadMenuItem.SetBitmap(wx.Bitmap("load.gif"))
        fileMenu.Append(loadMenuItem)

        fileMenu.AppendSeparator()
        saveMenuItem = wx.MenuItem(fileMenu, wx.ID_SAVE, text="Save", kind=wx.ITEM_NORMAL)
        saveMenuItem.SetBitmap(wx.Bitmap("save.gif"))
        fileMenu.Append(saveMenuItem)

        fileMenu.AppendSeparator()
        quit = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')

        fileMenu.Append(quit)
        self.Append(fileMenu, '&File')

        drawingMenu = wx.Menu()
        lineMenuItem = wx.MenuItem(drawingMenu, PyDrawConstants.LINE_ID, text="Line", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(lineMenuItem)
        squareMenuItem = wx.MenuItem(drawingMenu, PyDrawConstants.SQUARE_ID, text="Square", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(squareMenuItem)
        circleMenuItem = wx.MenuItem(drawingMenu, PyDrawConstants.CIRCLE_ID, text="Circle", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(circleMenuItem)
        textMenuItem = wx.MenuItem(drawingMenu, PyDrawConstants.TEXT_ID, text="Text", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(textMenuItem)

        self.Append(drawingMenu, '&Drawing')


class PyDrawToolBar(wx.ToolBar):

    def __init__(self, parent):
        super().__init__(parent)
        self.AddTool(toolId=wx.ID_NEW, label="New", bitmap=wx.Bitmap("new.gif"), shortHelp='Open drawing',
                     kind=wx.ITEM_NORMAL)
        self.AddTool(toolId=wx.ID_OPEN, label="Open", bitmap=wx.Bitmap("load.gif"), shortHelp='Open drawing',
                     kind=wx.ITEM_NORMAL)
        self.AddTool(toolId=wx.ID_SAVE, label="Save", bitmap=wx.Bitmap("save.gif"), shortHelp='Save drawing',
                     kind=wx.ITEM_NORMAL)
        self.Realize()


class PyDrawController:

    def __init__(self, view):
        self.view = view
        # Set the initial mode
        self.mode = PyDrawConstants.SQUARE_MODE

    def set_circle_mode(self):
        self.mode = PyDrawConstants.CIRCLE_MODE

    def set_line_mode(self):
        self.mode = PyDrawConstants.LINE_MODE

    def set_square_mode(self):
        self.mode = PyDrawConstants.SQUARE_MODE

    def set_text_mode(self):
        self.mode = PyDrawConstants.TEXT_MODE

    def clear_drawing(self):
        self.view.drawing_controller.clear()

    def get_mode(self):
        return self.mode

    def command_menu_handler(self, command_event):
        id = command_event.GetId()
        if id == wx.ID_NEW:
            print('Clear the drawing area')
            self.clear_drawing()
        elif id == wx.ID_OPEN:
            print('Open a drawing file')
        elif id == wx.ID_SAVE:
            print('Save a drawing file')
        elif id == wx.ID_EXIT:
            print('Quite the application')
            self.view.Close()
        elif id == PyDrawConstants.LINE_ID:
            print('set drawing mode to line')
            self.set_line_mode()
        elif id == PyDrawConstants.SQUARE_ID:
            print('set drawing mode to square')
            self.set_square_mode()
        elif id == PyDrawConstants.CIRCLE_ID:
            print('set drawing mode to circle')
            self.set_circle_mode()
        elif id == PyDrawConstants.TEXT_ID:
            print('set drawing mode to Text')
            self.set_text_mode()
        else:
            print('Unknown option', id)


class DrawingPanel(wx.Panel):

    def __init__(self, parent, get_mode):
        super().__init__(parent, -1)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.model = DrawingModel()
        self.controller = DrawingController(self, self.model, get_mode)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.controller.on_mouse_click)

    def on_paint(self, event):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        for figure in self.model.contents:
            figure.on_paint(dc)


class DrawingModel:

    def __init__(self):
        self.contents = []

    def clear_figures(self):
        self.contents = []

    def add_figure(self, figure):
        self.contents.append(figure)


class DrawingController:

    def __init__(self, view, model, get_mode):
        self.view = view
        self.model = model
        self.get_mode = get_mode

    def on_mouse_click(self, mouse_event):
        point = mouse_event.GetPosition()
        self.add(self.get_mode(), point)

    def add(self, mode, point, size=30):
        if mode == PyDrawConstants.SQUARE_MODE:
            fig = Square(self.view, point, wx.Size(size, size))
        elif mode == PyDrawConstants.CIRCLE_MODE:
            fig = Circle(self.view, point, size)
        elif mode == PyDrawConstants.TEXT_MODE:
            fig = Text(self.view, point, size)
        elif mode == PyDrawConstants.LINE_MODE:
            fig = Line(self.view, point, size)
        self.model.add_figure(fig)

    def clear(self):
        self.model.clear_figures()
        self.view.Refresh()


class PyDrawApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = PyDrawFrame(title='PyDraw')
        frame.Show()
        return True


# Run the GUI application
app = PyDrawApp()
app.MainLoop()
