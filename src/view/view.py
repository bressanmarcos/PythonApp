import os

from common.misc import Observer  # pylint: disable=no-name-in-module,import-error


class View(Observer):

    def __init__(self, controller=None):
        Observer.__init__(self)
        if controller is not None:
            self.set_controller(controller)

    def set_controller(self, controller):
        self.controller = controller
        controller.attach(self)

    def start(self):
        try:
            self.main()
        except (EOFError, KeyboardInterrupt):
            self.exit()

    def main(self):
        pass

    def exit(self):
        os.sys.exit(0)

    def update(self, *args, **kwargs):
        pass
