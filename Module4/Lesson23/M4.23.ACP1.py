print("=" * 40)
print("      CHARACTER FREQUENCY CHECKER")
print("=" * 40)

test_dict = {
    "A": "apple",
    "B": "banana",
    "C": "grape"
}

char = input("\nEnter a character to find: ")

frequency = 0

for value in test_dict.values():
    frequency += value.count(char)

print("\n" + "-" * 40)
print(f"Character: '{char}'")
print(f"Frequency: {frequency}")
print("-" * 40)