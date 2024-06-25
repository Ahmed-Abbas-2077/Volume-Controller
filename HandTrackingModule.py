import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5, complexity=1):
        """
            mode: In static images, set this to False. In video feed, set this to True.
            maxHands: Maximum number of hands to detect.
            detectionCon: Minimum detection confidence.
            trackCon: Minimum tracking confidence.
            complexity: Complexity of the model. 0 is the fastest, 2 is the slowest.
        """

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.complexity = complexity

        # Initialize the MediaPipe Hands model
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """ 
            Finds hands in the input image.

            Args:
                img: The input image.
                draw: Whether to draw the detected hands on the image.

            Returns:
                img: The image with the detected hands drawn.
        """

        # Convert the image to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the image to get the hand landmarks
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:  # For each detected hand
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)  # Draw the hand landmarks
        return img

    def findPosition(self, img, handNo=0, draw=True):
        """ 
            Finds the positions of the landmarks of a hand.

            Args:
                img: The input image.
                handNo: The hand number.
                draw: Whether to draw the landmarks on the image.

            Returns:
                lmList: A list of the landmarks of the hand.
        """
        lmList = []  # List to store the landmarks of the hand
        if self.results.multi_hand_landmarks:
            # Get the hand landmarks
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):  # For each landmark
                h, w, c = img.shape  # Get the height, width, and number of channels of the image
                # Get the pixel coordinates of the landmark
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 9, (0, 255, 0), cv2.FILLED)
        return lmList
