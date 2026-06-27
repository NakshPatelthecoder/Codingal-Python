# Function to display the symmetric difference of two sets
def show_symmetric_difference(set1, set2, question):
    print(f"Question {question}")
    print("Set 1:", set1)
    print("Set 2:", set2)

    symmetric_diff = set1.symmetric_difference(set2)

    print("Symmetric Difference:", symmetric_diff)
    print("-" * 40)


# Question A
set1 = {"blue", "green"}
set2 = {"blue", "yellow"}
show_symmetric_difference(set1, set2, "A")

# Question B
set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
show_symmetric_difference(set1, set2, "B")