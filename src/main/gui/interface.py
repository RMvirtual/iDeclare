import abc


class EoriGuiInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (all((
            hasattr(subclass, "exit_pressed"),
            callable(subclass.exit_pressed),
            hasattr(subclass, "eori_input_box_entry"),
            callable(subclass.eori_input_box_entry)
        )) or NotImplemented)

    @abc.abstractmethod
    def exit_pressed(self, event):
        raise NotImplementedError

    @abc.abstractmethod
    def eori_input_box_entry(self, event):
        raise NotImplementedError

