class ShortcutController:
    def __init__(self, parent_window, world):
        self.parent = parent_window
        self.world = world

        self.world.events.app_started.connect(self.init_items)

    def init_items(self):
        pass
