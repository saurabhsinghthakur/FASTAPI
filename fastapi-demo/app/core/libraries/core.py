import importlib

class Core():
    def __init__(self) -> None:
        pass

    def load_module(self, module_path, module_name):
        current_module = importlib.import_module(module_path)
        class_name = getattr(current_module, module_name.title())()
        return class_name