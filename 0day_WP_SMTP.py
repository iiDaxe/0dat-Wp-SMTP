import requests
import threading
from bs4 import BeautifulSoup as BS
from colorama import Fore, init

path = '/wp-content/plugins/easy-wp-smtp/'

init()


def Plugins(url):
    try:
        url = f"{url}{path}"
        re = requests.get(url=url)
        if re.status_code == 200:
            Soup = BS(re.text.lower(), 'html.parser')
            find = Soup.find('title')
            print(find)
            if "Index of /wp-content/plugins/easy-wp-smtp".lower() in find:
                Vuln = open('List.txt', 'a')
                urlVuln = f"\n{url}"
                Vuln.write(urlVuln)
                print(
                    f"\n{Fore.CYAN} [+] Found Path : [ {url } ] {Fore.YELLOW} {re.status_code}{Fore.RESET}"
                    .strip())

            else:
                print(
                    f"\n{Fore.RED} [+] NotFound Path : [ {url } ] {Fore.LIGHTBLACK_EX} {re.status_code}{Fore.RESET}"
                    .strip())
        else:
            print(
                f"\n{Fore.RED} [+] NotFound Path : [ {url } ] {Fore.LIGHTBLACK_EX} {re.status_code}{Fore.RESET}"
                .strip())

    except:
        print(
            f"\n{Fore.MAGENTA} [  ERROR ][ {url } ] {Fore.LIGHTMAGENTA_EX}{Fore.RESET}"
            .strip())


print(
    '\n', Fore.RED,
    '██████╗ ██████╗  █████╗ ██╗   ██╗     ██╗    ██╗██████╗       ███████╗███╗   ███╗████████╗██████╗ '
)
print(
    Fore.YELLOW,
    '██╔═████╗██╔══██╗██╔══██╗╚██╗ ██╔╝     ██║    ██║██╔══██╗      ██╔════╝████╗ ████║╚══██╔══╝██╔══██╗'
)
print(
    Fore.CYAN,
    '██║██╔██║██║  ██║███████║ ╚████╔╝█████╗██║ █╗ ██║██████╔╝█████╗███████╗██╔████╔██║   ██║   ██████╔╝'
)
print(
    Fore.LIGHTWHITE_EX,
    '████╔╝██║██║  ██║██╔══██║  ╚██╔╝ ╚════╝██║███╗██║██╔═══╝ ╚════╝╚════██║██║╚██╔╝██║   ██║   ██╔═══╝ '
)
print(
    Fore.GREEN,
    '╚██████╔╝██████╔╝██║  ██║   ██║        ╚███╔███╔╝██║           ███████║██║ ╚═╝ ██║   ██║   ██║     '
)
print(
    Fore.LIGHTBLACK_EX,
    ' ╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝         ╚══╝╚══╝ ╚═╝           ╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝     '
)
print('\tBy Mr.Daxe  ')

List = input(" [+] Enter Url list : ")
openList = open(List, 'r').readlines()
for i in openList:
    Target = f"{i}".strip()
    thred = threading.Thread(target=Plugins, args=(Target, ))
    thred.start()