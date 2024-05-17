import customtkinter
import keyboard
import threading

howManyKeysArePressed = 0

def detectsIfButtonPressedDown():
    global howManyKeysArePressed
    while True:
        # detects if key pressed down
        keyEvent = keyboard.read_event()
        if keyEvent.event_type == keyboard.KEY_UP:
            howManyKeysArePressed += 1
            print(howManyKeysArePressed)

threadToCheckIfButtonPressed = threading.Thread(target=detectsIfButtonPressedDown)
threadToCheckIfButtonPressed.start()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x720")
        self.title("Total Words Today")

        # add widgets to app
        self.wordsTypedTodayCounter = customtkinter.CTkLabel(self, text=str(howManyKeysArePressed), fg_color="transparent")
        self.wordsTypedTodayCounter.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    # add methods to app
    def updateCharacterCounter(self):
        self.wordsTypedTodayCounter.configure(text = str(howManyKeysArePressed))
        self.after(100, self.updateCharacterCounter)



app = App()
app.after(100, app.updateCharacterCounter)
app.mainloop()
