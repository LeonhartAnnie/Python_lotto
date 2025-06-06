import random

# Generate a list of 100,000 random numbers
numbers = [random.randint(1,10000) for _ in range(100000)]

# Write them to a file
with open("number.txt", "w") as generation:
    for num in numbers:
        generation.write(f"{num},")
    print("資料已寫入number.txt")