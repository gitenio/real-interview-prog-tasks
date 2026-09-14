"""
# CRISIL
A Python programming excercise.

REQUIREMENT:
------------
Given an array of integer values select the smallest integer value which is not in
the list and is not a sum of any combination of integers in the list:

INPUT & OUTPUT:
------------
An input to the program is a Python list of integer values. Sample input below:

Input #1: [1, 2, 5, 7] - Output should be 4
Input #2: [1, 2, 2, 5, 7] - Output should be 18

SOLUTION:
------------

STEP #1/. Create a list where each element is itself a list containing a possible combination
          of any integer values found in the user input

STEP #2/. Create a new list where each element is the sum of integer values found in each element
          of the list created in Step 1.

STEP #3/. Merge the lists created in Step 1/. and Step 2/., then create a set containing elements
          of both lists above, no duplicates

STEP #4/. Get minimum and maximum value of the set created in Step #3

STEP #5/. Generate range of values between MIN() and MAX() in Step #4.

STEP #6/. Loop over the range of values in Step 5. When looping save the smallest value that does
          not exist in the set created in Step 3/. or if no such value exists in the range select
          select MAX() value obtained in Step 1/. + 1 as the final answer.

REMARKS:
------------
The code makes no attempt to generalize input, optimize for performance or cater to specific Python version.

"""

usr_msg = "Smallest Integer not in input {} and not Sum of any input values is: {}"

user_input_list_1 = [1, 2, 5, 7]
user_input_list_2 = [1, 2, 2, 5, 7]


def get_all_list_elem_combinations(input_list):
    if len(input_list) == 0:
        return [[]]
    combinations_list_of_lists = []
    # loop over all slices of input array starting from second element in the list
    # recursively and insert into list the list of combinations
    for tmp_list in get_all_list_elem_combinations(input_list[1:]):
        # combine
        combinations_list_of_lists += [tmp_list, tmp_list + [input_list[0]]]
    return combinations_list_of_lists


def get_smallest_val_not_sum_and_not_in_list(input_list):
    # Step 1: find all possible combinations of elements in the input list
    possible_combinations_list = get_all_list_elem_combinations(input_list)

    # Step 2 - for each combination of elements calculate sum and create list,
    #          then combine this list with the user input list to create set
    joined_elem_set = set([sum(x) for x in possible_combinations_list] + input_list)

    # Step 3: get MIN and MAX values in the resulting set
    min_input_val = min(joined_elem_set)
    max_input_val = max(joined_elem_set)

    # Step 4: Set the initial smallest value to be the max value in set + 1
    smallest_not_sum_and_not_in_list = max_input_val + 1

    # Step 5: Loop over all values in range(min_input_val, max_input_val).
    #         If any of the values is smallet than the smallest so far
    #         reassign the smallest value not an input_list and not a sum
    #         of input values
    for val in range(min_input_val, max_input_val):
        if val in joined_elem_set:
            continue
        if val < smallest_not_sum_and_not_in_list:
            smallest_not_sum_and_not_in_list = val

    return smallest_not_sum_and_not_in_list


if __name__ == '__main__':
    smallest_int = get_smallest_val_not_sum_and_not_in_list(user_input_list_1)
    print(usr_msg.format(user_input_list_1, smallest_int))

    smallest_int = get_smallest_val_not_sum_and_not_in_list(user_input_list_2)
    print(usr_msg.format(user_input_list_2, smallest_int))