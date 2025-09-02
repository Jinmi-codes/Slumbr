print("Welcome, weary traveler...\nDo you struggle with sleep?")
start_program = input("Type 'yes' to begin , 'no' to exit and 'return' to revisit a sleep journey: ").strip().lower()
days = 0

def log_entry(date, sleep_duration, sleep_time, save_path):
    
    try:
        with open(save_path, 'r') as f:
            content = f.read()
        day_number = content.count('Day:') + 1
    except FileNotFoundError:
        day_number = 1
    with open(f'{save_path}', 'a') as log_file:
        log_file.write(f"Day:{day_number} \n Date:{date} \n Sleep time:{sleep_time} \n Sleep duration:{sleep_duration} hours\n")
        
    
while start_program not in ["yes", "no", "return"]:
    print("Invalid input. Please type 'yes', 'no', or 'return'.")
    start_program = input("Type 'yes' to begin , 'no' to exit and 'return' to revisit a sleep journey: ").strip().lower()
    
if start_program == "yes":
    print("Great! Let's embark on a journey to better sleep.")
    print("This program will help you have a look at your sleep habits and provide some tips to improve them.")
    goal = input("Specify a goal in days to track your sleep improvement: ").strip().lower()
    print(f"Your goal is to track your sleep for {goal} days.")
    save_path = input("Specify a file to save your sleep data (e.g., sleep_data.txt): ").strip()
    if not save_path:
        save_path = "sleep_data.txt"
    print(f"Your sleep data will be saved to {save_path}, revisit it using the 'return' option.\n")
    print("Let's log your first sleep entry. Ensure to revisit this program daily to track your progress.")
    while True:
        entry_date = input("Enter the date of your sleep entry (YYYY-MM-DD): ").strip()
        invalid_date = False
        try:
            from datetime import datetime
            datetime.strptime(entry_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            invalid_date = True
        if not invalid_date:
            break   
    while True:
        sleep_duration = input("Enter the duration of your sleep in hours: ").strip()
        invalid_time = False
        try:
            sleep_duration = float(sleep_duration)
            if sleep_duration < 0:
                raise ValueError("Sleep duration cannot be negative.")
        except ValueError as e:
            print(f"Invalid input for sleep duration: {e}")
            invalid_time = True
        if not invalid_time:
            break   
    while True:
        sleep_time = input("Enter the time you went to bed (HH:MM, 24-hour format): ").strip()
        invalid_time_format = False
        try:
            from datetime import datetime
            datetime.strptime(sleep_time, "%H:%M")
        except ValueError:
            print("Invalid time format. Please use HH:MM in 24-hour format.")
            invalid_time_format = True
        if not invalid_time_format:
            break 
    log_entry(entry_date, sleep_duration, sleep_time, save_path)
    print(f"\nYour sleep entry has been logged in {save_path}.")
    
elif start_program == "return":
    print("Welcome back! Let's revisit your sleep journey.")
    save_path = input("Specify the file where your sleep data is saved (e.g., sleep_data.txt): ").strip()
    if not save_path:
        save_path = "sleep_data.txt"
    try:
        with open(save_path, 'r') as log_file:
            print("\nYour previous sleep entries:")
            print(log_file.read())
    except FileNotFoundError:
        print(f"No data found in {save_path}. Please ensure the file exists.")
    else:
        print("\nYou can continue logging your sleep entries.")
        while True:
            entry_date = input("Enter the date of your sleep entry (YYYY-MM-DD): ").strip()
            invalid_date = False
            try:
                from datetime import datetime
                datetime.strptime(entry_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                invalid_date = True
            if not invalid_date:
                break   
        while True:
            sleep_duration = input("Enter the duration of your sleep in hours: ").strip()
            invalid_time = False
            try:
                sleep_duration = float(sleep_duration)
                if sleep_duration < 0:
                    raise ValueError("Sleep duration cannot be negative.")
            except ValueError as e:
                print(f"Invalid input for sleep duration: {e}")
                invalid_time = True
            if not invalid_time:
                break
        while True:
            sleep_time = input("Enter the time you went to bed (HH:MM, 24-hour format): ").strip()
            invalid_time_format = False
            try:
                from datetime import datetime
                datetime.strptime(sleep_time, "%H:%M")
            except ValueError:
                print("Invalid time format. Please use HH:MM in 24-hour format.")
                invalid_time_format = True
            if not invalid_time_format:
                break 
        log_entry(entry_date, sleep_duration, sleep_time, save_path)
        print(f"\nYour new sleep entry has been logged in {save_path}.")
elif start_program == "no":
    print("Thank you for visiting. Remember, a good night's sleep is essential for your well-being. Take care!")
else:
    print("Invalid input. Please type 'yes', 'no', or 'return'.")
    print("Exiting the program. Remember, a good night's sleep is essential for your well-being. Take care!")

            
