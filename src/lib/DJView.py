from src.lib.BPMObserver import BPMObserver
from src.lib.BeatObserver import BeatObserver
import tkinter as tk
from tkinter import ttk
from src.lib.Globals import *


class DJView(BeatObserver, BPMObserver):
    def __init__(self, controller, model):
        self.__model = model
        self.__controller = controller
        self.__current_BPM = 90
        self.__view_app = tk.Tk()
        self.__control_app = None
        self.__bpm_label = None
        self.bpm_string = tk.StringVar()
        self.bpm_string.set(CURRENT_BPM + str(self.__current_BPM))
        self.bpm_input = tk.StringVar()
        # modelをObserverに登録する
        self.__model.registerBeatObserver(self)
        self.__model.registerBPMObserver(self)

    # 作成画面１
    def createView(self):
        view_app = self.__view_app
        view_app.title(VIEW_APP_NAME)
        view_app.geometry(VIEW_WINDOW_SIZE + VIEW_WINDOW_LOCATION)
        canvas = ttk.Frame(view_app, padding=PADDING_MAIN)
        canvas.grid(column=0, row=0, sticky="news")
        canvas.columnconfigure(0, weight=1)
        canvas.rowconfigure(0, weight=1)
        bpm_label = tk.Label(canvas, justify="center", font=FONT, textvariable=self.bpm_string)
        bpm_label.grid(column=0, row=0, sticky="EW")
        bpm_label.columnconfigure(0, weight=1)
        bpm_label.rowconfigure(0, weight=1)
        view_app.mainloop(1)

    # 作成画面２
    def createControl(self):
        self.__control_app = tk.Tk()
        self.__control_app.title(CONTROL_APP_NAME)
        self.__control_app.geometry(CTRL_WINDOW_SIZE + CTRL_WINDOW_LOCATION)
        main_frame = ttk.Frame(self.__control_app, padding=PADDING_MAIN)
        main_frame.grid(column=0, row=0, sticky="news")

        self.__bpm_label = ttk.Label(main_frame, text=ENTER_BPM, font=FONT)
        self.__bpm_label.grid(column=0, row=0, sticky="w")

        self.bpm_input = ttk.Entry(main_frame, font=FONT, textvariable=self.bpm_input)
        self.bpm_input.grid(column=1, row=0, sticky="e")

        # 引数を渡すためのlambda
        self.set_btn = ttk.Button(main_frame, text=SET_BPM,
                                  command=lambda: [self.bpm_input.update(), self.__controller.setBPM(
                                      # 3項演算子によるパース（別出しにしても良いかもしれない）
                                      int(self.bpm_input.get()) if str(self.bpm_input.get()).isdigit()
                                      else self.__current_BPM)])
        self.set_btn.grid(column=0, row=1, pady="10", padx="10", sticky="we")
        self.set_btn.columnconfigure(0, weight=1)
        self.set_btn.rowconfigure(0, weight=1)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(column=0, row=1, sticky="news", columnspan=2, rowspan=2)
        increase_btn = ttk.Button(button_frame, text=INCREASE_BTN, command=self.__controller.increaseBPM)
        increase_btn.grid(column=1, row=2, pady="10", padx="10", sticky="we")
        increase_btn.columnconfigure(0, weight=1)
        increase_btn.rowconfigure(0, weight=1)

        decrease_btn = ttk.Button(button_frame, text=DECREASE_BTN, command=self.__controller.decreaseBPM)
        decrease_btn.grid(column=0, row=2, pady="10", padx="10", sticky="we")
        decrease_btn.columnconfigure(0, weight=1)
        decrease_btn.rowconfigure(0, weight=1)

        self.__control_app.columnconfigure(0, weight=1)
        self.__control_app.rowconfigure(0, weight=1)

        self.__control_app.mainloop(0)

    def updateBeat(self):
        pass

    def updateBPM(self):
        bpm = self.__model.getBPM()
        self.bpm_string.set(CURRENT_BPM + str(bpm))

