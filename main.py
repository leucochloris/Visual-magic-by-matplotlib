import matplotlib.pyplot as plt

### need a hepl spend to    https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html

# basic for graphic = [1, 2, 3, 4]
y = [2, 5, 0.5, 9]

# title, weight, font, color
plt.title("Линейный график", fontsize=16, fontweight='bold', color='b')

# name of axis
plt.xlabel('Значение X', fontsize=9, color='black')
plt.ylabel('Значение У', fontsize=9, color='black')

# make graphic by list X and Y
plt.plot(x, y, label='График №1', lw=4)

# append grid
plt.grid()

# show graphic
plt.show()
