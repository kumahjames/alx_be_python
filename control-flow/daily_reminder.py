Task = input("Enter your task")
Priority = input(" Priority (high/medium/low):")
Time_Bound = input("Is it time-bound? (yes/no):")

match Priority:
    case "high":
        if Time_Bound == "yes":
          print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
          print(f"Reminder: '{Task}' is a high priority task. Please complete it soon!")
    case "medium":
      if Time_Bound == "yes":
          print(f"Reminder: '{Task}' is a meduim priority task that should be done today!")
      else:
          print(f"Note: '{Task}'is a meduim priority task. Plan to do it this week!")
    case "low":
      if Time_Bound == "yes":
          print(f"Reminder: '{Task}' is a low priority task with a deadline.Try to complete it when possible.")
      else:
         print(f"Note '{Task}'is a low priority task. Consider completing it when you have free time!")
    case _:
        print("Invalid priority level! Kindly enter high, medium, or low.")