# Part1: implement the method: get_none()
def get_none():
    return None

# Part2_2: implement the method: flatten_dict()
def flatten_dict(received_dict):
    result_list  = list(received_dict.values())
    return result_list


if __name__ == '__main__':
    # print(get_none())
    print(f"is of type list? -> {type(flatten_dict({})) is list}")
    print(f"returns values of dict? -> {flatten_dict({'a': 42, 'b': 3.14})}")
    print(f"has [values] as part of dict items? -> {flatten_dict({'a': [42, 350], 'b': 3.14})}")