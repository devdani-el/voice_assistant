import sys
import tasks_list as tl
import time
from googlesearch import search
from translate import Translator
from wikisearch import wiki


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
