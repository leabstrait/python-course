text = """

Sorry this page can't be found

"""


words = text.split()
print(words)

for ctr, word in enumerate(words):
    if word.lower() == 'sorry':
        words[ctr] = 'haha'

print(words)

new_text = ""
for word in words:
    new_text = new_text + ' ' + word

print(new_text.strip())
