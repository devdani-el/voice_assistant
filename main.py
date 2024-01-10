import sys
from tasks_list import add_task_to_db, show_all_tasks, delete_task_keyword, delete_all_tasks
import time
import pyttsx3
import speech_recognition as sr
from googlesearch import search
from translate import Translator


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


def exit_program():
    voice('Goodbye!')
    sys.exit()


def commands(message):
    if 'help' in message:
        help_functions()

    # tasks commands 
    elif 'create' in message and 'task' in message:
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
            add_task_to_db(task)
        
        voice("Sure, I'll remind you about:")
        for i, message in enumerate(tasks, 1):
            voice(f'{i}. {message}')
        

    elif 'show' in message and 'task' in message:
        show_tasks = show_all_tasks
        if show_tasks:

            show_all_tasks()
            if not show_all_tasks():
                voice('No tasks found.')
            else:
                voice('Here are your tasks:')
                for i, message in enumerate(show_all_tasks.all_tasks, 1):
                    voice(f'{i}. {message[1]}')
        else:
            voice('No tasks yet.')

    elif 'delete' in message and 'task' in message:
        replace = ['delete', 'task']
        keyword = None

        for replace in replace:
            if replace in message:
                i = message.find(replace)
                keyword = message[i + len(replace):].strip()


        delete_task_keyword(message)
        if not delete_task_keyword(message):
            voice("Task not found.")
        else:
            voice("Task deleted successfully.")

    elif 'search' in message:
        query = message.replace('search', '').strip()
        voice(f"Here are the search results for {query}.")
        # Code to perform web search goes here
        for n, result in enumerate(search(query), start=1):
            print(f"{n}. {result}")
            time.sleep(1)

    elif 'translate to' in message:
        target_language = message.replace('translate to', '').strip()
        voice(f"What should I translate to {target_language}?")
        translated_message = speech_recognition()
    
        if translated_message is not None:
            translation = Translator(to_lang=target_language).translate(translated_message)
            if translation is not None:
                voice(f"The translation is: {translation}")
            else:
                voice("Sorry, I couldn't translate the message.")
        else:
            voice("Sorry, I couldn't recognize the message.")

    elif 'stop' in message:
        exit_program()


def help_functions():
    helps = {
        'Tasks': 'Do you have something important to remember? say "create task"',
        'Web search': 'Access the web by saying "search for", and then say what you want to search for.',
        'Translator': 'Translate any word you want with the command: "translate to", followed by the desired language'
    }
    for key, value in helps.items():
        voice(f'{key}: {value}')


def main():
    while True:
        message = speech_recognition()
        if message:
            print(f'You: {message}')
            commands(message)


if __name__ == '__main__':
    main_message = ''
    main()