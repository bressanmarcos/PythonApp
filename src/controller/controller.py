import time
import re
import json


from common.misc import Observer, Observable  # pylint: disable=no-name-in-module,import-error

class Controller(Observer, Observable):

    def __init__(self, model):
        Observer.__init__(self)
        Observable.__init__(self)
        self.model = model

    def update(self, *args, **kwargs):
        """Proxies updates to Observers"""
        self.notify(*args, **kwargs)
