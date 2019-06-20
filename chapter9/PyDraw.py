import wx


class Figure(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=None, size=None, style=wx.TAB_TRAVERSAL):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style)
        self.point = pos
        self.size = size


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
    LINE_ID = 100
    SQUARE_ID = 102
    CIRCLE_ID = 103
    TEXT_ID = 104

    SQUARE_MODE = 'square'
    LINE_MODE = 'line'
    CIRCLE_MODE = 'circle'
    TEXT_MODE = 'Text'

    def __init__(self, title):
        super().__init__(None,
                         title=title,
                         size=(300, 200))
        self.vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.vertical_box_sizer)
        self.set_square_mode()
        self._setup_menubar()
        self._setup_toolbar()
        self._setup_drawing_panel()
        self.Centre()

    def _setup_menubar(self):
        self.menubar = wx.MenuBar()
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
        self.menubar.Append(fileMenu, '&File')

        drawingMenu = wx.Menu()
        lineMenuItem = wx.MenuItem(drawingMenu, PyDrawFrame.LINE_ID, text="Line", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(lineMenuItem)
        squareMenuItem = wx.MenuItem(drawingMenu, PyDrawFrame.SQUARE_ID, text="Square", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(squareMenuItem)
        circleMenuItem = wx.MenuItem(drawingMenu, PyDrawFrame.CIRCLE_ID, text="Circle", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(circleMenuItem)
        textMenuItem = wx.MenuItem(drawingMenu, PyDrawFrame.TEXT_ID, text="Text", kind=wx.ITEM_NORMAL)
        drawingMenu.Append(textMenuItem)

        self.menubar.Append(drawingMenu, '&Drawing')
        self.SetMenuBar(self.menubar)
        self.Bind(wx.EVT_MENU, self.menu_handler)

    def _setup_toolbar(self):
        self.toolbar = wx.ToolBar(self, -1)
        self.toolbar.AddTool(toolId=wx.ID_NEW, label="New", bitmap=wx.Bitmap("new.gif"), shortHelp='Open drawing',
                             kind=wx.ITEM_NORMAL)
        self.toolbar.AddTool(toolId=wx.ID_OPEN, label="Open", bitmap=wx.Bitmap("load.gif"), shortHelp='Open drawing',
                             kind=wx.ITEM_NORMAL)
        self.toolbar.AddTool(toolId=wx.ID_SAVE, label="Save", bitmap=wx.Bitmap("save.gif"), shortHelp='Save drawing',
                             kind=wx.ITEM_NORMAL)
        self.toolbar.Realize()
        self.vertical_box_sizer.Add(self.toolbar,
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL, )

    def _setup_drawing_panel(self):
        self.drawing_panel = Drawing(self)
        # Add the Panel to the Frames Sizer
        self.vertical_box_sizer.Add(self.drawing_panel,
                                    wx.ID_ANY,
                                    wx.EXPAND | wx.ALL)

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
            self.Close()
        elif id == PyDrawFrame.LINE_ID:
            print('set drawing mode to line')
            self.set_line_mode()
        elif id == PyDrawFrame.SQUARE_ID:
            print('set drawing mode to square')
            self.set_square_mode()
        elif id == PyDrawFrame.CIRCLE_ID:
            print('set drawing mode to circle')
            self.set_circle_mode()
        elif id == PyDrawFrame.TEXT_ID:
            print('set drawing mode to Text')
            self.set_text_mode()
        else:
            print('Unknown option', id)

    def set_circle_mode(self):
        self.mode = PyDrawFrame.CIRCLE_MODE

    def set_line_mode(self):
        self.mode = PyDrawFrame.LINE_MODE

    def set_square_mode(self):
        self.mode = PyDrawFrame.SQUARE_MODE

    def set_text_mode(self):
        self.mode = PyDrawFrame.TEXT_MODE

    def clear_drawing(self):
        self.drawing_panel.clear()


class Drawing(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.contents = []
        self.parent = parent
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)

    def clear(self):
        self.contents = []
        self.Refresh()

    def add(self, mode, point, size=30):
        if mode == PyDrawFrame.SQUARE_MODE:
            fig = Square(self, point, wx.Size(size, size))
        elif mode == PyDrawFrame.CIRCLE_MODE:
            fig = Circle(self, point, size)
        elif mode == PyDrawFrame.TEXT_MODE:
            fig = Text(self, point, size)
        elif mode == PyDrawFrame.LINE_MODE:
            fig = Line(self, point, size)
        self.contents.append(fig)

    def on_paint(self, event):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        for fig in self.contents:
            fig.on_paint(dc)

    def on_mouse_click(self, mouse_event):
        point = mouse_event.GetPosition()
        self.add(self.parent.mode, point)


class PyDrawApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = PyDrawFrame(title='PyDraw')
        frame.Show()
        return True


# Run the GUI application
app = PyDrawApp()
app.MainLoop()
