#Daniel Durham 1851947


word = input()
password = ''

def change_password(password):
    replacements = {
        'i': '!',
        'a': '@',
        'm': 'M',
        'B': '8',
        'o': '.'
    }

    strengthened_password = ''
    for char in password:
        if char.lower() in replacements:
            strengthened_password += replacements[char.lower()]
        elif char.upper() in replacements:
            strengthened_password += replacements[char.upper()]
        else:
            strengthened_password += char
    strengthened_password += 'q*s'

    return strengthened_password

strengthened_password = change_password(word)
print(strengthened_password)