import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12:
        speak("Good Morning!!")

    elif hour >= 12 and hour <18:
        speak("Good AfterNoon!!")

    else:
        speak("Good Evening!!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = "en-in")
        print("User said : ", query)

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__ =="__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        #logic for executing tasks base on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('opening Google')
            webbrowser.open('www.google.com')

        elif 'open github' in query:
            speak('opening Github')
            webbrowser.open('www.github.com')
            
        elif 'play a movie' in query:
            speak('Enjoy your movie Sir')
            movie_dir = 'D:\\Movies\\Last Christmas (2019) [1080p] [BluRay] [5.1] [YTS.LT]'
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(strTime)
            speak("Sir The time is: ", strTime)


