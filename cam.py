import cv2
import dlib
from collections import OrderedDict
from scipy.spatial import distance
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.FaceDetectionModule import FaceDetector
from imutils import face_utils
import numpy as np
import imutils
import time

FACIAL_LANDMARKS_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 35)),
    ("jaw", (0, 17))
])

hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

blink_flag = False
yawn_flag = False   
EAR_THRESHOLD = 0.21
MAR_THRESHOLD = 0.6

blink_count = 0
yawn_count = 0
number = 0

class EngageWise(object):
    def __init__(self):
        self.number = 0
        self.blink_flag = False
        self.yawn_flag = False
        self.blink_count = 0
        self.yawn_count = 0
        self.d = 0
        self.state = ""

        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 640)
        self.cam.set(4, 480)
        width = self.cam.get(3)
        height = self.cam.get(4)
        print(f"Current Camera Resolution: {width} x {height}")

        self.detector = FaceMeshDetector()
        self.detector2 = FaceDetector()

    def __del__(self):
        self.cam.release()

    def calculate_EAR(self, eye):
        A = distance.euclidean(eye[1], eye[5])
        B = distance.euclidean(eye[2], eye[4])
        C = distance.euclidean(eye[0], eye[3])
        ear_aspect_ratio = (A + B) / (2.0 * C)
        return ear_aspect_ratio

    def cal_MAR(self, mouth):
        dist_x = distance.euclidean(mouth[0], mouth[6])
        dist_y = distance.euclidean(mouth[3], mouth[9])
        mar = dist_y / dist_x
        return mar

    def get_frame(self):
        ret, frame = self.cam.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting....")
            return None

        frame = cv2.flip(frame, 1)

        frame = cv2.GaussianBlur(frame, (7, 7), 0)

        frame, faces = self.detector.findFaceMesh(frame, draw=False)
        frame, bboxs = self.detector2.findFaces(frame, draw=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = None

        for bbox in bboxs:
            x, y, w, h = bbox["bbox"]
            l, r = (x, y), (x + w, y + h)
            w = distance.euclidean(l, r)
            W, f = 6.3, 825
            self.d = (W * f) / w * 2.54
            try:
                cv2.putText(frame, "Distance: {}cm".format(int(self.d)), (5, 50), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 2)
            except Exception as error:
                print(error)

        faces = hog_face_detector(gray)
        EAR = 0

        for face in faces:
            face_landmarks = dlib_facelandmark(gray, face)
            face_landmarks = face_utils.shape_to_np(face_landmarks)

            leftEye = face_landmarks[36:42]
            rightEye = face_landmarks[42:48]
            mouth = face_landmarks[mStart:mEnd]

            left_ear = self.calculate_EAR(leftEye)
            right_ear = self.calculate_EAR(rightEye)
            mar = self.cal_MAR(mouth)

            EAR = (left_ear + right_ear) / 2

            if EAR < EAR_THRESHOLD:
                if not self.blink_flag:
                    self.blink_flag = True
                    self.blink_count += 1
                    cv2.putText(frame, "Blink Detected!", (530, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
            else:
                self.blink_flag = False

            if mar > MAR_THRESHOLD:
                if not self.yawn_flag:
                    self.yawn_flag = True
                    self.yawn_count += 1
                    cv2.putText(frame, "Yawn Detected!", (530, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)
            else:
                self.yawn_flag = False

        cv2.putText(frame, "Blink count: {}".format(self.blink_count), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.putText(frame, "Yawn count: {}".format(self.yawn_count), (5, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        if EAR < EAR_THRESHOLD:
            self.state = "Drowsy"
        else:
            self.state = "Awake"
        
        cv2.putText(frame, f"{self.state}", (250, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

        key = cv2.waitKey(1)
        if key == ord('c'):
            self.number += 1
            print(f"Image {self.number} has been captured")
            cv2.imwrite(f'image{self.number}.jpeg', frame.copy(), [cv2.IMWRITE_JPEG_QUALITY, 95])
        if key == ord('q'):
            cv2.destroyAllWindows()
            return None

        return cv2.imencode('.jpg', frame)[1].tobytes()

    def reset(self):
        self.number = 0
        self.blink_flag = False
        self.yawn_flag = False
        self.blink_count = 0
        self.yawn_count = 0