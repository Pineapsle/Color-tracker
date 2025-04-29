import cv2
import numpy as np

class ObjectTracker:
    def __init__(self, color_lower, color_upper, camera_index=0):
        # Set color bounds for tracking
        # Initialize video capture 

        self.color_lower = np.array(color_lower, dtype=np.uint8) # Lower boundry of the color to track
        self.color_upper = np.array(color_upper, dtype=np.uint8) # Higher boundry of the color to track

        # Initialize the camera
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Could not open video")
    
    def process_frame(self, frame):
        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for a specified color
        mask = cv2.inRange(hsv, self.color_lower, self.color_upper)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        objects = []

        for contour in contours:
            # Calculate the area of each contour
            area = cv2.contourArea(contour)
            if area > 1000: # Considering only large contours
                x, y, w, h = cv2.boundingRect(contour)
                objects.append((x, y, w, h))
        
        return objects


    def draw_tracking(self, frame, objects):
        # Draw box around the detected objects
        for (x, y, w, h) in objects:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)


    def start_tracking(self):
        
        # Start a video capture loop
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Process the current frame to get objects
            objects = self.process_frame(frame)

            # Draw boxes for objects
            self.draw_tracking(frame, objects)

            # Display the frame with tracked objects
            cv2.imshow("Object Tracking", frame)

            # Exit the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Stop the video capture when done
        self.stop()


    def stop(self):
        # Release the video capture and close all OpenCV windows
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Define color bounds for tracking (USING PURPLE)
    color_lower = [125, 50, 50]  # Lower bound for PURPLE color
    color_upper = [155, 255, 255]  # Upper bound for PURPLE color

    # Create an instance of the ObjectTracker class
    tracker = ObjectTracker(color_lower, color_upper)

    # Start tracking objects
    tracker.start_tracking()



# CTRL + / to uncomment or comment massively