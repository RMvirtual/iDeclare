import wx
from src.main.tss.api.model import TssApi
from src.main.tss.api.environment.environments import ApiEnvironment
from src.main.gui.interface import EoriGuiInterface
from src.main.gui.gui import EoriGui


class TssGuiController(EoriGuiInterface):
    def __init__(self, environmment: ApiEnvironment):
        self._app = wx.App()
        self._api = TssApi(environmment)
        self._gui = EoriGui(self)

    def exit_pressed(self, event):
        self._gui.Close(True)

    def input_box(self, event):
        print("ITE....")

    def run(self):
        self._gui.Show()
        self._app.MainLoop()
