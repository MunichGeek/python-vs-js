import timeit, random

def find_entry_in_structure(structure_to_search, value_to_find):
    return (value_to_find in structure_to_search)

data_structure = list()
for i in range(1000):
    data_structure.append(random.random())
# print(data_structure)

time_to_run = timeit.timeit("find_entry_in_structure(data_structure, 1.0)", number=int(1e6), globals=globals())
print(f"\nIt took {time_to_run:.2f} seconds to search in {type(data_structure).__name__} of length {len(data_structure)}.")