import logging
import time

from app.core.worker_pool import pool, LongRunningProcess
from app.sections.work_items.external.work_itemsapi_type import WorkItemsApiType
from app.sections.work_items.work_item_entity import WorkItemEntity


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


class MockedWorkItemsExternalStore(LongRunningProcess):
    def __init__(self, api_type, **kwargs):
        self.api_type_func = {
            WorkItemsApiType.FETCH_ITEMS: self.fetch_items,
            WorkItemsApiType.FETCH_SINGLE_ITEM: self.fetch_single_item,
        }
        self.args = kwargs
        super().__init__(self.api_type_func.get(api_type), **kwargs)

    def fetch_items(self):
        time.sleep(5)
        logging.info("Received response from external API")
        self.success(dict(result=mocked_data()))

    def fetch_single_item(self):
        work_item_number = self.args.get("work_item_number")
        time.sleep(5)
        logging.info(f"Received response from external API for {work_item_number}")
        self.success(dict(result=[WorkItemEntity(
            number=99,
            title="FooBar",
            status="BACKLOG"
        )]))


class WorkItemsExternalStore:
    def fetch_items(self, **kwargs):
        self._schedule(WorkItemsApiType.FETCH_ITEMS, **kwargs)

    def fetch_work_item(self, **kwargs):
        self._schedule(WorkItemsApiType.FETCH_SINGLE_ITEM, **kwargs)

    def _schedule(self, api_type: WorkItemsApiType, **kwargs):
        logging.info(f"Scheduling {api_type}")
        pool.schedule(MockedWorkItemsExternalStore(api_type, **kwargs))
