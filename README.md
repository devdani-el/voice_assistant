# Voice Assistant with Speech Recognition and pyttsx3

![Voice Assistant](voice_assistant.jpg)

This is a feature-rich voice assistant that seamlessly combines Speech Recognition and pyttsx3 for interactive voice-based interactions. From managing tasks to web searching, Wikipedia queries, translation, and personalization, this assistant is designed to cater to various needs.

## Requirements

Ensure you have the necessary libraries installed before running the assistant:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia-api
pip install google
pip install translate
```

## Configuration

1. **Database Setup:**
   - Set up a local database by executing the `setup_database.sql` script to create the required table.

2. **Configuration File:**
   - Customize the assistant's behavior by modifying the `config.py` script to set language preferences, database settings, etc.

## Usage

Run the `main.py` script to initiate the voice assistant. The assistant awaits voice commands and responds dynamically based on the functionalities available.

### Available Commands

1. **Tasks:**
   - "Create task": Add tasks effortlessly using voice input.
   - "Show tasks": Display all your tasks.
   - "Delete task": Remove a specific task.
   - "Delete all tasks": Clear your task list.

2. **Web Search:**
   - "Search for [query]": Perform a Google search with voice-activated queries.

3. **Wikipedia Search:**
   - "Search Wikipedia [query]": Retrieve detailed information from Wikipedia effortlessly.

4. **Translator:**
   - "Translate to [language]": Get instant translations of spoken words to the language of your choice.

5. **Personalization:**
   - "Rename assistant": Make the assistant uniquely yours by changing its name.
   - "Change my name": Personalize the interaction by updating your name.

6. **Miscellaneous:**
   - "Help": Access a visual guide to available commands and their descriptions.
   - "Stop" or "Exit": Conveniently close the assistant when done.

## Contributions

Contributions are highly encouraged! Whether it's opening issues or submitting pull requests, your contribution can help enhance this voice assistant.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Enjoy your interactions with your personalized voice assistant!** 🎙️✨
