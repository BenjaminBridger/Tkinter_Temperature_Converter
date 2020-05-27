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
        self.help_button.grid(row=1, column=0)
        # Settings Button
        self.settings_button = Button(self.converter_frame, text='Settings', command=self.settings)
        self.settings_button.grid(row=2, column=0)

        # top header
        # self.menu_bar = Menu(self.converter_frame)
        # self.converter_frame.config(menu=self.menu_bar)
        # add functions to top header
        # self.file_menu = Menu(self.menu_bar, tearoff=0)
        # self.file_menu.add_command(label='Save', command=self.save)
        # self.file_menu.add_command(label='Export', command=self.export)
        # self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        #
        # self.menu_bar.add_command(label="Settings", command=self.settings)
        # self.menu_bar.add_command(label="Help", command=self.help)

    def help(self):
        print('Help')
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here123-----")

    def settings(self):
        print('Settings')
        get_settings = Settings(self)
        get_settings.settings_text.configure(text="Settings text goes here234--")

# potato
print('---------d-dsefsefjh4u----')
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


class Settings:
    def __init__(self, partner):
        # formatting variables
        background_colour = "green"

        # disable settings button
        partner.settings_button.config(state=DISABLED)

        # set up help box ie. child window
        self.settings_box = Toplevel()
        # release settings button if settings box X'd out of
        self.settings_box.protocol('WM_DELETE_WINDOW', partial(self.close_settings, partner))
        # set up gui frame
        self.settings_frame = Frame(self.settings_box, bg=background_colour)
        self.settings_frame.grid()

        # settings heading
        self.settings_heading = Label(self.settings_frame, text="settings/Instructions", bg=background_colour)
        self.settings_heading.grid(row=0)
        # dismiss button (row 2)
        self.dismiss_btn = Button(self.settings_frame, text="Dismiss", bg=background_colour,
                                  command=partial(self.close_settings, partner))
        self.dismiss_btn.grid(row=2, pady=10)

        # settings text
        self.settings_text = Label(self.settings_box, text="")
        self.settings_text.grid(row=1)

    def close_settings(self, partner):
        # put the button back to normal
        partner.settings_button.config(state=NORMAL)
        self.settings_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
