def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the list
    min_str = min(strs, key=len)
    
    # Iterate through characters of the shortest string
    for i, char in enumerate(min_str):
        # Check if the character is not common among all strings
        if any(s[i] != char for s in strs):
            return min_str[:i]
    
    # If no mismatch found, return the entire shortest string as the common prefix
    return min_str

# Test the function
strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print("Longest common prefix:", result)
