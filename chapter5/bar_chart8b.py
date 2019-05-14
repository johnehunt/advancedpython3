import matplotlib.pyplot as plt

n_groups = 5
bar_width = 0.35

teama_results = (60, 75, 56, 62, 58)
teamb_results = (55, 68, 80, 73, 55)

index_teama = range(n_groups)
index_teamb = [i + bar_width for i in index_teama]

ticks = [i + bar_width / 2 for i in index_teama]
tick_labels = ('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5')

plt.bar(index_teama, teama_results, bar_width, color='b', label='Team A')
plt.bar(index_teamb, teamb_results, bar_width, color='g', label='Team B')

plt.xlabel('Labs')
plt.ylabel('Scores')
plt.title('Scores by Lab')
plt.xticks(ticks, tick_labels)
plt.legend()

plt.show()
