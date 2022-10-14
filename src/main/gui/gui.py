import wx
from src.main.gui.interface import EoriGuiInterface


class EoriGui(wx.Frame):
    def __init__(self, interface: EoriGuiInterface):
        super().__init__(None, title="EORI Check")
        self._interface = interface
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._initialise_panel()
        self._initialise_top_menu_bar()
        self._initialise_status_bar()

    def _initialise_panel(self) -> None:
        self._panel = wx.Panel(self)
        self._initialise_text_box()

    def _initialise_text_box(self) -> None:
        text = wx.StaticText(self._panel, label="EORI IS VALID??")
        font = text.GetFont()
        font.PointSize += 10
        font = font.Bold()
        text.SetFont(font)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))

    def _initialise_status_bar(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("Welcome to EORI Checker")

    def _initialise_top_menu_bar(self):
        self._initialise_file_menu()
        self._initialise_help_menu()

        menu_bar = wx.MenuBar()
        menu_bar.Append(self._file_menu, "&File")
        menu_bar.Append(self._help_menu, "&Help")

        self.SetMenuBar(menu_bar)

    def _initialise_help_menu(self):
        self._help_menu = wx.Menu()
        about_item = self._help_menu.Append(wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def _initialise_file_menu(self) -> None:
        self._file_menu = wx.Menu()

        hello_item = self._file_menu.Append(
            -1, "&Hello...\tCtrl-H",
            "Help string shown in status bar for this menu item"
        )

        self._file_menu.AppendSeparator()
        exit_item = self._file_menu.Append(wx.ID_EXIT)

        self.Bind(wx.EVT_MENU, self.on_hello, hello_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

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
