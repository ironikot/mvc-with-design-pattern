from src.lib.ControllerInterface import ControllerInterface
from src.lib.BeatModelInterface import BeatModelInterface
from src.lib.DJView import DJView


class BeatController(ControllerInterface):

    def __init__(self, model):
        self.model = model
        view = DJView(self, self.model)
        view.createView()
        view.createControl()

    def start(self):
        pass

    def stop(self):
        pass

    def increaseBPM(self):
        bpm = (self.model.getBPM())+1
        self.model.setBPM(bpm)
        print("+ BPM!", bpm)

    def decreaseBPM(self):
        bpm = (self.model.getBPM())-1
        self.model.setBPM(bpm)
        print("- BPM", bpm)

    def setBPM(self, bpm):
        self.model.setBPM(bpm)
