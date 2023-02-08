from pyfiglet import figlet_format

def ascii_art_function(text):
    return figlet_format(text)

data = input()
print(ascii_art_function(data))