import wx
from abc import abstractmethod

class PyDraw_Constants:
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

    def on_paint(self, dc):
        circle_center = wx.Point(self.point.x + self.radius, self.point.y + self.radius)
        dc.DrawCircle(pt=circle_center, radius=self.radius)


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

        # Setup drawing panel
        self.drawing_panel = DrawingPanel(self, self.controller.get_mode)
        self.drawing_controller = self.drawing_panel.controller

        # Set up the layout fo the UI
        self.vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.vertical_box_sizer)

        # Set up the menu bar
        self.menubar = PyDrawMenuBar()
        self.SetMenuBar(self.menubar)

        self.Bind(wx.EVT_MENU, self.controller.menu_handler)

        # Set up the toolbar
        self.toolbar = PyDrawToolBar(self)
        self.vertical_box_sizer.Add(self.toolbar,
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL, )

        # Add the Panel to the Frames Sizer
        self.vertical_box_sizer.Add(self.drawing_panel,
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL)
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
        lineMenuItem = wx.MenuItem(drawingMenu, PyDraw_Constants.LINE_ID, text="Line", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(lineMenuItem)
        squareMenuItem = wx.MenuItem(drawingMenu, PyDraw_Constants.SQUARE_ID, text="Square", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(squareMenuItem)
        circleMenuItem = wx.MenuItem(drawingMenu, PyDraw_Constants.CIRCLE_ID, text="Circle", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(circleMenuItem)
        textMenuItem = wx.MenuItem(drawingMenu, PyDraw_Constants.TEXT_ID, text="Text", kind=wx.ITEM_NORMAL)
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

    def __init__(self, frame):
        self.frame = frame
        # Set the initial mode
        self.mode = PyDraw_Constants.SQUARE_MODE

    def set_circle_mode(self):
        self.mode = PyDraw_Constants.CIRCLE_MODE

    def set_line_mode(self):
        self.mode = PyDraw_Constants.LINE_MODE

    def set_square_mode(self):
        self.mode = PyDraw_Constants.SQUARE_MODE

    def set_text_mode(self):
        self.mode = PyDraw_Constants.TEXT_MODE

    def clear_drawing(self):
        self.frame.drawing_controller.clear()

    def get_mode(self):
        return self.mode

    def menu_handler(self, event):
        id = event.GetId()
        if id == wx.ID_NEW:
            print('Clear the drawing area')
            self.clear_drawing()
        elif id == wx.ID_OPEN:
            print('Open a drawing file')
        elif id == wx.ID_SAVE:
            print('Save a drawing file')
        elif id == wx.ID_EXIT:
            print('Quite the application')
            self.frame.Close()
        elif id == PyDraw_Constants.LINE_ID:
            print('set drawing mode to line')
            self.set_line_mode()
        elif id == PyDraw_Constants.SQUARE_ID:
            print('set drawing mode to square')
            self.set_square_mode()
        elif id == PyDraw_Constants.CIRCLE_ID:
            print('set drawing mode to circle')
            self.set_circle_mode()
        elif id == PyDraw_Constants.TEXT_ID:
            print('set drawing mode to Text')
            self.set_text_mode()
        else:
            print('Unknown option', id)


class DrawingPanel(wx.Panel):

    def __init__(self, parent, get_mode):
        super().__init__(parent, -1)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.model = DrawingModel(self)
        self.controller = DrawingController(self, self.model, get_mode)
        self.parent = parent
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.controller.on_mouse_click)

    def on_paint(self, event):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        for figure in self.model.contents:
            figure.on_paint(dc)


class DrawingModel:

    def __init__(self, panel):
        self.panel = panel
        self.contents = []

    def clear_figures(self):
        self.contents = []

    def add_figure(self, figure):
        self.contents.append(figure)


class DrawingController:

    def __init__(self, panel, model, get_mode):
        self.panel = panel
        self.model = model
        self.get_mode = get_mode

    def on_mouse_click(self, mouse_event):
        point = mouse_event.GetPosition()
        self.add(self.get_mode(), point)

    def add(self, mode, point, size=30):
        if mode == PyDraw_Constants.SQUARE_MODE:
            fig = Square(self.panel, point, wx.Size(size, size))
        elif mode == PyDraw_Constants.CIRCLE_MODE:
            fig = Circle(self.panel, point, size)
        elif mode == PyDraw_Constants.TEXT_MODE:
            fig = Text(self.panel, point, size)
        elif mode == PyDraw_Constants.LINE_MODE:
            fig = Line(self.panel, point, size)
        self.model.add_figure(fig)

    def clear(self):
        self.model.clear_figures()
        self.panel.Refresh()


class PyDrawApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = PyDrawFrame(title='PyDraw')
        frame.Show()
        return True


# Run the GUI application
app = PyDrawApp()
app.MainLoop()
