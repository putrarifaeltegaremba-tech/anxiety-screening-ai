import cv2
from deepface import DeepFace

def analyze_face():
    cap = cv2.VideoCapture(0)
    print("Tekan 's' untuk scan wajah")

    emotion = "Netral"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Face Scan", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']
            except:
                emotion = "Tidak terdeteksi"
            break

    cap.release()
    cv2.destroyAllWindows()
    return emotion
