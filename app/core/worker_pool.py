from PyQt5.QtCore import QThreadPool


class WorkerPool:
    thread_pool = QThreadPool()

    def schedule(self, worker):
        self.thread_pool.start(worker)

    def shutdown(self):
        self.thread_pool.clear()
        self.thread_pool.waitForDone(msecs=2)


pool = WorkerPool()
