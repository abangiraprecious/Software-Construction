## a function that takes a list of strings and returns the longest string in the list
def longest_string(list_of_strings):
    longest = ""
    for string in list_of_strings:
        if len(string) > len(longest):
            longest = string
    return longest

print(longest_string(["PHP", "Exercises", "Backend"]))
