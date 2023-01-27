import random

# function to generate Powerball numbers
def generate_powerball():
    # generate 5 numbers between 1 and 69
    numbers = random.sample(range(1, 70), 5)
    # generate 1 number between 1 and 26
    powerball = random.randint(1, 26)
    # return the generated numbers as a list
    return numbers + [powerball]

# generate and print the Powerball numbers
powerball_numbers = generate_powerball()
print(powerball_numbers)
