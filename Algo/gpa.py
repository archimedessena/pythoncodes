# algo to calculator the gpa
# map from letter grade to poing value
points = {'A+': 4.0, 'A':4.0, 'A-': 3.67, 
'B+': 3.33, 'B':3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-':1.67, 'D+': 1.33, 'D': 1.33, 'F': 0.0}

num_courses = 0
total_points = 0
done = False
while not done:
    grade = input() # red line from user 
    if grade == '': # empty line was entered
        done = True
    elif grade not in points: # unrecognized grade entered
        print("Unknown grade'{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0: # avoid division
    print("Your GPA IS {0.3}".format(total_points/ num_courses))






