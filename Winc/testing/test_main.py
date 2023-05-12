import pytest, main

# Part1: 
def test_get_none():
    assert main.get_none() == None

# Part2_1:

# check if the value returned by flatten_dict is a list at all:
def test_flatten_dict():
    # print(f"test1-> is it a list?: {type(main.flatten_dict({})) is list}")
    assert type(main.flatten_dict({})) is list
    # print(f"test1-> is it empty list?: {main.flatten_dict({})}")
    assert main.flatten_dict({}) == []


# check if it returns list with values of the given dict:
def test_flatten_dict_with_values():
    # om je eigen print ongeacht passed/failed te kunnen zien: 
    # geef volgende commando in terminal ->  pytest -rP -v
    # print(f"Result of test2: {main.flatten_dict({'a': 42, 'b': 3.14})}")
    assert main.flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
    
# check if returned, also contains list of values within returned list:
def test_flatten_dict_with_list_as_item():
    # print(f"Result of test3: {main.flatten_dict({'a': [42, 350], 'b': 3.14})}")
    assert main.flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]

""" # --------------------------------------
        # Part2_challange
#---------------------------------------
# implement flatten_dict in such a way that 
# the dictionary is flattened all the way down regardless of 
# how many nested levels original dictionary contains. For example: 
# flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
    # [42, 350, 3.14]

# flatten_dict({'a': [{'inner_inner_a': 42}]})
    # [42]

# To do this you may want to look into a 
# technique that is called recursion. """

def test_flatten_dict_challenge1():
    assert main.flatten_dict_challenge({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]
    
    
def test_flatten_dict_challenge2():
    assert main.flatten_dict_challenge({'a': [{'inner_inner_a': 42}]}) == [42]

