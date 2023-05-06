import pytest, main

# Part1: 
def test_get_none():
    assert main.get_none() == None

# Part2_1:

# check if the value returned by flatten_dict is a list at all:
def test_flatten_dict():
    assert type(main.flatten_dict({})) is list


# check if it returns list with values of the given dict:
def test_flatten_dict_with_values():
    assert main.flatten_dict({'a': 42, 'b': 3.14})
    
# check if returned, also contains list of values within returned list:
def test_flatten_dict_with_list_as_item():
    assert main.flatten_dict({'a': [42, 350], 'b': 3.14})


