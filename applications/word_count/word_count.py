def word_count(s):
    new_string = s.lower()
    for char in new_string:
        for char in new_string:
            if char in '":;,.-+=/\|[]{}()*^&':
                new_string = new_string.replace(char, '')

    word_list = new_string.split()

    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))