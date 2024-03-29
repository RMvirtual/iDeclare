import wx
from src.main.gui.interface import EoriGuiInterface


class EoriGui(wx.Frame):
    def __init__(self, interface: EoriGuiInterface):
        super().__init__(None, title="EORI Check")
        self._interface = interface
        self._initialise_widgets()

    def _initialise_widgets(self) -> None:
        self._initialise_panel()
        self._sizer = wx.BoxSizer(wx.VERTICAL)

        self._initialise_text_box()
        self._initialise_user_input_box()
        self._initialise_top_menu_bar()
        self._initialise_status_bar()

        self._sizer.SetSizeHints(self._panel)
        self._panel.SetSizer(self._sizer)

    def _initialise_panel(self) -> None:
        self._panel = wx.Panel(self)

    def _initialise_text_box(self) -> None:
        self._text_box = wx.StaticText(self._panel, label="EORI IS VALID??")
        font = self._text_box.GetFont()
        font.PointSize += 2
        font = font.Bold()
        self._text_box.SetFont(font)

        self._sizer.Add(self._text_box, 4, wx.EXPAND, 10)

    def _initialise_user_input_box(self) -> None:
        self._user_input_box = wx.TextCtrl(self._panel)
        self._user_input_box.SetLabelText("Enter here...")
        self._user_input_box.SetBackgroundColour(wx.LIGHT_GREY)

        self._sizer.Add(self._user_input_box, 1, wx.EXPAND, 10)

        self.Bind(
            wx.EVT_TEXT, self._on_eori_box_entry, self._user_input_box)

    def _initialise_status_bar(self) -> None:
        self.CreateStatusBar()
        self.SetStatusText("Welcome to EORI Checker")

    def _initialise_top_menu_bar(self):
        self._initialise_file_menu()
        self._initialise_help_menu()
        self._initialise_parent_menu_bar()

    def _initialise_parent_menu_bar(self):
        menu_bar = wx.MenuBar()
        menu_bar.Append(self._file_menu, "&File")
        menu_bar.Append(self._help_menu, "&Help")

        self.SetMenuBar(menu_bar)

    def _initialise_help_menu(self):
        self._help_menu = wx.Menu()
        self._initialise_about_menu_item()

    def _initialise_about_menu_item(self) -> None:
        about_item = self._help_menu.Append(wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self._on_about_menu_item, about_item)

    def _initialise_file_menu(self) -> None:
        self._file_menu = wx.Menu()

        hello_item = self._file_menu.Append(
            -1, "&Hello...\tCtrl-H",
            "Help string shown in status bar for this menu item"
        )

        self._file_menu.AppendSeparator()
        exit_item = self._file_menu.Append(wx.ID_EXIT)

        self.Bind(wx.EVT_MENU, self._on_hello_menu_item, hello_item)
        self.Bind(wx.EVT_MENU, self._on_exit_menu_item, exit_item)

    @property
    def text_box(self) -> str:
        return self._text_box.GetLabelText()

    @text_box.setter
    def text_box(self, new_text) -> None:
        self._text_box.SetLabelText(new_text)

    @property
    def eori_entry_box(self) -> str:
        return self._user_input_box.GetValue()

    @eori_entry_box.setter
    def eori_entry_box(self, new_text) -> None:
        self._user_input_box.SetValue(new_text)

    def _on_eori_box_entry(self, event: wx.Event) -> None:
        self._interface.eori_input_box_entry(self.eori_entry_box)

    def _on_exit_menu_item(self, event: wx.Event):
        self._interface.exit_pressed(event)

    def _on_hello_menu_item(self, event: wx.Event):
        wx.MessageBox("Sup Brah.")

    def _on_about_menu_item(self, event: wx.Event):
        wx.MessageBox(
            "Checks Importer EORI references are registered on TSS.",
            "About EORI Checker",
            wx.OK | wx.ICON_INFORMATION
        )
