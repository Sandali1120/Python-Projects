# Spot the Difference Game

import random

print("Welcome to the 'Spot the Difference' Game!")

# Two similar lists with one difference
list1 = [random.randint(1, 20) for _ in range(5)]
list2 = list1.copy()

# Change one random element in list2
index_to_change = random.randint(0, 4)
list2[index_to_change] = random.randint(21, 40)

print("\nList A:", list1)
print("List B:", list2)

guess = int(input("\nWhich index (0–4) is different? "))

if guess == index_to_change:
    print("🎉 Correct! You spotted the difference!")
else:
    print(f"❌ Wrong! The difference was at index {index_to_change}.")
