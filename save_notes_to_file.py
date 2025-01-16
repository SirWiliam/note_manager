filename = open('filename.txt', 'a+', encoding='utf-8')
filename.close()
notes = []
username = input('Введите имя пользователя: ').strip().capitalize()
title = input('Введите заголовок заметки: ').strip().capitalize()
content = input('Введите описание заметки: ').strip().capitalize()
status = input('Ведите статус заметки: ').strip().lower()
created_date = input('Введите дату создания заметки:')
issue_date = input('Введите дату дедлайна: ')
notes.append(username)
notes.append(title)
notes.append(content)
notes.append(status)
notes.append(created_date)
notes.append(issue_date)

def save_notes_to_file(notes, filename):
    filename = open('filename.txt', 'w', encoding='utf-8')
    filename.write(f"Имя пользователя: {notes[0]}\n")
    filename.write(f"Заголовок: {notes[1]}\n")
    filename.write(f"Описание: {notes[2]}\n")
    filename.write(f"Статус: {notes[3]}\n")
    filename.write(f"Дата создания: {notes[4]}\n")
    filename.write(f"Дедлайн: {notes[5]}\n")
    filename.close()
    return filename

notes = save_notes_to_file(notes, filename)
