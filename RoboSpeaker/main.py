import pyttsx3
def speak(text):
    ai = pyttsx3.init()
    ai.say(text)
    ai.runAndWait()


if __name__ == "__main__":
    while True:
        text = input("Enter what you want me to speak (type 'get lost' to stop): ")
        if text.lower() == "get lost":
            speak("i hate you")
            break
        speak(text)
