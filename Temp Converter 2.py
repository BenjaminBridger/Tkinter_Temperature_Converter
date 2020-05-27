from tkinter import *
from functools import partial
import random


class Converter:
    def __init__(self):
        # formatting variables
        background_colour = "light blue"

        # converter main screen gui
        self.converter_frame = Frame(bg=background_colour)
        self.converter_frame.grid()

        # temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter", bg=background_colour)
        self.temp_converter_label.grid(column=0, row=0)

        # help button
        self.help_button = Button(self.converter_frame, text='Help', command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print('Help')
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here123-----")


class Help:
    def __init__(self, partner):
        # formatting variables
        background_colour = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up help box ie. child window
        self.help_box = Toplevel()
        # release help button if help box X'd out of
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        # set up gui frame
        self.help_frame = Frame(self.help_box, bg=background_colour)
        self.help_frame.grid()

        # help heading
        self.how_heading = Label(self.help_frame, text="Help/Instructions", bg=background_colour)
        self.how_heading.grid(row=0)
        # dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", bg=background_colour,
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

        # help text
        self.help_text = Label(self.help_box, text="")
        self.help_text.grid(row=1)

    def close_help(self, partner):
        # put the button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
