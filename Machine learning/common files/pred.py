import cv2
import torch
import torch.backends.cudnn as cudnn
from utils.datasets import letterbox
from models.common import DetectMultiBackend
from utils.torch_utils import select_device

from utils.general import check_img_size, non_max_suppression, scale_coords
import numpy as np
import time

class Init():


    @torch.no_grad()
    def __init__(self, device, weights, data):
        # Load model
        self.device = select_device(device)
        self.model = DetectMultiBackend(weights, device=self.device, dnn=False, data=data)
        self.model.warmup((1,3, 416, 416))
    
    @torch.no_grad()
    def pred(self,
            sources,  # file/dir/URL/glob, 0 for webcam
            imgsz=(416, 416),  # inference size (height, width)
            conf_thres=0.5,  # confidence threshold
            iou_thres=0.5,  # NMS IOU threshold
            max_det=1000,  # maximum detections per image
            classes=0,  # filter by class: --class 0, or --class 0 2 3
            agnostic_nms=False,  # class-agnostic NMS
            hide_labels=False,  # hide labels
            hide_conf=True,  # hide confidences
            half=False,  # use FP16 half-precision inference
            ):

        stride, names, pt = self.model.stride, self.model.names, self.model.pt
        cudnn.benchmark = False
        imgsz = check_img_size(imgsz, s=stride)  # check image size
        for i, source in enumerate(sources) :
            img0 = cv2.imdecode(source, -1)
            if len(img0.shape) > 2 and img0.shape[2] == 4:
                #convert the image from RGBA2RGB
                img0 = cv2.cvtColor(img0, cv2.COLOR_BGRA2BGR)
            im = letterbox(img0, imgsz, stride=stride, auto=pt)[0]
            # Convert
            im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
            im = np.ascontiguousarray(im)
            im = torch.from_numpy(im).to(self.device)
            im = im.half() if half else im.float()  # uint8 to fp16/32
            im /= 255  # 0 - 255 to 0.0 - 1.0
            if len(im.shape) == 3:
                im = im[None]  # expand for batch dim
            pred = self.model(im)
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)
            lis = []
            for det in pred:
                im0 = img0.copy()
                if len(det):
                # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        c = int(cls)  # integer class
                        label = None if hide_labels else (names[c] if hide_conf else f'{names[c]} {conf:.2f}')
                        #z+=1
                        #temp[f'box{z}'] = [int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])]

                        # print(int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3]))
                        # top_left = (int(xyxy[0]), int(xyxy[1]))
                        # bottom_right = (int(xyxy[2]), int(xyxy[3]))
                        # cv2.rectangle(im0,top_left,bottom_right,(255,0,0),3)
                        # cv2.putText(im0, label, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
                        object_detection = {"type": label, "bounding_box": [int(xyxy[0]),int(xyxy[1]),int(xyxy[2]),int(xyxy[3])], "confidence": float(conf)}
                        lis.append(object_detection.copy())
            #cv2.imwrite(f'ut{i}.jpg', im0)
        return lis

