import cv2
import os

# Khởi tạo bộ phát hiện người với HOG + SVM được train sẵn
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

current_dir = os.path.dirname(__file__)
video_path = os.path.join(current_dir, "Media","video.mp4")

# Mở video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Không thể mở video. Kiểm tra lại đường dẫn!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize cho nhanh
    frame = cv2.resize(frame, (640, 480))

    # Phát hiện người
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))

    # Vẽ các bounding boxes
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    # Hiển thị kết quả
    cv2.imshow("Human Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
