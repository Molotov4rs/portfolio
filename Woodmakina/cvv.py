import cv2

# Initialize variables to store clicked points
clicked_points = []

# Mouse click event handler
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Clicked: ({x}, {y})")

# Load and display the image
image_path = r"C:\Users\exoha\OneDrive\Bureau\Woodmakina\giveup.png"
image = cv2.imread(image_path)
cv2.imshow('Image', image)

# Set the mouse click event callback
cv2.setMouseCallback('Image', click_event)

# Wait for user interaction
cv2.waitKey(0)

# Print the recorded points
print("Recorded Points:")
for point in clicked_points:
    print(point)

# Close the window
cv2.destroyAllWindows()
