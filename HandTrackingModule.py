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
