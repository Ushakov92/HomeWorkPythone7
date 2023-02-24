# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

def vowels_amount_equal(text0):
    vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
    # vowels_amount = []
    # for phrases in text0.split():
    #     counter = 0
    #     for word in phrases.split('-'):
    #         counter += len(list(filter(lambda symbol: symbol in vowels, word)))
    #     # counter = sum([len(list(filter(lambda symbol: symbol in vowels, word))) for word in phrases.split('-')])
    #     vowels_amount.append(counter)
    vowels_amount = list(map(lambda phrases: sum([len(list(filter(lambda symbol: symbol in vowels, word)))
                                                  for word in phrases.split('-')]), text0.split()))
    
    return all(x == vowels_amount[0] for x in vowels_amount)



text = input('Введите стих \n')

print('Ответ:', 'Парам пам-пам' if vowels_amount_equal(text) else 'Пам парам')