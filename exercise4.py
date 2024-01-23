def remove_chars(str1, n):
    """
    This function removes the first n characters from a string and returns the new string.

    Args:
        str1: The original string.
        n: The number of characters to remove from the beginning.
    
    Returns:
        The new string with the first n characters removed.
    
    Raises:
        ValueError: If n is greater than or equal to the length of the string.
    """
    if n >= len(str1):
        raise ValueError("n cannot be greater than or equal to the length of the string")
    return str1[n:]

# Example usage
str1 = "pynative"
n = 4

new_str = remove_chars(str1,n)
print(f"Original string: {str1}")
print(f"New string after removing {n} characters: {new_str}")