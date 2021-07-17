from abc import ABCMeta, abstractmethod


class BeatObserver(metaclass=ABCMeta):
    @abstractmethod
    def updateBeat(self):
        pass

