# Part1: implement the method: get_none()
def get_none():
    return None

# breakpoint()
# Part2_2: implement the method: flatten_dict()
""" def flatten_dict(received_dict):
    result_list  = []
    for item in received_dict:
        print(f"item : {item}")
        if type(item) is dict or type(item) is list:
             result_list.extend(flatten_dict(item)) 
        else:
            print(f"item is: {item}")
            result_list.append(item)
            print(f"result_list is na deze append: {result_list}")
    return result_list """
    
    
def flatten_dict(dict_arg):
  dict_list = [] 
  for k,v in dict_arg.items():
    dict_list.append(v)
  return dict_list


if __name__ == '__main__':
    # print('returned from first call: ',flatten_dict({'a': [42, 350], 'b': 3.14}))
    # print('-'*30)
    # print('returned from second call: ',flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))
    pass