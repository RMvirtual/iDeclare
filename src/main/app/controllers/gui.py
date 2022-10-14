import re
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

    def eori_input_box_entry(self, text):
        if self._is_valid_gb_eori_format(text):
            if self._api.is_eori_valid(text):
                self._gui.text_box = "EORI NO is TSS registered."

            else:
                self._gui.text_box = "NOT REGISTERED."

        else:
            self._gui.text_box = (
                "INVALID EORI FORMAT (must be GB followed by 12 digits).")

    def run(self):
        self._gui.Show()
        self._app.MainLoop()

    def _is_valid_gb_eori_format(self, eori_no):
        return bool(re.fullmatch(r"GB\d{12}", eori_no))
