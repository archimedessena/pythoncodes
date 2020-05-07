#You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a "too many values to unpack" exception 
#def drop_first_last(grades):
#    first, *middle, last = grades
 #   return avg(middle)



#grades = (3, 4, 5)
#first, *middle, last = grades


#print(drop_first_last(*middle))


# work on this later in the day and let it make a bit of sense to you whiles working on it.



# similar example
#record = ("Dave", "dave@gmail.com", "0542156890", "1234")
#name, email, *phone_numbers = record

#print(*phone_numbers, email, name)



# a sequence of tagged tuples:
records = [("foo", 1, 2), ("bar", "hello"), ("foo", 3, 4),]

def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)



print(do_foo("come",2))
print(do_bar("bar"))


# emphasis on * star expression 
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(*tail)


# other * expression
def sum(items):
    head, * tail = items
    return head + sum(tail) if tail else head



print(sum(items))


def cal(items):
    head, tail, *man = items
    return sum(man) + tail

print(cal(items))
























