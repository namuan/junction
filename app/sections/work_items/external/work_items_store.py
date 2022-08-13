import logging

from app.sections.work_items.work_item_entity import WorkItemEntity


class MockedWorkItemsExternalStore:
    def fetch_items(self):
        return [
            WorkItemEntity(
                number=1,
                title="WorkItem1",
                status="IN PROGRESS"
            ),WorkItemEntity(
                number=2,
                title="WorkItem2",
                status="COMPLETED"
            ),

        ]


class WorkItemsExternalStore():
    def __init__(self):
        # Later use some other property to setup delegated store
        self.delegated_store = MockedWorkItemsExternalStore()

    def fetch_items(self):
        logging.info("Fetching items from external store")
        return self.delegated_store.fetch_items()
