from listener import listen
from speaker import speak
from intent import get_intent, strip_wake_words, normalize_command
from actions import open_target, search_youtube, spotify_control
import sys

WAKE_WORDS = ["hey jarvis", "friday"]
EXIT_PHRASES = ["shutdown", "exit", "quit", "terminate"]

def is_exit(text):
    return any(p in text for p in EXIT_PHRASES)

waiting = False
print("Sleeping")

while True:
    text = listen()
    if not text:
        continue

    text = normalize_command(text)
    print("HEARD:", text)

    if is_exit(text):
        speak("Alright, shutting down")
        sys.exit(0)

    if waiting:
        if any(w in text for w in WAKE_WORDS):
            speak("I'm listening")
            continue

        waiting = False
        cmd = text
        intent = get_intent(cmd)

        if intent == "OPEN":
            res = open_target(cmd)
        elif intent == "YT_SEARCH":
            res = search_youtube(cmd)
        elif intent == "SPOTIFY_CONTROL":
            if "play" in cmd:
                res = spotify_control("play")
            elif "pause" in cmd:
                res = spotify_control("pause")
            elif "next" in cmd:
                res = spotify_control("next")
            elif "previous" in cmd:
                res = spotify_control("previous")
            else:
                res = None
        else:
            res = None

        speak(res if res else "I don't know how to do that yet")
        print("Sleeping")
        continue

    if any(w in text for w in WAKE_WORDS):
        rest = strip_wake_words(text, WAKE_WORDS)

        if rest:
            cmd = rest
            intent = get_intent(cmd)

            if intent == "OPEN":
                res = open_target(cmd)
            elif intent == "YT_SEARCH":
                res = search_youtube(cmd)
            elif intent == "SPOTIFY_CONTROL":
                if "play" in cmd:
                    res = spotify_control("play")
                elif "pause" in cmd:
                    res = spotify_control("pause")
                elif "next" in cmd:
                    res = spotify_control("next")
                elif "previous" in cmd:
                    res = spotify_control("previous")
                else:
                    res = None
            else:
                res = None

            speak(res if res else "I don't know how to do that yet")
            print("Sleeping")
        else:
            speak("What do you want me to do")
            waiting = True