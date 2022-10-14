import wx
from src.main.gui.interface import EoriGuiInterface


class EoriGui(wx.Frame):
    def __init__(self, interface: EoriGuiInterface):
        super().__init__(None, title="EORI Check")
        self._interface = interface

        panel = wx.Panel(self)
        text = wx.StaticText(panel, label="EORI IS VALID??")
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

        hello_item = file_menu.Append(
            -1, "&Hello...\tCtrl-H",
            "Help string shown in status bar for this menu item"
        )

        file_menu.AppendSeparator()
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

    def on_exit(self, event: wx.Event):
        self._interface.exit_pressed(event)


    def on_hello(self, event: wx.Event):
        wx.MessageBox("Sup Brah.")

    def on_about(self, event: wx.Event):
        wx.MessageBox(
            "Checks Importer EORI references are registered on TSS.",
            "About EORI Checker",
            wx.OK | wx.ICON_INFORMATION
        )
