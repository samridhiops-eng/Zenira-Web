# Day Flow.py
# AI Categorization + Personalized Timetable

wake_time = input("What time do you wake up? (1-24)")
energy = input("When are you most active? (morning/night)")

# AI logic to categorize the user
if int(wake_time) <= 8 and energy.lower() == "morning":
    category = "Early Bird"
    icon = "☀️"
elif int(wake_time) >= 11 or energy.lower() == "night":
    category = "Night Owl"
    icon = "🌙"
else:
    category = "Day Spinner"
    icon = "🌀"

print(f"AI Result: You are a creative {category}! {icon}")
print("-" * 30)
print("YOUR CUSTOM TIMETABLE:")

# Timetable logic based on the AI result
if category == "Early Bird":
    print("06:00 AM - Deep Work/Study")
    print("09:00 AM - Breakfast & Planning")
    print("01:00 PM - Light Review")
    print("09:00 PM - Wind down for sleep")

elif category == "Night Owl":
    print("11:00 AM - Gentle Start & Admin")
    print("03:00 PM - Active Study")
    print("08:00 PM - Deep Creative Work")
    print("01:00 AM - Revision,self care & Rest")

else:
    print("08:00 AM - Routine Tasks")
    print("11:00 AM - Peak Learning Hour")
    print("04:00 PM - Revision & Practice")
    print("10:00 PM - Relaxation")

