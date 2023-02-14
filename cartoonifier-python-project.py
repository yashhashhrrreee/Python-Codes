import cv2
import tkinter as tk
from tkinter import filedialog

def cartonify_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to the grayscale image to reduce noise
    blurred = cv2.medianBlur(gray, 5)
    
    # Apply adaptive thresholding to the blurred image to create a black and white image
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Return the thresholded image
    return thresh



# Create a GUI to select the image
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = "Select the Image", filetypes = (("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))

# Load the image
image = cv2.imread(file_path)

# Cartonify the image
cartonified = cartonify_image(image)

# Display the original and cartonified images
cv2.imshow("Original", image)
cv2.imshow("Cartonified", cartonified)

# Wait for a key press to exit the program
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
