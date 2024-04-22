import sys

# alpha-numeric dictionary
alpha_num = {
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4",
    "E": "5",
    "F": "6",
    "G": "7",
    "H": "8",
    "I": "9",
    "J": "10",
    "K": "11",
    "L": "12",
    "M": "13",
    "N": "14",
    "O": "15",
    "P": "16",
    "Q": "17",
    "R": "18",
    "S": "19",
    "T": "20",
    "U": "21",
    "V": "22",
    "W": "23",
    "X": "24",
    "Y": "25",
    "Z": "26"
}

# showing me the WORD passed in
word = sys.argv[1].upper()
print(f"the word you have entered is: {word}")

# create empty list and append integers
num_list = []
for i in word:
    num_list.append(int(alpha_num[i]))
print(f"this word is comprised of these numbers: {num_list}")

# sum the list and print the value
list_sum = sum(num_list)
print(f"the sum of these numbers is: {list_sum}")


total = list_sum
while total > 9:

    # new list and counter
    new_num_list = []
    nextTotal = 0

    for i in str(list_sum):
        new_num_list.append(int(i))    

    for i in new_num_list:
        nextTotal += i

    total = nextTotal

    print(f"this, then, sums to: {total}")
    

# take in word
# assign numerical values to list
# sum list
# check if resulting int is len > 1
# if yes, sum all digits
# repeat until len == 1
# print int

# TAKE THIS EVEN FURTHER by breaking down double digit numbers into single digit and then summing all of those

