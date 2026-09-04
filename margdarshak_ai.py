import json
import os

print("--- Welcome to Tumhara Apna MargDarshak AI ---")

CONFIG_FILE = "config.json"
FILE_NAME = "database.json"

# 📂 जादुई लॉजिक: अगर फाइल में बदला हुआ पासवर्ड है तो वो लोड करो, नहीं तो "bbd" रखो
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as config_file:
        config_data = json.load(config_file)
        correct_password = config_data.get("password", "bbd")
else:
    correct_password = "bbd"

attempts = 3

# 📂 यूजर डेटाबेस लोड करना
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        user_database = json.load(file)
else:
    user_database = []

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
        print("3. Change Login Password (Settings)")
        print("0. Exit Chatbot")
        
        choice = input("\nApni choice chunein (0-3): ")
        
        if choice == '0':
            print("\nMargDarshak AI se baat karne ke liye shukriya! Bye Bye!")
            break
            
        elif choice == '1':
            name = input("\nApna Shubh Naam bataiye: ")
            percent = input("Apne 12th ke percent likho: ")
            percent_number = int(percent)
            
            user_data = {
                "user_name": name,
                "user_marks": percent_number
            }
            user_database.append(user_data)
            
            with open(FILE_NAME, "w") as file:
                json.dump(user_database, file, indent=4)
                
            print(f"Hello {name}! Aapka data secure permanent file me save ho gaya hai.")
            
        elif choice == '2':
            print("\n--- 📂 PERMANENT DATABASE ANALYTICS ---")
            if len(user_database) == 0:
                print("Database khali hai!")
            else:
                for index, user in enumerate(user_database, 1):
                    print(f"{index}. Name: {user['user_name']} | 12th Marks: {user['user_marks']}%")
                    
        elif choice == '3':
            print("\n--- ⚙️ SETTINGS: CHANGE PASSWORD ---")
            old_p = input("Puraana password darj karein: ")
            
            if old_p == correct_password:
                new_p = input("Naya password banayein: ")
                confirm_p = input("Naya password fir se likhein (Confirm): ")
                
                if new_p == confirm_p:
                    correct_password = new_p
                    
                    # 💾 बदले हुए पासवर्ड को हमेशा के लिए फाइल में राइट (Save) करना
                    with open(CONFIG_FILE, "w") as config_file:
                        json.dump({"password": correct_password}, config_file, indent=4)
                        
                    print("✅ Shabaash! Password permanent file me badal gaya hai.")
                else:
                    print("❌ Error: Dono naye password match nahi huye!")
            else:
                print("❌ Error: Puraana password galat hai!")
        else:
            print("-> Galat option! Kripya 0, 1, 2, ya 3 hi chunein.")
