import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre
import matplotlib.animation as animation

# 1. Графики полиномов Лежандра
x = np.linspace(-1, 1, 1000)

plt.figure()
for n in range(1, 8):
    plt.plot(x, eval_legendre(n, x), label=f'n = {n}')
    plt.legend(title='Legendre Polynomials')
plt.title('Legendre Polynomials')
plt.show()

# 2. Ряд из фигур Лисажу
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2 * np.pi * 3 * t)
s2 = np.sin(2 * np.pi * 2 * t)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(s1, s2)
axs[0, 0].set_title('3:2')

axs[0, 1].plot(s1, s2, 'tab:orange')
axs[0, 1].set_title('3:4')

axs[1, 0].plot(s1, s2, 'tab:green')
axs[1, 0].set_title('5:4')

axs[1, 1].plot(s1, s2, 'tab:red')
axs[1, 1].set_title('5:6')

for ax in axs.flat:
    ax.set(xlabel='s1', ylabel='s2')

plt.show()

# 3. Анимация вращения фигуры Лисажу
fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(np.sin(x), np.cos(x))

def animate(i):
    line.set_xdata(np.sin(x + i/10))
    line.set_ydata(np.cos(x + i/10))
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()

# 4. Блок моделирования сложения 2 волн
fig, axs = plt.subplots(3)

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

axs[0].plot(t, s)

axs[1].plot(t, 2*s)

axs[2].plot(t, s + 2*s)

plt.show()

# 5. Изображение с двумя трехмерными графиками MSE
fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sqrt(x**2 + y**2)

ax1.plot_surface(x, y, z, cmap='viridis')
ax1.set_title('3D plot')

ax2.plot_surface(x, y, z, cmap='viridis')
ax2.set_yscale('log')
ax2.set_title('3D plot with log scale')

plt.show()
