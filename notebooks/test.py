import numpy as np
import matplotlib.pyplot as plt

N = 1000000

# Generate random numbers in one go
x = np.random.uniform(size=N)
y = np.random.uniform(size=N)

# Calculate squares of x and y in one go
x2 = x ** 2
y2 = y ** 2

# Calculate distance from origin in one go
dxy = np.sqrt(x2 + y2)

# Find points within the circle in one go
inside_circle = dxy <= 1

# Count the number of points inside the circle
counts = np.sum(inside_circle)

# Calculate the estimate for pi
piestimation = 4 * counts / N

# Print the result
print("O valor de pi e", piestimation)
# Plot the points
plt.scatter(x[inside_circle], y[inside_circle], s=1, color='blue')
plt.scatter(x[~inside_circle], y[~inside_circle], s=1, color='red')

# Add a circle to the plot
circle = plt.Circle((0, 0), 1, color='black', fill=False)
plt.gca().add_patch(circle)

# Set axes and show plot
plt.axis('square')
plt.show()