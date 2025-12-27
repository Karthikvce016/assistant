from listener import listen
from speaker import speak
from intent import get_intent, strip_wake_words
from actions import open_target, search_youtube
import sys

WAKE_WORDS = ["hey jarvis", "friday"]
EXIT_PHRASE = "shutdown"

waiting_for_command = False

print("Sleeping")

while True:
    text = listen()

    if not text:
        continue

    print("HEARD:", text)

    # 🔴 Global kill switch (works anytime)
    if EXIT_PHRASE in text:
        speak("Alright, shutting down")
        sys.exit(0)

    # 🔵 If already awake and waiting for command
    if waiting_for_command:
        if any(w in text for w in WAKE_WORDS):
            speak("I'm listening")
            continue

        command = text
        waiting_for_command = False

        intent = get_intent(command)

        if intent == "OPEN":
            result = open_target(command)
            speak(result if result else "I don't know how to open that yet")

        elif intent == "YT_SEARCH":
            result = search_youtube(command)
            speak(result if result else "What should I search on YouTube")

        else:
            speak("I don't know how to do that yet")

        print("Sleeping")
        continue

    # 🟢 Sleeping → detect wake
    if any(w in text for w in WAKE_WORDS):
        command_part = strip_wake_words(text, WAKE_WORDS)

        # Case: wake + command together
        if command_part:
            intent = get_intent(command_part)

            if intent == "OPEN":
                result = open_target(command_part)
                speak(result if result else "I don't know how to open that yet")

            elif intent == "YT_SEARCH":
                result = search_youtube(command_part)
                speak(result if result else "What should I search on YouTube")

            else:
                speak("I don't know how to do that yet")

            print("Sleeping")
            continue

        # Case: wake only
        speak("What do you want me to do")
        waiting_for_command = True