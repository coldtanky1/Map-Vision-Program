import cv2
import numpy as np

# Load the image
image = cv2.imread('map.png', cv2.IMREAD_GRAYSCALE)

# Define the number you want to search for
target_number = 570  # Change this to your desired number

# Apply thresholding to create a binary image
print("Applying thresholding...")
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

# Find all occurrences of the target number in the binary image
print("Finding occurrences...")
row_indices, col_indices = np.where(binary_image == 255)

# Define a function to find the neighboring numbers of the target number
def find_neighbors(image, row, col):
    neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < image.shape[0] and j >= 0 and j < image.shape[1] and (i != row or j != col):
                neighbors.append(image[i, j])
    return neighbors

# Store the neighboring numbers for each occurrence
neighbor_numbers = []
for row, col in zip(row_indices, col_indices):
    neighbors = find_neighbors(binary_image, row, col)
    neighbor_numbers.append(neighbors)

# Print the results
print("Results:")
for i, (row, col) in enumerate(zip(row_indices, col_indices)):
    print(f"Found {target_number} at position ({row}, {col}) with neighbors: {neighbor_numbers[i]}")

# Display the binary image with detected numbers (for visualization)
cv2.imshow('Binary Image with detected numbers', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
