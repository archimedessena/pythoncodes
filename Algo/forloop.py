# data structures`s for loop, determining the biggest number or value in list

data = [79, 1,]
biggest = data[0]
for val in data:
    if val > biggest:
        biggest = val

    
print(val)

# index-based for loop, talks about iterating through list or tuple but uses the range keyword
big_index = 0
for j in range(len(data)):
    if data[j] > data[big_index]:
        big_index = j

print(j)






