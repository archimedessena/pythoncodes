# understanding more functions
# this is the name of the function and its arguments are in this first line
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #format string defining the function
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #  a normal string
    print("Man that`s enough for a party!")
    print("Get a blanket.\n")

# out of function and printing a string
print("We can just give the function numbers directly:")
# calling the function and assigning values to the arguments
cheese_and_crackers(20, 30)

#printing a string 
print("OR, we can use variables from our script:")
# variables 
amount_of_cheese = 10
amount_of_crackers = 50

# calling the function and making good use of the variables just created
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print statement
print("We can even do math inside too:")
#  ccalling the function and using it to solve math without variables but direct
cheese_and_crackers(10 + 20, 5 + 6)

# this line combines both math and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)