# The pupils of Royal Family School and food they like by Archimedes on 30-03-19
print("\nPUPILS` AND CHOICE OF FOOD.")
print("What is your name?")
name = input()
print("Hi," , name)
print("In what class are you?")
basic = input()
print("Ok, you mean basic" , basic)

print("What day is today?")
Name_of_day = input()
days_for_option = ['Tuesday', 'Thursday']

Tuesday = "Beans or Rice or not interested any food"
Thursday = "Banku or Spaghetti or not interested any food"
while not Tuesday or Thursday:
    print("Be serious")
    break 
print("Select either Tuesday or Thursday.")
for day in days_for_option:
    print("What day is today?")
Name_of_day = input()


if Tuesday:
    print(f"Will you eat {Tuesday}?")
    food_selection = input()
elif Thursday:
    print(f"Will you eat {Thursday}?")
    food_selection = input()

print(f"This pupil {name} in basic {basic} selected {food_selection} for {Name_of_day}.") 

print("Thanks for the selection")


print("You are already sorted")












