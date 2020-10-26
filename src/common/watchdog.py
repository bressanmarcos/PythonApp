import time
from threading import Thread


class Watchdog(Thread):
    def __init__(self, name, on_timeout, timeout=5, sleep_time=0.5):
        Thread.__init__(
            self, name=f'{self.__class__.__name__}:{name}', daemon=True)
        self.__running = False
        self.timeout = timeout
        self.time = time.time()
        self.on_timeout = on_timeout
        self.sleep_time = sleep_time

    def start(self):
        self.__running = True
        Thread.start(self)

    def reset(self):
        self.time = time.time()

    def terminate(self):
        self.__running = False

    def is_running(self):
        return self.__running

    def run(self):
        while self.is_running():
            if time.time() - self.time > self.timeout:
                self.on_timeout()
                self.reset()

            time.sleep(self.sleep_time)
