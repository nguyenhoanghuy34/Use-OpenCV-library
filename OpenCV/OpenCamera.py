import cv2
import os

# Mở camera (0 thường là camera mặc định trên laptop)
cap = cv2.VideoCapture(0)

# Kiểm tra xem camera có mở thành công không
if not cap.isOpened():
    print("Không thể mở camera")
    exit()

while True:
    # Đọc frame từ camera
    ret, frame = cap.read()

    # Kiểm tra xem có đọc được frame không
    if not ret:
        print("Không thể đọc frame từ camera")
        break

    # Hiển thị video

    if ret:
        cv2.imshow('My Webcam', frame)
        path = "D:\Subject\Python\OpenCV\Picture"
        imagepath = os.path.join(path, "anh_test.jpg")
        cv2.imwrite(imagepath, frame)
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
