courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

result = ['Александр: 10 раз(а)', 'Евгений: 5 раз(а)', 'Максим: 4 раз(а)']


def unique_names_func(a, b):
    all_list = []
    for m in b:
        for i in m:
            all_list.append(i)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')
        name = name[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    all_names = sorted(unique_names)
    all_names_sorted = ', '.join(all_names)
    return all_names_list


def names_top(names):
    unique_names = names
    popular = []
    for name in unique_names:
        popular.append([name, unique_names.count(name)])
    popular.sort(key=lambda x: x[1], reverse=True)
    unique_list = []
    for i in popular:
        if i not in unique_list:
            unique_list.append(i)
    top_3 = [f'{str(x[0])}: {str(x[1])} раз(а)' for x in unique_list[:3]]
    return top_3

print(names_top(unique_names_func(courses, mentors)))

def test_2():
    for i, n in zip(names_top(unique_names_func(courses, mentors)), result):
        assert i == n, 'функция должна возвращать топ-3 имен'


if __name__ == '__main__':
    test_2()
