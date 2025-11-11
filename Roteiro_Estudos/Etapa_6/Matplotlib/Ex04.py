import matplotlib.pyplot as plt
import numpy as np

# bar chart = Circular chart divided into slices to show percentages of the total.
#             good for visualizing distribuition among categories.

categories = ['freshamen', 'Sophomores', 'Junior', 'Senior']
values = np.array([300, 250, 375, 200])
colors = ["red", "yellow", "blue", "green"]

plt.pie(values, labels=categories, autopct="%1.1f%%", colors = colors, explode=[0, 0, 0, 0.1], shadow=True, startangle=90)

plt.title("Class size")

plt.show()