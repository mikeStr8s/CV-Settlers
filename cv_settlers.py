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
    tiles = find_avg_color(cap, cont)  # List of mean color values for each contour
    assign_resource(tiles)  # Assign resources to each contour based on the tiles list

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

        for i in range(0, len(cont)):
            #  If a contour is within specified area threshold
            if 50000 > cv2.contourArea(cont[i]) > 20000:
                mask[...] = 0
                cv2.drawContours(mask, cont, i, 255, -1)  # Lay mask over the contour
                mean_val = cv2.mean(frame, mask)  # Gather the average color of the exposed camera frame
                mean_list.append(mean_val)  # Add to list
                cv2.drawContours(frame, cont, i, mean_val, -1)  # Graphically display mean color on screen for user

        cv2.imshow('colored contours', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return mean_list


def assign_resource(found_colors):
    """
    All logic that is needed for assigning resources to a tile in the list of contours
    """
    # LIST OF DUMMY DATA, CONTAINS DIRTY DATA --> TWO TOO MANY WOOD CONTOURS DUE TO CAMERA P.O.V. AT AN ANGLE TO BOARD
    # found_colors = [
    #     (104.56543261667541, 148.2875930781332, 191.76249606712113, 0.0),
    #     (116.84111463067529, 157.17359867786806, 163.180025708121, 0.0),
    #     (120.67670078266104, 162.42682721252257, 168.18292594822395, 0.0),
    #     (87.49339504387234, 106.06453090348086, 120.32947642464565, 0.0),
    #     (87.0, 106.0, 120.0, 0.0),                                          <--DUPLICATE WOOD
    #     (86.85432413079799, 106.22438804466015, 121.96509931842894, 0.0),
    #     (87.0, 106.0, 122.0, 0.0),                                          <--DUPLICATE WOOD
    #     (123.73147652707765, 130.9332281956687, 162.48173702441633, 0.0),
    #     (100.9769278187102, 143.39668887779962, 188.836410602636, 0.0),
    #     (84.12862131582624, 111.15736834753457, 163.4490850677469, 0.0),
    #     (118.34501275737257, 124.94265116003085, 154.37907197531598, 0.0),
    #     (117.39371774168012, 158.27478547227764, 163.75317437699883, 0.0),
    #     (153.60840099308865, 174.95302959135745, 214.4184056901295, 0.0),
    #     (75.94935185503559, 92.88938555169686, 151.2768971564144, 0.0),
    #     (98.69443167640685, 137.02715214393592, 182.12925996454135, 0.0),
    #     (90.78526894219593, 111.94497868892881, 129.76374652154004, 0.0),
    #     (74.62289062789749, 90.7386047546638, 152.83540407224714, 0.0),
    #     (112.09790720935601, 151.5843271524198, 157.7392859890744, 0.0),
    #     (112.16956133193457, 116.76718343241248, 144.87310098302055, 0.0),
    #     (98.32540036488952, 141.95503750253397, 187.91672410297994, 0.0),
    #     (80.77515587114652, 98.57897471423622, 118.33520956009698, 0.0)
    # ]

    # Dictionary of the resources and the colors associated. Colors are stored as BGR instead of RGB
    # IMPORTANT!!!!! - You MUST change these values depending on the environment that you are testing in.
    #                  These values are volitile depending on a whole lot of conditions.
    #                  The moment the camera is moved these values MUST be re-entered manually
    resource_dict = {(80,100,120,0): 'wood', (110,150,160,0): 'sheep', (75,100,150,0):  'brick', (120,130,160,0): 'stone', (100,140,190,0): 'wheat', (150,180,220,0): 'desert'}

    # Lists that I made because I forgot that you can do key value pairs in python
    # resource_colors = [(80,100,120,0),(110,150,160,0),(75,100,150,0),(120,130,160,0),(100,140,190,0),(150,180,220,0)]
    # resource_name = ['wood', 'sheep', 'brick', 'stone', 'wheat', 'desert']

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

    print(resource_type)
    print('Resouces found')


def find_pip_tokens():
    """
    Locate pip tiles, read values, and associate them with board tiles
    TODO: figure out if this can all be one function or if it needs to be broken up
    """


def find_settlments():
    """
    Locate settlements for each color on the board, assign them to the color that they belong to
    TODO: figure out if this can be combined with find roads
    """


def find_roads():
    """
    Locate roads for each color on the board, assign them to the color they belong to
    TODO: figure out if this can be combined with find settlements
    """


def calc_VP():
    """
    Calculate the victory points for each player. Identify the winner (assuming no one has: Largest road, Largest army, or VP cards)
    TODO: add logic and parameters
    """


##############################################################################
# THE STRECH GOAL FUNCTIONS ARE BELOW, THEY WILL REMAIN EMPTY AND BELOW THIS
# DO NOT ATTEMPT IMPLEMENTATION OF THESE FUNCTIONS UNLESS WE FIND THEY ARE
# NECESSARY OR WE HAVE ACHIEVED THE ABOVE FUNCTIONS
##############################################################################

# Function associated with handling player hands, this would assume that all players would play open handed

# Function associated with finding the longest road

# ALL functions associated with handling game assistant or AI implementation

if __name__ == '__main__':
    main()
