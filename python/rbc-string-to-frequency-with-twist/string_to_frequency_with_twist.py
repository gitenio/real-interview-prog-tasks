
"""
2026-09-07: RBC recruiter-given

Problem Statement: Given a string, rearrange it such that characters appear
in decreasing order of their frequency.
If two characters have the same frequency, maintain alphabetical order.
Example: "tree" → "eert" (e appears 2 times, t and r appear 1 time each)

"""
from itertools import groupby

a_str = "cmmxbaaa"
def run_module_code_brute_force():
    a_dict = {}
    for elem in usr_input[::]:
        if elem in a_dict:
            a_dict[elem] += 1
        else:
            a_dict[elem] = 1

    print("a_list_of_tuples: {}".format(sorted(a_dict.items(), key=lambda item: item[1], reverse=True)))

    tmp_buf = [] # stores all tuples with same count of appearances - if count changes flush and clear
    tmp_count = None # count of a currently examined char while processing hash entries
    for (k, v) in sorted(a_dict.items(), key=lambda item: item[1], reverse=True):
        if tmp_count is None:
            tmp_count = v
        if tmp_count != v:
            tmp_count = v
            print(sorted(tmp_buf))
            tmp_buf.clear()

        tmp_buf.append((k, v))
    if tmp_buf:
        print(sorted(tmp_buf))

def run_module_code_oneliner(usr_input):
    print("a appears {} times".format(usr_input.count("az")))
    a_list_sorted = sorted(list(set( [(a_char, usr_input.count(a_char)) for a_char in (usr_input)] )),
        key=lambda item: item[1], reverse=True
    )
    print("Unsorted: {}".format(a_list_sorted))
    print("Sorted:   {}".format(sorted(a_list_sorted, key=lambda x: (x[1], x[0]))))
    a_list_sorted_groupby = [e for e in groupby(a_list_sorted, key=lambda item: item[1])]
    print("Sorted groupby: {}".format(a_list_sorted_groupby))
    a_list_sorted_groupby = [(e, *list(e)) for e in groupby(a_list_sorted_groupby, key=lambda item: item[1])]
    print("Sorted groupby sorted: {}".format(a_list_sorted_groupby))



if __name__ == "__main__":
    print("**********************************************************************")
    print("* Given a string, rearrange it such that characters appear           *")
    print("* in decreasing order of their frequency. If two characters          *")
    print("* have the same frequency, maintain alphabetical order.              *")
    print("* Ex: 'tree' → 'eert' (e appears 2 times, t and r appear 1 time each *")
    print("* ------------------------------------------------------------------ *")
    print("*                     Running ..                                     *")
    print("* ------------------------------------------------------------------ *")
    usr_input = input("* --> Enter a string: ")
    print("* --> Printing characters in decreasing order of appearance and      *")
    print("*     alpha order if count of appearance is the same. Enter ..       *")
    enter = input()
    print("* ------------------------------------------------------------------ *")
    # run_module_code_brute_force()
    while True:
        run_module_code_oneliner(usr_input)
        usr_input = input("* --> Enter a string. Empty input to exit: ")
        if not usr_input:
            break
    print("* ------------------------------------------------------------------ *")
    print("*                     Done ..                                        *")
    print("* ------------------------------------------------------------------ *")



