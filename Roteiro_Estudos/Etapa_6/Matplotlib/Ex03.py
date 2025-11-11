import matplotlib.pyplot as plt
import numpy as np

# bar chart = compare categories of data by representing each category with a bar

categories = ["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"]
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color='skyblue')
# plt.barh(categories, values, color='skyblue')

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()