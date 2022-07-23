from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent

from app.sections.notes.notes_controller import NotesController


class NotesEvents(QObject):
    def __init__(self, parent, on_focus_out):
        super().__init__(parent)
        self.parent = parent
        self.on_focus_out = on_focus_out

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            self.on_focus_out()

        return super().eventFilter(source, event)


class NotesView:
    def __init__(self, parent):
        self.parent = parent
        self.controller = NotesController(self, self.parent.world)
        self.events = NotesEvents(self.parent, self.on_focus_out)

        # installing event filter
        self.parent.txtNotes.installEventFilter(self.events)

    def on_focus_out(self):
        self.controller.save_scratch_pad(self.parent.txtNotes.toPlainText())

    def render(self, scratch_note):
        self.parent.txtNotes.setPlainText(scratch_note)
