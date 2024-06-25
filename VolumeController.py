import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


cap = cv2.VideoCapture(0)  # 0 for webcam

detector = htm.HandDetector(detectionCon=0.7)  # 0.7 for detection confidence

devices = AudioUtilities.GetSpeakers()  # get the speakers device

interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)  # activate the speakers device

# cast the interface to a pointer of the speakers
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volBar = 400  # volume bar height
volPer = 0  # volume percentage


pTime = 0  # previous time for fps calculation
while True:
    success, img = cap.read()  # read the image from the webcam
    img = detector.findHands(img)  # find the hands in the image
    # find the landmarks of the hands
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]  # thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]  # index finger tip
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # center of the line

        cv2.circle(img, (x1, y1), 15, (255, 0, 255),
                   cv2.FILLED)  # thumb tip circle

        cv2.circle(img, (x2, y2), 15, (255, 0, 255),
                   cv2.FILLED)  # index finger tip circle

        # line between thumb tip and index finger tip
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        cv2.circle(img, (cx, cy), 15, (255, 0, 255),
                   cv2.FILLED)  # center of the line circle

        # length of the line between thumb tip and index finger tip
        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Hand range 15 - 170 (this varies depending on the distance from the camera, so you may need to adjust this range)
        # Volume Range -65 - 0

        # map the length to the volume
        vol = np.interp(length, [15, 170], [minVol, maxVol])

        # map the length to the volume bar
        volBar = np.interp(length, [15, 170], [400, 150])

        # map the length to the volume percentage
        volPer = np.interp(length, [15, 170], [0, 100])

        # print(int(length), vol)

        volume.SetMasterVolumeLevel(vol, None)
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)  # volume bar

    cv2.rectangle(img, (50, int(volBar)), (85, 400),
                  (255, 0, 0), cv2.FILLED)  # volume bar fill

    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)  # volume percentage

    # fps calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)  # fps

    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
