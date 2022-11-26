import sys
number_a = 1000
number_b = 1000.5
print(f"number_a has type {type(number_a)} and memory {sys.getsizeof(int())}")
print(f"number_b has type {type(number_b)} and memory {sys.getsizeof(float())}")