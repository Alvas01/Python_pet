dict = {
    'apple': 'яблоко',
    'orange': 'апельсин',
    'lemon': 'лемон'
}

print('=' * 10, 'Dictionary Eng-Rus', '=' * 10)
help = '''
s - search a word
a - add a new word
r - remove a word
k - all keys in the dictionary
d - display the dictionary
h - help
q - quit
'''

choice = ''
while choice != 'q':
    choice = input('(h - Help >>) ')
    if choice == 's':
        word = input('Enter a word: ')
        res = dict.get(word, 'No such word!')
        print(res)
    elif choice == 'a':
        word = input('Enter a word: ')
        value = input('Enter a translation: ')
        dict[word] = value
        print('The word has been added!')
    elif choice == 'r':
        word = input('Input a word: ')
        del dict[word]
        print('The word ', word, ' has been removed')
    elif choice == 'k':
        print(dict.keys())
    elif choice == 'd':
        for i in dict:
            print(i, ': ', dict[i])
    elif choice == 'h':
        print(help)
    elif choice == 'q':
        continue
    else:
        print('Unrecognized command. Enter h for help')