import marshal, zlib, base64

# আপনার আসল এনক্রিপ্টেড ফাইল থেকে ভ্যারিয়েবলটি লোড করা হচ্ছে
from main import jvQMNIlmCf

# ডিক্রিপশন প্রসেস (ঠিক যেভাবে আপনার মেইন ফাইলে ব্যাকগ্রাউন্ডে কাজ করে)
jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
FVP2EvO0F3 = [0]*15
eVsPqCPazB = bytes([jvQMNIlmCf[QMC0b7_arC]^FVP2EvO0F3[QMC0b7_arC%len(FVP2EvO0F3)] for QMC0b7_arC in range(len(jvQMNIlmCf))])
jvQMNIlmCf = eVsPqCPazB
jvQMNIlmCf = zlib.decompress(jvQMNIlmCf)
jvQMNIlmCf = base64.b64decode(jvQMNIlmCf)
Hql6aUFimF = jvQMNIlmCf[::-1]
Jg8SG6sQgH = Hql6aUFimF[::-1]
jvQMNIlmCf = Jg8SG6sQgH

# এবার কোডটি রান (exec) না করে সরাসরি একটি টেক্সট ফাইলে রাইট/সেভ করা হচ্ছে
try:
    # যদি সোর্স কোডটি সরাসরি টেক্সট/স্ট্রিং আকারে থাকে
    source_code = jvQMNIlmCf.decode('utf-8')
    with open("extracted_source.py", "w", encoding="utf-8") as f:
        f.write(source_code)
    print("সফল হয়েছে! আসল কোডটি 'extracted_source.py' ফাইলে সেভ হয়েছে।")
except Exception:
    # যদি এটি একটি কম্পাইল্ড মার্শাল অবজেক্ট হয়, তবে সেটিকে ডিসঅ্যাসেম্বল বা রিড করা
    print("কোডটি মার্শাল অবজেক্ট ফর্মে আছে। নিচের কোডটি টার্মিনালে প্রিন্ট হচ্ছে:")
    import编 uncompyle6 # অথবা সরাসরি marshal loads দিয়ে সোর্স প্রিন্ট করা
    code_obj = marshal.loads(jvQMNIlmCf)
    print(code_obj)
