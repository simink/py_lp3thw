## write a while loop function that takes in an initial value, number of times to loop and how much to increment

def run_while(max = 5, step = 1):

    i = 0
    numbers = []

    # while loop
    while i < max:
        print(f"start value {i}")
        numbers.append(i)

        i = i + step
        print("numbers in list: ", numbers)
        print(f"end value {i}")

    print(numbers)

# run while loop
run_while(10,2)
