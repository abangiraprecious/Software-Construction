# a function takes a list of strings and returns the shortest string in the list
def shortest_string(list_of_strings):
    shortest = list_of_strings[0]
    for string in list_of_strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest

print(shortest_string(["", "Exercises", "Backend"]))