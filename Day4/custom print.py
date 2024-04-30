import sys

def custom_print(*values: object, file=sys.stdout, sep: str = ' ', end: str = '\n', flush: bool = False) -> None:
    """
    Custom print function that prints values to a file-like object.
    """
    # Join values with separator
    output = sep.join(str(value) for value in values)
    
    # Append end string
    output += end
    
    # Write to the file-like object
    file.write(output)
    
    # Flush the stream if flush is True
    if flush:
        file.flush()

# Example usage
custom_print("apple", "banana", "orange")  # Output: apple banana orange\n (printed to sys.stdout)
custom_print("apple", "banana", "orange", file=open("Day4\\output.txt", "w"))  # Output written to output.txt
