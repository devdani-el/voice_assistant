import sys
import commands
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import tasks_list as Tl
from translate import Translator
import time
from googlesearch import search


def input_validation(message):
    MAX_INPUT_LENGTH = 100
    try:
        if not message.strip():
            raise ValueError(voice('Sorry, I didn\'t catch that. Could you please speak a bit more clearly and try again?'))

        if len(message) > MAX_INPUT_LENGTH:
            raise ValueError(voice('The message you submitted was too long. Could you shorten it and try again, please?'))
        
        return ''.join(char for char in message if char.isalnum() or char.isspace())
    except ValueError as e:
        print(f'Error: {e}')
        sys.exit()


def speech_recognition(timeout=30, language='en'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print('Speak now...')
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            print('I\'m sorry, but I couldn\'t understand what you said.')
        except sr.RequestError as e:
            print(f'I encountered an issue accessing the speech recognition service: {e}')
        except Exception as e:
            print(f'Something unexpected happened: {e}')

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
        print(f'Apologies, there was an error initializing the text-to-speech engine: {e}')
    except Exception as e:
        print(f'Oops! Something went wrong while speaking the message: {e}')


def assistant():
    info = {
    'name': 'Assistant',
    'month': 1,
    'year': 2024
    }

    current_month = datetime.now().month
    current_year = datetime.now().year
    months = (current_year - info['year']) * 12 + (current_month - info['month'])
    voice(f"I'm {months} months and {current_year - info['year']} years old")


def help_functions():
    voice('I\'m here to help! Currently, I can assist you with: tasks, perform web searches, and even translate words for you. Feel free to ask anything.')
    helps = {
        'Tasks': 'Do you have something important to remember or to-do? say \'create task\'',
        'Perform web search': 'Access the web by saying \'search for\', and then say what you want to search for.',
        'and even translate words for you': 'with the command: \'translate to\', followed by the desired language'
    }
    for key, value in helps.items():
        print(f'{key}: {value}')


def rename_assistant():
    try:
        print('What would you like to call me?')
        while True:
            new_name = str(input('Enter the name: '))

            if new_name.strip():
                print(f'You chose the name: {new_name}')
                verification = speech_recognition(f"Do you want to save '{new_name}' as my name?")
                if verification.lower() == 'yes':
                    assistant.info['name'] = new_name
                    print(f'My name is now {new_name}. How may I assist you?')
                    return
                else:
                    continue
            else:
                print('I understand it\'s a big decision. Could you please provide a name for me?')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')


def main_commands(message):
    try:
        if 'rename' in message and 'assistant' in message:
            rename_assistant()
        elif 'how old are you' in message:
            assistant()
        elif 'help' in message:
            help_functions()
    except Exception as e:
        print(f'Sorry, something went wrong while processing your request: {e}')


def commands(message):

    if 'create' in message and 'task' in message:
        tasks = []
        voice('Say "stop" to end adding tasks.')

        while True:
            message = speech_recognition()
            print(f'You: {message}')
            if not message:
                continue
            if 'stop' in message:
                break

        tasks.append(message)
        
        for task in tasks:
            Tl.add_task_to_db(task)

        voice("Sure, I'll remind you about:")
        for i, message in enumerate(tasks, 1):
            voice(f'{i}. {message}')
        
    elif 'display' in message and 'task' in message:
        show_tasks = Tl.show_all_tasks()
        if show_tasks:

            Tl.show_all_tasks()
            if not Tl.show_all_tasks():
                voice('No tasks found.')
            else:
                voice('Here are your tasks:')
                for i, message in enumerate(Tl.show_all_tasks.all_tasks, 1):
                    voice(f'{i}. {message[1]}')
        else:
            print('No tasks yet.')
    
    elif 'delete' in message and 'task' in message:
        replace = ['delete', 'task']
        keyword = None

        for replace in replace:
            if replace in message:
                i = message.find(replace)
                keyword = message[i + len(replace):].strip()

        Tl.delete_task_keyword(keyword)
        if not Tl.delete_task_keyword(keyword):
            voice("Task not found.")
        else:
            voice("Task deleted successfully.")

    elif 'delete all tasks' in message:
        Tl.delete_all_tasks()

    elif 'search' in message and 'google' in message:
        query = message.replace('search', '').strip()
        print(f"Here are the search results for {query}.")
        # Code to perform web search goes here
        for n, result in enumerate(search(query), start=1):
            print(f"{n}. {result}")
            time.sleep(1)

    elif 'translate to' in message:
        target_language = message.replace('translate to', '').strip()
        print(f"What should I translate to {target_language}?")
        translated_message = str(input('Msg: '))
    
        if translated_message is not None:
            translation = Translator(to_lang=target_language).translate(translated_message)
            if translation is not None:
                print(f"The translation is: {translation}")
            else:
                print("Sorry, I couldn't translate the message.")
        else:
            print("Sorry, I couldn't recognize the message.")

    elif message in ['stop', 'exit', 'quit']:
        print('Goodbye!')
        sys.exit()


def main():
    try:
        while True:
            keyword = speech_recognition().capitalize()
            message = input_validation(keyword)
            if message == assistant.info['name']:
                voice(f"Hello! I'm {assistant.info['name']}. How can I assist you today?")
                break
            else:
                continue

        while True:
            keyword = speech_recognition().capitalize()
            message = input_validation(keyword)
            if message:
                print(f'You: {message}')
                main_commands(message)
                commands(message)

    except KeyboardInterrupt:
        print("\nExiting the program.")


if __name__ == "__main__":
    main()
