import pyttsx3

print("Welcome to TextEcho! I will say what you type.....")
EXIT_KEYWORD="!"
print(f"Type {EXIT_KEYWORD}to exit.\n")

engine=pyttsx3.init()
while True:
    text=input("Enter text: ")

    if text=="!":
        print("Exiting... Thank you for using TextEcho!")
        engine.say("Goodbye")
        engine.runAndWait()
        break
   
    
    #To change the voice to male(index = 0) or Female(index = 1)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    #To Change the Speed of Speech (Rate)
    engine.setProperty('rate',200)

    #To change Volume 
    engine.setProperty('volume',0.8)
 
    engine.say(text)
    engine.runAndWait()


   
   



