# Exercise 1
# Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and false otherwise
#def is_multiple(n, m):
  #  if n % m == 0:
   #     return True
   # else:
   #     return False
 

#print(is_multiple(1,2))



# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
#def is_even(k:int):
 #   assert type(k) == int, "Your input must be an int"
 #   return (k&1 == 0)
    
#print(is_even(40))


# Exercise 3: Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of tuple of length two. Do not use the built in function min or max in implementing your solution.

#def minmax(data):
  #  if len(data):
  #      small = large = data[0]
  #      for value in data:
  #          if value<small: small = value
  #          elif value>large: large = value
 #       return small, large

 #   else:
 #       print("Your data is empty")
 #       return
        
   

#print(minmax([1, 2, 3, 4, 5, 6, 7]))
#print(minmax([2, 3, 4, 5, 6,45, 67, 90,12]))
#print(minmax([]))



# Exercise 4: Write a Python function that takes a positive integer n and returns the sum of the squares of all positive integers smaller than n.   
#result = 0
#for numb in range(12):
 #   result = numb**2 + result
#    result += 1

#print(result)

                         
# Exercise 5: Give a single command that computes the sum from Exercise 1.4, relying on Python`s comprehension syntax and the built in sum function.
#def sumsquares(q):
 #  return sum(b*b for b in range(1, q))

#print(sumsquares(12))


#Exercise 6 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
#def sumoddsquares(k):
#    return sum(x*x for x in range(1, k) if x%2 == 1)


#print(sumoddsquares(10))


def sumodd(x):
    return (y * y for y in range(1, x) if y % 2 ==1)


print(sumodd(20))
































