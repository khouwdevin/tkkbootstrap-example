import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

class SecondPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text ="Second Page", font = "TimesNewRoman 18 bold")
        label.place(anchor = "center", relx = 0.5, rely = 0.2)

        button = ttk.Button(self, text = "Change Page", bootstyle=(INFO, OUTLINE), command = lambda:controller.change_page(0))
        button.place(anchor = "center", relx = 0.5, rely = 0.5)
