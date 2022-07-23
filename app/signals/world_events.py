from PyQt5.QtCore import QObject, pyqtSignal


class WorldEvents(QObject):
    app_started = pyqtSignal()
