# Set Operations and Demonstrations

# Function to demonstrate basic set operations

def set_operations_demo():
    # Create sets
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}

    # Union
    union_set = set_a | set_b
    print(f'Union of A and B: {union_set}')

    # Intersection
    intersection_set = set_a & set_b
    print(f'Intersection of A and B: {intersection_set}')

    # Difference
    difference_set = set_a - set_b
    print(f'Difference of A and B (A - B): {difference_set}')

    # Symmetric Difference
    symmetric_difference_set = set_a ^ set_b
    print(f'Symmetric Difference of A and B: {symmetric_difference_set}')

# Execute demonstration
set_operations_demo()