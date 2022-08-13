from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent

from app.data.notes_store import NotesEntity


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
    def __init__(self, world, txtNotes):
        self.world = world
        self.txtNotes = txtNotes
        self.events = NotesEvents(txtNotes, self.on_focus_out)

        # installing event filter
        self.txtNotes.installEventFilter(self.events)

    def on_focus_out(self):
        self.world.events.txt_notes_focus_out.emit(self.txtNotes.toPlainText())

    def render(self, scratch_note:NotesEntity):
        self.txtNotes.setPlainText(scratch_note.content)
