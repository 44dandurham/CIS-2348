def palindrome(word):
    word = word.replace(" ", "")
    return word == word[::-1]

if __name__ == '__main__':
    input_word = input()

    if palindrome((input_word)):
        print(f'{input_word} is a palindrome')
    else:
        print(f'{input_word} is not a palindrome')