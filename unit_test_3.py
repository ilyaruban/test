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

result = ['На курсах Python-разработчик с нуля и Java-разработчик с нуля преподают:',
          'На курсах Python-разработчик с нуля и Fullstack-разработчик на Python преподают:',
          'На курсах Python-разработчик с нуля и Frontend-разработчик с нуля преподают:',
          'На курсах Java-разработчик с нуля и Fullstack-разработчик на Python преподают:',
          'На курсах Java-разработчик с нуля и Frontend-разработчик с нуля преподают:',
          'На курсах Fullstack-разработчик на Python и Frontend-разработчик с нуля преподают:'
          ]

mentors_names = []
for m in mentors:
    course_names = []
    for name in m:
        name_split = name.split(' ')
        name_split = name_split[0]
        course_names.append(name_split)
    mentors_names.append(course_names)


list_1 = []
def in_set_1(my_set, course_name):
    for i in range(len(mentors_names)):
        if n < 1 and i != 0:  # and (i == 1 or i == 2 or i == 3):
            my_set_1 = set(mentors_names[i])
            in_set = my_set.intersection(my_set_1)
            name_new = sorted(list(in_set))
            #print(f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new}")
            list_1.append([f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new}"])
        if n == 1 and (i != 0 and i != 1):
            my_set_1 = set(mentors_names[i])
            in_set = my_set.intersection(my_set_1)
            name_new_1 = sorted(list(in_set))
            #print(f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new_1}")
            list_1.append([f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new_1}"])

        if n == 2 and (i != 0 and i != 1 and i != 2):
            my_set_1 = set(mentors_names[i])
            in_set = my_set.intersection(my_set_1)
            name_new_2 = sorted(list(in_set))
            #print(f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new_2}")
            list_1.append([f"На курсах '{course_name[n]}' и '{course_name[i]}' преподают: {name_new_2}"])
    return list_1


n = 0
while n < len(mentors_names):
    new_set = set(mentors_names[n])
    res = in_set_1(new_set, courses)
    n = n + 1

count = 0
for i in res:
    count = count + 1

def test_3():
    count_result = 0
    for i in result:
        count_result = count_result + 1

    assert count == count_result, 'в выводе должно получиться 6 элементов'