CRISIL

A Python programming excercise.

REQUIREMENT:

Given an array of integer values select the smallest integer value which is not in the list and is not a sum of any combination of integers in the list:
INPUT & OUTPUT:

An input to the program is a Python list of integer values. Sample input below:

Input #1: [1, 2, 5, 7] - Output should be 4 Input #2: [1, 2, 2, 5, 7] - Output should be 18
SOLUTION:

STEP #1/. Create a list where each element is itself a list containing a possible combination of any integer values found in the user input

STEP #2/. Create a new list where each element is the sum of integer values found in each element of the list created in Step 1.

STEP #3/. Merge the lists created in Step 1/. and Step 2/., then create a set containing elements of both lists above, no duplicates

STEP #4/. Get minimum and maximum value of the set created in Step #3

STEP #5/. Generate range of values between MIN() and MAX() in Step #4.

STEP #6/. Loop over the range of values in Step 5. When looping save the smallest value that does not exist in the set created in Step 3/. or if no such value exists in the range select select MAX() value obtained in Step 1/. + 1 as the final answer.
REMARKS:

The code makes no attempt to generalize input, optimize for performance or cater to specific Python version.