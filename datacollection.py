import cv2
import time

# initializing webcam
cap = cv2.VideoCapture(0)

# saving the images we are going to train
folder = "Data/Ram"

counter = 0

while True:
    # showing and flipping frame window
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Frame", frame)

    # taking and saving pictures to later label
    counter += 1
    cv2.imwrite(f'{folder}/Ram{counter}.jpg', frame)
    print(f'Collecting data... {folder}')
    time.sleep(2)

    # press the escape key to close the program
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
