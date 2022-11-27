# %%
import matplotlib.pyplot as plt
from scipy import stats

x = [6, 9, 7, 7, 4, 19, 0, 8, 3, 11, 13, 10, 6]
y = [98, 87, 86, 88, 90, 88, 94, 88, 93, 80, 82, 87, 86]

slope, intercept, _, _, _ = stats.linregress(x, y)
linear_ml = list(map(lambda x_i: slope * x_i + intercept, x))

plt.scatter(x, y)
plt.plot(x, linear_ml)
# %%
