import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y = x * x

# Line plot using Matplotlib
plt.plot(x, y)
plt.show()

# Scatter plot using Matplotlib
plt.scatter(x, y)
plt.show()

# Histogram using Seaborn
sns.histplot(y)
plt.show()

# Heatmap using Seaborn
data = np.random.randn(10, 12)
sns.heatmap(data, cmap="YlGnBu")
plt.show()
