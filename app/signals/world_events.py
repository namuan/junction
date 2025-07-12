from PyQt6.QtCore import QObject, pyqtSignal


class WorldEvents(QObject):
    app_started = pyqtSignal()
    txt_notes_focus_out = pyqtSignal(str)
