# -*- coding: utf-8 -*-
import marshal
import zlib
import base64
import sys

print("==================================================")
print("          EXTRACTING TEXT & BRANDING LINKS        ")
print("==================================================")

try:
    # ১. main.py ফাইলটিকে ইন্টারনালি রান করে মেমোরিতে নেওয়া হচ্ছে
    import main
    
    # ২. মেমোরি থেকে এনক্রিপ্টেড আসল ডাটা ব্লকটি এক লাইনে নিয়ে আসা হচ্ছে
    full_encrypted_data = b""
    for var_name in dir(main):
        if not var_name.startswith('__'):
            val = getattr(main, var_name)
            if isinstance(val, bytes) and len(val) > 20: # শুধু বড় বাইটগুলো নেওয়া হচ্ছে
                full_encrypted_data += val

    if not full_encrypted_data:
        raise Exception("main.py ফাইলের ভেতর এনক্রিপ্টেড ডাটা পাওয়া যায়নি!")

    # ৩. ডিক্রিপশন এবং লেয়ার আনপ্যাকিং প্রসেস
    jvQMNIlmCf = base64.b64decode(full_encrypted_data)
    FVP2EvO0F3 = [0]*15
    eVsPqCPazB = bytes([jvQMNIlmCf[i]^FVP2EvO0F3[i%len(FVP2EvO0F3)] for i in range(len(jvQMNIlmCf))])
    jvQMNIlmCf = zlib.decompress(eVsPqCPazB)
    jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
    
    # ৪. মার্শাল অবজেক্ট লোড করা
    code_obj = marshal.loads(jvQMNIlmCf)
    
    print("\n[+] SUCCESS! EXTRACTED TEXT & BANNER STRINGS:\n")
    print("-" * 60)
    
    # ৫. স্ক্রিনে সমস্ত টেক্সট ও লিংক প্রিন্ট করা
    for const in code_obj.co_consts:
        if isinstance(const, str) and len(const.strip()) > 1:
            if const not in ['__main__', '__doc__', '__package__', '__name__']:
                print(f"-> {const}")
                
    print("-" * 60)
    print("\n[!] চেক করুন, ওপরের লাইনের ভেতরেই কাঙ্ক্ষিত নাম ও লিংক চলে এসেছে।")

except Exception as e:
    print(f"\n[X] ERROR OCCURRED: {e}")
