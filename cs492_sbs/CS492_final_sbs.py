import shutil
import sys
import os
import time
from pathlib import Path
import shutil
import cv2

import plate_crop as cr
import detect as D
import segmentation.predict as seg
import calorie_predict as cal
from PyQt5.QtWidgets import *  #  QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QComboBox, QLabel, QCheckBox, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import * # QPixmap, QImage

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))


def yolo_sbs(option = 'food',save_en = True):
    if (option == 'food'):
        yoloList = D.run(weights=ROOT / 'best.pt',  # model.pt path(s)
                source=ROOT / 'sbs_Data/resource',  # file/dir/URL/glob, 0 for webcam
                imgsz=[640, 640],  # inference size (pixels)
                conf_thres=0.45,  # confidence threshold
                iou_thres=0.45,  # NMS IOU threshold
                project=ROOT / 'sbs_Data',  # save results to project/name
                name='detect',
                exist_ok=True,
                view_img=False,
                save_txt=save_en,
                nosave=not save_en
                )
        return yoloList
    elif (option == 'base'):
        baseList = D.run(weights=ROOT / 'base_best.pt',  # model.pt path(s)
                source=ROOT / 'sbs_Data/resource',  # file/dir/URL/glob, 0 for webcam
                imgsz=[640, 640],  # inference size (pixels)
                conf_thres=0.45,  # confidence threshold
                iou_thres=0.45,  # NMS IOU threshold
                project=ROOT / 'sbs_Data',  # save results to project/name
                name='base',
                exist_ok=True,
                view_img=False,
                save_txt=save_en,
                nosave=not save_en
                )
        return baseList
    else : print('goodbye')

