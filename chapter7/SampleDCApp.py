import wx


class DrawingFrame(wx.Frame):

    def __init__(self, title):
        super().__init__(None,
                         title=title,
                         size=(300, 200))

        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        """set up the device context (DC) for painting"""
        dc = wx.PaintDC(self)
        dc.DrawLine(10, 10, 60, 20)
        dc.DrawRectangle(20, 40, 40, 20)
        dc.DrawText("Hello World", 30, 70)
        dc.DrawCircle(130, 40, radius=15)


class GraphicApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = DrawingFrame(title='PyDraw')
        frame.Show()
        return True


# Run the GUI application
app = GraphicApp()
app.MainLoop()
