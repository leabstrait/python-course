text = """
The quick brown fox jumps over the lazy dog
""" 

word_gen = (word for word in text.split())

my_word_gen = word_gen

while True:
    in_put = input()
    if in_put == 'n':
        print(next(my_word_gen))
    elif in_put == 'q':
        break 