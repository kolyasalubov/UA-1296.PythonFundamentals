from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time
import os


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("CAT")

        # Center the window
        self.center_window()

        # Set icon
        self.set_icon()

        # Initialize game parameters
        self.initialize_game()

        # Set default cat avatar
        self.set_avatar("cat1")

        # Create menu
        self.create_menu()

        # Create widgets
        self.create_widgets()

        # Start the game update
        self.update_clock()

    # Define constants
    MAX_HEALTH = 100
    MAX_LEISURE = 100
    HEALTH_DECREASE = 3
    LEISURE_DECREASE = 3
    HEALTH_INCREASE = 10
    LEISURE_INCREASE = 10
    LOSS_THRESHOLD = 0
    WIN_THRESHOLD = 100
    RESTART_THRESHOLD = 50
    TIK = 10000

    def center_window(self):
        """Centers the window on the screen"""
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.wm_geometry(f"+{int(x)}+{int(y)}")

    def create_menu(self):
        mainmenu = Menu(self.root)  # Create the main menu
        self.root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)  # Create a File submenu
        filemenu.add_command(label="New", command=self.new_game)  # Add New command
        filemenu.add_command(
            label="Open...", command=self.open_game
        )  # Add Open command
        filemenu.add_separator()  # Add separator
        filemenu.add_command(label="Exit", command=self.exit_game)  # Add Exit command

        helpmenu = Menu(mainmenu, tearoff=0)  # Create a Help submenu
        helpmenu.add_command(
            label="About", command=self.show_about
        )  # Add About command

        catmenu = Menu(mainmenu, tearoff=0)  # Add Cat selection menu
        catmenu.add_command(label="Cat 1", command=lambda: self.set_avatar("cat1"))
        catmenu.add_command(label="Cat 2", command=lambda: self.set_avatar("cat2"))
        catmenu.add_command(label="Cat 3", command=lambda: self.set_avatar("cat3"))

        mainmenu.add_cascade(label="File", menu=filemenu)  # Add File menu to main menu
        mainmenu.add_cascade(label="Help", menu=helpmenu)  # Add Help menu to main menu
        mainmenu.add_cascade(
            label="Cat", menu=catmenu
        )  # Add Cat selection menu to main menu

    def new_game(self):
        """Start a new game"""
        self.initialize_game()
        self.l1.configure(text=f"health - {self.healthCat}%")
        self.l2.configure(text=f"leisure - {self.leisureCat}%")
        self.l3.configure(text="your cat is alive")
        mb.showinfo("New Game", "New game started!")

    def open_game(self):
        """Open an existing game (not implemented yet)"""
        mb.showinfo("Open", "This feature is not implemented yet.")

    def exit_game(self):
        """Exit the game"""
        self.root.quit()

    def show_about(self):
        """Show about information"""
        mb.showinfo("About", "This is a simple Cat Game created using Tkinter.")

    def set_icon(self):
        """Sets the window icon"""
        icon = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "img", "iconCat.png")
        )
        self.root.iconphoto(False, icon)

    def set_avatar(self, cat_type):
        """Sets the cat avatar based on selected cat type"""
        avatar_map = {
            "cat1": "Cat.png",
            "cat2": "Cat2.png",  # Path to the second cat image
            "cat3": "Cat3.png",  # Path to the third cat image
        }

        if hasattr(self, "logo_label"):
            self.logo_label.destroy()  # Remove old avatar

        self.logo = PhotoImage(
            file=os.path.join(os.path.dirname(__file__), "img", avatar_map[cat_type])
        )
        self.logo_label = Label(self.root, image=self.logo)
        self.logo_label.grid(row=2, column=2, columnspan=5, rowspan=5)

    def initialize_game(self):
        """Initializes game parameters"""
        self.game = 3
        self.healthCat = self.MAX_HEALTH / 2
        self.leisureCat = self.MAX_LEISURE / 2

    def create_widgets(self):
        """Creates all widgets for the game"""
        self.label2 = Label(
            self.root, width=27, height=3, text="It is your Cat", font="Arial"
        )
        self.label2.grid(row=0, column=2, columnspan=3, rowspan=2)

        # Dictionary of buttons and corresponding methods
        button_actions = {
            "feed": self.health,
            "caress": self.leisure,
            "train": self.health,
            "play": self.leisure,
        }

        # Create buttons dynamically using a helper function
        self.create_buttons(button_actions)

        self.l1 = Label(
            self.root, width=20, height=3, text=f"health - {self.healthCat}%"
        )
        self.l1.grid(row=6, column=0)

        self.l2 = Label(
            self.root, width=20, height=2, text=f"leisure - {self.leisureCat}%"
        )
        self.l2.grid(row=7, column=0)

        self.l3 = Label(self.root, width=20, height=2, text="your cat is alive")
        self.l3.grid(row=7, column=3)

    def create_buttons(self, actions):
        """Helper function to create buttons dynamically"""
        row = 2
        for text, action in actions.items():
            button = ttk.Button(self.root, width=15, text=text, command=action)
            button.grid(row=row, column=0)
            row += 1

    def update_clock(self):
        """Updates the game state every second"""
        now = time.strftime("%H:%M:%S")
        self.root.after(self.TIK, self.update_clock)
        self.root.after(self.TIK, self.heppimin)

    def heppimin(self):
        """Updates the health and leisure of the cat"""
        if (
            self.healthCat <= self.LOSS_THRESHOLD
            or self.leisureCat <= self.LOSS_THRESHOLD
        ):
            answer = mb.askyesno(
                title="You lost", message="You lost!!!\n Do you want to play again?"
            )
            if answer:
                self.healthCat += self.RESTART_THRESHOLD
                self.leisureCat += self.RESTART_THRESHOLD
            else:
                self.game = 1
        elif self.healthCat >= self.MAX_HEALTH and self.leisureCat >= self.MAX_LEISURE:
            answer2 = mb.askyesno(
                title="You win", message="You win!!!\n Do you want to play again?"
            )
            if answer2:
                self.healthCat -= self.RESTART_THRESHOLD
                self.leisureCat -= self.RESTART_THRESHOLD
            else:
                self.game += 1

        # Decrease health and leisure
        self.healthCat -= self.HEALTH_DECREASE
        self.leisureCat -= self.LEISURE_DECREASE

        self.l1.configure(text=f"health - {self.healthCat}%")
        self.l2.configure(text=f"leisure - {self.leisureCat}%")

    def health(self):
        """Feeds the cat - increases health, decreases leisure"""
        self.healthCat += self.HEALTH_INCREASE
        self.leisureCat -= self.LEISURE_DECREASE
        self.l1.configure(text=f"health - {self.healthCat}%")
        self.l2.configure(text=f"leisure - {self.leisureCat}%")
        self.l3.configure(text="your cat is healthy")
        if self.leisureCat <= self.MAX_LEISURE / 10:
            mb.showerror("sorry", "your cat is sad")
            self.leisureCat += self.MAX_LEISURE / 5

    def leisure(self):
        """Caresses the cat - decreases health, increases leisure"""
        self.healthCat -= self.HEALTH_DECREASE
        self.leisureCat += self.LEISURE_INCREASE
        self.l1.configure(text=f"health - {self.healthCat}%")
        self.l2.configure(text=f"leisure - {self.leisureCat}%")
        self.l3.configure(text="your cat is having fun")
        if self.healthCat <= self.MAX_HEALTH / 10:
            mb.showerror("sorry", "your cat is ill")
            self.healthCat += self.MAX_HEALTH / 5


if __name__ == "__main__":
    root = Tk()
    game = Game(root)
    root.mainloop()
