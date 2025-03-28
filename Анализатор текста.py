text = input('Введите текст: ').lower()

punctuation = [".", ",", "!", "?"]

for item in punctuation:
    text = text.replace(item, '')

words = text.split()

word_counter = set(words)
print(f"Количество разных слов: {len(word_counter)}")

word_frequency = {
}

for word in words:

    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print('Частота слов:')
for key, val in word_frequency.items():
    print(f'{key}: {val}')
