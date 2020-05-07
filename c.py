#class SchoolLove:
 #   def __init__(self, name):
  #      self.name = name
  #      self.sense= []

   # def add_love(self,student):
    #    self.sense.append(student)

    #def student_not(self):
    #    return len(self.sense)

#class Physics:
  #  def __init__(self, velocity, acceleration):
 #       self.velocity = velocity
   #     self.acceleration = acceleration



#chemistry = Physics(4, 5)
#print(chemistry)




#def cool(start):
 #   a = 5 + q
 #   b = 7 + a
 #   c = 8 + b
  #  return a * b + c


#q = 4
#d = cool(5)
#print(d)        


#def hot(df,s):
 #   return df ** s


#l = hot(d, 3)
#print(l)



#the_count = [1, 2, 3, 4, 5]


#def com_():
#   fruits = ['apples', 'oranges', 'pears', 'apricots']

#change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#empty = []
#for item in change:
 #   print(item)



 # combination of dictionary, function and class

#in_need = {"help": "success",
  #          "love": "no failure"
  #          }

#class God:
#    pass

 #   def __init__(self, heaven, hell):
 #       self.heaven = heaven
 #       self.hell = hell


#class mercy:
#    def favour(self, grace):
#        self.grace = grace
#        return """God will deal with your problems,
#        I will always worship you for the rest of my life. God 
#        help me through this hard times. I am calling on you to 
#        come to my aid."""


#Archimedes = God("Archmedes", "Senadju")
#Archimedes1 = mercy()

#print(Archimedes1.favour(1))

#print (in_need["help"])
#print(in_need["love"])

#print(Archimedes.heaven)
#print((Archimedes.hell)  +  (Archimedes.hell))








#class Person:
#      def man(self):
 #           print("hello")

          

#kofi = Person()
#kofi.man()


#ama = mercy()
#print(ama.favour(2))
#print(ama.favour(5))

#print(in_need.get("love"))



#print(in_need["love"])




#good_morning = "man is not your fault"
#word = good_morning.split()
#print(word)
#words = word.pop(0)
#print(words)


#import heaven
#from heaven import blessing
#print(heaven.blessing(1))









#import ecommerce1.cars
#ecommerce1.cars()

#import random
#for i in range(3):
#      print (random.random())




#def question():
 #     print("ask any question")
 #     questions = input(">")
 #     if questions =="Do u love me?":
 #           print("ask another question")
 #           if questions == questions:
 #                 print("no")
  #    elif questions == ("do u hate me to that extend?"):
  #          print("it is normal")
  #    else:
   #         print("be serious")

          

#print(question())



# files and directory
#from pathlib import Path
#path = Path("email")
#print(path.exists ())



#class Eat:
  #    def __init__(self, come, go):
  #      self.come = come
  #      self.go = go
      
   #   def all(self):
     #       print("eat all the food in the plate")




#fufu = Eat(3,4)
#fufu.all()
            
            

#i = 0
#final = [ ]
#def cal_():
 #     for i in range(5, 19):
 #           i +=1
 #           final.append(i)
 #           return final
          


#final1 = cal_()

#print(final1)






#house = [4, 6, 7, 9]
#for item in house:
#      print(item)



#class normal:
          
  #    def oh(self):
  #          self.come = 12
   #         self.fish = 123
   #         self.fog = 45
   #         if fish > fog:
   #               print("that is how i like fishes")
   #         else:
   #             print("i hate fog")
   #         return "fishes"


          

#new = normal()
#new.come()


            
          
#import random
#values = ["Archimedes", "Sena", "Senadju"]
#print(random.choice(values))


#items = ['a', 'b', 'c']
#from itertools import permutations
#for p in permutations(items):
 #     print(p)



#def cal():
#      entry = int(input("Key in any number"))
 #     return (entry + entry * entry + entry * entry * entry)



#print(cal())





# Simple algorithm to switch on a tv
def _tv():
      print("Switch on the TV")
      print("Is the light on")
      light = input("Yes or No?")
      if light == "No":
            print("TV cannot be switched on")
            if light == "Yes":
                   print("We are good to go")
      else:
          print("The power is gone for good")

      socket = input("Is the socket working?")
      if socket  == "No":
            print("Put on the socket")
      if socket == "Yes":
            print("We are ready to watch the movies")
            print("Press the power button on the TV")
      else:
          print("It is impossible to switch the light on without power")
   


                  



switch = _tv()
print(switch)                 
            [/








def typed_property(name, expected_type):
    storage_name = '_' + name



def prop(self):
      return getattr(self, storage_name)



def prop(self, value):
      if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
          setattr(self, storage_name, value)
          return prop



class Person:
      name = typed_property('name', str)
      age = typed_property('age', int)


def __init__(self, name, age):
      self.n
























































































































