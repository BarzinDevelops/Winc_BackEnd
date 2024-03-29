# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    """foo = list(range(10))
    print(get_item_from_list(foo, 3))
    print(get_item_from_list(foo, '8e'))
    print(get_item_from_list(foo, 10)) """
    """ testfile1 = f'errors\\test.txt'
        testfile2 = f'errors\\dummy.py'
        print(read_file(testfile1))
        print(read_file(testfile2)) """
    print(add(4, 2))
    print(add("Hi",2))
    ...

"""Change the three functions below from Look Before You Leap (LBYL) to Easier to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
""" def add(x, y):
    if type(x) is str and (type(y) is int or type(y) is float):
        return 0
    elif type(y) is str and (type(x) is int or type(x) is float):
        return 0
    return x + y """


def add(x,y):
    try:
        return x + y
    except:
        return 0
    
# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
""" def read_file(filename):
    if os.path.exists(filename):
        return open(filename, "r").read()
    else:
        return "" """


def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        return f"ERROR: {e}"


# Returns item at `index` from list `l` if possible, otherwise returns None
""" def get_item_from_list(l, index):
    max_index = len(l) - 1
    min_index = -1 - max_index
    if index <= max_index and index >= min_index:
        return l[index]
    else:
        return None """
    
def get_item_from_list(l, index):
    try:
        return l[index]
    except IndexError:
        return None
    except Exception as err:
        return f"Your input caused this error:\n{err}"

if __name__ == "__main__":
    main()
