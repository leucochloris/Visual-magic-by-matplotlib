import matplotlib.pyplot as plt

# списки на основе которых - будет строиться график
x = [1, 2, 3, 4]
y = [2, 5, 0.5, 9]

# заголовок, толщина шрифта, цвет
plt.title("Линейный график", fontsize=16, fontweight='bold', color='b')

# называем оси
plt.xlabel('Значение X', fontsize=9, color='black')
plt.ylabel('Значение У', fontsize=9, color='black')

# строим линейный график по списку Х и У
plt.plot(x, y)

# добавляем сетку
plt.grid()

# отображаем график
plt.show()
