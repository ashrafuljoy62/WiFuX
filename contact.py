#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys

# ─────────────────────────────────────────────
#  Social Media Links — AMJ Ashraful
# ─────────────────────────────────────────────
CONTACTS = {
    1: {"name": "Facebook",   "url": "https://m.facebook.com/ashrafulalam05"},
    2: {"name": "Instagram",  "url": "https://instagram.com/fire.fighter.joy"},
    3: {"name": "Telegram",   "url": "https://t.me/premium_master_62"},
    4: {"name": "GitHub",     "url": "https://github.com/ashrafuljoy62"},
    5: {"name": "TG Channel",   "url": "https://t.me/movieallpremium"},
}

# ─────────────────────────────────────────────

def banner():
    print('''\033[1;32m
███╗   ███╗███████╗██████╗ 
████╗ ████║██╔════╝██╔══██╗
██╔████╔██║███████╗██████╔╝
██║╚██╔╝██║╚════██║██╔══██╗
██║ ╚═╝ ██║███████║██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝\033[0m
''')

def show_menu():
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')
    print('\033[1;33m  Contact AMJ Ashraful — Choose a Platform\033[0m')
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')
    print()
    for num, info in CONTACTS.items():
        print(
            f"  \033[1;36m[\033[1;32m{num}\033[1;36m]\033[0m"
            f"  \033[1;33m{info['name']}\033[0m"
        )
    print()
    print(f"  \033[1;36m[\033[1;31m0\033[1;36m]\033[0m  \033[1;31mExit\033[0m")
    print()
    print('\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m')
    print()

def open_url(url):
    try:
        result = subprocess.run(
            ['termux-open-url', url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            raise Exception()
    except Exception:
        try:
            subprocess.run(
                ['xdg-open', url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            print(f"\033[1;33m[i]\033[0m \033[1;37mCould not open browser. Visit manually:\033[0m")
            print(f"    \033[1;32m{url}\033[0m")

def goodbye():
    print()
    print('\033[1;36m╭──────────────────────────────────────────╮\033[0m')
    print('\033[1;36m│\033[0m        \033[1;32mSee you! — Stay With AMJ\033[0m          \033[1;36m│\033[0m')
    print('\033[1;36m╰──────────────────────────────────────────╯\033[0m')
    print()

def main():
    banner()

    while True:
        show_menu()
        try:
            choice = input(
                "\033[1;37m[\033[1;33m?\033[1;37m] Select a platform: \033[1;36m-> \033[0m"
            ).strip()

            if choice in ('0', 'q', 'exit', ''):
                goodbye()
                sys.exit(0)

            num = int(choice)

            if num not in CONTACTS:
                print(f"\n\033[1;31m[!]\033[0m \033[1;37mInvalid option. Enter a number between 1 and {len(CONTACTS)}.\033[0m\n")
                continue

            selected = CONTACTS[num]
            print()
            for frame in ['|', '/', '-', '\\', '|', '/', '-', '\\']:
                sys.stdout.write(f"\r\033[1;36m[{frame}]\033[0m \033[1;33mOpening\033[0m \033[1;32m{selected['name']}\033[0m\033[1;37m...\033[0m")
                sys.stdout.flush()
                __import__('time').sleep(0.08)
            sys.stdout.write(f"\r\033[1;32m[+]\033[0m \033[1;33mOpening\033[0m \033[1;32m{selected['name']}\033[0m\033[1;37m...    \033[0m\n")
            print()

            open_url(selected['url'])

            print(f"\033[1;32m[+]\033[0m \033[1;37mDone!\033[0m")
            print()

            again = input(
                "\033[1;37m[\033[1;33m?\033[1;37m] Open another platform? \033[1;36m[Y/n] -> \033[0m"
            ).strip().lower()

            if again in ('n', 'no'):
                goodbye()
                sys.exit(0)

            print()

        except ValueError:
            print(f"\n\033[1;31m[!]\033[0m \033[1;37mNumbers only. Enter between 1 and {len(CONTACTS)}.\033[0m\n")
        except KeyboardInterrupt:
            print()
            goodbye()
            sys.exit(0)

if __name__ == '__main__':
    main()
