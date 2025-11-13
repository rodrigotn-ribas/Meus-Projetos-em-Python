import matplotlib.pyplot as plt

# Create a figure
plt.figure()

# Get the current axes (creates one if none exist)
ax = plt.gca()

# Plot on the current axes
ax.plot([1, 2, 3], [4, 5, 6])

# Set a title for the current axes
ax.set_title("My Plot")

plt.show()