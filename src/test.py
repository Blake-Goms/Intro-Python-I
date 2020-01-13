test_list = [1, 2, 3, 4, 5]
test_tuple = (1, 2, 3, 4, 5)
test_set = set([1, 2, 3, 4, 5])
test_dictionary = {'key1': 'val1', 'key2': 'val2'}

# for foo in test_dictionary:
# print(foo)

for foo in test_dictionary.values():
    # prints the entire object
    print(test_dictionary)
