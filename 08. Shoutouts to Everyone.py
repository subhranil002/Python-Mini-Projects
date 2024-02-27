import pyttsx3


def text_to_speech(everyone):
    for someone in everyone:
        engine = pyttsx3.init()

        engine.say(f"Shoutout to {someone}")
        engine.runAndWait()


everyone = ["Subhranil1", "Subhranil2", "Subhranil3"]
text_to_speech(everyone)
