import sys
import tasks_list as tl
import time
from googlesearch import search
from translate import Translator
from wikisearch import wiki


def create_tasks():
        tasks = []
        print('Say "stop" to end adding tasks.')

        while True:
            message = str(input('Msg: '))
            print(f'You: {message}')
            if not message:
                continue
            if 'stop' in message:
                break
        
            tasks.append(message)
        
        for task in tasks:
            tl.add_task_to_db(task)
        
        print("Sure, I'll remind you about:")
        for i, message in enumerate(tasks, 1):
            print(f'{i}. {message}')


def display_tasks():
        show_tasks = tl.show_all_tasks()
        if show_tasks:

            tl.show_all_tasks()
            if not tl.show_all_tasks():
                print('No tasks found.')
            else:
                print('Here are your tasks:')
                for i, message in enumerate(tl.show_all_tasks.all_tasks, 1):
                    print(f'{i}. {message[1]}')
        else:
            print('No tasks yet.')


def delete_tasks(message):
        replace = ['delete', 'task']
        keyword = None

        for replace in replace:
            if replace in message:
                i = message.find(replace)
                keyword = message[i + len(replace):].strip()

        tl.delete_task_keyword(keyword)
        if not tl.delete_task_keyword(keyword):
            print("Task not found.")
        else:
            print("Task deleted successfully.")


def wiki_search(message):
        replace = ['search', 'wikipedia']

        query = message
        for word in replace:
            query = query.replace(word, '').strip()
        print(query)

        if query:
            info = wiki(query)
            if info:      
                print('Here results to your search:')
                for i, j in info.items():
                    print(f'{i}: {j}')
            else:
                print('No information found.')
        else:
            print('Please provide a valid search query.')


user_name = {'name': 'User'}


def your_name():
    try:
        print("What is your name?")
        while True:
            nickname = str(input('Msg: '))
            print(f'You said: {nickname}')
            if nickname is not None:
                user_name['name'] = nickname
                print(f"User's name updated to {nickname}")
                return
            else:
                print("Sorry, I didn't catch that. Could you please repeat?")
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')           


def commands(message):    
    if 'change my name' in message:
        your_name()
    elif 'create' in message and 'task' in message:
        create_tasks()
    elif 'show' in message and 'task' in message:
        display_tasks()
    elif 'delete' in message and 'task' in message:
        delete_tasks()
    elif 'delete all tasks' in message:
        tl.delete_all_tasks()

    elif 'search' in message and 'wikipedia' in message:
        wiki_search(message)

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
