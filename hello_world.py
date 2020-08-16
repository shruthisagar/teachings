def hello_world():
    # declaration and definition
    print("Hello World!")

# hello_world()
# calling the function


def add(a, b=None):
    if not b:
        if isinstance(a, int) or isinstance(a, float):
            b = 0
        elif isinstance(a, str):
            b = ""
        elif isinstance(a, list):
            b = []
    # if b is not passed, we have to add a with 0
    # a, b are the arguments
    return a + b
    # return value

# sum = add(2)

# 2, 4 are the parameters of the function add
# print(sum)
# lists_add = add([2, 4])
# print(lists_add, "adding 2 lists")
list_a = [1, [2], 3, [4], 5]
output = []

def flatten(_list):
    if isinstance(_list, list):
        for i in _list:
            if isinstance(i, list):
                flatten(i)
            #     recursion
            else:
                output.append(i)


if __name__ == "__main__":
    flatten([1, [2], 3, [4], 5])
