import cv2
import imutils
import datetime

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame not grabbed")
        break

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Define red color ranges
    redLower1 = (0, 120, 70)
    redUpper1 = (10, 255, 255)
    redLower2 = (170, 120, 70)
    redUpper2 = (180, 255, 255)

    # Create mask for red
    mask1 = cv2.inRange(hsv, redLower1, redUpper1)
    mask2 = cv2.inRange(hsv, redLower2, redUpper2)
    mask = cv2.bitwise_or(mask1, mask2)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        if M["m00"] > 0 and radius > 10:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Save frame
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            cv2.imwrite(f"captures/{timestamp}.jpg", frame)


            # Direction logic
            if radius > 100:
                print("Stop")
            elif center[0] < 150:
                print("Left")
            elif center[0] > 450:
                print("Right")
            elif radius < 400:
                print("Front")
            else:
                print("Stop")

    cv2.imshow("Red Detection", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()