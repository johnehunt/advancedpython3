import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 4, 6, 8, 11, 12, 11, 12, 13, 12]

# Set the axes headings
plt.ylabel('y values', fontsize=12)
plt.xlabel('x values', fontsize=12)

# Set the title
plt.title("Sample Graph")

# Plot and display the graph
plt.plot(x, y)
plt.show()
