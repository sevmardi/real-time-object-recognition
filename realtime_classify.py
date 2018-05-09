import tensorflow as tf
from keras.applications import imagenet_utils
from keras.applications import VGG16
from keras.applications import ResNet50
import cv2
import threading
import numpy as np

frame_to_predict = None
classification = True
label = ""
score = .0

print("Loading network.. ")

model = ResNet50(weights='imagenet')
graph = tf.get_default_graph()

print('Network loaded successfully!')


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global label
        global frame_to_predict
        global model
        global graph
        global score

        with graph.as_default():
            while classification is True:
                if frame_to_predict is not None:
                    frame_to_predict = cv2.cvtColor(
                        frame_to_predict, cv2.COLOR_BGR2RGB).astype(np.float32)
                    frame_to_predict = frame_to_predict.reshape(
                        (1, ) + frame_to_predict.shape)
                    frame_to_predict = imagenet_utils.preprocess_input(
                        frame_to_predict)
                    predictions = model.predict(frame_to_predict)
                    (imageID, label, score) = imagenet_utils.decode_predictions(
                        predictions)[0][0]


keras_thread = MyThread()
keras_thread.start()

# Initialize OpenCV video captue
video_capture = cv2.VideoCapture(0)  # Set to 1 for front camera
video_capture.set(4, 800)  # Width
video_capture.set(5, 600)  # Height


while(True):
    ret, original_frame = video_capture.read()
    frame_to_predict = cv2.resize(original_frame, (224, 224))

    cv2.putText(original_frame, "Label: %s | Score: %.2f" % (
        label, score), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("Classification", original_frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break


classification = False
video_capture.release()
cv2.destroyAllWindows()
