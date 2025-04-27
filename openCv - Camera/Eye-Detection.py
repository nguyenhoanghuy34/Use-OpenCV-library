import cv2

# Load mô hình Haar Cascade cho khuôn mặt và mắt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Đọc ảnh
img = cv2.imread('Media/Face-eye.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Phát hiện khuôn mặt
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    # Vẽ hình vuông quanh khuôn mặt
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]  # vùng khuôn mặt xám
    roi_color = img[y:y+h, x:x+w]  # vùng khuôn mặt màu

    # Phát hiện mắt trong vùng khuôn mặt
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        center = (ex + ew//2, ey + eh//2)  # Tính tâm elip
        axes = (ew//2, eh//2)              # Bán kính ngang và dọc
        cv2.ellipse(roi_color, center, axes, 0, 0, 360, (0, 255, 0), 2)


# Hiển thị ảnh kết quả
cv2.imshow('Detected Face and Eyes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
