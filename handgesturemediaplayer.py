
import cv2
import pyautogui as gui_control
import numpy as np
import math

# Initialize the webcam feed
video_feed = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret_val, current_frame = video_feed.read()
    current_frame = cv2.resize(current_frame, (600, 600))
    current_frame = cv2.flip(current_frame, 2)
    
    # Define the region of interest for hand detection
    cv2.rectangle(current_frame, (0, 1), (400, 600), (255, 0, 0), 0)
    cropped_hand_img = current_frame[1:600, 1:400]

    # Convert the cropped image to HSV color space
    hsv_conversion = cv2.cvtColor(cropped_hand_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_conversion, np.array([0, 17, 0]), np.array([255, 255, 255]))

    # Extract the hand using the mask
    filtered_hand = cv2.bitwise_and(cropped_hand_img, cropped_hand_img, mask=mask)
    _, binarized_img = cv2.threshold(mask, 219, 255, cv2.THRESH_BINARY)

    # Reduce noise using dilation
    noise_reduced_img = cv2.dilate(binarized_img, (3, 3), iterations=7)

    # Extract contours from the binary image
    hand_contours, _ = cv2.findContours(noise_reduced_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try:
        # Select the largest contour as the hand
        largest_contour = max(hand_contours, key=lambda x: cv2.contourArea(x))
        
        # Compute the convex hull for the contour
        convex_hull_shape = cv2.convexHull(largest_contour)
        defects = cv2.convexityDefects(largest_contour, cv2.convexHull(largest_contour, returnPoints=False))

        defects_count = 0
        for i in range(defects.shape[0]):
            s, e, f, _ = defects[i, 0]
            start, end, farthest = largest_contour[s][0], largest_contour[e][0], largest_contour[f][0]

            # Compute the angle between fingers using the cosine rule
            side_a = np.linalg.norm(end - start)
            side_b = np.linalg.norm(farthest - start)
            side_c = np.linalg.norm(end - farthest)
            angle_rad = np.arccos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c))
            angle_deg = np.degrees(angle_rad)

            if angle_deg <= 48:
                defects_count += 1
        
        # Execute media control based on detected gesture
        if defects_count == 1:
            gui_control.press("space")
        elif defects_count == 2:
            gui_control.press("up")
        elif defects_count == 3:
            gui_control.press("down")
        elif defects_count == 4:
            gui_control.press("right")

    except Exception as e:
        pass

    cv2.imshow('Binary Hand Image', binarized_img)
    cv2.imshow('Webcam Feed', current_frame)

    # Exit loop when 'Esc' key is pressed
    if cv2.waitKey(25) & 0xFF == 27:
        break

video_feed.release()
cv2.destroyAllWindows()
