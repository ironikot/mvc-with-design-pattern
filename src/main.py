from src.lib.BeatContoller import BeatController
from src.lib.BeatModel import BeatModel


def main():
    model = BeatModel()
    controller = BeatController(model)


if __name__ == "__main__":
    main()

