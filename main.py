import sys
import commands
import pyttsx3
import speech_recognition as sr
from datetime import datetime


def start():
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


    assistant = {
        'name': 'Assistant',
        'month': 1,
        'year': 2024
    }

    def age_assistant():
        month = datetime.now().month - assistant['month']
        year = datetime.now().year = assistant['year']
        voice(f'I have {month} months and {year} years old')
        return age_assistant
    
    def help_functions():
        voice('I am a virtual assistant, and I am here to help you. In my system, microsystems are being developed where each one has its own responsibility. Currently, I can:')
        helps = {
            'Tasks': 'Do you have something important to remember or to-do? say "create task"',
            'Web search': 'Access the web by saying "search for", and then say what you want to search for.',
            'Translator': 'Translate any word you want with the command: "translate to", followed by the desired language'
        }
        for key, value in helps.items():
            print(f'{key}: {value}')


    def rename_assistant():
        try:
            print("What is your assistant's name?")
            while True:
                new_name = str(input('Msg: '))
                print(f'You said: {new_name}')
                if new_name is not None:
                    assistant['name'] = new_name
                    print(f"Assistant's name updated to {new_name}")
                    return
                else:
                    print("Sorry, I didn't catch that. Could you please repeat?")
        except ValueError as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')


    def config_assistant():
        if 'rename' in message and 'assistant' in message:
            rename_assistant()
        elif 'how old are you' in message:
            age_assistant()
        elif 'help' in message:
            help_functions()


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
            config_assistant()
            commands(message)


start()
