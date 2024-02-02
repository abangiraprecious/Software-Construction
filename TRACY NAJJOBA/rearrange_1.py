#!/usr/bin/env python3

import re

def rearrange_name(name):
    # Using regular expression to match the pattern "Last, First"
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)

    # Checking if the pattern was not found
    if result == None:
        # If no match, return the original name unchanged
        return name

    # Rearrange the name using the captured groups from the regex match
    # Format: "First Last"
    return "{} {}".format(result[2], result[1])

