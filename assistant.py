import pyttsx3
import speech_recognition as sr


def speech_recognition(timeout=30, language='en'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print('Speak now...')
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print('Speech recognition could not understand audio')
        except sr.RequestError as e:
            print(f'Error accessing the speech recognition service: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

        return ''
        

def voice(message, voice_index=1, rate=180):
    engine = pyttsx3.init()

    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_index].id)
        engine.setProperty('rate', rate)

        print(f'Assistant: {message}')
        engine.say(message)
        engine.runAndWait()

    except pyttsx3.EngineError as e:
        print(f'Error initializing the text-to-speech engine: {e}')
    except Exception as e:
        print(f'Error speaking the message: {e}')