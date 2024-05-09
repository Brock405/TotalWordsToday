import keyboard
import customtkinter

def detectsIfButtonPressedDown():
    howManyKeysArePressed = 0
    # detects if key pressed down
    keyEvent = keyboard.read_event()
    if keyEvent.event_type == keyboard.KEY_UP:
        howManyKeysArePressed += 1
        print(howManyKeysArePressed) 

    return howManyKeysArePressed   


# ---------------------------gui-----------------------------

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, 
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1280x720")

wordsTypedTodayCounter = customtkinter.CTkLabel(app, text="asdf", fg_color="transparent")
wordsTypedTodayCounter.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()

