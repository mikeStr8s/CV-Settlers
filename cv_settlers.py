import cv2
import colorsys
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    All of the sequential code that is necesary to run this application  is located here
    """
    cap = cv2.VideoCapture(1)  # Incoming video stream
    cont = find_contours(cap)  # Contour nparray returned by find_contours
    colors, tiles = find_avg_color(cap, cont)  # List of mean color values for each contour
    assign_resource(cap, colors, tiles)  # Assign resources to each contour based on the tiles list

    # End program cleanup, releasing video capture device and destroying all windows
    cap.release()
    cv2.destroyAllWindows()


def find_contours(cap):
    """
    All of the logic that is needed for finding the contours is located here.
    """
    # Update for each frame of the camera
    while cap.isOpened():
        ret, frame = cap.read()  # frame is the actual image captured by the video stream

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale

        # Thresh is the binary (black and white) threshold mapping of the grayscale image
        # Threshold takes a grayscale and converts things that are close to white to white, and things that are close to black to black
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # We only care about contours, that holds all of the contours that the findContours() returns
        # Provide findContours() with a threshold mapping and it uses the boundaries between the black and white to generate an edge
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Remove the first contour from the list, this one is usually the entire screen
        cont = contours[1:]

        # Iterate through the list of contours and only display the ones that have an area between the two values given
        for i in range(0, len(cont)):
            if 50000 > cv2.contourArea(cont[i]) > 20000:
                frame = cv2.drawContours(frame, cont, i, (0, 255, 0), 3)  # Draw the contour on the original frame from the camera

        # Show the frame captured from the camera
        cv2.imshow('frame', frame)

        # If the 'q' key is pressed, return the list of contours
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return cont


def find_avg_color(cap, cont):
    """
    All of the logic that is needed for finding the average color inside a contour is located here
    """
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        final = np.zeros(frame.shape, np.uint8)  # Unused, ignore

        # Mask acts as a hole in a black overlay allowing only what is inside the hole to be seen
        mask = np.zeros(gray.shape, np.uint8)

        mean_list = []  # List of average colors inside each contour
        centroids = []  # List of contour centriods

        for i in range(0, len(cont)):
            #  If a contour is within specified area threshold
            if 50000 > cv2.contourArea(cont[i]) > 20000:
                mask[...] = 0
                cv2.drawContours(mask, cont, i, 255, -1)  # Lay mask over the contour
                mean_val = cv2.mean(frame, mask)  # Gather the average color of the exposed camera frame
                x, y, w, h = cv2.boundingRect(cont[i])
                cx = int(x + w/2)
                cy = int(y + h/2)
                centroids.append((cx,cy))  # Add centroid
                mean_list.append(mean_val)  # Add mean color
                cv2.drawContours(frame, cont, i, mean_val, -1)  # Graphically display mean color on screen for user

        cv2.imshow('colored contours', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            return mean_list, centroids


def assign_resource(cap, found_colors, centroids):
    """
    All logic that is needed for assigning resources to a tile in the list of contours

    IMPORTANT!!!!! - You MUST change dictionary values depending on the environment that you are testing in.
                     These values are volitile depending on a whole lot of conditions.
                     The moment the camera is moved these values MUST be re-entered manually.
    """
    # Dictionary of the resources and the colors associated. Colors are stored as BGR instead of RGB
    resource_dict = {(100,100,115,0): 'wood', (125,165,170,0): 'sheep', (100,125,175,0):  'brick', (130,135,160,0): 'stone', (110,150,190,0): 'wheat', (160,180,220,0): 'desert'}

    resource_type = []  # List of each resource associated with the valid contours
    closest_color = ''

    # Itterate through the provided list of colors found inside the contours
    for a in found_colors:
        min_dist = 1234567890  # Number to represent the distance between two colors
        f = np.array(a)  # Change RGB tuple 'a' to a numpy array 'f'

        # Itterate through possible resources
        for b in resource_dict.keys():
            r = np.array(b)  # Change RGB tuple 'b' to a numpy array 'r'
            dist = np.linalg.norm(f-r)  # Calculate the euclidean distance between the two numpy arrays

            # Find the smallest distance between the found colors and the colors that represent resources
            if dist < min_dist:
                min_dist = dist
                closest_color = resource_dict[b]

        # Add resource that was closest to the color in the contour
        resource_type.append(closest_color)

    while cap.isOpened():
        ret, frame = cap.read()
        for center in centroids:
            cv2.putText(frame, resource_type[centroids.index(center)], (center[0], center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def find_pip_tokens():
    """
    Locate pip tiles, read values, and associate them with board tiles
    TODO: figure out if this can all be one function or if it needs to be broken up
    """


def find_settlements():
    """
    Locate settlements for each color on the board, assign them to the color that they belong to
    TODO: figure out if this can be combined with find roads
    """


def find_roads():
    """
    Locate roads for each color on the board, assign them to the color they belong to
    TODO: figure out if this can be combined with find settlements
    """


def calc_vp():
    """
    Calculate the victory points for each player. Identify the winner (assuming no one has: Largest road, Largest army, or VP cards)
    TODO: add logic and parameters
    """


if __name__ == '__main__':
    main()
