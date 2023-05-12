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




def flatten_dict_challenge(dict_arg): # dict_arg = {'inner_inner_a': 42}
    dict_list2 = [] 
    new_list = []
    for k, v in dict_arg.items():
        if type(v) is dict: 
            for k, v in v.items(): 
                if type(v) is dict:  
                    dict_list2.extend(flatten_dict_challenge({k, v}))
                else:
                    dict_list2.append(v) 
        elif type(v) is list: 
            for i in v:
                if type(i) is dict or type(i) is list:
                    dict_list2.extend(flatten_dict_challenge(i))
                else: 
                    new_list.append(i)
            dict_list2.extend(new_list)
        else:
            dict_list2.append(v)  # second time v = 42
    return dict_list2


""" 
def flatten_dict_challenge(dict_arg):
    if not isinstance(dict_arg, dict):
        return [dict_arg]
    
    flattened_list = []
    for value in dict_arg.values():
        if isinstance(value, dict):
            flattened_list.extend(flatten_dict_challenge(value))
        elif isinstance(value, list):
            print(f"flattend_list in list check before extend: {flattened_list}")
            flattened_list.extend([item for sublist in value for item in flatten_dict_challenge(sublist)])
            print(f"flattend_list in list check after extend: {flattened_list}")
        else:
            flattened_list.append(value)
    return flattened_list
 """

if __name__ == '__main__':
    
    # ---------------------------------------------------------------
    print('\n\n','*'*20, f'\nTestcases for challenge:','\n','*'*20,'\n')
    # ---------------------------------------------------------------

    print("case4a: {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}\n\nExpected result: [42, 350, 3.14] ")

    result4a = flatten_dict_challenge({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
    print(f"my result4a: {result4a}")
    # [42, 350, 3.14]
    


    # ----------------------------
    print('-'*20)
    print("\ncase5: {'a': [{'inner_inner_a': 42}]}\n\nExpected result: [42]")

    flatten_dict({'a': [{'inner_inner_a': 42}]})
    result5 = flatten_dict_challenge({'a': [{'inner_inner_a': 42}]})

    print(f"my result5: {result5}")
    # [42]
    
    # ----------------------------
    print('-'*20)
    print("\ncase6: {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14, 'my_twisted_list_dict': [ { 'dict_in_list_1': 'kan_dit1', 'dict_in_list_2': 888, 'nog_een_moeilijke': 999 }, {'a': [ {'inner_inner_a': [33, 'appeltje', 'eitje']} ]} ] }\n\nExpected result: [42, 350, 3.14, 'kan_dit1', 888, 999, 33, 'appeltje', 'eitje'] ")
    
    result6 = flatten_dict_challenge({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14, 'my_twisted_list_dict': [ { 'dict_in_list_1': 'kan_dit1', 'dict_in_list_2': 888, 'nog_een_moeilijke': 999 }, {'a': [ {'inner_inner_a': [33, 'appeltje', 'eitje']} ]} ] })
    
    print(f"my result4b: {result6}")
    # [42, 350, 3.14, 'kan_dit1', 888, 999, 33, 'appeltje', 'eitje']