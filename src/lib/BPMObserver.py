from abc import ABCMeta, abstractmethod


class BPMObserver(metaclass=ABCMeta):
    @abstractmethod
    def updateBPM(self):
        pass
