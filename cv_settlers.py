import cv2
import matplotlib.pyplot as plt
import numpy as np

# Get the original image and set to grayscale, this makes it so that there is only ever "one" color on screen
catanBoardImg = cv2.imread("catan-game-board.jpg", 0)

# Canny edge detection on catanBoardImg
cannyBoardImg = cv2.Canny(catanBoardImg, 300, 400)

# Save resulting canny edge image to png file
cv2.imwrite("edges.png", cannyBoardImg)

# Logic to show the image and close the display window the moment ANY key is pressed
cv2.imshow("Edges", cannyBoardImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
