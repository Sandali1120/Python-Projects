# Magic Square Checker (3x3)

def is_magic_square(square):
    magic_sum = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != magic_sum:
            return False

    # Check columns
    for col in range(3):
        if square[0][col] + square[1][col] + square[2][col] != magic_sum:
            return False

    # Check diagonals
    if square[0][0] + square[1][1] + square[2][2] != magic_sum:
        return False
        
    if square[0][2] + square[1][1] + square[2][0] != magic_sum:
        return False

    return True


print("Magic Square Checker (3x3)")
square = []

# Taking input
print("Enter 3 rows (3 numbers each):")
for _ in range(3):
    row = list(map(int, input().split()))
    square.append(row)

# Checking
if is_magic_square(square):
    print("\n🎉 This is a Magic Square!")
else:
    print("\n❌ This is NOT a Magic Square.")
