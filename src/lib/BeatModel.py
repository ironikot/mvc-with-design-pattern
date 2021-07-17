from src.lib.BeatModelInterface import BeatModelInterface


class BeatModel(BeatModelInterface):

    def __init__(self):
        self.bpm = 90
        self.is_stop = False
        self.__beatObservers = []
        self.__bpmObservers = []
        super(BeatModel, self).__init__()

    def initialize(self):
        print("load wav file")

    def on(self):
        pass

    def off(self):
        self.is_stop = True

    def run(self):
        print("run")

    def setBPM(self, bpm):
        print(bpm)
        print(type(bpm))
        self.bpm = bpm
        self.notifyBPMObservers()

    def getBPM(self):
        return self.bpm

    def registerBeatObserver(self, BeatObserver):
        self.__beatObservers.append(BeatObserver)

    def notifyBeatObservers(self):
        for o in self.__beatObservers:
            o.update()

    def removeBeatObserver(self, BeatObserver):
        self.__beatObservers.remove(BeatObserver)

    def registerBPMObserver(self, BPMObserver):
        self.__bpmObservers.append(BPMObserver)

    def notifyBPMObservers(self):
        for o in self.__bpmObservers:
            o.updateBPM()

    def removeBPMObserver(self, BPMObserver):
        self.__bpmObservers.remove(BPMObserver)

    def playBeat(self):
        print("play!")

    def stopBeat(self):
        print("stop!")

