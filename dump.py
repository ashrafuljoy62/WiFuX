# -*- coding: utf-8 -*-
import marshal
import zlib
import base64
import re

print("==================================================")
print("          DUMPING SOURCE CODE...                  ")
print("==================================================")

try:
    # ১. সরাসরি main.py ফাইলটি টেক্সট হিসেবে ওপেন করে ভেতরের ডাটা পড়া হচ্ছে
    with open("main.py", "r", encoding="utf-8") as f:
        main_content = f.read()

    # ২. রেগুলার এক্সপ্রেশন দিয়ে জাদুকরী ভ্যারিয়েবল 'jvQMNIlmCf = b\"...\"' এর ডাটা খোঁজা হচ্ছে
    match = re.search(r'jvQMNIlmCf\s*=\s*b[\'\"](.*?)[\'\"]', main_content)
    
    if match:
        raw_base64_data = match.group(1).encode('utf-8')
    else:
        # যদি ভ্যারিয়েবলটি প্রথম দিকে বা অন্যভাবে ডিক্লেয়ার করা থাকে
        # ফাইলের সবচেয়ে বড় বাইট স্ট্রিংটি খোঁজা হচ্ছে
        all_bytes = re.findall(r'b[\'\"](.*?)[\'\"]', main_content)
        if all_bytes:
            raw_base64_data = max(all_bytes, key=len).encode('utf-8')
        else:
            raise Exception("main.py ফাইলের ভেতর এনক্রিপ্টেড ডাটা ব্লকটি খুঁজে পাওয়া যায়নি!")

    # ৩. ডিক্রিপশন এবং লেয়ার আনপ্যাকিং প্রসেস
    jvQMNIlmCf = base64.b64decode(raw_base64_data)
    FVP2EvO0F3 = [0]*15
    eVsPqCPazB = bytes([jvQMNIlmCf[i]^FVP2EvO0F3[i%len(FVP2EvO0F3)] for i in range(len(jvQMNIlmCf))])
    jvQMNIlmCf = zlib.decompress(eVsPqCPazB)
    jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
    
    # ৪. মার্শাল অবজেক্ট লোড করা
    code_obj = marshal.loads(jvQMNIlmCf)
    
    print("\n[+] SUCCESS! EXTRACTED TEXT & BRANDING LINKS:\n")
    print("-" * 60)
    
    # ৫. স্ক্রিনে সমস্ত টেক্সট ও লিংক প্রিন্ট করা
    for const in code_obj.co_consts:
        if isinstance(const, str) and len(const.strip()) > 1:
            if const not in ['__main__', '__doc__', '__package__', '__name__']:
                print(f"-> {const}")
                
    print("-" * 60)
    print("\n[!] চেক করুন, ওপরের লাইনের ভেতরেই কাঙ্ক্ষিত নাম ও লিংক চলে এসেছে।")

except FileNotFoundError:
    print("\n[X] ERROR: 'main.py' ফাইলটি ডিরেক্টরিতে পাওয়া যায়নি।")
except Exception as e:
    print(f"\n[X] ERROR OCCURRED: {e}")
