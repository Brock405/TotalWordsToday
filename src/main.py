import customtkinter
import keyboard
import threading
from tkinter import* # type: ignore

howManyKeysArePressed = 0
howManyWordsAreTyped = 0

def detectsIfButtonPressedDown():
    global howManyKeysArePressed
    global howManyWordsAreTyped
    while True:
        # detects if key pressed down
        keyEvent = keyboard.read_event()
        if keyEvent.event_type == keyboard.KEY_UP:
            howManyKeysArePressed += 1
            print(howManyKeysArePressed)
            if keyEvent.name == 'space':
                howManyWordsAreTyped += 1


threadToCheckIfButtonPressed = threading.Thread(target=detectsIfButtonPressedDown)
threadToCheckIfButtonPressed.start()

# --------------------------------gui-----------------------------------------

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("580x420")
        self.title("Total Words Today") 

        #  ------ add widgets to app ------

        self.charactersTypedTodayText = customtkinter.CTkLabel(self, font=('Roboto', 20), text="Key presses today: ", fg_color="transparent")
        self.charactersTypedTodayText.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)
        self.wordsTypedTodayText = customtkinter.CTkLabel(self, font=('Roboto', 20), text="Words typed today: ", fg_color="transparent")
        self.wordsTypedTodayText.place(relx=0.8, rely=0.1,  anchor=customtkinter.CENTER)

        # character counter
        self.charactersTypedTodayCounter = customtkinter.CTkLabel(self, font=('Roboto', 30, 'bold'), text=str(howManyKeysArePressed), fg_color="transparent")
        self.charactersTypedTodayCounter.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)
        # word counter
        self.wordsTypedTodayCounter = customtkinter.CTkLabel(self, font=('Roboto', 30, 'bold'), text= str(howManyWordsAreTyped), fg_color="transparent")
        self.wordsTypedTodayCounter.place(relx=0.8, rely=0.2,  anchor=customtkinter.CENTER)

    # add methods to app  
    def updateCounter(self):
        self.charactersTypedTodayCounter.configure(text = str(howManyKeysArePressed))
        self.wordsTypedTodayCounter.configure(text = str(howManyWordsAreTyped))
        self.after(100, self.updateCounter)

app = App()
app.after(100, app.updateCounter)
app.after(201, lambda :app.iconphoto(False, PhotoImage(file="C:/Users/bmapl/Documents/Code/python/TotalWordsTodayGit/src/TWT_Logo.png")))
app.mainloop()
