import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Assuming `image_list` is a list of 9 image paths

images = [mpimg.imread(f'car_detect_viewpoint_results/yolov8_viewpoint_{i+1}.png') for i in range(9)]
# Create a 3x3 grid of subplots with no spacing between them
fig, axs = plt.subplots(3, 3, figsize=(35, 10))
plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, top=1, bottom=0)

for ax, img in zip(axs.ravel(), images):
    ax.imshow(img)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

# If you want to save the figure without borders and axes
# plt.savefig('/path/to/save/image_grid.png', bbox_inches='tight', pad_inches=0)

plt.show()