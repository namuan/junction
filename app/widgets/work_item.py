from PyQt6 import QtWidgets, QtGui

from app.sections.work_items.work_item_entity import WorkItemEntity


class WorkItemWidget(QtWidgets.QWidget):
    url: str

    def __init__(self, parent=None):
        super(WorkItemWidget, self).__init__(parent)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.top_row_layout = QtWidgets.QHBoxLayout()

        self.lbl_icon = QtWidgets.QLabel()
        self.lbl_ticket_number = QtWidgets.QLabel()
        self.lbl_ticket_status = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_ticket_status.setFont(font)
        self.lbl_ticket_status.setFlat(True)
        self.lbl_ticket_status.setDisabled(True)
        self.lbl_ticket_status.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding
        )
        self.lbl_ticket_status.setStyleSheet('''
            QPushButton {
                padding: -5px;
            }
        ''')
        self.lbl_ticket_title = QtWidgets.QLabel()
        self.lbl_icon.setPixmap(QtGui.QPixmap(":/images/notifier-48.png"))

        self.top_row_layout.addWidget(self.lbl_icon)
        self.top_row_layout.addWidget(self.lbl_ticket_number)
        self.top_row_layout.addWidget(self.lbl_ticket_status)

        self.vertical_layout.addLayout(self.top_row_layout)
        self.vertical_layout.addWidget(self.lbl_ticket_title)

        self.setLayout(self.vertical_layout)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_ticket_number.setFont(font)

    def set_data(self, work_item: WorkItemEntity):
        self.lbl_ticket_number.setText(str(work_item.number))
        self.lbl_ticket_status.setText(work_item.status)
        self.lbl_ticket_title.setText(work_item.title)
        self.url = work_item.url
        self.setToolTip(work_item.title)

    def get_data(self):
        return self.lbl_ticket_number.text(), self.lbl_ticket_title.text(), self.url
