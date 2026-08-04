"""Plotting cubes and applying colour map to it."""
import matplotlib.pyplot as plt

x_vals = range(1, 5001)
y_vals = [x**3 for x in x_vals]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.Reds, s=10)

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.ticklabel_format(style='plain')

plt.show()
