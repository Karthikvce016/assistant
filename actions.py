import subprocess
import webbrowser

def open_target(command):
    c = command.lower()

    if "youtube" in c:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    if "google" in c:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    if "github" in c:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    if "spot" in c:
        subprocess.Popen(["open", "-a", "Spotify"])
        return "Opening Spotify"

    if "chrome" in c:
        subprocess.Popen(["open", "-a", "Google Chrome"])
        return "Opening Google Chrome"

    if "vscode" in c or "vs code" in c:
        subprocess.Popen(["open", "-a", "Visual Studio Code"])
        return "Opening VS Code"

    return None

def search_youtube(command):
    q = command.replace("search youtube", "").strip()
    if not q:
        return None
    url = "https://www.youtube.com/results?search_query=" + q.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching YouTube for {q}"

def spotify_control(action):
    if action == "play":
        s = 'tell application "Spotify" to play'
    elif action == "pause":
        s = 'tell application "Spotify" to pause'
    elif action == "next":
        s = 'tell application "Spotify" to next track'
    elif action == "previous":
        s = 'tell application "Spotify" to previous track'
    else:
        return None

    subprocess.Popen(["osascript", "-e", s])
    return f"Spotify {action}"