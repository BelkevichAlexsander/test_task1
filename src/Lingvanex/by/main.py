def _read_line(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline().split('\t')
            try:
                if line[0][0] in ('#', '\n'):
                    continue
            except IndexError:
                break

            _sort_words(line)


def _sort_words(lst_word):
    eng_words = lst_word[0].split(';')
    rus_words = lst_word[1].split(';')
    for eng in eng_words:
        for rus in rus_words:
            _write_text_file(eng, rus)


def _write_text_file(eng, rus):
    with open('English.txt', 'a', encoding='utf-8') as eng_f, \
        open('Russian.txt', 'a', encoding='utf-8') as rus_f:
            eng_f.write(f'{eng.strip()}\n')
            rus_f.write(f'{rus.strip()}\n')


def main(path):
    _read_line(path)


if __name__ == "__main__":
    main(path='src//Lingvanex//by//PythonTest.txt')