import cv2
import cv2.aruco
import numpy

# aruco dictionaties
# cv2.aruco.DICT_4X4_50,
# cv2.aruco.DICT_4X4_100,
# cv2.aruco.DICT_4X4_250,
# cv2.aruco.DICT_4X4_1000,
# cv2.aruco.DICT_5X5_50,
# cv2.aruco.DICT_5X5_100,
# cv2.aruco.DICT_5X5_250,
# cv2.aruco.DICT_5X5_1000,
# cv2.aruco.DICT_6X6_50,
# cv2.aruco.DICT_6X6_100,
# cv2.aruco.DICT_6X6_250,
# cv2.aruco.DICT_6X6_1000,
# cv2.aruco.DICT_7X7_50,
# cv2.aruco.DICT_7X7_100,
# cv2.aruco.DICT_7X7_250,
# cv2.aruco.DICT_7X7_1000,
# cv2.aruco.DICT_ARUCO_ORIGINAL

DICTIONARY = cv2.aruco.DICT_ARUCO_ORIGINAL
MARKER_ID = 1
MARKER_SIZE = 300
MARKER_BORDER_WIDTH = 1
MARKER_FILENAME = "marker.png"

dictionary = cv2.aruco.getPredefinedDictionary(DICTIONARY)
marker = numpy.zeros((MARKER_SIZE, MARKER_SIZE, 1), dtype="uint8")

cv2.aruco.generateImageMarker(
    dictionary,
    MARKER_ID,
    MARKER_SIZE,
    marker,
    MARKER_BORDER_WIDTH)

cv2.imwrite(MARKER_FILENAME, marker)
cv2.imshow("ArUco Marker", marker)
cv2.waitKey(0)
