import cv2
import numpy as np

image = cv2.imread("solar-system.jpg")


cv2.putText(image,
    "sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "mercury",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "venus",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "earth",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "mars",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "jupiter",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "saturn",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "urenum",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(image,
    "naptune",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.imshow("Output",image)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",image)
