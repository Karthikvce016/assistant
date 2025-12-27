import re

def strip_wake_words(text, wake_words):
    result = text.lower()
    for w in wake_words:
        pattern = r"\b" + re.escape(w.lower()) + r"\b"
        result = re.sub(pattern, "", result)
    return result.strip(" ,")

def get_intent(command):
    c = command.lower()

    if c.startswith("open"):
        return "OPEN"

    if c.startswith("search youtube"):
        return "YT_SEARCH"

    return "UNKNOWN"