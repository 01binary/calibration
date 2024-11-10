# camera calibration with checkerboard
import numpy as np
import cv2 as cv
import glob

ROWS = 9
COLS = 6
SEARCH_WINDOW = 11
ZERO_ZONE = (-1, -1)
SHOW = True
WAIT = 1000

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points
objp = np.zeros((COLS * ROWS, 3), np.float32)
objp[:,:2] = np.mgrid[0:ROWS, 0:COLS].T.reshape(-1, 2)

print('objp after reshape')
print(objp)

# arrays to store object points and image points from all images
objpoints = [] # 3ds point in real world space
imgpoints = [] # 2d points in image plane

images = glob.glob('*.jpg')

for fileName in images:
    img = cv.imread(fileName)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    print('Processing ' + fileName)

    # find chess board corners
    ret, corners = cv.findChessboardCorners(gray, (ROWS, COLS), None)

    # if found, add object points and image points
    if ret == True:
        print('Found pattern in ' + fileName)
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray, corners, (SEARCH_WINDOW, SEARCH_WINDOW), ZERO_ZONE, criteria)
        imgpoints.append(corners2)

        # visualize match
        if SHOW == True:
            cv.drawChessboardCorners(img, (ROWS, COLS), corners2, ret)
            cv.imshow('match', img)
            cv.waitKey(WAIT)

cv.destroyAllWindows()

# calibrate

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print()
print('Camera Matrix')
print(mtx)
print()

print('Distortion Matrix')
print(dist)
print()
