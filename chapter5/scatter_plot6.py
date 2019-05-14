import numpy as np
import matplotlib.pyplot as pyplot

# Create data
MAX_RANGE = 50
sailing = (0.3 * np.random.rand(MAX_RANGE), 0.3 * np.random.rand(MAX_RANGE))
swimming = (0.4 + 0.3 * np.random.rand(MAX_RANGE), 0.4 * np.random.rand(MAX_RANGE))
riding = (0.8 + 0.3 * np.random.rand(MAX_RANGE), 0.6 * np.random.rand(MAX_RANGE))

data = ((riding, 'red', 'riding'),
        (swimming, 'green', 'swimming'),
        (sailing, 'blue', 'sailing'))

# Create plot
for coords, color, activity in data:
    x, y = coords
    pyplot.scatter(x, y, c=color, label=activity)

pyplot.title('Activities Scatter Graph')
pyplot.legend()
pyplot.show()
