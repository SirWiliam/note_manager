
notes = [{
        'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
    },
        {
            'username': 'Мария',
            'title': 'Учеба',
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '25-11-2024',
            'issue_date': '01-12-2024'
        },
        {
            'username': 'Иван',
            'title': 'План работы',
            'content': 'Завершить проект',
            'status': 'выполнено',
            'created_date': '20-11-2024',
            'issue_date': '26-11-2024'
        }]



def search_notes(notes, keyword = None, status = None):
    for i in notes:
        if (i['title'] == keyword or
                i['username'] == keyword or
                i['content'] == keyword):
            print(*i.items(), sep='\n')
            break

    #a = 0
    #while True:
        #for i in range(len(notes)):
            #if (notes[i]['title'] != keyword and
                #notes[i]['username'] != keyword and
                #notes[i]['content'] != keyword):
                #continue
            #if notes[i]['status'] != status:
                #continue
            #elif notes[i]['status'] == status:
                #print(f'Заметка №{a + 1}:')
                #a += 1
                #print(*notes[i].items(), sep='\n')
                #print('-----------------------------')
            #elif (notes[i]['title'] == keyword or
                  #notes[i]['username'] == keyword or
                  #notes[i]['content'] == keyword):
                #print(f'Заметка №{a + 1}:')
                #a += 1
                #print(*notes[i].items(), sep='\n')
                #print('-----------------------------')
        #else:
            #break


while True:
    print('Какой тип пойска заметки хотите осуществить?')
    question = input('1 - по ключевому слову\n'
                     '2 - по статусу\n'
                     '3 - по ключевому слову и статусу\n'
                     'Введите цифру вашего выбора: ')
    if question == '1':
        keyword = input('Введите имя, название или описание заметки для поиска: ')
        print('Результат поиска по ключевому слову:')
        search_notes(notes, keyword)
        break
    if question == '2':
        status = input('Введите статус заметки для поиска (новая, в процессе, выполнено): ')
        print('Результат поиска по статусу:')
        search_notes(notes, status)
        break
    if question == '3':
        keyword = str(input('Введите имя, название или описание заметки для поиска: '))
        status = str(input('Введите статус заметки для поиска (новая, в процессе, выполнена): '))
        search_notes(notes, keyword, status)
        break




