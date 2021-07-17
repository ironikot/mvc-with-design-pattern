from abc import ABCMeta, abstractmethod


class BeatModelInterface(metaclass=ABCMeta):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def setBPM(self, bpm):
        pass

    @abstractmethod
    def getBPM(self):
        pass

    @abstractmethod
    def registerBeatObserver(self, BeatObserver):
        pass

    @abstractmethod
    def removeBeatObserver(self, BeatObserver):
        pass

    @abstractmethod
    def registerBPMObserver(self, BPMObserver):
        pass

    @abstractmethod
    def removeBPMObserver(self, BPMObserver):
        pass

