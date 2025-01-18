

file = open('filename.txt', encoding='utf-8')
file.close()

def load_notes_from_file(filename):
    notes = []
    note = {}

    with open('filename.txt', 'r', encoding='utf-8') as file:
        all_string = file.readlines()
        symbols = ('— — —\n')
        while symbols in all_string:
            all_string.remove(symbols)
        print(all_string) # Проверка избавления от ненужных символов
        for i in all_string:
            key, value = i.split(':')
            value = value.strip()
            note[key] = value
        notes.append(note) # Передвинул и теперь только последнюю заметку записывает как надо по заданию

        print(notes)











load_notes_from_file(file)