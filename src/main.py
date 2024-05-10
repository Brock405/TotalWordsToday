import keyboard
import customtkinter




# ---------------------------gui-----------------------------



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("CTk example")

        self.howManyKeysArePressed = 0
        self.detectsIfButtonPressedDown()

        # add widgets to app
        self.wordsTypedTodayCounter = customtkinter.CTkLabel(self, text=str(self.howManyKeysArePressed), fg_color="transparent")
        self.wordsTypedTodayCounter.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        

    # add methods to app
    def detectsIfButtonPressedDown(self):
        # detects if key pressed down
        keyEvent = keyboard.read_event()
        if keyEvent.event_type == keyboard.KEY_UP:
            self.howManyKeysArePressed += 1
            print(self.howManyKeysArePressed) 






app = App()
app.mainloop()
