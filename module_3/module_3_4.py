def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):  # перебираем *args
        if other_words[i].lower() in root_word.lower():  # если слово из *args состоит в root_word
            same_words.append(other_words[i])  # пополняем список
        elif root_word.lower() in other_words[i].lower():  # если root_word состоит в слове из *args
            same_words.append(other_words[i])  # пополняем список
    return same_words  # возвращаем список


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
