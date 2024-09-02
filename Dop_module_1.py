# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортируем список студентов
sorted_students = sorted(students)

# Итерация по индексам списка sorted_students
for i in range(len(sorted_students)):
    student_name = sorted_students[i]  # Получаем имя студента по индексу
    student_grades = grades[i]         # Получаем оценки студента по индексу
    print(f"{student_name}: {sum(grades[i]) / len(grades[i])}")