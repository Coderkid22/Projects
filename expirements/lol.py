def string_to_binary(input_string):
    return ''.join(f'{ord(char):999999999999}' for char in input_string)

print(string_to_binary("Hello World"))

