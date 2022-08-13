from app.sections.work_items.external.work_items_store import WorkItemsExternalStore
from app.sections.work_items.work_items_view import WorkItemsView


class WorkItemsController:
    def __init__(self, main_window, world):
        self.world = world
        self.main_window = main_window
        self.view = WorkItemsView(main_window.work_items_widget)
        self.external_store = WorkItemsExternalStore()
        self.world.events.app_started.connect(self.on_app_started)

    def on_app_started(self):
        work_items = self.external_store.fetch_items()
        self.view.render(work_items)