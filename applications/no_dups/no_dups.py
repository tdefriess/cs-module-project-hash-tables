def no_dups(s):
    # Your code here
    words = s.split()
    used_words = {}
    new_string = ''

    for word in words:
        if word not in used_words:
            used_words[word] = 1
            new_string += f'{word} '

    return new_string.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))