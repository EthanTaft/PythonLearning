"""Here is a function that takes a list as a parameter.  It squares each
element in the list and then appends that value to a new list that is originally
empty before the initialization of the for loop. This shows two ways to do it.
One sequentially in scripting fashion and then one functionally.
"""
start_list = [5, 3, 1, 2, 4]
square_list = []


for element in start_list:
  square_list.append(element**2)
square_list.sort()
print square_list

"""Or Make a function to do the same thing for future lists that need to be
squared and sorted
"""
def list_square_sort(ls):
    empty_ls = []
    for element in ls:
        empty_ls.append(element**2)
    empty_ls.sort()
    return(empty_ls)

list_square_sort(start_list)
