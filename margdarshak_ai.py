print("--- Welcome to Tumhara Apna MargDarshak AI ---")

correct_password = "bbd"
attempts = 3
user_database = []  # मेमोरी डायरी

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
        print("2. View Registered Users (Admin Corner)")
        print("0. Exit Chatbot")
        
        choice = input("\nApni choice chunein (0-2): ")
        
        if choice == '0':
            print("\nMargDarshak AI se baat karne ke liye shukriya! Bye Bye!")
            break
            
        elif choice == '1':
            name = input("\nApna Shubh Naam bataiye: ")
            user_database.append(name)  # डेटाबेस में नाम सेवे हुआ
            print(f"Hello {name}! MargDarshak AI me aapka swagat hai.")
            
            # यहाँ से पुराना सारा काम (करियर गाइडेंस) शुरू होगा
            print(f"\n--- GUIDANCE FOR {name.upper()} ---")
            print("A. Check Placement Eligibility (12th Marks)")
            print("B. Explore Career Fields (Web, AI, Cyber, Data)")
            sub_choice = input("Kya check karna chahte hain (A ya B): ")
            
            if sub_choice == 'A' or sub_choice == 'a':
                percent = input("Apne 12th ke percent likho: ")
                if int(percent) < 60:
                    print("-> Target: Product-Based Companies & Startups!")
                else:
                    print("-> Wah! Aap campus ki sabhi companies me baith sakte hain.")
                    
            elif sub_choice == 'B' or sub_choice == 'b':
                print("\n--- Fields ---")
                print("1. Web Dev\n2. AI / ML\n3. Cyber Security\n4. Data Science")
                field = input("Apna option chunein (1-4): ")
                if field == '1': print("-> JavaScript aur React seekhein!")
                elif field == '2': print("-> Python aur Mathematics par dhyan dein.")
                elif field == '3': print("-> Linux aur Networking seekhein.")
                elif field == '4': print("-> Libraries aur Statistics seekhein.")
            
        elif choice == '2':
            print("\n--- 📂 REGISTERED USERS DATABASE ---")
            if len(user_database) == 0:
                print("Database khali hai!")
            else:
                for index, user in enumerate(user_database, 1):
                    print(f"{index}. {user}")
 