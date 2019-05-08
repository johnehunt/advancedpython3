import matplotlib.pyplot as plt

n_groups = 5
bar_width = 0.35

teama_test_results = (60, 75, 56, 62, 58)
teamb_test_result = (55, 68, 80, 73, 55)

fig, ax = plt.subplots()

index_teama = range(n_groups)
index_teamb = [i + bar_width for i in index_teama]
ticks = [i + bar_width / 2 for i in index_teama]

opacity = 0.7

ax.bar(index_teama, teama_test_results, bar_width, alpha=opacity, color='b', label='Team A')
ax.bar(index_teamb, teamb_test_result, bar_width, alpha=opacity, color='g', label='Team B')

ax.set_xlabel('Labs')
ax.set_ylabel('Scores')

ax.set_title('Scores by Lab')
ax.set_xticks(ticks)
ax.set_xticklabels(('Lab 1', 'Lab 2', 'Lab 3', 'Lab 4', 'Lab 5'))

ax.legend()
fig.tight_layout()

plt.show()
