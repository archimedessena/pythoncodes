# write a prgrom to find the lcm of two given numbers

#ask for input from user
def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y
# boolean showing a true statement
    while(True):
#after dividing the remainder compared to x and y
        if ((z % x == 0) and (z % y == 0)):
            lcm = z
            break
        z += 1

 
    return lcm

print(lcm(599, 699))




def hcf(x, y):
    if x < y:
        z = x
    else:
        z = y
  
    while(True):
        if((z % x == 0) and (z % y == 0)):
            hcf = z
            break
        z += 1


    return hcf

print(hcf(4056, 60897))
 
  
















