from src.model.model import Model # pylint: disable=no-name-in-module,import-error
from src.view.view import View # pylint: disable=no-name-in-module,import-error
from src.controller.controller import Controller # pylint: disable=no-name-in-module,import-error

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    view = View(controller)
    
    view.start()