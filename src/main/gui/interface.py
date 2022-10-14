import abc


class EoriGuiInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (all((
            hasattr(subclass, "exit_pressed"),
            callable(subclass.exit_pressed),
            hasattr(subclass, "input_box"),
            callable(subclass.input_box)
        )) or NotImplemented)

    @abc.abstractmethod
    def exit_pressed(self, event):
        raise NotImplementedError

    @abc.abstractmethod
    def input_box(self, event):
        raise NotImplementedError

