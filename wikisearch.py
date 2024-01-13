import wikipedia
from assistant import speech_recognition, voice

def wiki(message, lang='en'):
    wikipedia.set_lang(lang)
    results = wikipedia.search(message)

    if results:
        if len(results) > 1:
            voice(f'The search term {message} is ambiguous. Please choose one of the following options:')
            for i, option in enumerate(results):
                print(f'{i + 1}. {option}')
            user = None
            while user is None:
                voice('Please say the number corresponding to your choice.')
                user = speech_recognition()
                try:
                    user = int(user) - 1
                    if user < 0 or user >= len(results):
                        raise ValueError
                except (ValueError, TypeError):
                    voice('Invalid choise. Please try again.')
                    user = None
            
            select = results[user]
        else:
            select = results[0]

        page = wikipedia.page(select, auto_suggest=False)
        info = {
            'title': page.title,
            'summary': page.summary
        }

        return info
    else:
        voice(f'No results found for the search: {message}')
        return None
    