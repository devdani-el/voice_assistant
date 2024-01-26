import sys
import commands
import pyttsx3
import speech_recognition as sr


def start():
    assistant = {'name': 'Assistant'}


    def input_validation(message):
        MAX_INPUT_LENGTH = 100
        try:
            if len(message) > MAX_INPUT_LENGTH:
                raise ValueError('The message you submitted was too long, please reload the conversation and submit something shorter.')
            return ''.join(char for char in message if char.isalnum() or char.isspace())
        except ValueError as e:
            print(f'Error parsing input: {e}')
            sys.exit()

    
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


    while True:
        keyword = speech_recognition().capitalize()
        message = input_validation(keyword)
        if message == assistant['name']:
            voice('Hello, welcome back!')
            break
        else:
            continue
    while True:
        keyword = speech_recognition()
        message = input_validation(keyword).capitalize()
        if message:
            print(f'You: {message}')
            commands(message)


start()
