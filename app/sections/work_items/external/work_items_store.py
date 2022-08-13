import logging
import time

from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot

from app.core.worker_pool import pool
from app.sections.work_items.external.work_itemsapi_type import WorkItemsApiType
from app.sections.work_items.work_item_entity import WorkItemEntity


class LongRunningProcessOutput(QObject):
    result = pyqtSignal(dict)
    error = pyqtSignal(dict)


def mocked_data():
    return [
        WorkItemEntity(
            number=1,
            title="WorkItem1",
            status="IN PROGRESS"
        ), WorkItemEntity(
            number=2,
            title="WorkItem2",
            status="COMPLETED"
        ),
    ]


class MockedWorkItemsExternalStore(QRunnable):
    def __init__(self, api_type, **kwargs):
        super().__init__()
        self.api_type = api_type
        self.args = kwargs
        self.signals = LongRunningProcessOutput()
        self.api_type_func = {
            WorkItemsApiType.FETCH_ITEMS: self.fetch_items,
        }

    def fetch_items(self):
        time.sleep(5)
        self.signals.result.emit(dict(result=mocked_data()))

    @pyqtSlot()
    def run(self):
        logging.info("Running MockedWorkItemsExternalStore")
        self.api_type_func.get(self.api_type)()


class WorkItemsExternalStore:
    def fetch_items(self, **kwargs):
        logging.info("Fetching items from external store")
        delegated_store = MockedWorkItemsExternalStore(WorkItemsApiType.FETCH_ITEMS, **kwargs)
        delegated_store.signals.result.connect(kwargs['on_success'])
        delegated_store.signals.error.connect(kwargs['on_failure'])
        pool.schedule(delegated_store)
