from threading import Lock


class Observer():
    def update(self, *args, **kwargs):
        raise NotImplementedError


class Observable():
    def __init__(self):
        self.__observers = []
        self.__lock_observers = Lock()

    def has_observers(self):
        with self.__lock_observers:
            return len(self.__observers) > 0

    def attach(self, observer):
        assert isinstance(observer, Observer)
        with self.__lock_observers:
            if observer not in self.__observers:
                self.__observers.append(observer)

    def detach(self, observer):
        assert isinstance(observer, Observer)
        with self.__lock_observers:
            if observer in self.__observers:
                self.__observers.remove(observer)

    def notify(self, *args, **kwargs):
        with self.__lock_observers:
            for observer in self.__observers:
                observer.update(*args, **kwargs)
