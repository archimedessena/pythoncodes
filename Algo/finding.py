def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
        return n



data = [4,3,5,4,6]
target = [2,4,5,6,4,7]
count1 = count(data, target)
print(count1)  