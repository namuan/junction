import logging
import sys
import traceback

from PyQt6.QtGui import QCloseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication

from app.controllers import (
    MainWindowController,
    ShortcutController,
)
from app.sections.work_items.work_items_controller import WorkItemsController
from app.generated.MainWindow_ui import Ui_MainWindow
from app.sections.notes.notes_controller import NotesController
from app.settings.app_world import AppWorld


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        world = AppWorld()

        # Initialise controllers
        self.main_controller = MainWindowController(self, world)
        self.shortcut_controller = ShortcutController(self, world)
        self.notes_controller = NotesController(self, world)
        self.work_items_controller = WorkItemsController(self, world)

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
            QApplication.instance().exit(0)
        except:
            pass
