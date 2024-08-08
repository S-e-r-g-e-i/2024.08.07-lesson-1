# Средний балл
# Дано:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

# Нужно: Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

# Решение:

avarage_grades = [sum(grades[0]) / len(grades[0]),
                  sum(grades[1]) / len(grades[1]),
                  sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]),
                  sum(grades[4]) / len(grades[4])] # создал список средних оценок учеников в той же последовательности
print(avarage_grades) # вывел на экран

print(type(students)) # уточнил тип данных - set (множество)
list_students = list(students) # перевел set в list (список) для последующей сортировки
sort_list_students = sorted(list_students) # отсортировал по возрастанию элементы списка (от A до Z)
print(sort_list_students) # вывел список на экран

new_dict_students = {sort_list_students[0]: avarage_grades[0],
                     sort_list_students[1]: avarage_grades[1],
                     sort_list_students[2]: avarage_grades[2],
                     sort_list_students[3]: avarage_grades[3],
                     sort_list_students[4]: avarage_grades[4]} # сформировал требуемый словарь при помощи списков sort_list_students и avarage_grades
print('Список средних баллов всех учеников: ', new_dict_students)  # вывел решение задания на экран
print(type(new_dict_students)) # уточнил тип данных dict (словарь)
# далее сделеал для себя - вывод среднего балла конкретного ученика
avarage_grades_oneperson = input('Введите фамилию ученикка для просмотра среднего балла: ') # создал переменную, значение которой будет вводится при запуске кода (запрос)
print('Средний балл:', new_dict_students.get(avarage_grades_oneperson, 'данный ученик отсутствует')) # Вывод на экран среднего балла ученика по ранее выполненному запросу