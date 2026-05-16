# -*- coding: utf-8 -*-
import marshal
import zlib
import base64
import sys

print("==================================================")
print("          SOURCE CODE DECRYPTER LOADED            ")
print("==================================================")

try:
    # main.py ফাইলটি লোড করা হচ্ছে
    import main
    
    # ফাইলের আসল এনক্রিপ্টেড ভ্যারিয়েবলটি খোঁজা হচ্ছে
    if hasattr(main, 'jvQMNIlmCf'):
        jvQMNIlmCf = main.jvQMNIlmCf
    else:
        variables = [v for v in dir(main) if not v.startswith('__')]
        bytes_vars = [getattr(main, v) for v in variables if isinstance(getattr(main, v), bytes)]
        if bytes_vars:
            jvQMNIlmCf = max(bytes_vars, key=len)
        else:
            raise Exception("Encrypted data block not found in main.py!")

    # ডিক্রিপশন প্রসেস
    jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
    FVP2EvO0F3 = [0]*15
    eVsPqCPazB = bytes([jvQMNIlmCf[i]^FVP2EvO0F3[i%len(FVP2EvO0F3)] for i in range(len(jvQMNIlmCf))])
    jvQMNIlmCf = zlib.decompress(eVsPqCPazB)
    jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
    
    # মার্শাল অবজেক্ট লোড করা
    code_obj = marshal.loads(jvQMNIlmCf)
    
    print("\n[+] SUCCESS! EXTRACTED TEXT & BRANDING LINKS:\n")
    print("-" * 60)
    
    # মার্শাল অবজেক্টের ভেতরের সমস্ত টেক্সট ও লিংক প্রিন্ট করা
    for const in code_obj.co_consts:
        if isinstance(const, str) and len(const.strip()) > 1:
            if const not in ['__main__', '__doc__', '__package__', '__name__']:
                print(f"-> {const}")
                
    print("-" * 60)
    print("\n[!] আপনি ওপরের টেক্সটগুলোর মধ্যেই নাম ও লিংকগুলো পেয়ে যাবেন।")

except ModuleNotFoundError:
    print("\n[X] ERROR: 'main.py' file not found! Please rename your file to 'main.py'.")
except Exception as e:
    print(f"\n[X] ERROR OCCURRED: {e}")
