import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.2. Created by Hunain\n")    
    

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set voice properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Speak the input text
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()