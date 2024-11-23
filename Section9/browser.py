import webbrowser

# webbrowser.open("http://www.python.org")

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chrome = webbrowser.get(f'"{chrome_path}" %s')
chrome.open_new("http://www.python.org")
