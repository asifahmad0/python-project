import pyttsx3
import speech_recognition 
import pyaudio
#listning and speek function
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

#2. Greet Me Function 

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Master , You can me call anytime")
                    break 
#3. Conversations
        elif "hello" in query:
            speak("Hello master, how are you ?")
        elif "i am fine" in query:
            speak("that's great, master")
        elif "how are you" in query:
            speak("Perfect, master")
        elif "thank you" in query:
            speak("you are welcome, master")
#4. Searching from web

        elif "google" in query:
          from SearchNow import searchGoogle
          searchGoogle(query)
        elif "youtube" in query:
          from SearchNow import searchYoutube
          searchYoutube(query)
        elif "wikipedia" in query:
          from SearchNow import searchWikipedia
          searchWikipedia(query)
        elif query in query:
          from SearchNow import searchGmail
          searchGmail(query)
