#!/usr/bin/python3
"""print text"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each
        of these characters: ., ? and :
        Args:
            text: string
        Raises:
            TypeError: text must be string
        Returns:
            None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()
            i += 1
            while text[i] == ' ':
                i += 1
        if i < len(text):
            print(text[i], end="")
            i += 1
