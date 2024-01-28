import gtts


def main():
    while True:
        show_menu()
        user_input = int(input('Enter Number: '))
        if user_input == 1:
            text = input('Please Enter Your Text: ')
            result = translate(text, 'fa')
            print(result)
            get_voice(result)
        elif user_input == 2:
            text = input('Please Enter Your Text: ')
            result = translate(text, 'en')
            print(result)
            get_voice(result)
        elif user_input == 3:
            en = input('Please Enter Your Word (en): ')
            fa = input('Please Enter Your Word (fa): ')
            add_word(en, fa)
        elif user_input == 4:
            exit()


def show_menu():
    print('1_ translate english to persian'.title())
    print('2_ translate persian to english'.title())
    print('3_ add new word'.title())
    print('4_ exit'.title())


def read_data():
    all_word = {}
    with open('file.txt', 'r') as file:
        data = file.read().split('\n')
    for num in range(0, len(data), 2):
        all_word[data[num]] = data[num + 1]
    return all_word


def translate(text: str, to):
    dictionary = read_data()
    result = ''
    if to == 'fa':
        sentences = text.split('.')
        for sentence in sentences:
            words = sentence.split(' ')
            for word in words:
                word = word.strip()
                if word == ' ' or word == '.':
                    continue
                try:
                    result += dictionary[word] + ' '
                except KeyError:
                    result += word + ' '
            result += '.'
    elif to == 'en':
        sentences = text.split('.')
        for sentence in sentences:
            words = sentence.split(' ')
            for word in words:
                word = word.strip()
                if word == ' ' or word == '.':
                    continue
                for key in dictionary.keys():
                    if dictionary[key] == word:
                        result += key + ' '
                        break
                else:
                    result += word + ' '
            result += '.'
    return result


def add_word(en, fa):
    with open('file.txt', 'a') as file:
        file.write(f'\n{en}')
        file.write(f'\n{fa}')


def get_voice(text):
    voice = gtts.gTTS(text, lang='en', slow=False)
    voice.save('voice.mp3')


if __name__ == '__main__':
    main()