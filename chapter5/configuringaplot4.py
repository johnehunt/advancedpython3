import matplotlib.pyplot as plt

x = range(1, 11)
y = [3, 4, 6, 9, 11, 12, 10, 11, 14, 16]

# Set the axes headings
plt.ylabel('y values', fontsize=12)
plt.xlabel('x values', fontsize=12)

# Set the title
plt.title("Sample Graph")

plt.plot(x, y, linewidth=2.0, label="samples", color='blue', linestyle='--')
plt.plot(y, x, label='inverse', color='green')
plt.plot(x, range(2, 12), 'bo', label='ranged', linestyle=':', color='red')

plt.legend()

plt.show()

# Can also write it to a file
# plt.savefig("foo.png")