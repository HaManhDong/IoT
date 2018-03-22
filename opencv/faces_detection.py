import cv2
import cv

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

# w,h = 960, 544
# video_capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, w)
# video_capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, h)

size = 4

arr_faces = []
number_of_faces = 10



while True:
    # capture frame by frame
    ret, frame = video_capture.read()

    frame = cv2.flip(frame, 1, 0)
    mini_frame = cv2.resize(frame, (frame.shape[1] / size, frame.shape[0] / size))

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(mini_frame)

    # draw a rectangle around the faces
    for f in faces:
        (x, y, w, h) = [v * size for v in f]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        if y and not y in arr_faces:
            print(y)
            sub_face = frame[y:y + h, x:x + w]
            FaceFileName = "faces/face_" + str(10 + len(arr_faces)) + ".jpg"
            cv2.imwrite(FaceFileName, sub_face)
            arr_faces.append(y)


    # display the resulting frame
    cv2.imshow('Video', frame)

    # enter character 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q') or len(arr_faces) >= number_of_faces:
        break

# when everything is done, release the capture
print("destroy....")
video_capture.release()
cv2.destroyAllWindows()

