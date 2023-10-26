import time, requests, threading
from pystyle import *
from colorama import *
import fade

intro = """
 █     █░▓█████  ▄▄▄▄        ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀       ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██       By Lekkos
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
  ░   ░     ░    ░    ░    ░  ░  ░  ░░         ░   ▒   ░      ░   
    ░       ░  ░ ░               ░                 ░  ░       ░   
                      ░                                                                                                                                             
                        >Press enter                                            
"""

Anime.Fade(Center.Center(intro), Colors.red_to_yellow, Colorate.Vertical, interval=0.1, enter=True) #Normalement 0.035

text = """
 █     █░▓█████  ▄▄▄▄        ██████  ██▓███   ▄▄▄       ███▄ ▄███▓
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀       ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░
  ░   ░     ░    ░    ░    ░  ░  ░  ░░         ░   ▒   ░      ░   
    ░       ░  ░ ░               ░                 ░  ░       ░   
                      ░                                            
"""
faded_text = fade.fire(text)
print(faded_text)
msg = input("Can you insert your webhook message ?: ")
webhook = input("Put your WebHook URL: ")
th = int(input('Number of thread ? (200 recommended): '))
sleep = int(input("Sleeping time ? (recommended 2): "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"WebHook have send {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
