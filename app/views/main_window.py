import logging
import sys
import traceback

from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, qApp

from app.controllers import (
    MainWindowController,
    ShortcutController,
)
from app.generated.MainWindow_ui import Ui_MainWindow
from app.sections.notes.notes_controller import NotesController
from app.settings.app_world import AppWorld


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.world = AppWorld()

        # Initialise controllers
        self.main_controller = MainWindowController(self, self.world)
        self.shortcut_controller = ShortcutController(self, self.world)
        self.notes_controller = NotesController(self, self.world)

        # Initialise Sub-Systems
        sys.excepthook = MainWindow.log_uncaught_exceptions

    # Main Window events
    def resizeEvent(self, event):
        self.main_controller.after_window_loaded()

    @staticmethod
    def log_uncaught_exceptions(cls, exc, tb) -> None:
        logging.critical("".join(traceback.format_tb(tb)))
        logging.critical("{0}: {1}".format(cls, exc))

    def closeEvent(self, event: QCloseEvent):
        logging.info("Received close event")
        event.accept()
        self.main_controller.shutdown()
        try:
            qApp.exit(0)
        except:
            pass
