# -*- coding: utf-8 -*-
# Ashraful Alam Joy
# Author: @Ashraful Joy
# GitHub: https://github.com/ashrafuljoy62
# Time: Sat May 16 20:35:00 2026
# ──────────────────────────────────────────────

import os
import sys
import time

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear_screen()
    print("\033[1;32m ──────────────────────────────────────────────\033[0m")
    print(" \033[1;36m       WELCOME TO ASHRAFUL ALAM JOY'S TOOL\033[0m")
    print(" \033[1;32m ──────────────────────────────────────────────\033[0m")
    print(" \033[1;34m [✓] Developer : Ashraful Alam Joy\033[0m")
    print(" \033[1;34m [✓] GitHub    : https://github.com/ashrafuljoy62\033[0m")
    print(" \033[1;34m [✓] Status    : Active / Premium\033[0m")
    print("\033[1;32m ──────────────────────────────────────────────\033[0m\n")

def main():
    banner()
    print(" \033[1;33m[*] স্ক্রিপ্টটি সফলভাবে লোড হয়েছে...\033[0m")
    time.sleep(1)
    
    print("\n \033[1;32m[+] আপনার কাস্টম অটোমেশন টুল এখন চালু আছে।\033[0m")
    print(" \033[1;37m[+] এখানে আপনার প্রয়োজনীয় সব কাজ অটোমেটিকভাবে সম্পন্ন হবে।\033[0m\n")
    
    # আপনার টুল বা অটোমেশনের বাকি কোডগুলো এই লাইনের নিচে লিখতে পারেন
    
    input(" \033[1;36m[ Press Enter To Exit ]\033[0m")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[1;31m[-] স্ক্রিপ্টটি বন্ধ করা হয়েছে!\033[0m\n")
        sys.exit()
