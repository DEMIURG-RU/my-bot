from tkinter import *
from main_th import get_response, bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

#    head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10)
#    head_label.place(relwidth=1)

#    line = Label(self.window, width=450, bg=BG_GRAY)
#   line.place(relwidth=1, rely=0.07, relheight=0.012)

#    self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
#    self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
#    self.text_widget.configure(cursor="arrow", state=DISABLED)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
