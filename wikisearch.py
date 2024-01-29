import wikipedia


def wiki(message, lang='en'):
    wikipedia.set_lang(lang)
    results = wikipedia.search(message)

    numbers = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5
    }

    if results:
        if len(results) > 1:
            print(f'The search term {message} is ambiguous. Please choose one of the following options:')
            for i, option in enumerate(results, 1):
                print(f'{i}. {option}')

            user = None
            while user is None:
                print('Please say the number corresponding to your choice.')
                user = str(input('Msg: '))
                user =  user.lower()
                print(f'User: {user}')

                if user in numbers:
                    try:    
                        user = numbers[user]
                        if 1 <= user <= len(results):
                            user -= 1
                        else:
                            raise ValueError
                    except (ValueError, TypeError):
                        print('Invalid choise. Please try again.')
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
        print(f'No results found for the search: {message}')
        return None
    