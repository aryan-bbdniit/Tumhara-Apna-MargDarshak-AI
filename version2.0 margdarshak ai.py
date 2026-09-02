print("--- Welcome to Tumhara Apna MargDarshak AI ---")
correct_password = "bbd"
attempts = 3  # यूजर को सिर्फ 3 मौके मिलेंगे

print("\n--- SECURITY LOGIN ---")

# जब तक मौके बचे हैं, तब तक पासवर्ड मांगते रहो
while attempts > 0:
    user_password = input(f"Kripya login password darj karein (Maukah bache hain: {attempts}): ")
    
    if user_password == correct_password:
        print("✅ Login Safal! Suraksha janch puri hui.")
        break  # सही पासवर्ड डालते ही लूप से बाहर आ जाओ
    else:
        attempts = attempts - 1  # एक मौका कम कर दो
        print(f"❌ Galat Password!")
        if attempts > 0:
            print(f"Kripya fir se koshish karein.\n")

# अगर सारे मौके खत्म हो गए और लॉगिन नहीं हुआ
if attempts == 0:
    print("\n🚨 SECURITY ALERT: 3 baar galat password! Aapka access BLOCK kar diya gaya hai.")
else:
    
    # यह पूरा हिस्सा अब बिल्कुल सही तरीके से else के अंदर खिसका हुआ है
    name = input("\nApna Shubh Naam bataiye: ")
    print(f"Hello {name}! MargDarshak AI me aapka swagat hai.")

    while True:
        print(f"\n--- MAIN MENU ({name}) ---")
        print("1. Check Company Eligibility (Marks scan)")
        print("2. Career Fields Guidance (Web, AI/ML, Android, Cyber, Data)")
        print("0. Exit Chatbot")
        
        choice = input("\nApni choice chunein (0-2): ")
        
        if choice == '0':
            print(f"\nMargDarshak AI se baat karne ke liye shukriya, {name}! Bye Bye!")
            break
            
        elif choice == '1':
            percent = input(f"\n{name}, apne 12th ke percent likho: ")
            percent_number = int(percent)
            if percent_number < 60:
                print("-> Target: Product-Based Companies & Startups (Marks don't matter there!)")
            else:
                print("-> Wah! Aap campus ki sabhi companies me baith sakte hain.")
                
        elif choice == '2':
            print("\n--- Career Options ---")
            print("A. Web Development")
            print("B. AI / ML")
            print("C. Android Development")
            print("D. Cyber Security")
            print("E. Data Science")
            
            field = input("Apna option chunein (A, B, C, D, ya E): ")
            
            if field == 'A' or field == 'a':
                print("-> JavaScript aur React seekhna shuru karein!")
            elif field == 'B' or field == 'b':
                print("-> Sahi chunav! Python aur Mathematics par dhyan dein.")
            elif field == 'C' or field == 'c':
                print("-> Mobile App ke liye Java ya Kotlin seekhein.")
            elif field == 'D' or field == 'd':
                print("-> Great choice! Cyber Security ke liye Linux aur Networking seekhein.")
            elif field == 'E' or field == 'e':
                print("-> Data Science ke liye Libraries aur Statistics seekhein!")
            else:
                print("-> Invalid option!")
        else:
            print("-> Galat option! Kripya 0, 1, ya 2 hi chunein.")
  