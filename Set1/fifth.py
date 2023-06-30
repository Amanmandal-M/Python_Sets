# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"

def reverse_string(original_string):
    reversed_str = ""
    for char in original_string:
        reversed_str = char + reversed_str
    return reversed_str

# Test the function
original_string = "Python"
reversed_str = reverse_string(original_string)
print(reversed_str)
