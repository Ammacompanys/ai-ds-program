import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((12, 12))
# creates a 12 x 12 table of random numbers because heatmaps need the table format
plt.imshow(data, cmap="autumn", interpolation="nearest")
'''
display a heat map from data

plt.imshow(data) : imshow means image show turn the table into heat maps

cmap = sets the color style for heat map
colormaps = "viridis", "hot", "autumn", "cool" , "blues"

interpolation = "nearest" controls how the squares are drawn
"nearest" = means no smooth blending each number becomes a sharp square
"bicubic" = Even smoother blending, very soft look


'''
plt.colorbar() # display the color and value scaler
plt.title("2-D heat map")
plt.xlabel("Year")
plt.ylabel("Median income")
plt.show()