from typing import List

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QListWidget

from app.sections.work_items.work_item_entity import WorkItemEntity
from app.widgets.work_item import WorkItemWidget


class WorkItemsView:
    def __init__(self, work_items_widget):
        self.work_items_widget: QListWidget = work_items_widget

    def render(self, work_items: List[WorkItemEntity]):
        self.work_items_widget.clear()
        for wi in work_items:
            work_item_widget = WorkItemWidget(self.work_items_widget)
            work_item_widget.set_data(wi)
            work_item_widget_item = QtWidgets.QListWidgetItem(self.work_items_widget)
            work_item_widget_item.setSizeHint(work_item_widget.sizeHint())

            self.work_items_widget.addItem(work_item_widget_item)
            self.work_items_widget.setItemWidget(work_item_widget_item, work_item_widget)
