the_input: str = "A man, a plan, a canal: Panama"


def is_palindrome(input_text: str) -> bool:
    """
    Checks if the given input_text is a palindrome, i.e., reads the same backward as forward.
    Ignores non-alphanumeric characters and is case-insensitive.

    Args:
        input_text (str): The string to check.

    Returns:
        bool: True if input_text is a palindrome, False otherwise.
    """
    start, end = 0, len(input_text) - 1

    while start < end:
        # Skip non-alphanumeric characters from the start
        if not input_text[start].isalnum():
            start += 1
            continue

        # Skip non-alphanumeric characters from the end
        if not input_text[end].isalnum():
            end -= 1
            continue

        # Compare characters (case-insensitive)
        if input_text[start].lower() != input_text[end].lower():
            return False

        start += 1
        end -= 1

    return True


print(is_palindrome(the_input))
