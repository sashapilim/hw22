# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
from operator import itemgetter

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(string):
    # Чтение данных из строки
    data = []
    for line in string.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def _sort(users_list):
    # Сортировка по возрасту по возрастанию
    return sorted(users_list, key=itemgetter('age'))


def _filter(users_list):
    # Фильтрация (старше 10 лет)
    result = []
    for person in users_list:
        if person['age'] >= 10:
            result.append(person)
    return result


def get_users_list():
    users_list = _read(csv)
    list_sorted = _sort(users_list)
    result = _filter(list_sorted)
    return result


if __name__ == '__main__':
    print(get_users_list())
