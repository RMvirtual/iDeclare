import wx


class EoriGui(wx.Frame):
    def __init__(self, controller):
        super().__init__(None, title='Hello World 2')
        self._controller = controller

        panel = wx.Panel(self)
        text = wx.StaticText(panel, label="Hello, World!")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

        self.make_menu_bar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to EORI Checker")

    def make_menu_bar(self):
        file_menu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        hello_item = file_menu.Append(
            -1, "&Hello...\tCtrl-H",
            "Help string shown in status bar for this menu item"
        )

        file_menu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label

        exit_item = file_menu.Append(wx.ID_EXIT)

        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT)

        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")

        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.on_hello, hello_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def on_exit(self, event):
        self.Close(True)

    def on_hello(self, event):
        wx.MessageBox("Hello again from wxPython")

    def on_about(self, event):
        wx.MessageBox(
            "This is a wxPython Hello World sample",
            "About Hello World 2",
            wx.OK | wx.ICON_INFORMATION
        )
