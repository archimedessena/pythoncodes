
print("\nPUPILS` AND CHOICE OF FOOD.")
name = input("What is your name?")
print("Hi," , name)
print("In what class are you?")
basic = input()
print("Ok, you mean basic" , basic)

print("What day is today?")
Name_of_day = input()
days_for_option = ['Tuesday', 'Thursday']

Tuesday = "Beans or Rice or not interested any food"
Thursday = "Banku or Spaghetti or not interested any food"
while Tuesday or Thursday:
    print("Ok")
for day in days_for_option:
    print("You got your senses back")
if Tuesday:
    print(f"Will you eat {Tuesday}?")
    food_selection = input()
elif Thursday:
    print(f"Will you eat {Thursday}?")
    food_selection = input()

print(f"This pupil {name} in basic {basic} selected {food_selection} for {Name_of_day}.") 
print("Thanks for the selection")





