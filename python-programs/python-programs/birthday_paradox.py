# Birthday Paradox Program
# This program checks the probability that two people in a group share the same birthday.

import random

def has_duplicate_birthdays(birthdays):
    return len(birthdays) != len(set(birthdays))

def simulate(num_people, num_simulations=10000):
    duplicate_count = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if has_duplicate_birthdays(birthdays):
            duplicate_count += 1

    probability = duplicate_count / num_simulations
    return probability

print("Birthday Paradox Simulation")
num_people = int(input("Enter number of people in the room: "))
probability = simulate(num_people)

print(f"\nProbability that at least two people share a birthday in a group of {num_people} people is: {probability:.2%}")
