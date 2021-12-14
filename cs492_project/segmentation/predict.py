from detectron2.utils.logger import setup_logger
setup_logger()
import cv2
import os
from . import seg_final
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from detectron2.config import get_cfg

def segmen(imdir, savedir, filename):
	cfg = get_cfg()
	cfg.merge_from_file("./mask_rcnn_R_50_FPN_3x.yaml")
	cfg.DATASETS.TRAIN = ("food",)
	cfg.DATASETS.TEST = ()   # no metrics implemented for this dataset
	cfg.DATALOADER.NUM_WORKERS = 2
	cfg.MODEL.WEIGHTS = "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"  # initialize from model zoo
	cfg.SOLVER.IMS_PER_BATCH = 2
	cfg.SOLVER.BASE_LR = 0.02
	cfg.SOLVER.MAX_ITER = 300    # 300 iterations seems good enough, but you can certainly train longer
	cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128   # faster, and good enough for this toy dataset
	cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1  # 1 classes (person)
	os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
	cfg.MODEL.WEIGHTS = "./model_final_best.pth"
	cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
	cfg.DATASETS.TEST = ("food", )
	predictor = DefaultPredictor(cfg)

	foodloc = []
	pixs = []
	for i in range(6):
		im = cv2.imread(imdir+'/'+filename+'_crop_'+str(i+1)+'.jpg')
		outputs = predictor(im)
		v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
		v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
		final_im, cnt, foodarea =  seg_final.final_step(im, v.get_image()[:, :, ::-1])
		foodloc.append(foodarea)
		pixs.append(cnt)
		cv2.imwrite(savedir+'/'+filename+'_seg_'+str(i+1)+'.jpg', final_im)
	return pixs, foodloc