class SBS_App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 800
        self.top = 300
        self.width = 1000
        self.height = 550
        self.save = True
        self.calories = 0.
        self.ind = 1
        self.list1 = []
        self.list2 = []
        self.filename = ""
        self.img_data = ""
        self.foodlocs = []
        self.croppix = []
        self.first = True
        self.loaded = False
        self.detected = False
        self.segmented = False
        self.lb_img1 = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle('KAIST DIET MANAGER (SBS)')
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button_inc = QPushButton('>', self)
        self.button_dec = QPushButton('<', self)
        self.button_inc.move(150, 480)
        self.button_dec.move(70, 480)
        self.button_inc.clicked.connect(self.increment)
        self.button_dec.clicked.connect(self.decrement)

        self.label0 = QLabel('Step0:', self)
        self.label0.move(70, 30)

        self.button_load_img = QPushButton('Load', self)
        self.button_load_img.setToolTip('please not tilted image if you can')
        self.button_load_img.move(150, 25)
        self.button_load_img.clicked.connect(self.load_Img)

        self.label1 = QLabel('Step1:', self)
        self.label1.move(70, 60)

        self.button_detect_img = QPushButton('Detect', self)
        self.button_detect_img.setToolTip('please not tilted image if you can')
        self.button_detect_img.move(150, 55)
        self.button_detect_img.clicked.connect(self.detect_Img)

        self.label2 = QLabel('Step2:', self)
        self.label2.move(70, 90)

        self.button_load_base = QPushButton('Set Base', self)
        self.button_load_base.setToolTip('please not tilted image if you can')
        self.button_load_base.move(150, 85)
        self.button_load_base.clicked.connect(self.load_Base)

        self.label3 = QLabel('Step3:', self)
        self.label3.move(70, 120)

        self.button_crop_img = QPushButton('Crop', self)
        self.button_crop_img.setToolTip('please not tilted image if you can')
        self.button_crop_img.move(150, 115)
        self.button_crop_img.clicked.connect(self.crop_Img)

        self.label4 = QLabel('Step4:', self)
        self.label4.move(70, 150)

        self.button_seg = QPushButton('segmentation', self)
        self.button_seg.setToolTip('please not tilted image if you can')
        self.button_seg.move(150, 145)
        self.button_seg.clicked.connect(self.seg_Img)

        self.label5 = QLabel('Step5:', self)
        self.label5.move(70, 180)

        self.button_cal = QPushButton('predict calories', self)
        self.button_cal.setToolTip('please not tilted image if you can')
        self.button_cal.move(150, 175)
        self.button_cal.clicked.connect(self.pred_Cal)

        self.button_detect_img.setFixedSize(125, 30)
        self.button_load_img.setFixedSize(125, 30)
        self.button_load_base.setFixedSize(125, 30)
        self.button_crop_img.setFixedSize(125, 30)
        self.button_seg.setFixedSize(125, 30)
        self.button_cal.setFixedSize(125, 30)

        self.label6 = QLabel('Calories =   ' + str(self.calories)+ ' kCal', self)
        self.label6.setFixedSize(220,30)
        self.label6.move(70, 210)

        # str(ROOT / 'sbs_Data/resource/gaon_kaist_n11_256666277_579576373127519_8770024017735097740_n.jpg')
        self.lb_img = QLabel(self)
        self.lb_img.move(300,30)
        self.lb_img.resize(640,480) #w ,h
        self.res_pic = QPixmap()
        self.lb_img.setPixmap(self.res_pic)


        self.lb_img1.move(50,250)
        self.lb_img1.resize(200,200) #w ,h
        self.lb_img1.setPixmap(self.res_pic)

        self.show()

    def increment(self):
        if (self.ind < 6) :
            self.ind = self.ind + 1
        if(not self.first) : self.image_update2()


    def decrement(self):
        if (self.ind > 1):
            self.ind = self.ind - 1
        if(not self.first) : self.image_update2()

    def image_update2(self):

        qq1 = QPixmap()
        img1 = self.img_data[:-5] + str(int(self.ind))+'.jpg'
        qq1.load(img1)
        qq1 = qq1.scaled(200, 200)
        self.lb_img1.setPixmap(qq1)
        self.lb_img1.repaint()

    def image_update(self):
        qq = QPixmap()
        qq.load(self.img_data)
        qq = qq.scaled(640, 480)
        self.lb_img.setPixmap(qq)
        self.lb_img.repaint()

    @pyqtSlot()
    def pred_Cal(self):
        if(self.segmented):
            calories = cal.calculate_kalorie(self.croppix,self.list1)
            self.calories = float(calories/1.2).__round__(2)
            self.label6.setText('Calories = ' + str(self.calories)+ ' kCal')
            self.label6.repaint()
        else :
            self.seg_Img()
            time.sleep(2)
            print('segment first')
            self.pred_Cal()

    @pyqtSlot()
    def seg_Img(self):
        if (not self.first):
            self.croppix ,self.foodarea = seg.segmen(imdir=str(ROOT / 'sbs_Data/crop/') , savedir=str(ROOT / 'sbs_Data/seg/'), filename=self.filename[:-4])
            self.img_data = str(ROOT / 'sbs_Data/detect/') + '/' + self.filename
            self.image_update()
            self.img_data = str(ROOT / 'sbs_Data/seg/') + '/' + self.filename[:-4] + '_seg_1.jpg'
            self.image_update2()
            self.segmented = True
        else:
            self.crop_Img()
            time.sleep(2)
            print('crop first')
            self.seg_Img()

    @pyqtSlot()
    def crop_Img(self):
        if(self.detected and self.loaded):
            cr.crop(dir=str(ROOT / 'sbs_Data/crop/'), img=str(ROOT / 'sbs_Data/resource/'), lab=str(ROOT / 'sbs_Data/base/labels/'),
                    filename='/'+self.filename[:-4])
            self.img_data = str(ROOT / 'sbs_Data/detect/') + '/' + self.filename
            self.image_update()
            self.img_data = str(ROOT / 'sbs_Data/crop/') + '/' + self.filename[:-4] + '_crop_1.jpg'
            self.image_update2()
            self.first = False
        else:
            self.detect_Img()
            time.sleep(2)
            self.load_Base()
            time.sleep(2)
            print('detect first')
            self.crop_Img()

    def load_Img(self):
        temp_name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        self.filename = temp_name.split('/')[-1]
        self.img_data = temp_name
        self.image_update()
        # print(str(ROOT / 'sbs_Data/resource/') + self.filename)
        
        if(self.filename != ''): 
        	shutil.copyfile(temp_name,str(ROOT/'sbs_Data/resource/')+'/'+self.filename)
        	self.loaded = True

    @pyqtSlot()
    def detect_Img(self):
        if (self.loaded):
            self.list1 = yolo_sbs(option='food', save_en = self.save)
            # print(self.).
            self.img_data =str(ROOT/ 'sbs_Data/detect/')+'/'+self.filename
            self.image_update()
            self.detected = True
        else:
            self.load_Img()
            print('load image first')
            self.detect_Img()
    @pyqtSlot()
    def load_Base(self):
        if (self.loaded):
            self.list2 = yolo_sbs(option='base', save_en = self.save)
            self.img_data = str(ROOT / 'sbs_Data/base/') + '/' + self.filename
            self.image_update()
            self.detected = True
        else:
            self.load_Img()
            print('load image first')
            self.load_Base()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SBS_App()
    sys.exit(app.exec_())
