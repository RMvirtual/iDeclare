import unittest
import wx

from src.main.gui.gui import EoriGui


class TestGUI(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_launch_gui(self):
        app = wx.App()
        gui = EoriGui(app)
        gui.Show()
        app.MainLoop()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
