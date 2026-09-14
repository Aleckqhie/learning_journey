#asking the user for their task 
task = input("What is your task for today? ")
#asking for  the priority level 
priority = input("What is the priority level (high, medium, low)? ")    
#asking for time bound 
time_bound = input("What is the time bound for this task? yes or no ")
match time_bound:
    case "yes":
        deadline = input("Please enter the deadline (e.g., YYYY-MM-DD HH:MM): ")
        if priority.lower() == "high":
            print(f"Reminder: Your high-priority task '{task}' is due by {deadline}. Please ensure to complete it on time!") 
        elif priority.lower() == "medium":
            print(f"Reminder: Your medium-priority task '{task}' is due by {deadline}. Please plan accordingly.")
        elif priority.lower() == "low":
            print(f"Reminder: Your low-priority task '{task}' is due by {deadline}. Don't forget to get it done!")
        else:
            print("Invalid priority level. Please enter high, medium, or low.")
    case "no":
        if priority.lower() == "high":
            print(f"Reminder: Your high-priority task '{task}' needs your immediate attention!")
        elif priority.lower() == "medium":
            print(f"Reminder: Your medium-priority task '{task}' should be addressed soon.")
        elif priority.lower() == "low":
            print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
        else:
            print("Invalid priority level. Please enter high, medium, or low.")
    case _:
        print("Invalid input for time bound. Please enter yes or no.")      
