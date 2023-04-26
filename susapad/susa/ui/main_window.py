
import dataclasses as ds
import time

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.susa.controler import susapad
from susapad.susa.ui import alert_dialog, settings_window
from susapad.susa.ui.widgets import main_window
from susapad.susa.ui.widgets.common import window


class MainWindow(window.BaseWindow):

    def __init__(self, susapad):

        ## Configuration
        super().__init__(susapad)

        self.settings_window = None

        ## Configure Layout
        self.main_widget = main_window.WindowLayout(self)
        self.layout.addWidget(self.main_widget)

        ## Startup
        self.connect_to_susapad()

    
    @QtCore.Slot()
    def connect_to_susapad(self):
        port = self.susapad.find()
        if "" == port:
            # Todo: set it as false for production
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText("SusaPad não encontrado!")
            
            alert = alert_dialog.AlertDialog(self)
            alert.show()

        else:
            self.main_widget.group_button.main.set_found(True)
            self.main_widget.group_header.status.setText(f"SusaPad encontrado na porta {port}")

    @QtCore.Slot()
    def open_settings_window(self):
        if not self.settings_window:
            self.settings_window = settings_window.SettingsWindow(self)
            self.settings_window.show()

    @QtCore.Slot()
    def close_settings_window(self):
        self.settings_window.close()
        self.settings_window = None
