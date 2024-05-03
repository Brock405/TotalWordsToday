import keyboard

howManyKeysArePressed = 0

while True:
    # detects if key pressed down
    keyEvent = keyboard.read_event()
    if keyEvent.event_type == keyboard.KEY_DOWN:
        howManyKeysArePressed += 1
        print(howManyKeysArePressed)
