task = input("Enter your task")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match Priority:
    case "high":
        if time_bound == "yes" :
         print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
           print(f"Reminder: '{task}' is a high priority task. please complete is it soon!")
    case "medium":
      if time_bound == "yes":
          print(f"Reminder: '{task}' is a meduim priority task that should be done today!")
      else:
         print(f"Note '{task}'is a meduim priority task. plan to do it this week!")
    case "low":
      if time_bound == "yes":
         print(f"Reminder: '{task}' is a low priority task with a deadline.Try to complete it as soon as possible!")
      else:
        print(f"Note '{task}'is a low priority task. consider completing it when you have free time !")
    case _ :
      print("Invalid priority level! Kindly enter high, medium, or low. ")