day = str(input("Enter the day (monday,tuesday,wednesday,thursday,.....)-->"))
match day:
  case "monday":
    print("**Chest Day**\n 1.Dumbbell Bench Press\n 2.Incline Dumbbell Bench Press \n 3.Push ups\n 4.Dips\n 5.Cable Curls\n 6.Tricep Dips \n 7.Cable Crossover \n 8.Weighted Dip")
  case "tuesday":
    print("Back Day\n 1.Dumbbell Row\n 2.Incline Dumbbell Row \n 3.Seated Row\n 4.Seated Cable Row \n 5.Dumbbell Shrugs \n 6.Deadlift \n 7.Pull ups \n 8.Cable Reverse Fly")
  case "wednesday":
      print("Arms Day\n 1.Triceps Pushdown\n 2.Incline Dumbbell Bicep Curl \n 3.Dumbbell Hammer Curl \n 4.Preacher Curl \n 5.Dumbbell Tricep Extension \n 6.Dumbbell Skullcrusher \n 7.Dumbbell Overhead Tricep Extension \n 8.Barbell Curl ")
  case "thursday":
      print("Legs Day\n 1.Barbell Squat \n 2.Dumbbell Squat \n 3.Leg Press \n 4.Deadlift\n 5.Leg Extensions \n 6.Calf Raises \n 7.Leg Curls \n 8.Lunges")
  case "friday":
    print("Cardio Day\n 1.Running \n 2.Cycling \n 3.Mountain Climbers \n 4.Yoga \n 5.Pilates \n 6.Rowing \n 7.Burpeesm \n 8.Push ups")
  case "saturday":
    print("Triceps Day\n 1.Triceps Pushdown\n 2.Incline Dumbbell Bicep Curl \n 3.Dumbbell Hammer \n 4.Preacher Curl \n 5.Dumbbell Tricep Extension \n 6.Dumbbell Skullcrusher \n 7.Dumbbell Overhead Tricep Extension \n 8.Triceps Kickback")
  case "sunday":
    print("Rest Day")    
print("Thanks follow for more")
