text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
words = text.split()
ing_words = []
ending = 'ing'
for word in words:
    if word.endswith((',', '.')):
        word = word[:-1] + ending + word[-1]
    else:
        word = word + ending
    ing_words.append(word)
print(' '.join(ing_words))
