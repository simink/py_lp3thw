## ex38 - doing things with lists

ten_things = "apples oranges crows telephone light sugar"

print("there's less than 10 things")

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'frisbee', 'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding : ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} things now")

print("all ten things ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

