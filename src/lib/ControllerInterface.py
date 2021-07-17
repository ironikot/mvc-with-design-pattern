from abc import ABCMeta, abstractmethod


class ControllerInterface(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def increaseBPM(self):
        pass

    @abstractmethod
    def decreaseBPM(self):
        pass

    @abstractmethod
    def setBPM(self, bpm):
        pass

