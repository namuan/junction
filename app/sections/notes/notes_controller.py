class NotesController:
    def __init__(self, view, world):
        self.view = view
        self.world = world
        self.world.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        scratch_note = self.world.notes_store.get_scratch_note()
        self.view.render(scratch_note)

    def save_scratch_pad(self, plain_text_notes):
        self.world.notes_store.update_scratch_note(plain_text_notes)
