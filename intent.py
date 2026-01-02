import re

def strip_wake_words(text, wake_words):
    t = text.lower()
    for w in wake_words:
        t = re.sub(rf"\b{re.escape(w)}\b", "", t)
    return t.strip(" ,")

def normalize_command(text):
    replacements = {
        "pass": "pause",
        "stop": "pause",
        "resume": "play",
        "start": "play"
    }
    words = text.lower().split()
    return " ".join(replacements.get(w, w) for w in words)

def get_intent(command):
    c = command.lower()

    if c.startswith("open"):
        return "OPEN"

    if c.startswith("search youtube"):
        return "YT_SEARCH"

    if any(w in c for w in ["play", "pause", "next", "previous"]):
        return "SPOTIFY_CONTROL"

    return "UNKNOWN"