import logging

from app.settings.app_world import AppWorld


class MainWindowController:
    def __init__(self, parent_window, world):
        self.parent = parent_window
        self.initial_load = True
        self.world: AppWorld = world
        self.init_app()

    def init_app(self):
        self.world.init()
        self.world.init_logger()
        if self.world.geometry():
            self.parent.restoreGeometry(self.world.geometry())
        if self.world.window_state():
            self.parent.restoreState(self.world.window_state())

    def save_settings(self):
        logging.info("Saving settings for Main Window")
        self.world.save_window_state(
            geometry=self.parent.saveGeometry(), window_state=self.parent.saveState()
        )

    def shutdown(self):
        self.save_settings()

    def after_window_loaded(self):
        if not self.initial_load:
            return

        self.initial_load = False
        self.on_first_load()

    def on_first_load(self):
        self.world.started()
