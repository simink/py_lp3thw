## ex37 - symbol review

# and operator
def test_and():
    choice = input("true and false is: > ")
    result = True and False

    if choice == str(result):
        print('got it right, baby')
    else:
        print('try again')

# test_and()


## with as
with open("ex15_sample.txt") as file:
    print(file.read())

## assert
x = input("type hello > ")
assert x == "hello", "x should be hello"
