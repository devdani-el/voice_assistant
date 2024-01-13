import wikipedia


def wiki(message, lang='en'):
    wikipedia.set_lang(lang)
    results = wikipedia.search(message)

    if results:
        page = wikipedia.page(results[0])
        info = {
            'title': page.title,
            'resume': page.summary
        }

        return info
    else:
        print(f'No results found for the search: {message}')
        return None
    