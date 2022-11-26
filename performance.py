import time

num_iterations = int(1e7)
list_of_numbers = list(range(10))
print(f"Going to perform SUM of the following list, {num_iterations} times!")
print(list_of_numbers)

start_time = time.process_time()
for x in range(num_iterations):
    sum = 0
    for index in range(len(list_of_numbers)):
        sum += list_of_numbers[index]

end_time = time.process_time()
print(f"It took {(end_time - start_time)} seconds")
