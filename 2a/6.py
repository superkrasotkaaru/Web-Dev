# sWAP cASE
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    swapped = ""

    for c in s:
        if c.islower():
            swapped = swapped + c.upper()
        elif c.isupper():
            swapped = swapped + c.lower()
        else:
            swapped = swapped + c

    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)