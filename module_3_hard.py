def calculate_structure_sum(data):

    def recursive_sum(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, str):
            return len(item)
        elif isinstance(item, (list, tuple, set)):
            return sum(recursive_sum(sub_item) for sub_item in item)
        elif isinstance(item, dict):
            return sum(recursive_sum(k) + recursive_sum(v) for k, v in item.items())
        return 0

    return recursive_sum(data)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
