list_poems = input('Введите пыхтелку/сопелку/кричалку: ').split()

list_vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']

list_poems_vowels = []
for i in range (len(list_poems)):
    list_poems_vowels.append(list(filter(lambda x: x in list_vowels, list_poems[i])))

list_count = list(map(lambda x: True if len(x) == len(list_poems_vowels[0]) else False, list_poems_vowels))

if sum(list_count) == len(list_count):
    print('Парам пам-пам') 
else: 
    print('Пам парам')