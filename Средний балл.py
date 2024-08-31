#Оценки
grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
#Среднее арифмитическое оценок
average_grades = [sum(sublist) / len(sublist) for sublist in grades]
#Имена студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Имена студентов в алфавитном порядке
name = sorted(list(students))
#Имена студентов и их среднее арифметическое
student_grades = dict(zip(name, average_grades))
#Вывод
print(student_grades)