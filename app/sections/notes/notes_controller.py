from app.sections.notes.notes_view import NotesView


class NotesController:
    def __init__(self, main_window, world):
        self.notes_view = NotesView(world, main_window.txtNotes)
        self.world = world
        self.world.events.app_started.connect(self.on_app_started)
        self.world.events.txt_notes_focus_out.connect(self.save_scratch_pad)

    def on_app_started(self):
        scratch_note = self.world.notes_store.get_scratch_note()
        self.notes_view.render(scratch_note)

    def save_scratch_pad(self, plain_text_notes):
        self.world.notes_store.update_scratch_note(plain_text_notes)
