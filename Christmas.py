#merry christmas 2020
#from Mink Alex Vina with love
from colorama import Fore, Back, Style, init
init()
size = 30

for i in range(0, size):
    if i == 0:
        print(Fore.YELLOW + "★".center(size, " "))
    elif i % 2 == 0 and i > 0:
        print(Fore.GREEN + ("*"*i).center(size, " "))
    else:
        print(Fore.RED + ("'"*(i+1)).center(size, " "))

for i in range(5):
    print(Fore.GREEN + "■".center(size, " "))

init(autoreset=True)
print()
print(Back.RED + "Merry Christmas...!!".center(size+2, " "))
