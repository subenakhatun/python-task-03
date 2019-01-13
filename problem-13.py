'''
Write a function that takes a list of strings and prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
********
* Hello *
* World *
* in       *
* a        *
* frame *
******

'''
def print_in_a_frame(*words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))

print_in_a_frame("Hello", "World", "in", "a", "frame")