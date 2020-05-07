#data = [ 2, 4, 6, 8]
#i = iter(data)
#next(i)
#print(i)


#class Person(object):
   # men = [2, 3, 4]
   # list_iterator(men)
    
  #  def women(self, men):
   #     self.men = men

#generators
#def factors(n): #traditional function that computes factors
  #  results = [] # store factors in a new list
  #  for k in range(1, n+ 1):
   #     if n % k == 0: # divides evenly, thus k is a factor
     #       results.append(k) # add k to the list of factors
   # return results # return the entire list


#print(factors(100))


# A better or another way of writing the above code
#def factor(b):
  # for c in range(1, b+1):
   #     if b % c == 0:
  #          yield c

#print(factor(130))          








# personal example
#def man(t):
 #   women = []
  #  for w in range(2, t + 4):
  #      if w % t == 3:
    #        women.append(w)
   # return women


#print(man(1033333))

    


# testing the square root of  a number
#def factors(n): # generator that computres factors
  #  k = 1
  #  while k * k < n: # while k < sqrt(n)
  #      if n % k == 0:
   #         yield k
  #          yield n // k
 #       k += 1
 #   if k * k == n:  # special case if n is perfect square
 #       yield k


#d = factors(100) # result 1, 100, 2, 50, 4, 25,5, 20, 10

#print(d)







# the fibonacci sequence
def fibonacci():
    a = 0
    b = 1
    while True:  # keep going 
        yield a  # report value, a, during this pass
        future = a + b
        a = b   # this will be next value reported
        b = future # and sequentially this
print(fibonacci())
# end of the iterator and generators



#import time
#print("The time is:", time.ctime())




