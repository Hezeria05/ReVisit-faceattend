import cv2
from db_con import login_attendance
from face_recognition import load_face_data, KNN

# Initialize the video capture
cap = cv2.VideoCapture(0)
cas_path = "C:\\Users\\grace\\Desktop\\GitReVisit\\ReVisit-faceattend\\data\\haarcascade_frontalface_default.xml" #copy the path on your local computer
dirpath = "C:\\Users\\grace\\Desktop\\GitReVisit\\ReVisit-faceattend\\data" #copy the path on your local computer

# Load face data
face_dataset, face_labels, name = load_face_data(dirpath)

# Initialize face cascade
face_cascade = cv2.CascadeClassifier(cas_path)

# Main loop to read frames and make predictions
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)

    for face in faces[-1:]:
        x, y, w, h = face
        face_section = gray_frame[y:y+h, x:x+w]
        face_section = cv2.resize(face_section, (100, 100))
        pred = KNN(face_dataset, face_labels, face_section)
        pred_name = name[int(pred)]
        cv2.putText(frame, pred_name, (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("camera", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('i'):
        if login_attendance(pred_name):
            print("Attendance recorded for", pred_name)
            cv2.destroyAllWindows() # Close the window
            cap.release() # Release the camera
            break # Break out of the loop to end the program
        else:
            print("Failed to record attendance.")
    elif key_pressed == ord('o'):
        if login_attendance(pred_name, logout=True):
            print("Logout recorded for", pred_name)
        else:
            print("Failed to record logout.")

    elif key_pressed == ord('x'):
        cv2.destroyAllWindows()  # Close the window
        cap.release()  # Release the camera
        break  # Break out of the loop to end the program

cv2.destroyAllWindows()
cap.release()
