from colorama import Fore, Style, init
init(autoreset=True)
def success(message):
    print(Fore.GREEN + "SUCCESS: " + message)
def error(message):
    print(Fore.RED + "ERROR: " + message)
def warning(message):
    print(Fore.YELLOW + "WARNING: " + message)
def info(message):
    print(Fore.CYAN  + message)
def title(message):
    print(Fore.BLUE + Style.BRIGHT + message)
