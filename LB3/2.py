import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

# Загрузка данных
data = np.genfromtxt('data2.csv', delimiter=';', skip_header=1)
x = data[:, 0]
y = data[:, 1]

# 1. Сформируйте систему линейных уравнений (СЛУ) для полинома 2й степени
n = len(x)
indices = [0, n//2, -1]
selected_x = x[indices]
selected_y = y[indices]

print("Выбранные точки для СЛУ:")
for i, (xi, yi) in enumerate(zip(selected_x, selected_y)):
    print(f"Точка {i+1}: x={xi:.2f}, y={yi:.2f}")

A = np.column_stack([selected_x**2, selected_x, np.ones(3)])
print("\nМатрица коэффициентов A:")
print(A)
print("Вектор правой части b:")
print(selected_y)

# 2. Решите СЛУ
coefficients = solve(A, selected_y)
a2, a1, a0 = coefficients
print(f"\nКоэффициенты полинома:")
print(f"a2 = {a2:.4f}, a1 = {a1:.4f}, a0 = {a0:.4f}")

# 3. Получите вектор значений построенного полинома для заданных точек
poly_values = a2 * x**2 + a1 * x + a0
print("\nВектор значений полинома: " + ', '.join(map(str, poly_values)))

# 4. Постройте в одной области два графика
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7, label='Исходные данные', color='blue')
plt.plot(x, poly_values, label=f'Полином 2-й степени', color='red', linewidth=2)
plt.scatter(selected_x, selected_y, color='green', s=100, zorder=5, label='Точки для СЛУ')
plt.xlabel('Скидка')
plt.ylabel('Прибыль')
plt.title('Аппроксимация полиномом 2-й степени')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 5. Посчитайте значение квадратичного отклонения RSS
RSS = np.sum((y - poly_values)**2)
print(f"\nRSS (квадратичное отклонение) = {RSS:.4f}")

# 6. Повторите шаги 1-5 для полинома 3й степени

# 6.1. Сформируйте систему линейных уравнений (СЛУ) для полинома 3й степени
n = len(x)
indices = [0, n//3, 2*n//3, -1]  # 4 точки: начало, 1/3, 2/3, конец
selected_x_3 = x[indices]
selected_y_3 = y[indices]

print("Выбранные точки для кубического полинома:")
for i, (xi, yi) in enumerate(zip(selected_x_3, selected_y_3)):
    print(f"Точка {i+1}: x={xi:.2f}, y={yi:.2f}")

A_3 = np.column_stack([selected_x_3**3, selected_x_3**2, selected_x_3, np.ones(4)])
print("\nМатрица коэффициентов A для кубического полинома:")
print(A_3)
print("Вектор правой части b:")
print(selected_y_3)

# 6.2. Решите СЛУ для кубического полинома
coefficients_3 = solve(A_3, selected_y_3)
a3, a2, a1, a0 = coefficients_3
print(f"\nКоэффициенты кубического полинома:")
print(f"a3 = {a3:.4f}, a2 = {a2:.4f}, a1 = {a1:.4f}, a0 = {a0:.4f}")

# 6.3. Получите вектор значений построенного полинома для заданных точек
poly_values_3 = a3 * x**3 + a2 * x**2 + a1 * x + a0
print("\nВектор значений кубического полинома: " + ', '.join(map(str, poly_values_3)))

# 6.4. Постройте в одной области два графика
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7, label='Исходные данные', color='blue')
plt.plot(x, poly_values_3, label='Кубический полином', color='purple', linewidth=2)
plt.scatter(selected_x_3, selected_y_3, color='orange', s=100, zorder=5, label='Точки для СЛУ (куб.)')
plt.xlabel('Скидка')
plt.ylabel('Прибыль')
plt.title('Аппроксимация кубическим полиномом')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 6.5. Посчитайте значение квадратичного отклонения RSS для кубического полинома
RSS_3 = np.sum((y - poly_values_3)**2)
print(f"\nRSS для кубического полинома = {RSS_3:.4f}")

# 8. Выберите тот вариант, где значение отклонения (RSS) получается наименьшим
print(f"\nСравнение RSS:")
print(f"Квадратичный полином: {RSS:.4f}")
print(f"Кубический полином: {RSS_3:.4f}")

if RSS < RSS_3:
    best_poly = "квадратичный"
    best_coeff = coefficients
    best_RSS = RSS
else:
    best_poly = "кубический" 
    best_coeff = coefficients_3
    best_RSS = RSS_3

print(f"\nЛучшая модель: {best_poly} полином (RSS = {best_RSS:.4f})")

# Расчет ожидаемого значения прибыли при скидках 6 и 8 процентов
x_new = np.array([6.0, 8.0])

if best_poly == "квадратичный":
    a2, a1, a0 = best_coeff
    predictions = a2 * x_new**2 + a1 * x_new + a0
else:
    a3, a2, a1, a0 = best_coeff
    predictions = a3 * x_new**3 + a2 * x_new**2 + a1 * x_new + a0

print(f"\nОжидаемая прибыль при скидках 6% и 8%:")
for i, (discount, profit) in enumerate(zip(x_new, predictions)):
    print(f"Скидка {discount}%: прибыль = {profit:.2f}")