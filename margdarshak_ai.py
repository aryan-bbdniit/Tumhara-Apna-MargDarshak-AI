import json
import os

print("--- Welcome to Tumhara Apna MargDarshak AI ---")

CONFIG_FILE = "config.json"
FILE_NAME = "database.json"

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as config_file:
        config_data = json.load(config_file)
        correct_password = config_data.get("password", "bbd")
else:
    correct_password = "bbd"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        user_database = json.load(file)
else:
    user_database = []

while True:
    print("\n--- MargDarshak AI Chatbot ---")
    name_input = input("Kripya apna shubh naam darj karein (Ya Exit likhein): ")
    
    if name_input.lower() == 'exit':
        print("\nMargDarshak AI se baat karne ke liye shukriya! Bye Bye!")
        break
        
    elif name_input == 'bbd_boss':
        print("\n🔒 SYSTEM RECOGNIZED: Welcome Creator/Admin.")
        attempts = 3
        login_success = False
        
        while attempts > 0:
            pass_check = input(f"Kripya Admin Password darj karein (Maukah bache hain: {attempts}): ")
            if pass_check == correct_password:
                print("✅ Admin Login Safal!")
                login_success = True
                break
            else:
                attempts -= 1
                print("❌ Galat Password!")
                
        if login_success:
            while True:
                print("\n--- ⚙️ CONTROL ROOM (ADMIN CORNER) ---")
                print("1. View All Registered Users & Marks")
                print("2. Change Admin Password")
                print("3. Clear Entire Database (Reset System)")
                print("0. Back to Chatbot Mode")
                
                admin_choice = input("\nApni choice chunein (0-3): ")
                
                if admin_choice == '0':
                    break
                elif admin_choice == '1':
                    print("\n--- 📂 PERMANENT DATABASE ANALYTICS ---")
                    if len(user_database) == 0:
                        print("Database khali hai!")
                    else:
                        for index, user in enumerate(user_database, 1):
                            user_class = user.get("user_class", "12th")
                            print(f"{index}. Name: {user['user_name']} | Class: {user_class} | Marks: {user['user_marks']}%")
                elif admin_choice == '2':
                    print("\n--- CHANGE ADMIN PASSWORD ---")
                    old_p = input("Puraana password likhein: ")
                    if old_p == correct_password:
                        new_p = input("Naya password banayein: ")
                        confirm_p = input("Naya password Fir se (Confirm): ")
                        if new_p == confirm_p:
                            correct_password = new_p
                            with open(CONFIG_FILE, "w") as config_file:
                                json.dump({"password": correct_password}, config_file, indent=4)
                            print("✅ Password permanent save ho gaya!")
                        else:
                            print("❌ Password match nahi huye!")
                    else:
                        print("❌ Puraana password galat hai!")
                elif admin_choice == '3':
                    confirm_clear = input("🚨 WARNING: Kya aap sach me pura data delete karna chahte hain? (yes/no): ")
                    if confirm_clear.lower() == 'yes':
                        user_database = []
                        if os.path.exists(FILE_NAME):
                            os.remove(FILE_NAME)
                        print("🗑️ Database successfully cleared/reset!")
        continue

    else:
        print(f"\nHello {name_input}! MargDarshak AI me aapka swagat hai.")
        
        while True:
            class_choice = input("Aap kis class me hain? (10 ya 12) likhein: ")
            if class_choice == "10" or class_choice == "12":
                break
            else:
                print("❌ Galat input! Kripya sirf '10' ya '12' hi likhein.\n")
                
        percent = input(f"Apne Class {class_choice} ke percent likho: ")
        percent_number = int(percent)
        
        user_data = {
            "user_name": name_input,
            "user_class": class_choice,
            "user_marks": percent_number
        }
        user_database.append(user_data)
        with open(FILE_NAME, "w") as file:
            json.dump(user_database, file, indent=4)
            
        print(f"\n--- 🎯 GUIDANCE REPORT FOR {name_input.upper()} (CLASS {class_choice}) ---")
        
        if class_choice == "10":
            print("\n📌 [YOUR STREAM SELECTION PLAN BASED ON MARKS]")
            if percent_number >= 80:
                print("-> RECOMMENDATION: Science Stream (PCM/PCB) lein.")
            elif percent_number >= 60:
                print("-> RECOMMENDATION: Commerce Stream lein.")
            else:
                print("-> RECOMMENDATION: Arts Stream lein.")
                
            while True:
                print("\n📌 [SELECT FUTURE ROADMAP PLAN]")
                print("A. View Complete Study Plan for Next 2 Years")
                print("B. Top Technical Skills to master right now")
                print("C. I have a Doubt/Question in mind (FAQs) 🧐")
                sub_choice = input("Kya check karna chahte hain (A, B ya C): ")
                
                if sub_choice.upper() == 'A':
                    print("\n--- 📆 2-YEAR MASTER STUDY PLAN ---")
                    print("Phase 1 (Class 11): NCERT ke Concepts mazboot karein, Base hilega to competitive exams nahi nikalenge.")
                    print("Phase 2 (Class 12): Board exams ke sath-sath JEE, NEET, ya CA-Foundation ke mock tests dena shuru karein.")
                    break
                elif sub_choice.upper() == 'B':
                    print("\n--- 🛠️ TECHNICAL SKILLS ROADMAP ---")
                    print("1. Coding: YouTube se Basic Python programming seekhein (FreeCodeCamp channel check karein).")
                    print("2. Designing: Canva aur Photoshop par Haath saaf karein, freelancing ki duniya me paisa kama sakte hain.")
                    break
                elif sub_choice.upper() == 'C':
                    print("\n--- 🧐 FREQUENTLY ASKED QUESTIONS (CLASS 10) ---")
                    print("1. Mere percent achhe hain par mujhe doosri stream me interest hai (Marks vs Interest)?")
                    print("2. School aur coaching ke sath skills ke liye time kaise nikalein (Time Management)?")
                    faq_choice = input("Apna sawal chunein (1-2): ")
                    if faq_choice == '1':
                        print("\n💡 JAWAB: Marks sirf aapki mehnat dikhate hain, interest nahi! Agar aapka sapna UPSC/Arts me hai, to 90% aane par bhi aap Arts le sakte hain. Kisi ke dabav me Science na lein.")
                    elif faq_choice == '2':
                        print("\n💡 JAWAB: Roz sirf 45 minutes nikalna seekhein. School bus me aate-jaate YouTube par tutorials dekhein, aur Sunday ko 2 ghante practical practice karein. Consistency hi sab kuch hai!")
                    break
                else:
                    print("❌ Galat input! Kripya sirf 'A', 'B' ya 'C' hi darj karein.\n")
                    
        elif class_choice == "12":
            while True:
                print("A. Check Placement Eligibility (12th Marks)")
                print("B. Explore Career Fields & Implementation Ideas")
                print("C. I have a Doubt/Question in mind (FAQs) 🧐")
                sub_choice = input("Kya check karna chahte hain (A, B ya C): ")
                
                if sub_choice.upper() == 'A':
                    if percent_number < 60:
                        print("-> Target: Product-Based Companies & Startups (Marks don't matter there!)")
                    else:
                        print("-> Wah! Aap campus ki sabhi companies me baith sakte hain.")
                    break
                    
                elif sub_choice.upper() == 'B':
                    print("\n--- Career Fields ---")
                    print("1. Web Dev\n2. AI / ML\n3. Cyber Security\n4. Data Science")
                    field = input("Apna option chunein (1-4): ")
                    
                    print("\n--- 💡 ACTION PLAN & IMPLEMENTATION IDEA ---")
                    if field == '1':
                        print("-> WHAT TO DO: JavaScript aur React seekhna shuru karein!")
                        print("-> HOW TO COMPLETE: YouTube par 'Chai aur Code' channel se Web Dev playlist khatam karein aur 3 projects banakar GitHub par daalein.")
                    elif field == '2':
                        print("-> WHAT TO DO: Python aur Mathematics (Linear Algebra) par dhyan dein.")
                        print("-> HOW TO COMPLETE: Coursera se Andrew Ng ka 'Machine Learning' free course karein aur Kaggle par datasets analyze karna shuru karein.")
                    elif field == '3':
                        print("-> WHAT TO DO: Linux Terminal aur Networking ke basics seekhein.")
                        print("-> HOW TO COMPLETE: Phone me Termux ya laptop me Ubuntu install karein. 'Cisco CCNA' ki free videos dekhein aur Port Scanning sikhein.")
                    elif field == '4':
                        print("-> WHAT TO DO: Python Libraries (Pandas, NumPy) aur Statistics seekhein.")
                        print("-> HOW TO COMPLETE: 'Codebasics' YouTube channel se Data Analytics roadmap follow karein aur Excel ke basic formulas sikhein.")
                    else:
                        print("-> Invalid option!")
                    break
                elif sub_choice.upper() == 'C':
                    print("\n--- 🧐 FREQUENTLY ASKED QUESTIONS (CLASS 12) ---")
                    print("1. Kya free YouTube courses se sach me job milegi ya paid certificate chahiye?")
