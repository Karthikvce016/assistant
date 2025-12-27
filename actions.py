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
    query = command.replace("search youtube", "").strip()
    if not query:
        return None
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
    return f"Searching YouTube for {query}"