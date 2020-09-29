import cv2
from yolo import YOLO


class Detector():
    def __init__(self):
        self.cameras = [0]
        self.yolo = YOLO(configPath = "yolov4/yolov4-tiny.cfg", weightPath = "yolov4/yolov4-tiny_final.weights",
                 metaPath = "yolov4/obj.data", classPath = "yolov4/obj.names")
        # self.items_count = self.detect()
        self.items_count = self.detect_image("images/1.jpg")
        print("Init", self.items_count)

    def detect_image(self, imgpath):
        img = cv2.imread(imgpath)
        return self.yolo.count(img)


    def detect(self):
        items_count = dict()
        for cam in self.cameras:
            capture = cv2.VideoCapture(cam)
            frame, res = capture.read()
            layer_count = self.yolo.count(frame)
            items_count = items_count.update(layer_count)
            capture.release()
        return items_count

    def detect_difference(self):
        diff_count = dict()
        # items_count = self.detect()
        items_count = self.detect_image("images/51.jpg")
        for k, v in self.items_count.items():
            count = items_count.get(k, 0)
            minus = v - count
            if minus > 0:
                diff_count[k] = minus
        self.items_count = items_count
        return diff_count
