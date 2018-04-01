import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, minDist=100, maxRadius=100)

    cv2.line(frame, (50, 0), (50, 100), (0,255,0), 1)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            print("x: ", x, ", y: ", y)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()









# field_tile = cv2.imread("many_tiles.jpg")
# output = field_tile.copy()
# gray = cv2.cvtColor(field_tile, cv2.COLOR_BGR2GRAY)
#
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, minDist=500, minRadius=150, maxRadius=300)
#
# if circles is not None:
#     circles = np.round(circles[0, :]).astype("int")
#     for (x, y, r) in circles:
#         # draw the circle in the output image, then draw a rectangle
#         # corresponding to the center of the circle
#         cv2.circle(output, (x, y), r, (0, 255, 0), 4)
#         cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
#
# cv2.imwrite('those_arent_circles.jpg', output)
#
# cv2.namedWindow('Image')
# cv2.imshow('Image', np.hstack([field_tile, output]))
# cv2.resizeWindow('Image', 600, 600)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
