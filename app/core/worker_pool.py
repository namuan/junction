import logging

from PyQt6.QtCore import QThreadPool, QRunnable, pyqtSlot, QObject, pyqtSignal


class LongRunningProcessOutput(QObject):
    result = pyqtSignal(dict)
    error = pyqtSignal(dict)


class LongRunningProcess(QRunnable):
    def __init__(self, callable, **kwargs):
        super().__init__()
        self.callable = callable
        self.signals = LongRunningProcessOutput()
        if "on_success" in kwargs:
            self.signals.result.connect(kwargs['on_success'])

        if "on_failure" in kwargs:
            self.signals.error.connect(kwargs['on_failure'])

    def success(self, output):
        self.signals.result.emit(output)

    def failure(self, output):
        self.signals.error.emit(output)

    @pyqtSlot()
    def run(self):
        logging.info("Running LongRunningProcess")
        self.callable()


class WorkerPool:
    thread_pool = QThreadPool()

    def schedule(self, worker):
        self.thread_pool.start(worker)

    def shutdown(self):
        self.thread_pool.clear()
        self.thread_pool.waitForDone(msecs=2)


pool = WorkerPool()
