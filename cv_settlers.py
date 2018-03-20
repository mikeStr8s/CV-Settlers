import cv2
import matplotlib.pyplot as plt
import numpy as np

# Get the original image and set to grayscale, this makes it so that there is only ever "one" color on screen
imgOriginal = cv2.imread("catan-game-board.jpg", cv2.IMREAD_GRAYSCALE)

# Scale down the original image to half scale because source image is huge
imgScaled = cv2.resize(imgOriginal, (0, 0), fx=0.5, fy=0.5)

# Logic to show the image and close the display window the moment ANY key is pressed
cv2.imshow("GreyImage", imgScaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
