# Лаба 5 (вариант 14) - Анализ столбцов матрицы
print("Результат работы программы:\n")

# Готовые матрицы 3x3 
matrix1 = [[5, 12, 30], [15, 8, 45], [25, 40, 55]]
matrix2 = [[1, 60, 70], [9, 15, 25], [11, 20, 30]]

# Функция для анализа столбца
def check_column(col):
    count = 0
    total = 0
    for num in col:
        if 10 <= num <= 50:  # Диапазон 10-50
            count += 1
            total += num
    return count, total

# Анализ первой матрицы
print("Матрица 1:")
for i in range(3):
    column = [matrix1[0][i], matrix1[1][i], matrix1[2][i]]
    cnt, sm = check_column(column)
    print(f"Столбец {i+1}: {cnt} элементов (сумма={sm})" if cnt > 0 else f"Столбец {i+1}: нет подходящих чисел")

# Анализ второй матрицы
print("\nМатрица 2:")
for i in range(3):
    column = [matrix2[0][i], matrix2[1][i], matrix2[2][i]]
    cnt, sm = check_column(column)
    print(f"Столбец {i+1}: {cnt} элементов (сумма={sm})" if cnt > 0 else f"Столбец {i+1}: нет подходящих чисел")

# Чтобы окно не закрылось
input("\nНажми Enter чтобы выйти...")
