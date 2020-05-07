# write a python program that accept a user`s first name and second name and prints on the terminal in the reverse way
#first_name = input("What is your first name?")
#second_name = input("What is your second name?")
#print(second_name, first_name)




# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
# Sample data: 3, 5, 7, 23
# output List ['3' ,'5','7', '23']
#Tuple: ('3','5','7','23')

#numbers = input("Input some comma separated numbers:")
#no_ = numbers.split(' , ')
#numbers_list = tuple(numbers)
#print('no_:' , no_)
#print('number_list:', numbers_list)



# write a python program to accept a filename from the user and print the extension of that. 
# sample filename: abc.java and output : java
#filename = input("Input the filename:")
#f_extns = filename.split(".")
#print("The extension of the file is: " + repr(f_extns[-1]))

#kofi = input(" ")
#extn = kofi.split(".")
#print(repr(extn[-1]))



# write a python program to display the first and last colors from the following list
#color_list = ["Red", "Green", "White", "Black"]
#print(color_list[0], color_list[-1])



# write a python program to diplay the examination schedule
#extact the date from st_date
#exam_schedule =( 11, 12, 2014)
#print("The examination will start from: %i / %i / %i " %exam_schedule)


#var = "it will be my birthday come next month,"
#date = (1, 11, 2020)
#print(var, "the date is : %i / %i / %i"%date)



#mo = "do u know ur date of birth?"
#ans = input(">")
#varr = int(input("state it here", ' '))
#print("Oh u mean, ur date of birth is:%i / %i / %i"%varr)






# write a program to get the python version you are using
#import sys
#print("System version")
#print(sys.version)
#print("System information")
#print(sys.version_info)


# write a python program that accept an integer n and computes the value of n+nn+nnn
#a = int(input("Input an integer: "))
#n1 = int("%s" % a)
#n2 = int("%s%s" % (a, a) )
#n3 = int("%s%s%s" % (a, a, a) )
#print(n1+n2+n3)



# write a python program to print the document (syntax, description of python buitl_in_function
#Sample function : abs()
#Expected Result : abs(number) -> number
#print(abs.__doc__)



# write a python program to print the calendar of a given month and year
#import calendar
#y = int(input("Input the year: "))
#m = int(input("the month: "))
#print(calendar.month(y,m))



# write a python program that will display the first and last color of the following list
#List = ["Red", "Green", "White", "Black"]

#print(List[0], List[-1]) 



#Write a Python program to print the following here document. 
#Sample string :  a string that you "don't" have to escape
#This is a ....... multi-line heredoc 
#string --------> example
#print("""
#a string that you "don`t" have to escape
#This 
#is a ........ multiline
#heredoc string-------> example
#""")


#Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days
#from datetime import date
#firstdate = date(2010, 7, 2)
#seconddate = date(2020, 7, 11)
#number_of_days = seconddate - firstdate
#print(number_of_days)





#Write a Python program to get the volume of a sphere with radius 6.
#from math import pi
#r = 6.0
#v = 4.0/3.0*pi*r**3
#print("The volume of sphere is:", v)

# the total surface area of a cylinder
#area = 2*pi*r*9 + 2*pi*r**2
#print("The total surface area of a cylinder #is:", area)




#j = 5
#x = complex(5, 4)
#print(x)




#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
#def difference(n):
 #    if n <= 17:
 #        return 17 - n
 #    else:
 #        return (n - 17) * 2


#print(difference(87))
#print(difference(5))



#find the product of two numbers if the result is greater than 100, return out of bounds, if less return you are on track

#def multiplication(n, m):
#    if n * m >= 100:
 #       return "You are out of bounds", n*m
 #   elif n * m <= 100:
 #       return "You are on track", n*m


#print(multiplication(9, 10))
#print(multiplication(10,19))



#Write a Python program to test whether a number is within 100 of 1000 or 2000.
#number = 100
#def determine(user):
#    if user > number and user < 1000:
#        return "It is within 100 and 1000", user
 #   elif user > 1000:
  #      return "It is within 1000 and 2000", user


#print(determine(40))


#def near_thousand(n):
 #   return((abs(1000 - n) <= 100, n) or (abs(2000 - n) <= 100, n))


#print(near_thousand(900))


#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
#def addition(x, y, z):
 #   if x == y == z:
  #      return ( x + y + z) * 3
  #  else:
  #      return x + y + z


    
#print(addition(1, 2, 3))
#print(addition(3,3,3))


#Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
#def new_string(str):
#    if len(str) >= 2 and str[:3] == "Is":
 #       return str
#    return "Is" + str


#print(new_string("Array"))
#print(new_string("Archimedes"))



#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
#def larger_string(str, n):
 #   result = " "
  #  for i in range(n):
  #      result = result + str
   # return result



#print(larger_string("abc", 2))
#print(larger_string(".py", 3))



# write a Python program to find whether a given number (accept from the user) is even of odd, print out an appropriate message to the user.
#num = int(input("Enter a number:"))
#mod = num % 2
#if mod > 0:
#      print("This is an odd number")
#else:
#      print("This is an even number")

      

# Write a Python program to count the number 4 in a given list
#def list_count_4(nums):
 #     count = 0
 #     for num in nums:
  #          if num == 4:
 #                 count = count + 1
  #    return count
    

#print(list_count_4([1, 4, 6, 7, 4]))
#print(list_count_4([1, 4, 6, 4, 7, 4]))


















































