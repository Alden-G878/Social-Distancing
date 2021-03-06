import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

#histogram of oriented gradients detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def Detect(frame):
    #using sliding window concept
    rect, weight = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    #a, b are the x, y co-ordinates and c, d are the width and height of the frame respectively
    rect = np.array([[a, b, a + c, b + d] for (a, b, c, d) in rect])
    get = non_max_suppression(rect, probs=None, overlapThresh=0.65)
    x = 1
    for a, b, c, d in get:
        cv2.rectangle(frame, (a, b), (c, d), (139, 34, 104), 2)
        cv2.rectangle(frame, (a, b - 20), (c,b), (139, 34, 104), -1)
        cv2.putText(frame, f'Person {x}', (a, b), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 250, 0), 2)
        x += 1
    
    #final output
    cv2.putText(frame, f'Total People : {x - 1}', (20, 450), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 250), 2)
    if x > 10:
        cv2.putText(frame, f'Alert! Too Many People...', (250, 250), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 0, 0), 2)
    cv2.imshow('output', frame)
    return frame
