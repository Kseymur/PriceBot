import torch
import cv2
import pandas as pd
import psutil
import torchvision


model_nikora = torch.hub.load('ultralytics/yolov5', 'custom', path="/Users/kseniiamurasheva/PycharmProjects/PriceBot/yolov5/runs/train/yolo_price_det8/weights/best.pt")
model_universami = torch.hub.load('ultralytics/yolov5', 'custom', path="/Users/kseniiamurasheva/PycharmProjects/PriceBot/yolov5/runs/train/yolo_price_det5/weights/best.pt")


# Получаем результаты детектирования
def get_split_nikora(img):

    results = model_nikora(img)
    if results.pred:
        # Вывод результатов
        results.print()
        results.pandas().xyxy[0]

        # Вырезаем найденные сегменты, для дальнейшего распознования
        crops = results.crop(save=True)

def get_split_universami(img):

    results = model_universami(img)
    if results.pred:
        # Вывод результатов
        results.print()
        results.pandas().xyxy[0]

        # Вырезаем найденные сегменты, для дальнейшего распознования
        crops = results.crop(save=True)