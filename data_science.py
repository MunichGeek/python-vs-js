# %% 
import matplotlib.pyplot as plt
from scipy import stats

x = [6, 9, 7, 7, 4, 19, 0, 8, 3, 11, 13, 10, 6]
y = [101, 87, 86, 88, 113, 88, 102, 88, 93, 80, 77, 87, 86]

slope, intercept, _, _, _ = stats.linregress(x, y)
mymodel = list(map(lambda x:slope * x + intercept, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
# %%
