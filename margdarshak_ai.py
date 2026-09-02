print("--- Welcome to Tumhara Apna MargDarshak AI ---")

correct_password = "bbd"
attempts = 3
user_database = []  # एडवांस्ड डेटाबेस (डिक्शनरी लिस्ट)

print("\n--- SECURITY LOGIN ---")

while attempts > 0:
    user_password = input(f"Kripya login password darj karein (Maukah bache hain: {attempts}): ")
    if user_password == correct_password:
        print("✅ Login Safal! Suraksha janch puri hui.")
        break
    else:
        attempts = attempts - 1
        print(f"❌ Galat Password!")

if attempts == 0:
    print("\n🚨 SECURITY ALERT: Aapka access BLOCK kar diya gaya hai.")
else:
    while True:
        print("\n--- MAIN MENU ---")
        print("1. New User Registration & Guidance (Talk to AI)")
        print("2. View Registered Users & Marks (Admin Corner)")
        print("0. Exit Chatbot")
        
        choice = input("\nApni choice chunein (0-2): ")
        
        if choice == '0':
            print("\nMargDarshak AI se baat karne ke liye shukriya! Bye Bye!")
            break
            
        elif choice == '1':
            name = input("\nApna Shubh Naam bataiye: ")
            percent = input("Apne 12th ke percent likho: ")
            percent_number = int(percent)
            
            # नाम और मार्क्स का जोड़ा बनाकर डेटाबेस में सेव करना
            user_data = {
                "user_name": name,
                "user_marks": percent_number
            }
            user_database.append(user_data)
            
            print(f"Hello {name}! Aapka data secure database me safe ho gaya hai.")
            
            # 🔥 यहाँ से शुरू होता है आगे का पूरा करियर गाइडेंस काम!
            print(f"\n--- GUIDANCE FOR {name.upper()} ---")
            print("A. Check Placement Eligibility (12th Marks)")
            print("B. Explore Career Fields (Web, AI, Cyber, Data)")
            sub_choice = input("Kya check karna chahte hain (A ya B): ")
            
            if sub_choice == 'A' or sub_choice == 'a':
                if percent_number < 60:
                    print("-> Target: Product-Based Companies & Startups (Marks don't matter there!)")
                else:
                    print("-> Wah! Aap campus ki sabhi companies me baith sakte hain.")
                    
            elif sub_choice == 'B' or sub_choice == 'b':
                print("\n--- Career Fields ---")
                print("1. Web Dev\n2. AI / ML\n3. Cyber Security\n4. Data Science")
                field = input("Apna option chunein (1-4): ")
                if field == '1':
                    print("-> JavaScript aur React seekhna shuru karein!")
                elif field == '2':
                    print("-> Sahi chunav! Python aur Mathematics par dhyan dein.")
                elif field == '3':
                    print("-> Great choice! Cyber Security ke liye Linux aur Networking seekhein.")
                elif field == '4':
                    print("-> Data Science ke liye Libraries aur Statistics seekhein!")
                else:
                    print("-> Invalid option!")
            else:
                print("-> Invalid sub-choice!")
            
        elif choice == '2':
            print("\n--- 📂 ADMIN DATABASE ANALYTICS ---")
            if len(user_database) == 0:
                print("Database khali hai!")
            else:
                for index, user in enumerate(user_database, 1):
                    print(f"{index}. Name: {user['user_name']} | 12th Marks: {user['user_marks']}%")
        else:
            print("-> Galat option! Kripya 0, 1, ya 2 hi chunein.")
