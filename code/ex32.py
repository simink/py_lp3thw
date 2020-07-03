## loops and lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# go through list
for number in the_count:
    print(f"the number is {number}")

for x in fruits:
    print('Fruit type: {}'.format(x))

# create empty list and build it
elements = []

# use range
for i in range(0,5):
    print(f"adding {i} to the list")
    # append
    elements.append(i)

# print elements
for i in elements:
    print(f"element was: {i}")

# test building a list
test = range(0,5)

for i in test:
    print(f"element was: {i}")
