from tkinter import *
from functools import partial


class Converter:
    def __init__(self):
        self.master = master
        # formatting variables
        bg_colour = "light blue"

        # top header
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)
        # add functions to top header
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Save', command=self.save)
        self.file_menu.add_command(label='Export', command=self.export)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.menu_bar.add_command(label="Settings", command=self.settings)
        self.menu_bar.add_command(label="Help", command=self.help)

        # Function buttons
        self.export_button = Button(self.master, text="Export ", padx=10, command=self.export)
        self.export_button.grid(column=0, row=1)

        self.save_button = Button(self.master, text="Save ", padx=10, command=self.save)
        self.save_button.grid(column=1, row=1)

        self.save2_button = Button(self.master, text="Save 2", padx=10, command=self.save)
        self.save2_button.grid(column=2, row=1)

        # Input boxes
        self.input_c = Entry(master, width=7)
        self.input_c.grid(column=0, row=2)

        self.input_f = Entry(master, width=7)
        self.input_f.grid(column=1, row=2)

        self.input_k = Entry(master, width=7)
        self.input_k.grid(column=2, row=2)

    def save(self):
        print("Save function")

    def export(self):
        print('export')

    def settings(self):
        print('settings')

    def help(self):
        print('help')
        help_menu = Help()
        # help_menu.help_text.configure(text="Help text goes here xyz ---")


# class Help:
#     def __init__(self):
#         print("Help class")

class Help:
    def __init__(self, partner):
        # formatting variables
        background_colour = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

    #     # set up help box ie. child window
    #     self.help_box = Toplevel()
    #     # release help button if help box X'd out of
    #     self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
    #     # set up gui frame
    #     self.help_frame = Frame(self.help_box, bg=background_colour)
    #     self.help_frame.grid()
    #
    #     # help heading
    #     self.how_heading = Label(self.help_frame, text="Help/Instructions", bg=background_colour)
    #     self.how_heading.grid(row=0)
    #     # dismiss button (row 2)
    #     self.dismiss_btn = Button(self.help_frame, text="Dismiss", bg=background_colour,
    #                               command=partial(self.close_help, partner))
    #     self.dismiss_btn.grid(row=2, pady=10)
    #
    #     # help text
    #     self.help_text = Label(self.help_box, text="")
    #     self.help_text.grid(row=1)
    #
    # def close_help(self, partner):
    #     # put the button back to normal
    #     partner.help_button.config(state=NORMAL)
    #     self.help_box.destroy()


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    master = Tk()
    master.title("Temperature Converter")
    # master.geometry("200x300")
    main_screen = Converter()

    master.mainloop()
