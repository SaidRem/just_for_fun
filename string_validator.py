# Find out if the string contains: alphanumeric character, alphabetical
# characters, digits, lowercase and uppercase characters.

# Input format: a single line containing a string.


def string_validator(string):
    if any(s.isalnum() for s in string):
        print('The string has alphanumeric characters')

    if any(s.isalpha() for s in string):
        print('The string has alphabetical characters')

    if any(s.isdigit() for s in string):
        print('The string has digits')

    if any(s.islower() for s in string):
        print('The string has lowercase characters')

    if any(s.isupper() for s in string):
        print('The string has uppercase characters')



if __name__ == '__main__':
    string = input()
    # print(any(i.isalnum() for i in string))
    # print(any(i.isalpha() for i in string))
    # print(any(i.isdigit() for i in string))
    # print(any(i.islower() for i in string))
    # print(any(i.isupper() for i in string))
    print(string_validator(string))
